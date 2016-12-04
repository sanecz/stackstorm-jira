from base import JiraBaseAction


class JiraSprints(JiraBaseAction):
    def _run(self, board_id, **kwargs):
      return self.jira.sprints(board_id)

