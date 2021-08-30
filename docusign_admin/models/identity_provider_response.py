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


class IdentityProviderResponse(object):
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
        'id': 'str',
        'friendly_name': 'str',
        'auto_provision_users': 'bool',
        'type': 'str',
        'saml_20': 'Saml2IdentityProviderResponse',
        'links': 'list[LinkResponse]'
    }

    attribute_map = {
        'id': 'id',
        'friendly_name': 'friendly_name',
        'auto_provision_users': 'auto_provision_users',
        'type': 'type',
        'saml_20': 'saml_20',
        'links': 'links'
    }

    def __init__(self, id=None, friendly_name=None, auto_provision_users=None, type=None, saml_20=None, links=None):  # noqa: E501
        """IdentityProviderResponse - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._friendly_name = None
        self._auto_provision_users = None
        self._type = None
        self._saml_20 = None
        self._links = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if friendly_name is not None:
            self.friendly_name = friendly_name
        if auto_provision_users is not None:
            self.auto_provision_users = auto_provision_users
        if type is not None:
            self.type = type
        if saml_20 is not None:
            self.saml_20 = saml_20
        if links is not None:
            self.links = links

    @property
    def id(self):
        """Gets the id of this IdentityProviderResponse.  # noqa: E501


        :return: The id of this IdentityProviderResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IdentityProviderResponse.


        :param id: The id of this IdentityProviderResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def friendly_name(self):
        """Gets the friendly_name of this IdentityProviderResponse.  # noqa: E501


        :return: The friendly_name of this IdentityProviderResponse.  # noqa: E501
        :rtype: str
        """
        return self._friendly_name

    @friendly_name.setter
    def friendly_name(self, friendly_name):
        """Sets the friendly_name of this IdentityProviderResponse.


        :param friendly_name: The friendly_name of this IdentityProviderResponse.  # noqa: E501
        :type: str
        """

        self._friendly_name = friendly_name

    @property
    def auto_provision_users(self):
        """Gets the auto_provision_users of this IdentityProviderResponse.  # noqa: E501


        :return: The auto_provision_users of this IdentityProviderResponse.  # noqa: E501
        :rtype: bool
        """
        return self._auto_provision_users

    @auto_provision_users.setter
    def auto_provision_users(self, auto_provision_users):
        """Sets the auto_provision_users of this IdentityProviderResponse.


        :param auto_provision_users: The auto_provision_users of this IdentityProviderResponse.  # noqa: E501
        :type: bool
        """

        self._auto_provision_users = auto_provision_users

    @property
    def type(self):
        """Gets the type of this IdentityProviderResponse.  # noqa: E501


        :return: The type of this IdentityProviderResponse.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IdentityProviderResponse.


        :param type: The type of this IdentityProviderResponse.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def saml_20(self):
        """Gets the saml_20 of this IdentityProviderResponse.  # noqa: E501


        :return: The saml_20 of this IdentityProviderResponse.  # noqa: E501
        :rtype: Saml2IdentityProviderResponse
        """
        return self._saml_20

    @saml_20.setter
    def saml_20(self, saml_20):
        """Sets the saml_20 of this IdentityProviderResponse.


        :param saml_20: The saml_20 of this IdentityProviderResponse.  # noqa: E501
        :type: Saml2IdentityProviderResponse
        """

        self._saml_20 = saml_20

    @property
    def links(self):
        """Gets the links of this IdentityProviderResponse.  # noqa: E501


        :return: The links of this IdentityProviderResponse.  # noqa: E501
        :rtype: list[LinkResponse]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this IdentityProviderResponse.


        :param links: The links of this IdentityProviderResponse.  # noqa: E501
        :type: list[LinkResponse]
        """

        self._links = links

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
        if issubclass(IdentityProviderResponse, dict):
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
        if not isinstance(other, IdentityProviderResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
