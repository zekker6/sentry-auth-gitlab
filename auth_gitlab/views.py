from sentry.auth.view import AuthView

from .client import GitLabClient

class FetchUser(AuthView):
    def handle(self, request, helper):
        with GitLabClient(helper.fetch_state('data')['access_token']) as client:
            user = client.get_user()
            helper.bind_state('user', user)
            return helper.next_step()
