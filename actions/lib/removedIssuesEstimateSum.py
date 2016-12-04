from base import JiraBaseAction


class JiraRemovedissuesestimatesum(JiraBaseAction):
    def _run(self, board_id, sprint_id):
      return self.jira.removedIssuesEstimateSum(board_id, sprint_id)

