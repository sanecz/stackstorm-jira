from base import JiraBaseAction


class JiraSearchAssignableUsersForIssues(JiraBaseAction):
    def _run(self, username, **kwargs):
      return self.jira.search_assignable_users_for_issues(username, **kwargs)

