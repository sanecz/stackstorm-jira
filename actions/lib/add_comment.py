from base import JiraBaseAction


class JiraAddComment(JiraBaseAction):
    def _run(self, issue, body, **kwargs):
      return self.jira.add_comment(issue, body)

