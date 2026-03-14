from sentry.auth.view import AuthView

from .client import GitLabClient
from .constants import GROUPS

class FetchUser(AuthView):
    def handle(self, request, pipeline):
        with GitLabClient(pipeline.fetch_state('data')['access_token']) as client:
            user = client.get_user()

            user_groups = user.get('groups', [])
            if GROUPS and set(GROUPS).isdisjoint(user_groups):
                return pipeline.error(
                    f'Only members of {GROUPS} are allowed to log in.'
                    f' Your groups are {user_groups}'
                )

            pipeline.bind_state('user', user)
            return pipeline.next_step()
