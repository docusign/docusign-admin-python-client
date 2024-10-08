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


class UserProductPermissionProfilesRequest(object):
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
        'email': 'str',
        'product_permission_profiles': 'list[ProductPermissionProfileRequest]'
    }

    attribute_map = {
        'email': 'email',
        'product_permission_profiles': 'product_permission_profiles'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """UserProductPermissionProfilesRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._email = None
        self._product_permission_profiles = None
        self.discriminator = None

        setattr(self, "_{}".format('email'), kwargs.get('email', None))
        setattr(self, "_{}".format('product_permission_profiles'), kwargs.get('product_permission_profiles', None))

    @property
    def email(self):
        """Gets the email of this UserProductPermissionProfilesRequest.  # noqa: E501


        :return: The email of this UserProductPermissionProfilesRequest.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserProductPermissionProfilesRequest.


        :param email: The email of this UserProductPermissionProfilesRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def product_permission_profiles(self):
        """Gets the product_permission_profiles of this UserProductPermissionProfilesRequest.  # noqa: E501


        :return: The product_permission_profiles of this UserProductPermissionProfilesRequest.  # noqa: E501
        :rtype: list[ProductPermissionProfileRequest]
        """
        return self._product_permission_profiles

    @product_permission_profiles.setter
    def product_permission_profiles(self, product_permission_profiles):
        """Sets the product_permission_profiles of this UserProductPermissionProfilesRequest.


        :param product_permission_profiles: The product_permission_profiles of this UserProductPermissionProfilesRequest.  # noqa: E501
        :type: list[ProductPermissionProfileRequest]
        """
        if self._configuration.client_side_validation and product_permission_profiles is None:
            raise ValueError("Invalid value for `product_permission_profiles`, must not be `None`")  # noqa: E501

        self._product_permission_profiles = product_permission_profiles

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
        if issubclass(UserProductPermissionProfilesRequest, dict):
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
        if not isinstance(other, UserProductPermissionProfilesRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserProductPermissionProfilesRequest):
            return True

        return self.to_dict() != other.to_dict()
