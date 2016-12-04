from base import JiraBaseAction


class JiraReindex(JiraBaseAction):
    def _run(self, **kwargs):
      return self.jira.reindex()

