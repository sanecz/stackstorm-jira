from base import JiraBaseAction


class JiraSearchIssues(JiraBaseAction):
    def _run(self, jql_str, **kwargs):
      issues = self.jira.search_issues(jql_str, json_result=True, **kwargs)
      return issues

