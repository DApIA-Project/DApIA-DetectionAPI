from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from dapia_detection_api.models.base_model import Model
from dapia_detection_api import util


class Data(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, messages=None, error=None):  # noqa: E501
        """Data - a model defined in OpenAPI

        :param messages: The messages of this Data.  # noqa: E501
        :type messages: List[object]
        :param error: The error of this Data.  # noqa: E501
        :type error: str
        """
        self.openapi_types = {
            'messages': List[object],
            'error': str
        }

        self.attribute_map = {
            'messages': 'messages',
            'error': 'error'
        }

        self._messages = messages
        self._error = error

    @classmethod
    def from_dict(cls, dikt) -> 'Data':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The data of this Data.  # noqa: E501
        :rtype: Data
        """
        return util.deserialize_model(dikt, cls)

    @property
    def messages(self) -> List[object]:
        """Gets the messages of this Data.


        :return: The messages of this Data.
        :rtype: List[object]
        """
        return self._messages

    @messages.setter
    def messages(self, messages: List[object]):
        """Sets the messages of this Data.


        :param messages: The messages of this Data.
        :type messages: List[object]
        """

        self._messages = messages

    @property
    def error(self) -> str:
        """Gets the error of this Data.

        Error name found  # noqa: E501

        :return: The error of this Data.
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error: str):
        """Sets the error of this Data.

        Error name found  # noqa: E501

        :param error: The error of this Data.
        :type error: str
        """

        self._error = error
