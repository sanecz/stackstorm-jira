from base import JiraBaseAction


class JiraEditmeta(JiraBaseAction):
    def _run(self, issue):
      return self.jira.editmeta(issue)

