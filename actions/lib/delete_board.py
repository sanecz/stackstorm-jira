from base import JiraBaseAction


class JiraDeleteBoard(JiraBaseAction):
    def _run(self, id):
      return self.jira.delete_board(id)

