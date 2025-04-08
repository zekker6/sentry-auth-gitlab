from django.apps import AppConfig

class Config(AppConfig):
    name = "auth_gitlab"

    def ready(self):
        from sentry.auth import register

        from .provider import GitLabOAuth2Provider

        try:
            # Sentry 25.3.0 and above
            register(GitLabOAuth2Provider)
        except TypeError:
            # Sentry 25.2.0 and below
            register('auth_gitlab', GitLabOAuth2Provider)
