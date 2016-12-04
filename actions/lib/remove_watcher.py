from base import JiraBaseAction


class JiraRemoveWatcher(JiraBaseAction):
    def _run(self, issue, watcher):
      return self.jira.remove_watcher(issue, watcher)

