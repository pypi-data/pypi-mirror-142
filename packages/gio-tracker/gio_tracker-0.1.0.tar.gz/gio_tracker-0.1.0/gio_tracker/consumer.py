# -*- coding: utf-8 -*-

import requests
import six
import urllib3


class GrowingIOException(Exception):
    """Raised by consumers when unable to send messages.
    This could be caused by a network outage or interruption.
    """
    pass


class GrowingParamException(Exception):
    """Raised by consumers when unable to send messages.
    This could be caused by a param outage or interruption.
    """
    pass


class Consumer(object):

    def __init__(self, product_id,
                 retry_limit=3,
                 request_timeout=5,
                 retry_backoff_factor=0.25,
                 verify_cert=True):

        if product_id is None:
            raise (GrowingParamException('ProjectId is NULL'))

        server_host = 'https://api.growingio.com'  # /v3/ai/s2s/cstm

        if server_host[-1] == '/':
            self._server_host = server_host[:-1]
        else:
            self._server_host = server_host

        self._product_id = product_id

        self._verify_cert = verify_cert
        self._request_timeout = request_timeout

        self.endpoints = {
            'cstm': '{0}/v3/{1}/s2s/cstm'.format(server_host, product_id),
        }

        retry_args = {
            "total": retry_limit,
            "backoff_factor": retry_backoff_factor,
            "status_forcelist": set(range(500, 600)),
            "allowed_methods": {"POST"},
        }
        adapter = requests.adapters.HTTPAdapter(
            max_retries=urllib3.Retry(**retry_args),
        )

        self._session = requests.Session()
        self._session.mount('http', adapter)

    def send(self, message):
        pass

    def send_data(self, request_url, data, params=None, headers=None):
        return self._write_request(request_url, data, params, headers)

    def _write_request(self, request_url, data, params=None, headers=None):
        print(data)
        request_result = False
        try:
            response = self._session.post(
                request_url,
                data=data,
                timeout=self._request_timeout,
                verify=self._verify_cert,
                params=params,
                headers=headers
            )
        except Exception as e:
            six.raise_from(GrowingIOException(e), e)

        try:
            if response.ok: request_result = True
        except ValueError:
            raise GrowingIOException('Cannot interpret GrowingIO server response: {0}'.format(response.text))

        return request_result
