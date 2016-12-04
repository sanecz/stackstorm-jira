from base import JiraBaseAction


class JiraGroupMembers(JiraBaseAction):
    def _run(self, group):
      return self.jira.group_members(group)

