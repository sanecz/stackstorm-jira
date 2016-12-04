from base import JiraBaseAction


class JiraWatchers(JiraBaseAction):
    def _run(self, issue):
      return self.jira.watchers(issue)

