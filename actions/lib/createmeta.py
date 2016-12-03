from base import JiraBaseAction


class JiraCreatemeta(JiraBaseAction):
    def _run(self, **kwargs):
      return self.jira.createmeta()

