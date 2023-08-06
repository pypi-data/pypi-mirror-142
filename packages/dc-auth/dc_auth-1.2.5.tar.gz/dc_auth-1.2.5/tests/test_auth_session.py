from copy import deepcopy

import pytest

from django.apps import apps
from django.db import transaction
from django.contrib.auth.middleware import AuthenticationMiddleware
from django.contrib.sessions.middleware import SessionMiddleware
from django.dispatch import receiver
from django.test import RequestFactory
from django.urls import reverse

from django_cas_ng.backends import CASBackend
from django_cas_ng.views import LoginView
from django_cas_ng.signals import cas_user_authenticated

from dc_auth.testing_support.factories.user import UserFactory

LOGIN_URL = reverse('cas_ng_login')


# function takes a request and applies a middleware process
def process_request_for_middleware(request, middleware):
    middleware = middleware()
    middleware.process_request(request)


def add_mock_verification(username, user_attrs, monkeypatch):
    def mock_verify(self, ticket):
        """Mock verification"""
        attrs = deepcopy(user_attrs)
        attrs.update({'ticket': ticket, 'service': 'service_url'})
        proxy_ticket = None
        return username, attrs, proxy_ticket

    # we mock out the verify method so that we can bypass the external http
    # calls needed for real authentication since we are testing the logic
    # around authentication.
    monkeypatch.setattr('cas.CASClientV2.verify_ticket', mock_verify)


def mock_login_cas(monkeypatch, django_user_model, username, user_attrs):
    """

    :param monkeypatch:
    :param django_user_model:
    :param user:
    :return:
    """
    factory = RequestFactory()
    request = factory.get('/login/')
    request.session = {}

    callback_values = {}

    @receiver(cas_user_authenticated)
    def callback(sender, **kwargs):
        callback_values.update(kwargs)

    add_mock_verification(username, user_attrs, monkeypatch)

    # sanity check
    with transaction.atomic():
        assert not django_user_model.objects.filter(
            username=username,
        ).exists()

    with transaction.atomic():
        backend = CASBackend()
        auth_user = backend.authenticate(
            ticket='fake-ticket', service='fake-service', request=request,
        )

    assert auth_user is not None

    return callback_values, auth_user, request


@pytest.mark.django_db
def test_signal_when_user_is_created(monkeypatch, django_user_model):
    """
    Test basic login for cas user.

    Note. This user does not exist in ldap. CAS verification on client is
    mocked.
    """
    # using a fixture would auto-add user to the db, which do not want
    user = UserFactory()

    user_attrs = {
        'affiliation': user.profile.affiliation,
        'orcid': user.profile.orcid,
    }

    callback_values, auth_user, request = mock_login_cas(
        monkeypatch, django_user_model, user.username, user_attrs,
    )

    assert 'user' in callback_values
    assert callback_values.get('user') == auth_user
    assert callback_values.get('created')
    assert 'attributes' in callback_values
    for key, val in user_attrs.items():
        assert callback_values['attributes'][key] == val
    assert 'ticket' in callback_values
    assert callback_values['ticket'] == 'fake-ticket'
    assert 'service' in callback_values
    assert callback_values['service'] == 'fake-service'

    # ensure user is created in db
    django_user = django_user_model.objects.get(username=user.username)
    assert django_user.profile.affiliation == user.profile.affiliation
    assert django_user.profile.orcid == user.profile.orcid


@pytest.mark.django_db
def test_signal_user_created_with_groups(monkeypatch, django_user_model):
    """
    Test login for cas user with groups.

    Note. This user does not exist in ldap. CAS verification on client is
    mocked.
    """
    # using a fixture would auto-add user to the db, which do not want
    user = UserFactory()

    user_attrs = {
        'affiliation': user.profile.affiliation,
        'orcid': user.profile.orcid,
        'groups': [
            'CN=DEVILS,OU=Groups,OU=Accounts,DC=ASVO,DC=AAO,DC=GOV,DC=AU',
        ]
    }

    callback_values, auth_user, request = mock_login_cas(
        monkeypatch, django_user_model, user.username, user_attrs,
    )

    assert 'user' in callback_values
    assert callback_values.get('user') == auth_user
    assert callback_values.get('created')
    assert 'attributes' in callback_values
    for key, val in user_attrs.items():
        assert callback_values['attributes'][key] == val
    assert 'ticket' in callback_values
    assert callback_values['ticket'] == 'fake-ticket'
    assert 'service' in callback_values
    assert callback_values['service'] == 'fake-service'

    # ensure user is created in db
    django_user = django_user_model.objects.get(username=user.username)
    user_groups = django_user.groups.all()
    assert len(user_groups) == 1
    assert user_groups[0].name == "DEVILS"


@pytest.mark.django_db
def test_signal_user_created_with_admin_group(monkeypatch, django_user_model):
    """
    Test login for cas user with groups.

    Note. This user does not exist in ldap. CAS verification on client is
    mocked.
    """
    # using a fixture would auto-add user to the db, which do not want
    user = UserFactory()

    user_attrs = {
        'affiliation': user.profile.affiliation,
        'orcid': user.profile.orcid,
        'groups': [
            'CN=dc-admin,OU=Groups,OU=Accounts,DC=ASVO,DC=AAO,DC=GOV,DC=AU',
        ]
    }

    callback_values, auth_user, request = mock_login_cas(
        monkeypatch, django_user_model, user.username, user_attrs,
    )

    assert 'user' in callback_values
    assert callback_values.get('user') == auth_user
    assert callback_values.get('created')
    assert 'attributes' in callback_values
    for key, val in user_attrs.items():
        assert callback_values['attributes'][key] == val
    assert 'ticket' in callback_values
    assert callback_values['ticket'] == 'fake-ticket'
    assert 'service' in callback_values
    assert callback_values['service'] == 'fake-service'

    # ensure user is created in db
    django_user = django_user_model.objects.get(username=user.username)
    user_groups = django_user.groups.all()
    assert len(user_groups) == 1
    assert user_groups[0].name == "dc-admin"
    assert django_user.is_staff


@pytest.mark.django_db
def test_login_authenticate_and_create_user(monkeypatch, django_user_model, settings):
    """
    Test the consequence of the dc_auth handler for cas_user_authenticated
    i.e., has_unusable_password=True, email_confirmed=True etc
    Handle missing orcid

    Note. This user does not exist in ldap. CAS verification on client is mocked.
    """
    # using a fixture would auto-add user to the db, which do not want
    user = UserFactory()

    # No need to test the message framework
    settings.CAS_LOGIN_MSG = None
    # Make sure we use our backend
    settings.AUTHENTICATION_BACKENDS = ['django_cas_ng.backends.CASBackend']

    add_mock_verification(
        user.username, {'affiliation': user.profile.affiliation}, monkeypatch,
    )

    factory = RequestFactory()
    request = factory.get(LOGIN_URL, {'ticket': 'fake-ticket',
                                      'service': 'fake-service'})

    # Create a session object from the middleware
    process_request_for_middleware(request, SessionMiddleware)
    # Create a user object from middleware
    process_request_for_middleware(request, AuthenticationMiddleware)

    response = LoginView().get(request)
    assert response.status_code == 302
    assert response['Location'] == '/'
    django_user = django_user_model.objects.get(username=user.username)
    assert django_user.is_authenticated is True
    assert django_user.profile.affiliation == user.profile.affiliation
    assert django_user.profile.email_confirmed is True
    assert django_user.is_active is True
    assert django_user.has_usable_password() is False
    assert django_user.profile.orcid == '-'


@pytest.mark.django_db
def test_login_group_removal(
    monkeypatch, django_user_model, settings, user,
):
    """
    Test the consequence of the dc_auth handler for cas_user_authenticated
    i.e., has_unusable_password=True, email_confirmed=True etc
    Handle missing orcid

    Note. This user does not exist in ldap. CAS verification on client is mocked.
    """
    # If user not active, login fails
    user.is_active = True
    user.save()

    group_name = "testgroup"
    group_model = apps.get_model(app_label='auth', model_name="group")
    group, created = group_model.objects.get_or_create(name=group_name)
    group.user_set.add(user)

    add_mock_verification(
        user.username, {'affiliation': user.profile.affiliation}, monkeypatch,
    )

    factory = RequestFactory()
    request = factory.get(LOGIN_URL, {'ticket': 'fake-ticket',
                                      'service': 'fake-service'})

    ## Create a session object from the middleware
    process_request_for_middleware(request, SessionMiddleware)
    ## Create a user object from middleware
    process_request_for_middleware(request, AuthenticationMiddleware)

    response = LoginView().get(request)
    assert response.status_code == 302
    assert response['Location'] == '/'

    django_user = django_user_model.objects.get(username=user.username)
    user_groups = django_user.groups.all()
    assert len(user_groups) == 0
