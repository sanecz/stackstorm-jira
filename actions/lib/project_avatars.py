from base import JiraBaseAction


class JiraProjectAvatars(JiraBaseAction):
    def _run(self, project):
      return self.jira.project_avatars(project)

