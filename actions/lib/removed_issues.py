from base import JiraBaseAction


class JiraRemovedIssues(JiraBaseAction):
    def _run(self, board_id, sprint_id):
      return self.jira.removed_issues(board_id, sprint_id)

