from base import JiraBaseAction


class JiraAddAttachment(JiraBaseAction):
    def _run(self, issue, attachment, **kwargs):
      return self.jira.add_attachment(issue, attachment, **kwargs)

