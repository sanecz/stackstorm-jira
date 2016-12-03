from base import JiraBaseAction


class JiraConfirmUserAvatar(JiraBaseAction):
    def _run(self, user, cropping_properties):
      return self.jira.confirm_user_avatar(user, cropping_properties)

