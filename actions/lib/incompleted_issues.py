from base import JiraBaseAction


class JiraIncompletedIssues(JiraBaseAction):
    def _run(self, board_id, sprint_id):
      return self.jira.incompleted_issues(board_id, sprint_id)

