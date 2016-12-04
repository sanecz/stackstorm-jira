from base import JiraBaseAction


class JiraResolutions(JiraBaseAction):
    def _run(self, ):
      return self.jira.resolutions()

