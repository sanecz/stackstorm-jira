from base import JiraBaseAction


class JiraCreateIssue(JiraBaseAction):
    def _run(self, key, summary, description, issuetype, fields):
      all_fields = {
        "project": {"key": key},
        "summary": summary,
        "description": description,
        "issuetype": {"name": issuetype}
      }
      if fields:
          all_fields.update(fields)
      return self.jira.create_issue(fields=all_fields)

