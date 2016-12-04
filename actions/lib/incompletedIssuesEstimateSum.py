from base import JiraBaseAction


class JiraIncompletedissuesestimatesum(JiraBaseAction):
    def _run(self, board_id, sprint_id):
      return self.jira.incompletedIssuesEstimateSum(board_id, sprint_id)

