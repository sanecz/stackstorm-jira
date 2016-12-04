from base import JiraBaseAction


class JiraWorklog(JiraBaseAction):
    def _run(self, issue, id):
      return self.jira.worklog(issue, id)

