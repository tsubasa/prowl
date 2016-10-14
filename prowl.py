from __future__ import print_function

import requests

from .errors import ProwlError

class Prowl(object):

    PUSH_URL = 'https://api.prowlapp.com/publicapi/add'

    def __init__(self, api_key):
        self.api_key = api_key

    def add(self, application, event, description, priority=0, url=None, providerkey=None):
        data = {'apikey': self.api_key, 'application': application, 'event': event, 'description': description, 'priority': priority}

        if url:
            data['url'] = url[0:512]
        if providerkey:
            data['providerkey'] = providerkey

        return self._push(data)

    def _push(self, data):
        r = requests.post(self.PUSH_URL, data=data)

        if r.status_code == requests.codes.ok:
            return True
        else:
            raise ProwlError(r.text)
