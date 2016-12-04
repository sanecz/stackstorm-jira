from base import JiraBaseAction


class JiraIssueLink(JiraBaseAction):
    def _run(self, id):
      return self.jira.issue_link(id)

