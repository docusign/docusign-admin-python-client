# coding: utf-8

"""
    DocuSign Admin API

    An API for an organization administrator to manage organizations, accounts and users  # noqa: E501

    OpenAPI spec version: v2.1
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from docusign_admin.client.configuration import Configuration


class UsersUpdateResponse(object):
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
        'success': 'bool',
        'users': 'list[UserUpdateResponse]'
    }

    attribute_map = {
        'success': 'success',
        'users': 'users'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """UsersUpdateResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._success = None
        self._users = None
        self.discriminator = None

        setattr(self, "_{}".format('success'), kwargs.get('success', None))
        setattr(self, "_{}".format('users'), kwargs.get('users', None))

    @property
    def success(self):
        """Gets the success of this UsersUpdateResponse.  # noqa: E501


        :return: The success of this UsersUpdateResponse.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this UsersUpdateResponse.


        :param success: The success of this UsersUpdateResponse.  # noqa: E501
        :type: bool
        """

        self._success = success

    @property
    def users(self):
        """Gets the users of this UsersUpdateResponse.  # noqa: E501


        :return: The users of this UsersUpdateResponse.  # noqa: E501
        :rtype: list[UserUpdateResponse]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this UsersUpdateResponse.


        :param users: The users of this UsersUpdateResponse.  # noqa: E501
        :type: list[UserUpdateResponse]
        """

        self._users = users

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
        if issubclass(UsersUpdateResponse, dict):
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
        if not isinstance(other, UsersUpdateResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UsersUpdateResponse):
            return True

        return self.to_dict() != other.to_dict()
