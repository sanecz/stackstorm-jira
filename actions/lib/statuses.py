from base import JiraBaseAction


class JiraStatuses(JiraBaseAction):
    def _run(self, ):
      return self.jira.statuses()

