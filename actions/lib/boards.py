from base import JiraBaseAction


class JiraBoards(JiraBaseAction):
    def _run(self, **kwargs):
      return self.jira.boards(**kwargs)

