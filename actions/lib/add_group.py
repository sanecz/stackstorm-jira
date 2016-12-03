from base import JiraBaseAction


class JiraAddGroup(JiraBaseAction):
    def _run(self, groupname):
      return self.jira.add_group(groupname)

