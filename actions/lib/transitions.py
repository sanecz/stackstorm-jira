from base import JiraBaseAction


class JiraTransitions(JiraBaseAction):
    def _run(self, issue, **kwargs):
      return self.jira.transitions(issue)

