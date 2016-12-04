from base import JiraBaseAction


class JiraSetProjectAvatar(JiraBaseAction):
    def _run(self, project, avatar):
      return self.jira.set_project_avatar(project, avatar)

