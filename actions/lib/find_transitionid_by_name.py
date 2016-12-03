from base import JiraBaseAction


class JiraFindTransitionidByName(JiraBaseAction):
    def _run(self, issue, transition_name):
      return self.jira.find_transitionid_by_name(issue, transition_name)

