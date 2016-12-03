from base import JiraBaseAction


class JiraCreateTempProjectAvatar(JiraBaseAction):
    def _run(self, project, filename, size, avatar_img, **kwargs):
      return self.jira.create_temp_project_avatar(project, filename, size, avatar_img)

