from __future__ import absolute_import
from django.apps import AppConfig

class Config(AppConfig):
    name = "auth_gitlab"

    def ready(self):
        from sentry import auth
        from .provider import GitLabOAuth2Provider

        auth.register('auth_gitlab', GitLabOAuth2Provider)