from base import JiraBaseAction


class JiraCreateBoard(JiraBaseAction):
    def _run(self, name, project_ids, **kwargs):
      return self.jira.create_board(name, project_ids, **kwargs)

