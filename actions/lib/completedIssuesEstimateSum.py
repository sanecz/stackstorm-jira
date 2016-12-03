from base import JiraBaseAction


class JiraCompletedissuesestimatesum(JiraBaseAction):
    def _run(self, board_id, sprint_id):
      return self.jira.completedIssuesEstimateSum(board_id, sprint_id)

