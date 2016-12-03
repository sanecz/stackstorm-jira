from base import JiraBaseAction


class JiraCreateTempUserAvatar(JiraBaseAction):
    def _run(self, user, filename, size, **kwargs):
      avatar_img = open(filename, "r")
      return self.jira.create_temp_user_avatar(user, filename, size, avatar_img.read(), **kwargs)

