from base import JiraBaseAction


class JiraVersionCountRelatedIssues(JiraBaseAction):
    def _run(self, id):
      return self.jira.version_count_related_issues(id)

