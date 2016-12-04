from base import JiraBaseAction


class JiraProjectComponents(JiraBaseAction):
    def _run(self, project):
      return self.jira.project_components(project)

