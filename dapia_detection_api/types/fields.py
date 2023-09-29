from enum import StrEnum


class AdsbMessageField(StrEnum):
    TIMESTAMP = 'timestamp'
    ICAO = 'icao24'
    LATITUDE = 'latitude'
    LONGITUDE = 'longitude'
    GROUND_SPEED = 'groundspeed'
    TRACK = 'track'
    VERTICAL_RATE = 'vertical_rate'
    CALLSIGN = 'callsign'
    ON_GROUND = 'onground'
    ALERT = 'alert'
    SPI = 'spi'
    SQUAWK = 'squawk'
    ALTITUDE = 'altitude'
    GEO_ALTITUDE = 'geoaltitude'
    LAST_POSITION = 'last_position'
    LAST_CONTACT = 'lastcontact'
    HOUR = 'hour'
