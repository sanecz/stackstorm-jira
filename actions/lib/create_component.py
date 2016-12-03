from base import JiraBaseAction


class JiraCreateComponent(JiraBaseAction):
    def _run(self, name, project, **kwargs):
      return self.jira.create_component(name, project)

