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
    orginalMessage = body["message"]
    message = body["message"]

    try:
        icao = message[AdsbMessageField.ICAO]

        predictions = {}
        predictions[icao] = []
        message[AdsbMessageField.TIMESTAMP] = int(orginalMessage[AdsbMessageField.TIMESTAMP])
        message[AdsbMessageField.LATITUDE] = float(orginalMessage[AdsbMessageField.LATITUDE])
        message[AdsbMessageField.LONGITUDE] = float(orginalMessage[AdsbMessageField.LONGITUDE])
        message[AdsbMessageField.GROUND_SPEED] = float(orginalMessage[AdsbMessageField.GROUND_SPEED])
        message[AdsbMessageField.TRACK] = float(orginalMessage[AdsbMessageField.TRACK])
        message[AdsbMessageField.VERTICAL_RATE] = float(orginalMessage[AdsbMessageField.VERTICAL_RATE])

        message[AdsbMessageField.ALTITUDE] = float(orginalMessage[AdsbMessageField.ALTITUDE])
        message[AdsbMessageField.GEO_ALTITUDE] = float(orginalMessage[AdsbMessageField.GEO_ALTITUDE])

        if message[AdsbMessageField.SQUAWK] != "NaN":
            message[AdsbMessageField.SQUAWK] = int(orginalMessage[AdsbMessageField.SQUAWK])
        else:
            message[AdsbMessageField.SQUAWK] = None

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

        return {'message': orginalMessage, 'prediction': labelToName(major_label_flight_1),
                'truth': labelToName(truth)}, 200
    except Exception as e:
        return {'message': orginalMessage, 'error': f'{e}'}, 500