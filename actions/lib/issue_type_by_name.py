from base import JiraBaseAction


class JiraIssueTypeByName(JiraBaseAction):
    def _run(self, name):
      return self.jira.issue_type_by_name(name)

