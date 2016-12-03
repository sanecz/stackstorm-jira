from base import JiraBaseAction
import os

class JiraAttachment(JiraBaseAction):
    def _run(self, id):
      attachment = self.jira.attachment(id)
      with open(os.path.join(self.attachment_dir, attachment.filename), "w") as handle:
          handle.write(attachment.get())
      return attachment.filename

