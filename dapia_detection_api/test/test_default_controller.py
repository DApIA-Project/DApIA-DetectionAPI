import unittest
from dapia_detection_api.controllers.default_controller import classify_aircraft, classify_aircrafts
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

    def test_classify_aircrafts_valid(self):
        """Test case for classify_aircrafts

        Send an array message ADS-B to the server.
        """
        example_message = {
            'message': [
                {
                    'timestamp': '1481274814',
                    'icao24': '396441',
                    'latitude': '',
                    'longitude': '',
                    'groundspeed': '416.8',
                    'track': '321.2',
                    'vertical_rate': '-1408',
                    'callsign': '',
                    'onground': '',
                    'alert': '',
                    'spi': '',
                    'squawk': '',
                    'altitude': '',
                    'geoaltitude': '',
                    'last_position': '',
                    'lastcontact': '',
                    'hour': '',
                },
                {
                    'timestamp': '1481274814',
                    'icao24': '396441',
                    'latitude': '',
                    'longitude': '',
                    'groundspeed': '',
                    'track': '',
                    'vertical_rate': '',
                    'callsign': '',
                    'onground': 'False',
                    'alert': 'False',
                    'spi': 'False',
                    'squawk': '',
                    'altitude': '',
                    'geoaltitude': '35175',
                    'last_position': '',
                    'lastcontact': '',
                    'hour': '',
                },
                {
                    'timestamp': '1481274814',
                    'icao24': '396441',
                    'latitude': '',
                    'longitude': '',
                    'groundspeed': '',
                    'track': '',
                    'vertical_rate': '',
                    'callsign': '',
                    'onground': 'False',
                    'alert': 'False',
                    'spi': 'False',
                    'squawk': '',
                    'altitude': '',
                    'geoaltitude': '35175',
                    'last_position': '',
                    'lastcontact': '',
                    'hour': '',
                }
            ]
        }
        # Appelez votre fonction de classification
        result = classify_aircrafts(example_message)

        # Vérifiez si le résultat est correct
        self.assertEqual(result[0]['message'], example_message['message'])
        self.assertEqual(result[0]['prediction'], 'PLANE')
        self.assertEqual(result[0]['truth'], 'UNKNOWN')
        self.assertEqual(result[1],200)

    def test_classify_aircrafts_no_valid_missing_icao_first_message(self):
        """Test case for classify_aircrafts

        Send an array message ADS-B to the server.
        """
        example_message = {
            'message': [
                {
                    'timestamp': '1481274815',
                    'latitude': '',
                    'longitude': '',
                    'groundspeed': '416.8',
                    'track': '321.2',
                    'vertical_rate': '-1408',
                    'callsign': '',
                    'onground': '',
                    'alert': '',
                    'spi': '',
                    'squawk': '',
                    'altitude': '',
                    'geoaltitude': '',
                    'last_position': '',
                    'lastcontact': '',
                    'hour': '',
                },
                {
                    'timestamp': '1481274815',
                    'icao24': '396441',
                    'latitude': '',
                    'longitude': '',
                    'groundspeed': '',
                    'track': '',
                    'vertical_rate': '',
                    'callsign': '',
                    'onground': 'False',
                    'alert': 'False',
                    'spi': 'False',
                    'squawk': '',
                    'altitude': '',
                    'geoaltitude': '35175',
                    'last_position': '',
                    'lastcontact': '',
                    'hour': '',
                },
                {
                    'timestamp': '1481274815',
                    'icao24': '396441',
                    'latitude': '',
                    'longitude': '',
                    'groundspeed': '',
                    'track': '',
                    'vertical_rate': '',
                    'callsign': '',
                    'onground': 'False',
                    'alert': 'False',
                    'spi': 'False',
                    'squawk': '',
                    'altitude': '',
                    'geoaltitude': '35175',
                    'last_position': '',
                    'lastcontact': '',
                    'hour': '',
                }
            ]
        }
        # Appelez votre fonction de classification
        result = classify_aircrafts(example_message)

        # Vérifiez si le résultat est correct
        self.assertEqual(result[0]['message'], example_message['message'])
        self.assertEqual(result[0]['error'], "<AdsbMessageField.ICAO: 'icao24'>")
        self.assertEqual(result[1], 500)

    def test_classify_aircrafts_valid_missing_icao_second_message(self):
        """Test case for classify_aircrafts

        Send an array message ADS-B to the server.
        """
        example_message = {
            'message': [
                {
                    'timestamp': '1481274816',
                    'icao24': '396441',
                    'latitude': '',
                    'longitude': '',
                    'groundspeed': '416.8',
                    'track': '321.2',
                    'vertical_rate': '-1408',
                    'callsign': '',
                    'onground': '',
                    'alert': '',
                    'spi': '',
                    'squawk': '',
                    'altitude': '',
                    'geoaltitude': '',
                    'last_position': '',
                    'lastcontact': '',
                    'hour': '',
                },
                {
                    'timestamp': '1481274816',
                    'latitude': '',
                    'longitude': '',
                    'groundspeed': '',
                    'track': '',
                    'vertical_rate': '',
                    'callsign': '',
                    'onground': 'False',
                    'alert': 'False',
                    'spi': 'False',
                    'squawk': '',
                    'altitude': '',
                    'geoaltitude': '35175',
                    'last_position': '',
                    'lastcontact': '',
                    'hour': '',
                },
                {
                    'timestamp': '1481274816',
                    'icao24': '396441',
                    'latitude': '',
                    'longitude': '',
                    'groundspeed': '',
                    'track': '',
                    'vertical_rate': '',
                    'callsign': '',
                    'onground': 'False',
                    'alert': 'False',
                    'spi': 'False',
                    'squawk': '',
                    'altitude': '',
                    'geoaltitude': '35175',
                    'last_position': '',
                    'lastcontact': '',
                    'hour': '',
                }
            ]
        }
        # Appelez votre fonction de classification
        result = classify_aircrafts(example_message)

        # Vérifiez si le résultat est correct
        self.assertEqual(result[0]['message'], example_message['message'])
        self.assertEqual(result[0]['prediction'], 'LIGHT')
        self.assertEqual(result[0]['truth'], 'UNKNOWN')
        self.assertEqual(result[1], 200)

    def test_classify_aircrafts_valid2(self):
        """Test case for classify_aircrafts

        Send an array message ADS-B to the server.
        """
        example_message = {
            'message': [
                {
                    'timestamp': '1481274814',
                    'icao24': '394C19',
                    'latitude': '',
                    'longitude': '',
                    'groundspeed': '',
                    'track': '',
                    'vertical_rate': '',
                    'callsign': '',
                    'onground': 'False',
                    'alert': '',
                    'spi': '',
                    'squawk': '',
                    'altitude': '',
                    'geoaltitude': '',
                    'last_position': '',
                    'lastcontact': '',
                    'hour': '',
                },
                {
                    'timestamp': '1481274814',
                    'icao24': '394C19',
                    'latitude': '43.56546',
                    'longitude': '0.90741',
                    'groundspeed': '',
                    'track': '',
                    'vertical_rate': '',
                    'callsign': '',
                    'onground': 'False',
                    'alert': 'False',
                    'spi': 'False',
                    'squawk': '',
                    'altitude': '',
                    'geoaltitude': '23800',
                    'last_position': '',
                    'lastcontact': '',
                    'hour': '',
                }

            ]
        }
        # Appelez votre fonction de classification
        result = classify_aircrafts(example_message)

        # Vérifiez si le résultat est correct
        self.assertEqual(result[0]['message'], example_message['message'])
        self.assertEqual(result[0]['prediction'], 'LIGHT')
        self.assertEqual(result[0]['truth'], 'UNKNOWN')
        self.assertEqual(result[1],200)

if __name__ == '__main__':
    unittest.main()
