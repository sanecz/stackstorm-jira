from base import JiraBaseAction


class JiraProjectRoles(JiraBaseAction):
    def _run(self, project):
      return self.jira.project_roles(project)

