from base import JiraBaseAction


class JiraGetIgrid(JiraBaseAction):
    def _run(self, issueid, customfield, schemeid):
      return self.jira.get_igrid(issueid, customfield, schemeid)

