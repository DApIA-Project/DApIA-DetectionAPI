# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.send_message_post200_response import SendMessagePost200Response  # noqa: E501
from openapi_server.models.send_message_post_request import SendMessagePostRequest  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_send_message_post(self):
        """Test case for send_message_post

        Send a message ADS-B to the server.
        """
        send_message_post_request = openapi_server.SendMessagePostRequest()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/send-message',
            method='POST',
            headers=headers,
            data=json.dumps(send_message_post_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
