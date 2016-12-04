from base import JiraBaseAction


class JiraProjectRole(JiraBaseAction):
    def _run(self, project, id):
      return self.jira.project_role(project, id)

