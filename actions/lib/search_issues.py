from base import JiraBaseAction


class JiraSearchIssues(JiraBaseAction):
    def _run(self, jql_str, **kwargs):
      return self.jira.search_issues(jql_str)

