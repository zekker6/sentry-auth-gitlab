from sentry.auth.view import AuthView

from .client import GitLabClient

class FetchUser(AuthView):
    def handle(self, request, pipeline):
        with GitLabClient(pipeline.fetch_state('data')['access_token']) as client:
            user = client.get_user()
            pipeline.bind_state('user', user)
            return pipeline.next_step()
