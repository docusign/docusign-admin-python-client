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


class DSGroupAndUsersResponse(object):
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
        'group': 'DSGroupResponse',
        'group_users': 'DSGroupUsersResponse'
    }

    attribute_map = {
        'group': 'group',
        'group_users': 'group_users'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """DSGroupAndUsersResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._group = None
        self._group_users = None
        self.discriminator = None

        setattr(self, "_{}".format('group'), kwargs.get('group', None))
        setattr(self, "_{}".format('group_users'), kwargs.get('group_users', None))

    @property
    def group(self):
        """Gets the group of this DSGroupAndUsersResponse.  # noqa: E501


        :return: The group of this DSGroupAndUsersResponse.  # noqa: E501
        :rtype: DSGroupResponse
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this DSGroupAndUsersResponse.


        :param group: The group of this DSGroupAndUsersResponse.  # noqa: E501
        :type: DSGroupResponse
        """

        self._group = group

    @property
    def group_users(self):
        """Gets the group_users of this DSGroupAndUsersResponse.  # noqa: E501


        :return: The group_users of this DSGroupAndUsersResponse.  # noqa: E501
        :rtype: DSGroupUsersResponse
        """
        return self._group_users

    @group_users.setter
    def group_users(self, group_users):
        """Sets the group_users of this DSGroupAndUsersResponse.


        :param group_users: The group_users of this DSGroupAndUsersResponse.  # noqa: E501
        :type: DSGroupUsersResponse
        """

        self._group_users = group_users

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
        if issubclass(DSGroupAndUsersResponse, dict):
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
        if not isinstance(other, DSGroupAndUsersResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DSGroupAndUsersResponse):
            return True

        return self.to_dict() != other.to_dict()
