from base import JiraBaseAction


class JiraTransitionIssue(JiraBaseAction):
    def _run(self, issue, transition, fieldargs, **kwargs):
      return self.jira.transition_issue(issue, transition, fieldargs)

