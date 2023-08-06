# -*- coding: utf-8 -*-

from .data_parser import JsonParser
from .consumer import Consumer


class DebugConsumer(Consumer):
    def __init__(self, product_id, data_parser=None,
                 retry_limit=3, request_timeout=2, retry_backoff_factor=0.25, verify_cert=True):
        super(DebugConsumer, self).__init__(product_id, retry_limit, request_timeout, retry_backoff_factor, verify_cert)
        self._data_parse = data_parser or JsonParser()
        print("GrowingIO Configuration:{"
              + "productId=" + product_id + "}"
              )

    def send(self, message):
        print('SEND MESSAGE:' + str(message))
        request_url = '{0}/v3/{1}/s2s/cstm/'.format("https://collect.growingio.com", self._product_id)
        messages = [message]
        self.post_data(request_url, messages)

    def post_data(self, request_url, messages):
        stm = self._data_parse.get_timestamp()
        data = self._data_parse.get_bytes(messages, stm)
        print("╔═════════════════════════════HTTP POST══════════════════════════════════")
        print("--> POST " + request_url + " HTTP_1_1")
        print(' (' + str(len(data)) + '-byte body)')
        print(self._data_parse.get_headers())
        print(data)

        result = self.send_data(
            request_url,
            data,
            params=self._data_parse.get_params(stm=stm),
            headers=self._data_parse.get_headers()
        )
        print('<-- RESULT:' + str(result))
        print("╚═════════════════════════════POST  END══════════════════════════════════")
