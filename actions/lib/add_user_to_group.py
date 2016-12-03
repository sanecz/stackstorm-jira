from base import JiraBaseAction


class JiraAddUserToGroup(JiraBaseAction):
    def _run(self, username, group):
      return self.jira.add_user_to_group(username, group)

