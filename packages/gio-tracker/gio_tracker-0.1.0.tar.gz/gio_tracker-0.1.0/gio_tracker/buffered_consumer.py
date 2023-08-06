# -*- coding: utf-8 -*-
from .default_consumer import DefaultConsumer


class BufferedConsumer(DefaultConsumer):

    def __init__(self, product_id, data_parser=None, max_size=500,
                 retry_limit=3, request_timeout=5, retry_backoff_factor=0.25, verify_cert=True):
        super(BufferedConsumer, self).__init__(product_id, data_parser,
                                               retry_limit, request_timeout, retry_backoff_factor, verify_cert)
        self._events = []
        self._max_size = min(2000, max_size)

    def send(self, message):
        request_url = self.endpoints['cstm']
        buf = self._events
        buf.append(message)
        if len(buf) >= self._max_size:
            self._flush_event(request_url)

    def _flush_event(self, request_url):
        buf = self._events
        while buf:
            batch = buf[:self._max_size]
            self.post_data(request_url, batch)
            buf = buf[self._max_size:]
        self._events = buf

    def flush(self):
        request_url = self.endpoints['cstm']
        self._flush_event(request_url)
