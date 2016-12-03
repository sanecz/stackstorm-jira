from base import JiraBaseAction


class JiraAssignIssue(JiraBaseAction):
    def _run(self, issue, assignee):
      return self.jira.assign_issue(issue, assignee)

