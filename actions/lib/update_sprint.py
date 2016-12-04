from base import JiraBaseAction


class JiraUpdateSprint(JiraBaseAction):
    def _run(self, id, **kwargs):
      return self.jira.update_sprint(id)

