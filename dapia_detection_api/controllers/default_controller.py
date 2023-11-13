import copy

import numpy as np
from AdsbAnomalyDetector import predictAircraftType, probabilityToLabel, labelToName, getTruthLabelFromIcao

from dapia_detection_api.types.fields import AdsbMessageField

message_by_icao = {}

def classify_aircrafts(body):
    """Send an array message ADS-B to the server.

         # noqa: E501

        :param body:
        :type body: {message : string}

        :rtype: Union[SendMessagePost200Response, Tuple[SendMessagePost200Response, int], Tuple[SendMessagePost200Response, int, Dict[str, str]]
        """

    originalMessage = copy.copy(body["message"])

    try:
        message = copy.copy(body["message"][0])
        for mes in body["message"]:
            if message[AdsbMessageField.ICAO] == '':
                message[AdsbMessageField.ICAO] = mes[AdsbMessageField.ICAO]
            if message[AdsbMessageField.TIMESTAMP] == '':
                message[AdsbMessageField.TIMESTAMP] = mes[AdsbMessageField.TIMESTAMP]
            if message[AdsbMessageField.LATITUDE] == '':
                message[AdsbMessageField.LATITUDE] = mes[AdsbMessageField.LATITUDE]
            if message[AdsbMessageField.LONGITUDE] == '':
                message[AdsbMessageField.LONGITUDE] = mes[AdsbMessageField.LONGITUDE]
            if message[AdsbMessageField.GROUND_SPEED] == '':
                message[AdsbMessageField.GROUND_SPEED] = mes[AdsbMessageField.GROUND_SPEED]
            if message[AdsbMessageField.TRACK] == '':
                message[AdsbMessageField.TRACK] = mes[AdsbMessageField.TRACK]
            if message[AdsbMessageField.VERTICAL_RATE] == '':
                message[AdsbMessageField.VERTICAL_RATE] = mes[AdsbMessageField.VERTICAL_RATE]
            if message[AdsbMessageField.CALLSIGN] == '':
                message[AdsbMessageField.CALLSIGN] = mes[AdsbMessageField.CALLSIGN]
            if message[AdsbMessageField.ON_GROUND] == '':
                message[AdsbMessageField.ON_GROUND] = mes[AdsbMessageField.ON_GROUND]
            if message[AdsbMessageField.ALERT] == '':
                message[AdsbMessageField.ALERT] = mes[AdsbMessageField.ALERT]
            if message[AdsbMessageField.SPI] == '':
                message[AdsbMessageField.SPI] = mes[AdsbMessageField.SPI]
            if message[AdsbMessageField.SQUAWK] == '':
                message[AdsbMessageField.SQUAWK] = mes[AdsbMessageField.SQUAWK]
            if message[AdsbMessageField.ALTITUDE] == '':
                message[AdsbMessageField.ALTITUDE] = mes[AdsbMessageField.ALTITUDE]
            if message[AdsbMessageField.GEO_ALTITUDE] == '':
                message[AdsbMessageField.GEO_ALTITUDE] = mes[AdsbMessageField.GEO_ALTITUDE]
            if message[AdsbMessageField.LAST_POSITION] == '':
                message[AdsbMessageField.LAST_POSITION] = mes[AdsbMessageField.LAST_POSITION]
            if message[AdsbMessageField.LAST_CONTACT] == '':
                message[AdsbMessageField.LAST_CONTACT] = mes[AdsbMessageField.LAST_CONTACT]
            if message[AdsbMessageField.HOUR] == '':
                message[AdsbMessageField.HOUR] = mes[AdsbMessageField.HOUR]

        icao = message[AdsbMessageField.ICAO]

        predictions = {}
        predictions[icao] = []
        if message[AdsbMessageField.TIMESTAMP] != '':
            message[AdsbMessageField.TIMESTAMP] = int(message[AdsbMessageField.TIMESTAMP])
        else:
            message[AdsbMessageField.TIMESTAMP] = np.nan
        if message[AdsbMessageField.LATITUDE] != '':
            message[AdsbMessageField.LATITUDE] = float(message[AdsbMessageField.LATITUDE])
        else:
            message[AdsbMessageField.LATITUDE] = np.nan
        if message[AdsbMessageField.LONGITUDE] != '':
            message[AdsbMessageField.LONGITUDE] = float(message[AdsbMessageField.LONGITUDE])
        else:
            message[AdsbMessageField.LONGITUDE] = np.nan
        if message[AdsbMessageField.GROUND_SPEED] != '':
            message[AdsbMessageField.GROUND_SPEED] = float(message[AdsbMessageField.GROUND_SPEED])
        else:
            message[AdsbMessageField.GROUND_SPEED] = np.nan
        if message[AdsbMessageField.TRACK] != '':
            message[AdsbMessageField.TRACK] = float(message[AdsbMessageField.TRACK])
        else:
            message[AdsbMessageField.TRACK] = np.nan
        if message[AdsbMessageField.VERTICAL_RATE] != '':
            message[AdsbMessageField.VERTICAL_RATE] = float(message[AdsbMessageField.VERTICAL_RATE])
        else:
            message[AdsbMessageField.VERTICAL_RATE] = np.nan
        if message[AdsbMessageField.ALTITUDE] != '':
            message[AdsbMessageField.ALTITUDE] = float(message[AdsbMessageField.ALTITUDE])
        else:
            message[AdsbMessageField.ALTITUDE] = np.nan
        if message[AdsbMessageField.GEO_ALTITUDE] != '':
            message[AdsbMessageField.GEO_ALTITUDE] = float(message[AdsbMessageField.GEO_ALTITUDE])
        else:
            message[AdsbMessageField.GEO_ALTITUDE] = np.nan

        if message[AdsbMessageField.SQUAWK] != "NaN" and message[AdsbMessageField.SQUAWK] != "":
            message[AdsbMessageField.SQUAWK] = int(message[AdsbMessageField.SQUAWK])
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
