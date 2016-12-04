from base import JiraBaseAction


class JiraMyPermissions(JiraBaseAction):
    def _run(self, **kwargs):
      return self.jira.my_permissions()

