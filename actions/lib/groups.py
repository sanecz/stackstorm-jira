from base import JiraBaseAction


class JiraGroups(JiraBaseAction):
    def _run(self, **kwargs):
      return self.jira.groups()

