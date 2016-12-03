from base import JiraBaseAction


class JiraAddVote(JiraBaseAction):
    def _run(self, issue):
      return self.jira.add_vote(issue)

