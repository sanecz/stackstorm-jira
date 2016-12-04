from base import JiraBaseAction


class JiraSearchAllowedUsersForIssue(JiraBaseAction):
    def _run(self, user, **kwargs):
      return self.jira.search_allowed_users_for_issue(user)

