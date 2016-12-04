from base import JiraBaseAction


class JiraSecurityLevel(JiraBaseAction):
    def _run(self, id):
      return self.jira.security_level(id)

