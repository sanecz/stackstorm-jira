from base import JiraBaseAction


class JiraRank(JiraBaseAction):
    def _run(self, issue, next_issue):
      return self.jira.rank(issue, next_issue)

