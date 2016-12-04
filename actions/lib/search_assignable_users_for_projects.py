from base import JiraBaseAction


class JiraSearchAssignableUsersForProjects(JiraBaseAction):
    def _run(self, username, projectKeys, **kwargs):
      return self.jira.search_assignable_users_for_projects(username, projectKeys)

