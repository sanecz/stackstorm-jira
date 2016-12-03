from base import JiraBaseAction


class JiraCustomFieldOption(JiraBaseAction):
    def _run(self, id):
      return self.jira.custom_field_option(id)

