from base import JiraBaseAction


class JiraComponentCountRelatedIssues(JiraBaseAction):
    def _run(self, id):
      return self.jira.component_count_related_issues(str(id))

