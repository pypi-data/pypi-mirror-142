from django.conf import settings
from django.conf.urls import url, include
from django.urls import path
from django.views.generic.base import RedirectView

import django_cas_ng.views


"""


"""

urlpatterns = [
    # -- Favicons and app icons --
    # keep favicon urls at root, but redirect to the favicon folder
    url(r'^favicon\.ico$', RedirectView.as_view(url=settings.STATIC_URL + 'dc_auth/img/favicon/favicon.ico')),
    url(r'^favicon-32x32\.png$',
        RedirectView.as_view(url=settings.STATIC_URL + 'dc_auth/img/favicon/favicon-32x32.png')),
    url(r'^favicon-16x16\.png$',
        RedirectView.as_view(url=settings.STATIC_URL + 'dc_auth/img/favicon/favicon-16x16.png')),
    url(r'^manifest\.json$',
        RedirectView.as_view(url=settings.STATIC_URL + 'dc_auth/img/favicon/manifest.json')),
    url(r'^safari-pinned-tab\.svg$',
        RedirectView.as_view(url=settings.STATIC_URL + 'dc_auth/img/favicon/safari-pinned-tab.svg')),
    url(r'^android-chrome-192x192\.png$',
        RedirectView.as_view(url=settings.STATIC_URL + 'dc_auth/img/favicon/android-chrome-192x192.png')),
    url(r'^android-chrome-512x512\.png$',
        RedirectView.as_view(url=settings.STATIC_URL + 'dc_auth/img/favicon/android-chrome-512x512')),
    url(r'^apple-touch-icon\.png',
        RedirectView.as_view(url=settings.STATIC_URL + 'dc_auth/img/favicon/apple-touch-icon.png')),
    url(r'^browserconfig\.xml',
        RedirectView.as_view(url=settings.STATIC_URL + 'dc_auth/img/favicon/browserconfig.xml')),
    url(r'^mstile-150x150\.png',
        RedirectView.as_view(url=settings.STATIC_URL + 'dc_auth/img/favicon/mstile-150x150.png')),

    path('accounts/login/', django_cas_ng.views.LoginView.as_view(), name='cas_ng_login'),
    path('accounts/logout/', django_cas_ng.views.LogoutView.as_view(), name='cas_ng_logout'),
    path('accounts/callback/', django_cas_ng.views.CallbackView.as_view(), name='cas_ng_proxy_callback'),
]

