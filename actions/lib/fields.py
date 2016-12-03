from base import JiraBaseAction


class JiraFields(JiraBaseAction):
    def _run(self, ):
      return self.jira.fields()

