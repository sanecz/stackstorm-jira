from base import JiraBaseAction


class JiraAsyncDo(JiraBaseAction):
    def _run(self, **kwargs):
      return self.jira.async_do()

