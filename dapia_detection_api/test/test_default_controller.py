import unittest
from dapia_detection_api.controllers.default_controller import classify_aircraft
from dapia_detection_api.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_classify_aircraft_valid(self):
        """Test case for classify_aircraft

        Send a message ADS-B to the server.
        """
        example_message = {
            'message': {
            'timestamp': '1656652128',
            'icao24': '39ac45',
            'latitude': '43.61274331302966',
            'longitude': '1.4005606515066964',
            'groundspeed': '22.0',
            'track': '327.7243556854224',
            'vertical_rate': '-64.0',
            'callsign': 'SAMUCF',
            'onground': 'False',
            'alert': 'False',
            'spi': 'False',
            'squawk': '7015',
            'altitude': '550.0',
            'geoaltitude': '550.0',
            'last_position': '',
            'lastcontact': '',
            'hour': '',
    }
        }
        # Appelez votre fonction de classification
        result = classify_aircraft(example_message)

        # Vérifiez si le résultat est correct
        self.assertEqual(result[0]['message'], example_message['message'])
        self.assertEqual(result[0]['prediction'], 'HELICOPTER')
        self.assertEqual(result[0]['truth'], 'HELICOPTER')
        self.assertEqual(result[1],200)


    def test_classify_aircraft_valid_truth_unknown(self):
        """Test case for classify_aircraft

        Send a message ADS-B to the server.
        """
        example_message = {
            'message': {
                'timestamp': '1656652128',
                'icao24': '',
                'latitude': '43.61274331302966',
                'longitude': '1.4005606515066964',
                'groundspeed': '22.0',
                'track': '327.7243556854224',
                'vertical_rate': '-64.0',
                'callsign': 'SAMUCF',
                'onground': 'False',
                'alert': 'False',
                'spi': 'False',
                'squawk': '7015',
                'altitude': '550.0',
                'geoaltitude': '550.0',
                'last_position': '',
                'lastcontact': '',
                'hour': '',
            }
        }
        # Appelez votre fonction de classification
        result = classify_aircraft(example_message)

        # Vérifiez si le résultat est correct
        self.assertEqual(result[0]['message'], example_message['message'])
        self.assertEqual(result[0]['prediction'], 'HELICOPTER')
        self.assertEqual(result[0]['truth'], 'UNKNOWN')
        self.assertEqual(result[1],200)


    def test_classify_aircraft_invalid_missing_icao(self):
        """Test case for classify_aircraft

        Send a message ADS-B to the server.
        """
        example_message = {
            'message': {
                'timestamp': '1656652128',
                'latitude': '43.61274331302966',
                'longitude': '1.4005606515066964',
                'groundspeed': '22.0',
                'track': '327.7243556854224',
                'vertical_rate': '-64.0',
                'callsign': 'SAMUCF',
                'onground': 'False',
                'alert': 'False',
                'spi': 'False',
                'squawk': '7015',
                'altitude': '550.0',
                'geoaltitude': '550.0',
                'last_position': '',
                'lastcontact': '',
                'hour': '',
            }
        }
        # Appelez votre fonction de classification
        result = classify_aircraft(example_message)

        # Vérifiez si le résultat est correct
        self.assertEqual(result[0]['message'], example_message['message'])
        self.assertEqual(result[0]['error'], "<AdsbMessageField.ICAO: 'icao24'>")
        self.assertEqual(result[1],500)


if __name__ == '__main__':
    unittest.main()
