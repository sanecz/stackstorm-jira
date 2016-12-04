from base import JiraBaseAction


class JiraServerInfo(JiraBaseAction):
    def _run(self):
      return self.jira.server_info()

