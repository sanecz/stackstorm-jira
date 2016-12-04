from base import JiraBaseAction


class JiraStatus(JiraBaseAction):
    def _run(self, id):
      return self.jira.status(id)

