from base import JiraBaseAction


class JiraDeleteUserAvatar(JiraBaseAction):
    def _run(self, username, avatar):
      return self.jira.delete_user_avatar(username, avatar)

