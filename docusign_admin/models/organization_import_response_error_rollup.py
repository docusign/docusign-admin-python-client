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


class OrganizationImportResponseErrorRollup(object):
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
        'error_type': 'str',
        'count': 'int'
    }

    attribute_map = {
        'error_type': 'error_type',
        'count': 'count'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """OrganizationImportResponseErrorRollup - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._error_type = None
        self._count = None
        self.discriminator = None

        setattr(self, "_{}".format('error_type'), kwargs.get('error_type', None))
        setattr(self, "_{}".format('count'), kwargs.get('count', None))

    @property
    def error_type(self):
        """Gets the error_type of this OrganizationImportResponseErrorRollup.  # noqa: E501


        :return: The error_type of this OrganizationImportResponseErrorRollup.  # noqa: E501
        :rtype: str
        """
        return self._error_type

    @error_type.setter
    def error_type(self, error_type):
        """Sets the error_type of this OrganizationImportResponseErrorRollup.


        :param error_type: The error_type of this OrganizationImportResponseErrorRollup.  # noqa: E501
        :type: str
        """

        self._error_type = error_type

    @property
    def count(self):
        """Gets the count of this OrganizationImportResponseErrorRollup.  # noqa: E501


        :return: The count of this OrganizationImportResponseErrorRollup.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this OrganizationImportResponseErrorRollup.


        :param count: The count of this OrganizationImportResponseErrorRollup.  # noqa: E501
        :type: int
        """

        self._count = count

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
        if issubclass(OrganizationImportResponseErrorRollup, dict):
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
        if not isinstance(other, OrganizationImportResponseErrorRollup):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrganizationImportResponseErrorRollup):
            return True

        return self.to_dict() != other.to_dict()
