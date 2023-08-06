# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from .version import VERSION
from .default_consumer import DefaultConsumer
from .debug_consumer import DebugConsumer
from .buffered_consumer import BufferedConsumer
from .async_buffered_consumer import AsyncBufferedConsumer
from .consumer import Consumer
from .message import CustomEventMessage

__version__ = VERSION


class GrowingTracker(object):

    def __init__(self, product_id, consumer=None):
        self._product_id = product_id
        self._consumer = consumer or DefaultConsumer(product_id)

    @staticmethod
    def consumer(consumer):
        return GrowingTracker(consumer._product_id, consumer)

    def track_custom_event(self, event_name, login_user_id, event_time=None, domain=None, num=None,
                           attributes=None):
        message = CustomEventMessage.EventBuilder() \
            .set_product_id(self._product_id).set_event_name(event_name).set_event_time(event_time) \
            .set_domain(domain).set_login_user_id(login_user_id).set_num(num).set_attributes(
            attributes).build()
        self._consumer.send(message)

    def track(self, message):
        message.set_product_id(self._product_id)
        self._consumer.send(message)
