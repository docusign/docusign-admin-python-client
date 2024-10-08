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


class DSGroupUsersRemoveRequest(object):
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
        'user_ids': 'list[str]',
        'user_emails': 'list[str]'
    }

    attribute_map = {
        'user_ids': 'user_ids',
        'user_emails': 'user_emails'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """DSGroupUsersRemoveRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._user_ids = None
        self._user_emails = None
        self.discriminator = None

        setattr(self, "_{}".format('user_ids'), kwargs.get('user_ids', None))
        setattr(self, "_{}".format('user_emails'), kwargs.get('user_emails', None))

    @property
    def user_ids(self):
        """Gets the user_ids of this DSGroupUsersRemoveRequest.  # noqa: E501


        :return: The user_ids of this DSGroupUsersRemoveRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._user_ids

    @user_ids.setter
    def user_ids(self, user_ids):
        """Sets the user_ids of this DSGroupUsersRemoveRequest.


        :param user_ids: The user_ids of this DSGroupUsersRemoveRequest.  # noqa: E501
        :type: list[str]
        """

        self._user_ids = user_ids

    @property
    def user_emails(self):
        """Gets the user_emails of this DSGroupUsersRemoveRequest.  # noqa: E501


        :return: The user_emails of this DSGroupUsersRemoveRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._user_emails

    @user_emails.setter
    def user_emails(self, user_emails):
        """Sets the user_emails of this DSGroupUsersRemoveRequest.


        :param user_emails: The user_emails of this DSGroupUsersRemoveRequest.  # noqa: E501
        :type: list[str]
        """

        self._user_emails = user_emails

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
        if issubclass(DSGroupUsersRemoveRequest, dict):
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
        if not isinstance(other, DSGroupUsersRemoveRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DSGroupUsersRemoveRequest):
            return True

        return self.to_dict() != other.to_dict()
