from base import JiraBaseAction


class JiraBackupDownload(JiraBaseAction):
    def _run(self, **kwargs):
      return self.jira.backup_download(**kwargs)

