from django.conf import settings

CLIENT_ID = settings.GITLAB_APP_ID
CLIENT_SECRET = settings.GITLAB_APP_SECRET

SCOPE = getattr(settings, 'GITLAB_AUTH_SCOPE', 'api')

BASE_DOMAIN = settings.GITLAB_BASE_DOMAIN

ACCESS_TOKEN_URL = f"https://{BASE_DOMAIN}/oauth/token"
AUTHORIZE_URL = f"https://{BASE_DOMAIN}/oauth/authorize"
API_ENDPOINT = f"https://{BASE_DOMAIN}/api/v4"
