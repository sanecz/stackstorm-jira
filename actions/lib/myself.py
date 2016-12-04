from base import JiraBaseAction


class JiraMyself(JiraBaseAction):
    def _run(self):
      return self.jira.myself()

