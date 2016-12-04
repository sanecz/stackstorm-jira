from base import JiraBaseAction


class JiraWorklogs(JiraBaseAction):
    def _run(self, issue):
      return self.jira.worklogs(issue)

