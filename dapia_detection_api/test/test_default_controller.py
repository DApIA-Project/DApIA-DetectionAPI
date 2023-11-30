import unittest
from dapia_detection_api.controllers.default_controller import classify_aircrafts
from dapia_detection_api.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_classify_aircrafts_valid(self):
        """Test case for classify_aircraft

        Send a message ADS-B to the server.
        """
        example_message = {
            'message': [{
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
            ]
        }
        # Appelez votre fonction de classification
        result = classify_aircrafts(example_message)

        # Vérifiez si le résultat est correct
        self.assertEqual(result[0][0]['icao24'], '39ac45')
        self.assertEqual(result[0][0]['timestamp'], '1656652128')
        self.assertEqual(result[0][0]['prediction'], 'HELICOPTER')
        self.assertEqual(result[0][0]['truth'], 'HELICOPTER')
        self.assertEqual(result[1],200)



    def test_classify_many_aircrafts_valid(self):
        """Test case for classify_aircraft

        Send a message ADS-B to the server.
        """
        example_message = {
            'message': [{
                'timestamp': '1481274833',
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
            },
            {
                'timestamp': '1481274833',
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
            },
            {
                'timestamp': '1481274833',
                'icao24': '391245',
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
            },
            {
                'timestamp': '1481274834',
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
            },
            {
                'timestamp': '1481274834',
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
            },
            {
                'timestamp': '1481274834',
                'icao24': '391245',
                'latitude': '43.61274338327598',
                'longitude': '1.4005606513261897',
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
            }
            ]
        }
        # Appelez votre fonction de classification
        result = classify_aircrafts(example_message)

        # Vérifiez si le résultat est correct
        self.assertEqual(result[0][0]['icao24'], '396441')
        self.assertEqual(result[0][0]['timestamp'], '1481274833')
        self.assertEqual(result[0][0]['prediction'], 'PLANE')
        self.assertEqual(result[0][0]['truth'], 'UNKNOWN')

        self.assertEqual(result[0][1]['icao24'], '396441')
        self.assertEqual(result[0][1]['timestamp'], '1481274834')
        self.assertEqual(result[0][1]['prediction'], 'PLANE')
        self.assertEqual(result[0][1]['truth'], 'UNKNOWN')

        self.assertEqual(result[0][2]['icao24'], '391245')
        self.assertEqual(result[0][2]['timestamp'], '1481274833')
        self.assertEqual(result[0][2]['prediction'], 'HELICOPTER')
        self.assertEqual(result[0][2]['truth'], 'UNKNOWN')

        self.assertEqual(result[0][3]['icao24'], '391245')
        self.assertEqual(result[0][3]['timestamp'], '1481274834')
        self.assertEqual(result[0][3]['prediction'], 'HELICOPTER')
        self.assertEqual(result[0][3]['truth'], 'UNKNOWN')
        self.assertEqual(result[1], 200)


    def test_classify_aircrafts_valid_truth_unknown(self):
        """Test case for classify_aircraft

        Send a message ADS-B to the server.
        """
        example_message = {
            'message': [{
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
            }]
        }
        # Appelez votre fonction de classification
        result = classify_aircrafts(example_message)

        # Vérifiez si le résultat est correct
        self.assertEqual(result[0][0]['icao24'], '')
        self.assertEqual(result[0][0]['timestamp'], '1656652128')
        self.assertEqual(result[0][0]['prediction'], 'HELICOPTER')
        self.assertEqual(result[0][0]['truth'], 'UNKNOWN')
        self.assertEqual(result[1],200)


    def test_classify_aircrafts_invalid_missing_icao(self):
        """Test case for classify_aircraft

        Send a message ADS-B to the server.
        """
        example_message = {
            'message': [{
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
            }]
        }
        # Appelez votre fonction de classification
        result = classify_aircrafts(example_message)

        # Vérifiez si le résultat est correct
        self.assertEqual(result[0][0]['messages'], example_message['message'])
        self.assertEqual(result[0][0]['error'], "'icao24'")
        self.assertEqual(result[1],500)

    def test_classify_aircrafts_valid2(self):
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
        self.assertEqual(result[0][0]['icao24'], '396441')
        self.assertEqual(result[0][0]['timestamp'], '1481274814')
        self.assertEqual(result[0][0]['prediction'], 'PLANE')
        self.assertEqual(result[0][0]['truth'], 'UNKNOWN')
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
        self.assertEqual(result[0][0]['messages'], example_message['message'])
        self.assertEqual(result[0][0]['error'], "'icao24'")
        self.assertEqual(result[1], 500)

    def test_classify_aircrafts_no_valid_missing_icao_second_message(self):
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
        self.assertEqual(result[0][0]['messages'], example_message['message'])
        self.assertEqual(result[0][0]['error'], "'icao24'")
        self.assertEqual(result[1], 500)

    def test_classify_aircrafts_valid3(self):
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
        self.assertEqual(result[0][0]['icao24'], '394C19')
        self.assertEqual(result[0][0]['timestamp'], '1481274814')
        self.assertEqual(result[0][0]['prediction'], 'HELICOPTER')
        self.assertEqual(result[0][0]['truth'], 'UNKNOWN')
        self.assertEqual(result[1],200)


    def test_classify_aircrafts_valid4(self):
        """Test case for classify_aircrafts

        Send an array message ADS-B to the server.
        """
        example_message = {
            'message': [
                {
                    'timestamp': '1656766070',
                    'icao24': '39ac45',
                    'latitude': '43.60437',
                    'longitude': '1.23156',
                    'groundspeed': '116',
                    'track': '311.1',
                    'vertical_rate': '64',
                    'callsign': 'SAMUCF',
                    'onground': 'False',
                    'alert': 'False',
                    'spi': 'False',
                    'squawk': 'NaN',
                    'altitude': '1850.0',
                    'geoaltitude': '1850',
                    'last_position': '',
                    'lastcontact': '',
                    'hour': '',
                }

            ]
        }
        # Appelez votre fonction de classification
        result = classify_aircrafts(example_message)

        # Vérifiez si le résultat est correct
        self.assertEqual(result[0][0]['icao24'], '39ac45')
        self.assertEqual(result[0][0]['timestamp'], '1656766070')
        self.assertEqual(result[0][0]['prediction'], 'HELICOPTER')
        self.assertEqual(result[0][0]['truth'], 'HELICOPTER')
        self.assertEqual(result[1],200)

if __name__ == '__main__':
    unittest.main()
