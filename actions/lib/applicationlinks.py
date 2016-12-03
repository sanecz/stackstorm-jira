from base import JiraBaseAction


class JiraApplicationlinks(JiraBaseAction):
    def _run(self, **kwargs):
      return self.jira.applicationlinks(**kwargs)

