from base import JiraBaseAction


class JiraSetUserAvatar(JiraBaseAction):
    def _run(self, username, avatar):
      return self.jira.set_user_avatar(username, avatar)

