from base import JiraBaseAction


class JiraRemoteLinks(JiraBaseAction):
    def _run(self, issue):
      return self.jira.remote_links(issue)

