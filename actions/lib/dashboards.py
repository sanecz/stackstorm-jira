from base import JiraBaseAction


class JiraDashboards(JiraBaseAction):
    def _run(self, **kwargs):
      return self.jira.dashboards()

