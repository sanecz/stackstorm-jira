from base import JiraBaseAction


class JiraBackup(JiraBaseAction):
    def _run(self, **kwargs):
      return self.jira.backup(**kwargs)

