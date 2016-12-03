from base import JiraBaseAction


class JiraAddSimpleLink(JiraBaseAction):
    def _run(self, issue, object):
      return self.jira.add_simple_link(issue, object)

