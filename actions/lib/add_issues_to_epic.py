from base import JiraBaseAction


class JiraAddIssuesToEpic(JiraBaseAction):
    def _run(self, epic_id, issue_keys, **kwargs):
      return self.jira.add_issues_to_epic(epic_id, issue_keys, **kwargs)

