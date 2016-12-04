from base import JiraBaseAction


class JiraDashboard(JiraBaseAction):
    def _run(self, id):
      return self.jira.dashboard(id)

