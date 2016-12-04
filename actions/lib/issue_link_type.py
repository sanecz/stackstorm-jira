from base import JiraBaseAction


class JiraIssueLinkType(JiraBaseAction):
    def _run(self, id):
      return self.jira.issue_link_type(id)

