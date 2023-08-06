# -*- coding: utf-8 -*-

import time


class CustomEventMessage(object):
    def __init__(self, event_time, event_name, login_user_id, domain, num, attributes, product_id=None):
        self.event_type = "cstm"  # 1
        self.product_id = product_id
        self.event_time = event_time
        self.event_name = event_name
        self.domain = domain
        self.login_user_id = login_user_id
        self.num = num
        self.attributes = attributes

    def set_data_source_id(self, data_source_id):
        self.data_source_id = data_source_id

    def set_product_id(self, product_id):
        self.product_id = product_id

    def __str__(self):
        message_str = '{event_type:' + self.event_type
        message_str += ',event_name:' + self.event_name
        message_str += ',product_id:' + self.product_id
        message_str += ',event_time:' + str(self.event_time)
        if self.num is not None:
            message_str += ',num:' + str(self.num)
        if self.domain is not None:
            message_str += ',domain:' + self.domain
        if self.login_user_id is not None:
            message_str += ',login_user_id:' + self.login_user_id
        if self.attributes is not None:
            message_str += ',attributes:' + str(self.attributes)
        message_str += '}'
        return message_str

    class EventBuilder(object):
        def __init__(self):
            self.product_id = None
            self.event_time = int(time.time() * 1000)
            self.event_name = None
            self.domain = None
            self.num = None
            self.login_user_id = None
            self.attributes = None
            pass

        def set_num(self, num):
            self.num = num
            return self

        def set_product_id(self, product_id):
            self.product_id = product_id
            return self

        def set_event_time(self, timestamp):
            if timestamp is not None:
                self.event_time = timestamp
            return self

        def set_event_name(self, name):
            self.event_name = name
            return self

        def set_domain(self, device_id):
            self.domain = device_id
            return self

        def set_login_user_id(self, user_id):
            self.login_user_id = user_id
            return self

        def add_attribute(self, key, value):
            if self.attributes is None:
                self.attributes = {}
            self.attributes[key] = value
            return self

        def set_attributes(self, map):
            self.attributes = map
            return self

        def build(self):
            return CustomEventMessage(self.event_time, self.event_name,
                                      self.login_user_id, self.domain, self.num, self.attributes,
                                      self.product_id)
