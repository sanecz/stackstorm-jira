from base import JiraBaseAction


class JiraCreateTempUserAvatar(JiraBaseAction):
    def _run(self, user, filename, size, avatar_img, **kwargs):
      return self.jira.create_temp_user_avatar(user, filename, size, avatar_img)

