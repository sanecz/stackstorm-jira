from base import JiraBaseAction


class JiraApplicationProperties(JiraBaseAction):
    def _run(self, **kwargs):
      return self.jira.application_properties()

