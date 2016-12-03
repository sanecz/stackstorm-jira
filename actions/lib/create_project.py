from base import JiraBaseAction


class JiraCreateProject(JiraBaseAction):
    def _run(self, key, **kwargs):
      return self.jira.create_project(key, **kwargs)

