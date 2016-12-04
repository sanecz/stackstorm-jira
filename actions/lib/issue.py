from base import JiraBaseAction


class JiraIssue(JiraBaseAction):
    def _run(self, id, **kwargs):
      return self.jira.issue(id)

