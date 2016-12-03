from base import JiraBaseAction


class JiraFilter(JiraBaseAction):
    def _run(self, id):
      return self.jira.filter(id)

