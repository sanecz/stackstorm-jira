from base import JiraBaseAction


class JiraRemoveGroup(JiraBaseAction):
    def _run(self, groupname):
      return self.jira.remove_group(groupname)

