from base import JiraBaseAction


class JiraCreateIssue(JiraBaseAction):
    def _run(self, fieldargs, **kwargs):
      return self.jira.create_issue(fieldargs)

