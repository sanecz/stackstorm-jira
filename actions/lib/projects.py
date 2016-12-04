from base import JiraBaseAction


class JiraProjects(JiraBaseAction):
    def _run(self):
      return self.jira.projects()

