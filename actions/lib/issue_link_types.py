from base import JiraBaseAction


class JiraIssueLinkTypes(JiraBaseAction):
    def _run(self, ):
      return self.jira.issue_link_types()

