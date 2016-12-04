from base import JiraBaseAction


class JiraIssueType(JiraBaseAction):
    def _run(self, id):
      return self.jira.issue_type(id)

