from base import JiraBaseAction


class JiraRemoveVote(JiraBaseAction):
    def _run(self, issue):
      return self.jira.remove_vote(issue)

