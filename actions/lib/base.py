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
            headers = {'response': {}, 'request': {}}
            try:
                error_message = json.loads(e.response.text)
                error_message = " ".join(error_message.get('errorMessages'))
            except ValueError:
                error_message = e.response.text
            if hasattr(e.response, 'text'):
                headers['response'].setdefault('text', e.response.text)
            if hasattr(e.request, 'text'):
                headers['request'].setdefault('text', e.request.text)
            if hasattr(e.response, 'headers'):
                headers['response'].setdefault('headers', e.response.headers)
            if hasattr(e.request, 'headers'):
                headers['request'].setdefault('headers', e.request.headers)
            error_string = u"Error {}: {}\n\nDetails: {}".format(e.status_code, error_message, headers)
            return (False, error_string)
