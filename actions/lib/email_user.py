from base import JiraBaseAction


class JiraEmailUser(JiraBaseAction):
    def _run(self, user, body, **kwargs):
      return self.jira.email_user(user, body)

