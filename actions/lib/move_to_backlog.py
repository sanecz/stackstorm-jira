from base import JiraBaseAction


class JiraMoveToBacklog(JiraBaseAction):
    def _run(self, issue_keys):
      return self.jira.move_to_backlog(issue_keys)

