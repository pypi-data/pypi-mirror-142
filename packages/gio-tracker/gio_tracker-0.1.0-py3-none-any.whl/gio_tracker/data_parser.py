# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals
import json
import time
from .version import VERSION


class DataParser(object):
    def get_bytes(self, messages, stm=None):
        pass

    def get_params(self, stm=None):
        pass

    def get_headers(self):
        pass

    @staticmethod
    def get_timestamp():
        return int(time.time() * 1000)


class JsonParser(DataParser):

    def __init__(self):
        pass

    def get_bytes(self, messages, stm=None):
        batch = []
        for message in messages:
            batch.append(self.json(message))
        batch_json = '[{0}]'.format(','.join(batch))
        return batch_json

    def get_headers(self):
        return {'content-type': 'application/json'}

    def get_params(self, stm=None):
        return {'stm': stm}

    @staticmethod
    def json_dumps(data, cls=None):
        return json.dumps(data, separators=(',', ':'), cls=cls)

    def json(self, message):
        dict = {}

        # event message
        if hasattr(message, 'event_type') and message.event_type is not None:
            dict['t'] = message.event_type
        if hasattr(message, 'event_time') and message.event_time is not None:
            dict['tm'] = message.event_time
        if hasattr(message, 'login_user_id') and message.login_user_id is not None:
            dict['cs1'] = message.login_user_id
        if hasattr(message, 'event_name') and message.event_name is not None:
            dict['n'] = message.event_name
        if hasattr(message, 'num') and message.num is not None:
            dict['num'] = message.num
        if hasattr(message, 'attributes') and message.attributes is not None:
            dict['var'] = message.attributes

        dict['av'] = VERSION
        dict['b'] = 'python'

        return self.json_dumps(dict)
