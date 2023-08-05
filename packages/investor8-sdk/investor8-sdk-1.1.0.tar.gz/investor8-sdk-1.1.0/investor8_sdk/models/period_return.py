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

class PeriodReturn(object):
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
        'period': 'str',
        '_return': 'float'
    }

    attribute_map = {
        'period': 'Period',
        '_return': 'Return'
    }

    def __init__(self, period=None, _return=None):  # noqa: E501
        """PeriodReturn - a model defined in Swagger"""  # noqa: E501
        self._period = None
        self.__return = None
        self.discriminator = None
        if period is not None:
            self.period = period
        if _return is not None:
            self._return = _return

    @property
    def period(self):
        """Gets the period of this PeriodReturn.  # noqa: E501


        :return: The period of this PeriodReturn.  # noqa: E501
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this PeriodReturn.


        :param period: The period of this PeriodReturn.  # noqa: E501
        :type: str
        """

        self._period = period

    @property
    def _return(self):
        """Gets the _return of this PeriodReturn.  # noqa: E501


        :return: The _return of this PeriodReturn.  # noqa: E501
        :rtype: float
        """
        return self.__return

    @_return.setter
    def _return(self, _return):
        """Sets the _return of this PeriodReturn.


        :param _return: The _return of this PeriodReturn.  # noqa: E501
        :type: float
        """

        self.__return = _return

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
        if issubclass(PeriodReturn, dict):
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
        if not isinstance(other, PeriodReturn):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
