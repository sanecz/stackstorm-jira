from base import JiraBaseAction


class JiraVersionCountUnresolvedIssues(JiraBaseAction):
    def _run(self, id):
      return self.jira.version_count_unresolved_issues(id)

