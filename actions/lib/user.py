from base import JiraBaseAction


class JiraUser(JiraBaseAction):
    def _run(self, id, **kwargs):
      return self.jira.user(id)

