from base import JiraBaseAction


class JiraVersion(JiraBaseAction):
    def _run(self, id, **kwargs):
      return self.jira.version(id)

