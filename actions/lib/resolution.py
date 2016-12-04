from base import JiraBaseAction


class JiraResolution(JiraBaseAction):
    def _run(self, id):
      return self.jira.resolution(id)

