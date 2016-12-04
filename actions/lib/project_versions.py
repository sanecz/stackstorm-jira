from base import JiraBaseAction


class JiraProjectVersions(JiraBaseAction):
    def _run(self, project):
      return self.jira.project_versions(project)

