from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from dapia_detection_api.models.base_model import Model
from dapia_detection_api import util


class ClassifyAircraftRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, message=None):  # noqa: E501
        """ClassifyAircraftRequest - a model defined in OpenAPI

        :param message: The message of this ClassifyAircraftRequest.  # noqa: E501
        :type message: object
        """
        self.openapi_types = {
            'message': object
        }

        self.attribute_map = {
            'message': 'message'
        }

        self._message = message

    @classmethod
    def from_dict(cls, dikt) -> 'ClassifyAircraftRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The classify_aircraft_request of this ClassifyAircraftRequest.  # noqa: E501
        :rtype: ClassifyAircraftRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def message(self) -> object:
        """Gets the message of this ClassifyAircraftRequest.

        An ADS-B message  # noqa: E501

        :return: The message of this ClassifyAircraftRequest.
        :rtype: object
        """
        return self._message

    @message.setter
    def message(self, message: object):
        """Sets the message of this ClassifyAircraftRequest.

        An ADS-B message  # noqa: E501

        :param message: The message of this ClassifyAircraftRequest.
        :type message: object
        """

        self._message = message