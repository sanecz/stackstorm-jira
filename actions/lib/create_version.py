from base import JiraBaseAction


class JiraCreateVersion(JiraBaseAction):
    def _run(self, name, project, **kwargs):
      return self.jira.create_version(name, project, **kwargs)

