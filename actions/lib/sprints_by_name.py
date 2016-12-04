from base import JiraBaseAction


class JiraSprintsByName(JiraBaseAction):
    def _run(self, id, **kwargs):
      return self.jira.sprints_by_name(id, **kwargs)

