from base import JiraBaseAction


class JiraCreateFilter(JiraBaseAction):
    def _run(self, **kwargs):
      return self.jira.create_filter()

