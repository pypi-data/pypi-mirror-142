import pytest

from .factories import SECURE_PASSWORD


@pytest.fixture
def profile_factory(db):
    from .factories.user import ProfileFactory
    return ProfileFactory

@pytest.fixture
def user_factory(db):
    from .factories.user import UserFactory
    return UserFactory


@pytest.fixture
def profile(profile_factory):
    return profile_factory.create()


@pytest.fixture
def user(profile):
    return profile.user


@pytest.fixture
def affiliation(faker):
    return faker.company()


@pytest.fixture
def secure_password():
    return SECURE_PASSWORD
