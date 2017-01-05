from base import JiraBaseAction


class JiraIssue(JiraBaseAction):
    def _run(self, id, **kwargs):
      issue = self.jira.issue(id, **kwargs)
      return issue.raw

