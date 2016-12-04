from base import JiraBaseAction


class JiraRenameUser(JiraBaseAction):
    def _run(self, old_user, new_user):
      return self.jira.rename_user(old_user, new_user)

