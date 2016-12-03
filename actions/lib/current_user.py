from base import JiraBaseAction


class JiraCurrentUser(JiraBaseAction):
    def _run(self, ):
      return self.jira.current_user()

