from base import JiraBaseAction


class JiraSetApplicationProperty(JiraBaseAction):
    def _run(self, key, value):
      return self.jira.set_application_property(key, value)

