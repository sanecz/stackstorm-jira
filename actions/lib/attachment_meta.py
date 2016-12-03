from base import JiraBaseAction


class JiraAttachmentMeta(JiraBaseAction):
    def _run(self):
      return self.jira.attachment_meta()

