from base import JiraBaseAction


class JiraAddComment(JiraBaseAction):
    def _run(self, issue, body):
      return self.jira.add_comment(issue, body)

