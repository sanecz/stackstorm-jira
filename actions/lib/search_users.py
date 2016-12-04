from base import JiraBaseAction


class JiraSearchUsers(JiraBaseAction):
    def _run(self, user, **kwargs):
      return self.jira.search_users(user, **kwargs)

