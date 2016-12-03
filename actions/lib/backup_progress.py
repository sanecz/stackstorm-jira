from base import JiraBaseAction


class JiraBackupProgress(JiraBaseAction):
    def _run(self):
      return self.jira.backup_progress()

