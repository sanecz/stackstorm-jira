from base import JiraBaseAction


class JiraFind(JiraBaseAction):
    def _run(self, resource_format, **kwargs):
      return self.jira.find(resource_format)

