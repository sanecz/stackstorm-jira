from base import JiraBaseAction


class JiraComponent(JiraBaseAction):
    def _run(self, id):
      return self.jira.component(id)

