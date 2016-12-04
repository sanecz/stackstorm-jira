from base import JiraBaseAction


class JiraProject(JiraBaseAction):
    def _run(self, id):
      return self.jira.project(id)

