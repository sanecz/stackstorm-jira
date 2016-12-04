from base import JiraBaseAction


class JiraSprint(JiraBaseAction):
    def _run(self, id):
      return self.jira.sprint(id)

