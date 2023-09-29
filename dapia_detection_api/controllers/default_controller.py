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

    messages = message_by_icao[icao]
    if len(messages) == CONTEXT.HISTORY + 1:
        df = pd.DataFrame(messages)
        data = df.values

        # Trouver l'indice de chaque colonne
        # column_indices = {header: index for index, header in enumerate(headers)}

        # Convertir les colonnes nécessaires en tableaux NumPy
        timestamp = [np.int64(row[0]['timestamp']) for row in data]
        latitude = [np.float64(row[0]['latitude']) for row in data]
        longitude = [np.float64(row[0]['longitude']) for row in data]
        ground_speed = [np.float64(row[0]['groundspeed']) for row in data]
        track = [np.float64(row[0]['track']) for row in data]
        vertical_rate = [np.float64(row[0]['vertical_rate']) for row in data]

        on_ground = [True if row[0]['onground'] == 'True' else False for row in data]
        alert = [True if row[0]['alert'] == 'True' else False for row in data]
        spi = [True if row[0]['spi'] == 'True' else False for row in data]

        squawk = [int(row[0]['squawk']) if row[0]['squawk'] and row[0]['squawk'] != 'NaN' else None for row in
                 data]
        altitude = [np.float64(row[0]['altitude']) for row in data]
        geo_altitude = [np.float64(row[0]['geoaltitude']) for row in data]

        timestamp = [timestamp[i:i + CONTEXT.HISTORY] for i in range(0, len(timestamp) - CONTEXT.HISTORY, 1)]
        latitude = [latitude[i:i + CONTEXT.HISTORY] for i in range(0, len(latitude) - CONTEXT.HISTORY, 1)]
        longitude = [longitude[i:i + CONTEXT.HISTORY] for i in range(0, len(longitude) - CONTEXT.HISTORY, 1)]
        ground_speed = [ground_speed[i:i + CONTEXT.HISTORY] for i in
                       range(0, len(ground_speed) - CONTEXT.HISTORY, 1)]
        track = [track[i:i + CONTEXT.HISTORY] for i in range(0, len(track) - CONTEXT.HISTORY, 1)]
        vertical_rate = [vertical_rate[i:i + CONTEXT.HISTORY] for i in
                        range(0, len(vertical_rate) - CONTEXT.HISTORY, 1)]
        on_ground = [on_ground[i:i + CONTEXT.HISTORY] for i in range(0, len(on_ground) - CONTEXT.HISTORY, 1)]
        alert = [alert[i:i + CONTEXT.HISTORY] for i in range(0, len(alert) - CONTEXT.HISTORY, 1)]
        spi = [spi[i:i + CONTEXT.HISTORY] for i in range(0, len(spi) - CONTEXT.HISTORY, 1)]
        squawk = [squawk[i:i + CONTEXT.HISTORY] for i in range(0, len(squawk) - CONTEXT.HISTORY, 1)]
        altitude = [altitude[i:i + CONTEXT.HISTORY] for i in range(0, len(altitude) - CONTEXT.HISTORY, 1)]
        geo_altitude = [geo_altitude[i:i + CONTEXT.HISTORY] for i in
                       range(0, len(geo_altitude) - CONTEXT.HISTORY, 1)]

        proba = predictAircraftType(
            timestamp,
            latitude,
            longitude,
            ground_speed,
            track,
            vertical_rate,
            on_ground,
            alert,
            spi,
            squawk,
            altitude,
            geo_altitude
        )

        max_proba = [proba[np.argmax(np.max(proba, axis=1))]]
        label = probabilityToLabel(max_proba)
        name = labelToName(label)
        print("prediced : ", name[0])

        messages.pop(0)

        return {'message': message, 'prediction': name[0]}
    else:
        return {'message': message, 'prediction': "Not available"}
