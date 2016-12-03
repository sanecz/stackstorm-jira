from base import JiraBaseAction


class JiraDeleteProjectAvatar(JiraBaseAction):
    def _run(self, project, avatar):
      return self.jira.delete_project_avatar(project, avatar)

