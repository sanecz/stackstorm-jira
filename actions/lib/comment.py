from base import JiraBaseAction


class JiraComment(JiraBaseAction):
    def _run(self, issue, comment):
      return self.jira.comment(issue, comment)

