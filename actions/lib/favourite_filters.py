from base import JiraBaseAction


class JiraFavouriteFilters(JiraBaseAction):
    def _run(self, ):
      return self.jira.favourite_filters()

