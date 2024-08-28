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


class DeleteUserIdentityRequest(object):
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
        'identities': 'list[UserIdentityRequest]'
    }

    attribute_map = {
        'identities': 'identities'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """DeleteUserIdentityRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._identities = None
        self.discriminator = None

        setattr(self, "_{}".format('identities'), kwargs.get('identities', None))

    @property
    def identities(self):
        """Gets the identities of this DeleteUserIdentityRequest.  # noqa: E501


        :return: The identities of this DeleteUserIdentityRequest.  # noqa: E501
        :rtype: list[UserIdentityRequest]
        """
        return self._identities

    @identities.setter
    def identities(self, identities):
        """Sets the identities of this DeleteUserIdentityRequest.


        :param identities: The identities of this DeleteUserIdentityRequest.  # noqa: E501
        :type: list[UserIdentityRequest]
        """
        if self._configuration.client_side_validation and identities is None:
            raise ValueError("Invalid value for `identities`, must not be `None`")  # noqa: E501

        self._identities = identities

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
        if issubclass(DeleteUserIdentityRequest, dict):
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
        if not isinstance(other, DeleteUserIdentityRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeleteUserIdentityRequest):
            return True

        return self.to_dict() != other.to_dict()
