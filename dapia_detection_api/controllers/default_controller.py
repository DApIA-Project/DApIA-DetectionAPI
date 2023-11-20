import copy
import warnings
import numpy as np
from AdsbAnomalyDetector import predictAircraftType, probabilityToLabel, labelToName, getTruthLabelFromIcao

from dapia_detection_api.types.fields import AdsbMessageField

warnings.filterwarnings("ignore", category=FutureWarning, module="AdsbAnomalyDetector")
message_by_icao = {}


def classify_aircrafts(body):
    """Send an array message ADS-B to the server.

         # noqa: E501

        :param body:
        :type body: {message : string}

        :rtype: Union[SendMessagePost200Response, Tuple[SendMessagePost200Response, int], Tuple[SendMessagePost200Response, int, Dict[str, str]]
        """
    print(body)
    originalMessage = copy.copy(body["message"])

    messagesWithoutDouble = mergeDouble(copy.copy(body["message"]))
    if 'error' in messagesWithoutDouble:
        return {'result': {'messages': originalMessage, 'error': messagesWithoutDouble['error']}, 'cpde': 500}
    predictions = {}
    try:
        for messageWithoutDouble in messagesWithoutDouble:

            icao = messageWithoutDouble[AdsbMessageField.ICAO]
            if icao not in predictions:
                predictions[icao] = {}
            timestamp = messageWithoutDouble[AdsbMessageField.TIMESTAMP]
            if timestamp not in predictions[icao]:
                predictions[icao][timestamp] = []

            if messageWithoutDouble[AdsbMessageField.TIMESTAMP] != '' and messageWithoutDouble[
                AdsbMessageField.GROUND_SPEED] is not None:
                messageWithoutDouble[AdsbMessageField.TIMESTAMP] = int(messageWithoutDouble[AdsbMessageField.TIMESTAMP])
            else:
                messageWithoutDouble[AdsbMessageField.TIMESTAMP] = np.nan
            if messageWithoutDouble[AdsbMessageField.LATITUDE] != '' and messageWithoutDouble[
                AdsbMessageField.GROUND_SPEED] is not None:
                messageWithoutDouble[AdsbMessageField.LATITUDE] = float(messageWithoutDouble[AdsbMessageField.LATITUDE])
            else:
                messageWithoutDouble[AdsbMessageField.LATITUDE] = np.nan
            if messageWithoutDouble[AdsbMessageField.LONGITUDE] != '' and messageWithoutDouble[
                AdsbMessageField.GROUND_SPEED] is not None:
                messageWithoutDouble[AdsbMessageField.LONGITUDE] = float(
                    messageWithoutDouble[AdsbMessageField.LONGITUDE])
            else:
                messageWithoutDouble[AdsbMessageField.LONGITUDE] = np.nan
            if messageWithoutDouble[AdsbMessageField.GROUND_SPEED] != '' and messageWithoutDouble[
                AdsbMessageField.GROUND_SPEED] is not None:
                messageWithoutDouble[AdsbMessageField.GROUND_SPEED] = float(
                    messageWithoutDouble[AdsbMessageField.GROUND_SPEED])
            else:
                messageWithoutDouble[AdsbMessageField.GROUND_SPEED] = np.nan
            if messageWithoutDouble[AdsbMessageField.TRACK] != '' and messageWithoutDouble[
                AdsbMessageField.TRACK] is not None:
                messageWithoutDouble[AdsbMessageField.TRACK] = float(messageWithoutDouble[AdsbMessageField.TRACK])
            else:
                messageWithoutDouble[AdsbMessageField.TRACK] = np.nan
            if messageWithoutDouble[AdsbMessageField.VERTICAL_RATE] != '' and messageWithoutDouble[
                AdsbMessageField.VERTICAL_RATE] is not None:
                messageWithoutDouble[AdsbMessageField.VERTICAL_RATE] = float(
                    messageWithoutDouble[AdsbMessageField.VERTICAL_RATE])
            else:
                messageWithoutDouble[AdsbMessageField.VERTICAL_RATE] = np.nan
            if messageWithoutDouble[AdsbMessageField.ALTITUDE] != '' and messageWithoutDouble[
                AdsbMessageField.GROUND_SPEED] is not None:
                messageWithoutDouble[AdsbMessageField.ALTITUDE] = float(messageWithoutDouble[AdsbMessageField.ALTITUDE])
            else:
                messageWithoutDouble[AdsbMessageField.ALTITUDE] = np.nan
            if messageWithoutDouble[AdsbMessageField.GEO_ALTITUDE] != '' and messageWithoutDouble[
                AdsbMessageField.GROUND_SPEED] is not None:
                messageWithoutDouble[AdsbMessageField.GEO_ALTITUDE] = float(
                    messageWithoutDouble[AdsbMessageField.GEO_ALTITUDE])
            else:
                messageWithoutDouble[AdsbMessageField.GEO_ALTITUDE] = np.nan

            if messageWithoutDouble[AdsbMessageField.SQUAWK] != "NaN" and messageWithoutDouble[
                AdsbMessageField.SQUAWK] != "" and messageWithoutDouble[
                AdsbMessageField.SQUAWK] is not None:
                messageWithoutDouble[AdsbMessageField.SQUAWK] = int(messageWithoutDouble[AdsbMessageField.SQUAWK])
            else:
                messageWithoutDouble[AdsbMessageField.SQUAWK] = np.nan

            if messageWithoutDouble[AdsbMessageField.ON_GROUND] == "True":
                messageWithoutDouble[AdsbMessageField.ON_GROUND] = True
            else:
                messageWithoutDouble[AdsbMessageField.ON_GROUND] = False

            if messageWithoutDouble[AdsbMessageField.ALERT] == "True":
                messageWithoutDouble[AdsbMessageField.ALERT] = True
            else:
                messageWithoutDouble[AdsbMessageField.ALERT] = False

            if messageWithoutDouble[AdsbMessageField.SPI] == "True":
                messageWithoutDouble[AdsbMessageField.SPI] = True
            else:
                messageWithoutDouble[AdsbMessageField.SPI] = False

            print(messageWithoutDouble)

            a = predictAircraftType([messageWithoutDouble])
            for icao, proba in a.items():
                predictions[icao][timestamp].append(proba)

        result = []
        for messageWithoutDouble in messagesWithoutDouble:
            labels_flight_1 = probabilityToLabel(predictions[messageWithoutDouble[AdsbMessageField.ICAO]][
                                                     str(messageWithoutDouble[AdsbMessageField.TIMESTAMP])])
            major_label_flight_1 = np.bincount(labels_flight_1).argmax()
            truth = getTruthLabelFromIcao(messageWithoutDouble[AdsbMessageField.ICAO])
            result.append({'icao24': messageWithoutDouble[AdsbMessageField.ICAO],
                           'timestamp': messageWithoutDouble[AdsbMessageField.TIMESTAMP],
                           'prediction': labelToName(major_label_flight_1),
                           'truth': labelToName(truth)})
            print(labelToName(major_label_flight_1), " : ", labelToName(truth))

        return {'result': result, 'code': 200}
    except Exception as e:
        print(e)
        return {'result': {'messages': originalMessage, 'error': f'{e}'}, 'code': 500}


def mergeDouble(messages):
    try:
        messagesWithoutDouble = [messages[0]]
        for message in messages:
            hasBeenMerged = False
            for messageWithoutDouble in messagesWithoutDouble:
                if message[AdsbMessageField.ICAO] == messageWithoutDouble[AdsbMessageField.ICAO] and message[
                    AdsbMessageField.TIMESTAMP] == messageWithoutDouble[AdsbMessageField.TIMESTAMP]:
                    if messageWithoutDouble[AdsbMessageField.ICAO] == '':
                        messageWithoutDouble[AdsbMessageField.ICAO] = message[AdsbMessageField.ICAO]
                    if messageWithoutDouble[AdsbMessageField.TIMESTAMP] == '':
                        messageWithoutDouble[AdsbMessageField.TIMESTAMP] = message[AdsbMessageField.TIMESTAMP]
                    if messageWithoutDouble[AdsbMessageField.LATITUDE] == '':
                        messageWithoutDouble[AdsbMessageField.LATITUDE] = message[AdsbMessageField.LATITUDE]
                    if messageWithoutDouble[AdsbMessageField.LONGITUDE] == '':
                        messageWithoutDouble[AdsbMessageField.LONGITUDE] = message[AdsbMessageField.LONGITUDE]
                    if messageWithoutDouble[AdsbMessageField.GROUND_SPEED] == '':
                        messageWithoutDouble[AdsbMessageField.GROUND_SPEED] = message[AdsbMessageField.GROUND_SPEED]
                    if messageWithoutDouble[AdsbMessageField.TRACK] == '':
                        messageWithoutDouble[AdsbMessageField.TRACK] = message[AdsbMessageField.TRACK]
                    if messageWithoutDouble[AdsbMessageField.VERTICAL_RATE] == '':
                        messageWithoutDouble[AdsbMessageField.VERTICAL_RATE] = message[AdsbMessageField.VERTICAL_RATE]
                    if messageWithoutDouble[AdsbMessageField.CALLSIGN] == '':
                        messageWithoutDouble[AdsbMessageField.CALLSIGN] = message[AdsbMessageField.CALLSIGN]
                    if messageWithoutDouble[AdsbMessageField.ON_GROUND] == '':
                        messageWithoutDouble[AdsbMessageField.ON_GROUND] = message[AdsbMessageField.ON_GROUND]
                    if messageWithoutDouble[AdsbMessageField.ALERT] == '':
                        messageWithoutDouble[AdsbMessageField.ALERT] = message[AdsbMessageField.ALERT]
                    if messageWithoutDouble[AdsbMessageField.SPI] == '':
                        messageWithoutDouble[AdsbMessageField.SPI] = message[AdsbMessageField.SPI]
                    if messageWithoutDouble[AdsbMessageField.SQUAWK] == '':
                        messageWithoutDouble[AdsbMessageField.SQUAWK] = message[AdsbMessageField.SQUAWK]
                    if messageWithoutDouble[AdsbMessageField.ALTITUDE] == '':
                        messageWithoutDouble[AdsbMessageField.ALTITUDE] = message[AdsbMessageField.ALTITUDE]
                    if messageWithoutDouble[AdsbMessageField.GEO_ALTITUDE] == '':
                        messageWithoutDouble[AdsbMessageField.GEO_ALTITUDE] = message[AdsbMessageField.GEO_ALTITUDE]
                    if messageWithoutDouble[AdsbMessageField.LAST_POSITION] == '':
                        messageWithoutDouble[AdsbMessageField.LAST_POSITION] = message[AdsbMessageField.LAST_POSITION]
                    if messageWithoutDouble[AdsbMessageField.LAST_CONTACT] == '':
                        messageWithoutDouble[AdsbMessageField.LAST_CONTACT] = message[AdsbMessageField.LAST_CONTACT]
                    if messageWithoutDouble[AdsbMessageField.HOUR] == '':
                        messageWithoutDouble[AdsbMessageField.HOUR] = message[AdsbMessageField.HOUR]

                    hasBeenMerged = True
            if not hasBeenMerged:
                messagesWithoutDouble.append(message)
        return messagesWithoutDouble
    except Exception as e:
        print(e)
        return [{'error': f'{e}'}]
