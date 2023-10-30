import numpy as np
import pandas as pd
from AdsbAnomalyDetector import predictAircraftType, probabilityToLabel, labelToName, getTruthLabelFromIcao

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
    print(message)
    icao = message[AdsbMessageField.ICAO]

    predictions = {}
    predictions[icao] = []

    a = predictAircraftType([message])
    for icao, proba in a.items():
        predictions[icao].append(proba)
    print("done")
    print(predictions)
