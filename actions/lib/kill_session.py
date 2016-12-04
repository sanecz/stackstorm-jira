from base import JiraBaseAction


class JiraKillSession(JiraBaseAction):
    def _run(self):
      return self.jira.kill_session()

