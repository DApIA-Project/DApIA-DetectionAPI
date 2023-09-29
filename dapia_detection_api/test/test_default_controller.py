import unittest

from flask import json

from dapia_detection_api.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_classify_aircraft(self):
        """Test case for classify_aircraft

        Send a message ADS-B to the server.
        """
        classify_aircraft_request = dapia_detection_api.ClassifyAircraftRequest()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/send-message',
            method='POST',
            headers=headers,
            data=json.dumps(classify_aircraft_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
