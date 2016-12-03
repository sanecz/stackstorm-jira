from base import JiraBaseAction


class JiraConfirmProjectAvatar(JiraBaseAction):
    def _run(self, project, cropping_properties):
      return self.jira.confirm_project_avatar(project, cropping_properties)

