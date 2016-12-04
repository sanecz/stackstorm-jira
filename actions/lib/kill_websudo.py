from base import JiraBaseAction


class JiraKillWebsudo(JiraBaseAction):
    def _run(self, ):
      return self.jira.kill_websudo()

