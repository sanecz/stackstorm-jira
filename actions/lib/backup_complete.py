from base import JiraBaseAction


class JiraBackupComplete(JiraBaseAction):
    def _run(self):
      return self.jira.backup_complete()

