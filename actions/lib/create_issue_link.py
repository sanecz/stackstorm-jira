from base import JiraBaseAction


class JiraCreateIssueLink(JiraBaseAction):
    def _run(self, type, inwardIssue, outwardIssue, **kwargs):
      return self.jira.create_issue_link(type, inwardIssue, outwardIssue)

