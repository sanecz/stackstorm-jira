from base import JiraBaseAction


class JiraDeleteUser(JiraBaseAction):
    def _run(self, username):
      return self.jira.delete_user(username)

