from base import JiraBaseAction


class JiraUpdateFilter(JiraBaseAction):
    def _run(self, filter_id, **kwargs):
      return self.jira.update_filter(filter_id)

