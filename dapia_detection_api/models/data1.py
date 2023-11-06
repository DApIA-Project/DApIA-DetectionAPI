from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from dapia_detection_api.models.base_model import Model
from dapia_detection_api import util


class Data1(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, message=None, error=None):  # noqa: E501
        """Data1 - a model defined in OpenAPI

        :param message: The message of this Data1.  # noqa: E501
        :type message: object
        :param error: The error of this Data1.  # noqa: E501
        :type error: str
        """
        self.openapi_types = {
            'message': object,
            'error': str
        }

        self.attribute_map = {
            'message': 'message',
            'error': 'error'
        }

        self._message = message
        self._error = error

    @classmethod
    def from_dict(cls, dikt) -> 'Data1':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The data_1 of this Data1.  # noqa: E501
        :rtype: Data1
        """
        return util.deserialize_model(dikt, cls)

    @property
    def message(self) -> object:
        """Gets the message of this Data1.

        An ADS-B message  # noqa: E501

        :return: The message of this Data1.
        :rtype: object
        """
        return self._message

    @message.setter
    def message(self, message: object):
        """Sets the message of this Data1.

        An ADS-B message  # noqa: E501

        :param message: The message of this Data1.
        :type message: object
        """

        self._message = message

    @property
    def error(self) -> str:
        """Gets the error of this Data1.

        Error name found  # noqa: E501

        :return: The error of this Data1.
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error: str):
        """Sets the error of this Data1.

        Error name found  # noqa: E501

        :param error: The error of this Data1.
        :type error: str
        """

        self._error = error
