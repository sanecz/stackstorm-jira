from base import JiraBaseAction


class JiraAttachment(JiraBaseAction):
    def _run(self, id):
      return self.jira.attachment(id)

