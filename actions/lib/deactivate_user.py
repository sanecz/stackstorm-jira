from base import JiraBaseAction


class JiraDeactivateUser(JiraBaseAction):
    def _run(self, username):
      return self.jira.deactivate_user(username)

