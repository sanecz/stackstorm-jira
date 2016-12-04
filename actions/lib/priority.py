from base import JiraBaseAction


class JiraPriority(JiraBaseAction):
    def _run(self, id):
      return self.jira.priority(id)

