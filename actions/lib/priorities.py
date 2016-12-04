from base import JiraBaseAction


class JiraPriorities(JiraBaseAction):
    def _run(self, ):
      return self.jira.priorities()

