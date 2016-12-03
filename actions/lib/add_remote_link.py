from base import JiraBaseAction


class JiraAddRemoteLink(JiraBaseAction):
    def _run(self, issue, destination, **kwargs):
      return self.jira.add_remote_link(issue, destination)

