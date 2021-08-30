# coding: utf-8

"""
    DocuSign Admin API

    An API for an organization administrator to manage organizations, accounts and users  # noqa: E501

    OpenAPI spec version: v2
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PermissionProfileResponse21(object):
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
        'permission_profile_id': 'str',
        'permission_profile_name': 'str'
    }

    attribute_map = {
        'permission_profile_id': 'permission_profile_id',
        'permission_profile_name': 'permission_profile_name'
    }

    def __init__(self, permission_profile_id=None, permission_profile_name=None):  # noqa: E501
        """PermissionProfileResponse21 - a model defined in Swagger"""  # noqa: E501

        self._permission_profile_id = None
        self._permission_profile_name = None
        self.discriminator = None

        if permission_profile_id is not None:
            self.permission_profile_id = permission_profile_id
        if permission_profile_name is not None:
            self.permission_profile_name = permission_profile_name

    @property
    def permission_profile_id(self):
        """Gets the permission_profile_id of this PermissionProfileResponse21.  # noqa: E501


        :return: The permission_profile_id of this PermissionProfileResponse21.  # noqa: E501
        :rtype: str
        """
        return self._permission_profile_id

    @permission_profile_id.setter
    def permission_profile_id(self, permission_profile_id):
        """Sets the permission_profile_id of this PermissionProfileResponse21.


        :param permission_profile_id: The permission_profile_id of this PermissionProfileResponse21.  # noqa: E501
        :type: str
        """

        self._permission_profile_id = permission_profile_id

    @property
    def permission_profile_name(self):
        """Gets the permission_profile_name of this PermissionProfileResponse21.  # noqa: E501


        :return: The permission_profile_name of this PermissionProfileResponse21.  # noqa: E501
        :rtype: str
        """
        return self._permission_profile_name

    @permission_profile_name.setter
    def permission_profile_name(self, permission_profile_name):
        """Sets the permission_profile_name of this PermissionProfileResponse21.


        :param permission_profile_name: The permission_profile_name of this PermissionProfileResponse21.  # noqa: E501
        :type: str
        """

        self._permission_profile_name = permission_profile_name

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
        if issubclass(PermissionProfileResponse21, dict):
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
        if not isinstance(other, PermissionProfileResponse21):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
