from base import JiraBaseAction


class JiraRemoveUserFromGroup(JiraBaseAction):
    def _run(self, username, groupname):
      return self.jira.remove_user_from_group(username, groupname)

