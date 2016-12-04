from base import JiraBaseAction


class JiraSprintInfo(JiraBaseAction):
    def _run(self, board_id, sprint_id):
      return self.jira.sprint_info(board_id, sprint_id)

