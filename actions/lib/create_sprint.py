from base import JiraBaseAction


class JiraCreateSprint(JiraBaseAction):
    def _run(self, name, board_id, **kwargs):
      return self.jira.create_sprint(name, board_id)

