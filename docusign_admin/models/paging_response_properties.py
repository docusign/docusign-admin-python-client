# coding: utf-8

"""
    Docusign Admin API

    An API for an organization administrator to manage organizations, accounts and users  # noqa: E501

    OpenAPI spec version: v2.1
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from docusign_admin.client.configuration import Configuration


class PagingResponseProperties(object):
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
        'result_set_size': 'int',
        'result_set_start_position': 'int',
        'result_set_end_position': 'int',
        'total_set_size': 'int',
        'next': 'str',
        'previous': 'str'
    }

    attribute_map = {
        'result_set_size': 'result_set_size',
        'result_set_start_position': 'result_set_start_position',
        'result_set_end_position': 'result_set_end_position',
        'total_set_size': 'total_set_size',
        'next': 'next',
        'previous': 'previous'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """PagingResponseProperties - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._result_set_size = None
        self._result_set_start_position = None
        self._result_set_end_position = None
        self._total_set_size = None
        self._next = None
        self._previous = None
        self.discriminator = None

        setattr(self, "_{}".format('result_set_size'), kwargs.get('result_set_size', None))
        setattr(self, "_{}".format('result_set_start_position'), kwargs.get('result_set_start_position', None))
        setattr(self, "_{}".format('result_set_end_position'), kwargs.get('result_set_end_position', None))
        setattr(self, "_{}".format('total_set_size'), kwargs.get('total_set_size', None))
        setattr(self, "_{}".format('next'), kwargs.get('next', None))
        setattr(self, "_{}".format('previous'), kwargs.get('previous', None))

    @property
    def result_set_size(self):
        """Gets the result_set_size of this PagingResponseProperties.  # noqa: E501


        :return: The result_set_size of this PagingResponseProperties.  # noqa: E501
        :rtype: int
        """
        return self._result_set_size

    @result_set_size.setter
    def result_set_size(self, result_set_size):
        """Sets the result_set_size of this PagingResponseProperties.


        :param result_set_size: The result_set_size of this PagingResponseProperties.  # noqa: E501
        :type: int
        """

        self._result_set_size = result_set_size

    @property
    def result_set_start_position(self):
        """Gets the result_set_start_position of this PagingResponseProperties.  # noqa: E501


        :return: The result_set_start_position of this PagingResponseProperties.  # noqa: E501
        :rtype: int
        """
        return self._result_set_start_position

    @result_set_start_position.setter
    def result_set_start_position(self, result_set_start_position):
        """Sets the result_set_start_position of this PagingResponseProperties.


        :param result_set_start_position: The result_set_start_position of this PagingResponseProperties.  # noqa: E501
        :type: int
        """

        self._result_set_start_position = result_set_start_position

    @property
    def result_set_end_position(self):
        """Gets the result_set_end_position of this PagingResponseProperties.  # noqa: E501


        :return: The result_set_end_position of this PagingResponseProperties.  # noqa: E501
        :rtype: int
        """
        return self._result_set_end_position

    @result_set_end_position.setter
    def result_set_end_position(self, result_set_end_position):
        """Sets the result_set_end_position of this PagingResponseProperties.


        :param result_set_end_position: The result_set_end_position of this PagingResponseProperties.  # noqa: E501
        :type: int
        """

        self._result_set_end_position = result_set_end_position

    @property
    def total_set_size(self):
        """Gets the total_set_size of this PagingResponseProperties.  # noqa: E501


        :return: The total_set_size of this PagingResponseProperties.  # noqa: E501
        :rtype: int
        """
        return self._total_set_size

    @total_set_size.setter
    def total_set_size(self, total_set_size):
        """Sets the total_set_size of this PagingResponseProperties.


        :param total_set_size: The total_set_size of this PagingResponseProperties.  # noqa: E501
        :type: int
        """

        self._total_set_size = total_set_size

    @property
    def next(self):
        """Gets the next of this PagingResponseProperties.  # noqa: E501


        :return: The next of this PagingResponseProperties.  # noqa: E501
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this PagingResponseProperties.


        :param next: The next of this PagingResponseProperties.  # noqa: E501
        :type: str
        """

        self._next = next

    @property
    def previous(self):
        """Gets the previous of this PagingResponseProperties.  # noqa: E501


        :return: The previous of this PagingResponseProperties.  # noqa: E501
        :rtype: str
        """
        return self._previous

    @previous.setter
    def previous(self, previous):
        """Sets the previous of this PagingResponseProperties.


        :param previous: The previous of this PagingResponseProperties.  # noqa: E501
        :type: str
        """

        self._previous = previous

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
        if issubclass(PagingResponseProperties, dict):
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
        if not isinstance(other, PagingResponseProperties):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PagingResponseProperties):
            return True

        return self.to_dict() != other.to_dict()
