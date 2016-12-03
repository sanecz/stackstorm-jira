from base import JiraBaseAction


class JiraAddWatcher(JiraBaseAction):
    def _run(self, issue, watcher):
      return self.jira.add_watcher(issue, watcher)

