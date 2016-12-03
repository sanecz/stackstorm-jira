from base import JiraBaseAction


class JiraDeleteProject(JiraBaseAction):
    def _run(self, pid):
      return self.jira.delete_project(pid)

