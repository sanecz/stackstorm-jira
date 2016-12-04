from base import JiraBaseAction


class JiraRemoteLink(JiraBaseAction):
    def _run(self, issue, id):
      return self.jira.remote_link(issue, id)

