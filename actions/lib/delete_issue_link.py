from base import JiraBaseAction


class JiraDeleteIssueLink(JiraBaseAction):
    def _run(self, id):
      return self.jira.delete_issue_link(id)

