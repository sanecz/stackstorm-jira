from base import JiraBaseAction


class JiraMoveVersion(JiraBaseAction):
    def _run(self, id, **kwargs):
      return self.jira.move_version(id, **kwargs)

