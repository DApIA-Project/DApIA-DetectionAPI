import copy

import numpy as np
from AdsbAnomalyDetector import predictAircraftType, probabilityToLabel, labelToName, getTruthLabelFromIcao

from dapia_detection_api.types.fields import AdsbMessageField

message_by_icao = {}


def classify_aircraft(body):  # noqa: E501
    """Send a message ADS-B to the server.

     # noqa: E501

    :param body:
    :type body: {message : string}

    :rtype: Union[SendMessagePost200Response, Tuple[SendMessagePost200Response, int], Tuple[SendMessagePost200Response, int, Dict[str, str]]
    """

    originalMessage = copy.copy(body["message"])
    message = copy.copy(body["message"])
    try:
        icao = message[AdsbMessageField.ICAO]

        predictions = {}
        predictions[icao] = []
        if message[AdsbMessageField.TIMESTAMP] != '':
            message[AdsbMessageField.TIMESTAMP] = int(originalMessage[AdsbMessageField.TIMESTAMP])
        else:
            message[AdsbMessageField.TIMESTAMP] = np.nan
        if message[AdsbMessageField.LATITUDE] != '':
            message[AdsbMessageField.LATITUDE] = float(originalMessage[AdsbMessageField.LATITUDE])
        else:
            message[AdsbMessageField.LATITUDE] = np.nan
        if message[AdsbMessageField.LONGITUDE] != '':
            message[AdsbMessageField.LONGITUDE] = float(originalMessage[AdsbMessageField.LONGITUDE])
        else:
            message[AdsbMessageField.LONGITUDE] = np.nan
        if message[AdsbMessageField.GROUND_SPEED] != '':
            message[AdsbMessageField.GROUND_SPEED] = float(originalMessage[AdsbMessageField.GROUND_SPEED])
        else:
            message[AdsbMessageField.GROUND_SPEED] = np.nan
        if message[AdsbMessageField.TRACK] != '':
            message[AdsbMessageField.TRACK] = float(originalMessage[AdsbMessageField.TRACK])
        else:
            message[AdsbMessageField.TRACK] = np.nan
        if message[AdsbMessageField.VERTICAL_RATE] != '':
            message[AdsbMessageField.VERTICAL_RATE] = float(originalMessage[AdsbMessageField.VERTICAL_RATE])
        else:
            message[AdsbMessageField.VERTICAL_RATE] = np.nan
        if message[AdsbMessageField.ALTITUDE] != '':
            message[AdsbMessageField.ALTITUDE] = float(originalMessage[AdsbMessageField.ALTITUDE])
        else:
            message[AdsbMessageField.ALTITUDE] = np.nan
        if message[AdsbMessageField.GEO_ALTITUDE] != '':
            message[AdsbMessageField.GEO_ALTITUDE] = float(originalMessage[AdsbMessageField.GEO_ALTITUDE])
        else:
            message[AdsbMessageField.GEO_ALTITUDE] = np.nan

        if message[AdsbMessageField.SQUAWK] != "NaN" and message[AdsbMessageField.SQUAWK] != "":
            message[AdsbMessageField.SQUAWK] = int(originalMessage[AdsbMessageField.SQUAWK])
        else:
            message[AdsbMessageField.SQUAWK] = np.nan

        if message[AdsbMessageField.ON_GROUND] == "True":
            message[AdsbMessageField.ON_GROUND] = True
        else:
            message[AdsbMessageField.ON_GROUND] = False

        if message[AdsbMessageField.ALERT] == "True":
            message[AdsbMessageField.ALERT] = True
        else:
            message[AdsbMessageField.ALERT] = False

        if message[AdsbMessageField.SPI] == "True":
            message[AdsbMessageField.SPI] = True
        else:
            message[AdsbMessageField.SPI] = False

        a = predictAircraftType([message])
        for icao, proba in a.items():
            predictions[icao].append(proba)

        labels_flight_1 = probabilityToLabel(predictions[icao])
        major_label_flight_1 = np.bincount(labels_flight_1).argmax()
        truth = getTruthLabelFromIcao(icao)
        print(labelToName(major_label_flight_1))
        return {'message': originalMessage, 'prediction': labelToName(major_label_flight_1),
                'truth': labelToName(truth)}, 200
    except Exception as e:
        return {'message': originalMessage, 'error': f'{e}'}, 500
