from base import JiraBaseAction


class JiraAddUser(JiraBaseAction):
    def _run(self, username, email, **kwargs):
      return self.jira.add_user(username, email, **kwargs)

