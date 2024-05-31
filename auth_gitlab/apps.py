from django.apps import AppConfig

class Config(AppConfig):
    name = "auth_gitlab"

    def ready(self):
        from sentry.auth import register

        from .provider import GitLabOAuth2Provider

        register('auth_gitlab', GitLabOAuth2Provider)
