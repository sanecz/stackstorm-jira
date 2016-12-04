from base import JiraBaseAction


class JiraUserAvatars(JiraBaseAction):
    def _run(self, username):
      return self.jira.user_avatars(username)

