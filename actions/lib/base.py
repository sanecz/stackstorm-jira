from st2actions.runners.pythonrunner import Action
from abc import ABCMeta, abstractmethod
from jira import JIRA
from jira.exceptions import JIRAError

import json


class JiraBaseAction(Action):
    __metaclass__ = ABCMeta

    def __init__(self, config):
        super(JiraBaseAction, self).__init__()
        self.attachment_dir = config.get('attachment_dir', '/tmp')
        self._init_jira(config)

    def _init_jira(self, config):
        options = {
            'server': config.get('server')
        }

        with open(config.get('key_cert_path'), 'r') as handle:
            key_cert_content = handle.read()

        oauth = {
            'access_token': config.get('access_token'),
            'access_token_secret': config.get('access_token_secret'),
            'consumer_key': config.get('consumer_key'),
            'key_cert': key_cert_content,
         }

        self.jira = JIRA(options, oauth=oauth)

    @abstractmethod
    def _run(self, *args, **kwargs):
        pass

    def run(self, *args, **kwargs):
        try:
            return (True, self._run(*args, **kwargs))
        except JIRAError as e:
            try:
                error_message = json.loads(e.response.text)
                error_message = " ".join(error_message.get('errorMessages'))
            except ValueError:
                error_message = e.response.text
            error_string = u"Error {}: {}".format(e.status_code, error_message)
            return (False, error_string)
