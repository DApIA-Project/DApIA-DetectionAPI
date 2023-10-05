import numpy as np
import pandas as pd
from AircraftClassifier import predictAircraftType, probabilityToLabel, labelToName, CONTEXT

from dapia_detection_api.types.fields import AdsbMessageField

message_by_icao = {}
dtype = np.dtype([('timestamp', np.int64), ('icao24', 'U6'), ('latitude', np.float64), ('longitude', np.float64),
                  ('groundspeed', np.float64), ('track', np.float64), ('vertical_rate', np.float64),
                  ('callsign', 'U10'), ('onground', bool), ('alert', bool), ('spi', bool), ('squawk', np.float64),
                  ('altitude', np.float64), ('geoaltitude', np.float64), ('last_position', np.float64),
                  ('lastcontact', np.float64), ('hour', np.int64)])


def classify_aircraft(body):  # noqa: E501
    """Send a message ADS-B to the server.

     # noqa: E501

    :param body:
    :type body: {message : string}

    :rtype: Union[SendMessagePost200Response, Tuple[SendMessagePost200Response, int], Tuple[SendMessagePost200Response, int, Dict[str, str]]
    """
    message = body["message"]
    icao = message[AdsbMessageField.ICAO]

    if icao not in message_by_icao:
        message_by_icao[icao] = []
    message_by_icao[icao].append(message)
    messages = message_by_icao[icao][-CONTEXT.HISTORY:]

    if len(messages) == CONTEXT.HISTORY:
        df = (pd.DataFrame(messages)
              .replace('', np.NaN)
              .fillna(method='ffill')
              .fillna(method='bfill')
              .fillna(value=0))

        try:
            probability = predictAircraftType(
                np.array([np.int64(value) for value in df[AdsbMessageField.TIMESTAMP]]).reshape([1, 128]),
                np.array([np.float64(value) for value in df[AdsbMessageField.LATITUDE]]).reshape([1, 128]),
                np.array([np.float64(value) for value in df[AdsbMessageField.LONGITUDE]]).reshape([1, 128]),
                np.array([np.float64(value) for value in df[AdsbMessageField.GROUND_SPEED]]).reshape([1, 128]),
                np.array([np.float64(value) for value in df[AdsbMessageField.TRACK]]).reshape([1, 128]),
                np.array([np.float64(value) for value in df[AdsbMessageField.VERTICAL_RATE]]).reshape([1, 128]),
                np.array([np.bool_(value) for value in df[AdsbMessageField.ON_GROUND]]).reshape([1, 128]),
                np.array([np.bool_(value) for value in df[AdsbMessageField.ALERT]]).reshape([1, 128]),
                np.array([np.bool_(value) for value in df[AdsbMessageField.SPI]]).reshape([1, 128]),
                np.array([np.int64(value) for value in df[AdsbMessageField.SQUAWK]]).reshape([1, 128]),
                np.array([np.float64(value) for value in df[AdsbMessageField.ALTITUDE]]).reshape([1, 128]),
                np.array([np.float64(value) for value in df[AdsbMessageField.GEO_ALTITUDE]]).reshape([1, 128])
            )
            response = {'message': message, 'prediction': probability_to_name(probability)}
        except Exception as e:
            response = {'message': message, 'error': f'{e}'}, 500

        return response
    else:
        return {'message': message, 'prediction': "Not available"}


def probability_to_name(probability):
    label = probabilityToLabel(probability)
    name = labelToName(label)
    if len(name) > 0:
        return name[0]
    return 'Unavailable'
