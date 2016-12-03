from base import JiraBaseAction


class JiraCompletedIssues(JiraBaseAction):
    def _run(self, board_id, sprint_id):
      return self.jira.completed_issues(board_id, sprint_id)

