from base import JiraBaseAction


class JiraAddWorklog(JiraBaseAction):
    def _run(self, issue, **kwargs):
      return self.jira.add_worklog(issue)

