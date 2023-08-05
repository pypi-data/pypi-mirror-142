# coding: utf-8

"""
    Investor8.Core

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ValidateWatchlistNameRequestDto(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'user_id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'user_id': 'UserId',
        'name': 'Name'
    }

    def __init__(self, user_id=None, name=None):  # noqa: E501
        """ValidateWatchlistNameRequestDto - a model defined in Swagger"""  # noqa: E501
        self._user_id = None
        self._name = None
        self.discriminator = None
        if user_id is not None:
            self.user_id = user_id
        if name is not None:
            self.name = name

    @property
    def user_id(self):
        """Gets the user_id of this ValidateWatchlistNameRequestDto.  # noqa: E501


        :return: The user_id of this ValidateWatchlistNameRequestDto.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ValidateWatchlistNameRequestDto.


        :param user_id: The user_id of this ValidateWatchlistNameRequestDto.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def name(self):
        """Gets the name of this ValidateWatchlistNameRequestDto.  # noqa: E501


        :return: The name of this ValidateWatchlistNameRequestDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ValidateWatchlistNameRequestDto.


        :param name: The name of this ValidateWatchlistNameRequestDto.  # noqa: E501
        :type: str
        """

        self._name = name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ValidateWatchlistNameRequestDto, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ValidateWatchlistNameRequestDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
