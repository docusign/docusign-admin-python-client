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


class OrganizationAccountSettingsImportRequestorResponse(object):
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
        'type': 'str',
        'name': 'str',
        'email': 'str'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'name': 'name',
        'email': 'email'
    }

    def __init__(self, id=None, type=None, name=None, email=None):  # noqa: E501
        """OrganizationAccountSettingsImportRequestorResponse - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._type = None
        self._name = None
        self._email = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if name is not None:
            self.name = name
        if email is not None:
            self.email = email

    @property
    def id(self):
        """Gets the id of this OrganizationAccountSettingsImportRequestorResponse.  # noqa: E501


        :return: The id of this OrganizationAccountSettingsImportRequestorResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OrganizationAccountSettingsImportRequestorResponse.


        :param id: The id of this OrganizationAccountSettingsImportRequestorResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this OrganizationAccountSettingsImportRequestorResponse.  # noqa: E501


        :return: The type of this OrganizationAccountSettingsImportRequestorResponse.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OrganizationAccountSettingsImportRequestorResponse.


        :param type: The type of this OrganizationAccountSettingsImportRequestorResponse.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def name(self):
        """Gets the name of this OrganizationAccountSettingsImportRequestorResponse.  # noqa: E501


        :return: The name of this OrganizationAccountSettingsImportRequestorResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OrganizationAccountSettingsImportRequestorResponse.


        :param name: The name of this OrganizationAccountSettingsImportRequestorResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def email(self):
        """Gets the email of this OrganizationAccountSettingsImportRequestorResponse.  # noqa: E501


        :return: The email of this OrganizationAccountSettingsImportRequestorResponse.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this OrganizationAccountSettingsImportRequestorResponse.


        :param email: The email of this OrganizationAccountSettingsImportRequestorResponse.  # noqa: E501
        :type: str
        """

        self._email = email

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
        if issubclass(OrganizationAccountSettingsImportRequestorResponse, dict):
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
        if not isinstance(other, OrganizationAccountSettingsImportRequestorResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
