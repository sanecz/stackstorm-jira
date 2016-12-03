from base import JiraBaseAction


class JiraClientInfo(JiraBaseAction):
    def _run(self):
      return self.jira.client_info()

