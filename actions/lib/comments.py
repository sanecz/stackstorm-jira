from base import JiraBaseAction


class JiraComments(JiraBaseAction):
    def _run(self, issue):
      return self.jira.comments(issue)

