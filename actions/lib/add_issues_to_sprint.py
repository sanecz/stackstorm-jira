from base import JiraBaseAction


class JiraAddIssuesToSprint(JiraBaseAction):
    def _run(self, sprint_id, issue_keys):
      return self.jira.add_issues_to_sprint(sprint_id, issue_keys)

