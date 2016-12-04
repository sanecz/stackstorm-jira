from base import JiraBaseAction


class JiraVotes(JiraBaseAction):
    def _run(self, issue):
      return self.jira.votes(issue)

