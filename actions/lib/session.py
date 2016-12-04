from base import JiraBaseAction


class JiraSession(JiraBaseAction):
    def _run(self, ):
      return self.jira.session()

