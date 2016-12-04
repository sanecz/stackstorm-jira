from base import JiraBaseAction


class JiraIssueTypes(JiraBaseAction):
    def _run(self, ):
      return self.jira.issue_types()

