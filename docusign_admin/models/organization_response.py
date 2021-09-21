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


class OrganizationResponse(object):
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
        'name': 'str',
        'description': 'str',
        'default_account_id': 'str',
        'default_permission_profile_id': 'int',
        'created_on': 'datetime',
        'created_by': 'str',
        'last_modified_on': 'datetime',
        'last_modified_by': 'str',
        'accounts': 'list[OrganizationAccountResponse]',
        'users': 'list[OrganizationSimpleIdObject]',
        'reserved_domains': 'list[DomainResponse]',
        'identity_providers': 'list[IdentityProvidersResponse]',
        'links': 'list[LinkResponse]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'default_account_id': 'default_account_id',
        'default_permission_profile_id': 'default_permission_profile_id',
        'created_on': 'created_on',
        'created_by': 'created_by',
        'last_modified_on': 'last_modified_on',
        'last_modified_by': 'last_modified_by',
        'accounts': 'accounts',
        'users': 'users',
        'reserved_domains': 'reserved_domains',
        'identity_providers': 'identity_providers',
        'links': 'links'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """OrganizationResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._name = None
        self._description = None
        self._default_account_id = None
        self._default_permission_profile_id = None
        self._created_on = None
        self._created_by = None
        self._last_modified_on = None
        self._last_modified_by = None
        self._accounts = None
        self._users = None
        self._reserved_domains = None
        self._identity_providers = None
        self._links = None
        self.discriminator = None

        setattr(self, "_{}".format('id'), kwargs.get('id', None))
        setattr(self, "_{}".format('name'), kwargs.get('name', None))
        setattr(self, "_{}".format('description'), kwargs.get('description', None))
        setattr(self, "_{}".format('default_account_id'), kwargs.get('default_account_id', None))
        setattr(self, "_{}".format('default_permission_profile_id'), kwargs.get('default_permission_profile_id', None))
        setattr(self, "_{}".format('created_on'), kwargs.get('created_on', None))
        setattr(self, "_{}".format('created_by'), kwargs.get('created_by', None))
        setattr(self, "_{}".format('last_modified_on'), kwargs.get('last_modified_on', None))
        setattr(self, "_{}".format('last_modified_by'), kwargs.get('last_modified_by', None))
        setattr(self, "_{}".format('accounts'), kwargs.get('accounts', None))
        setattr(self, "_{}".format('users'), kwargs.get('users', None))
        setattr(self, "_{}".format('reserved_domains'), kwargs.get('reserved_domains', None))
        setattr(self, "_{}".format('identity_providers'), kwargs.get('identity_providers', None))
        setattr(self, "_{}".format('links'), kwargs.get('links', None))

    @property
    def id(self):
        """Gets the id of this OrganizationResponse.  # noqa: E501


        :return: The id of this OrganizationResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OrganizationResponse.


        :param id: The id of this OrganizationResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this OrganizationResponse.  # noqa: E501


        :return: The name of this OrganizationResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OrganizationResponse.


        :param name: The name of this OrganizationResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this OrganizationResponse.  # noqa: E501


        :return: The description of this OrganizationResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this OrganizationResponse.


        :param description: The description of this OrganizationResponse.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def default_account_id(self):
        """Gets the default_account_id of this OrganizationResponse.  # noqa: E501


        :return: The default_account_id of this OrganizationResponse.  # noqa: E501
        :rtype: str
        """
        return self._default_account_id

    @default_account_id.setter
    def default_account_id(self, default_account_id):
        """Sets the default_account_id of this OrganizationResponse.


        :param default_account_id: The default_account_id of this OrganizationResponse.  # noqa: E501
        :type: str
        """

        self._default_account_id = default_account_id

    @property
    def default_permission_profile_id(self):
        """Gets the default_permission_profile_id of this OrganizationResponse.  # noqa: E501


        :return: The default_permission_profile_id of this OrganizationResponse.  # noqa: E501
        :rtype: int
        """
        return self._default_permission_profile_id

    @default_permission_profile_id.setter
    def default_permission_profile_id(self, default_permission_profile_id):
        """Sets the default_permission_profile_id of this OrganizationResponse.


        :param default_permission_profile_id: The default_permission_profile_id of this OrganizationResponse.  # noqa: E501
        :type: int
        """

        self._default_permission_profile_id = default_permission_profile_id

    @property
    def created_on(self):
        """Gets the created_on of this OrganizationResponse.  # noqa: E501


        :return: The created_on of this OrganizationResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this OrganizationResponse.


        :param created_on: The created_on of this OrganizationResponse.  # noqa: E501
        :type: datetime
        """

        self._created_on = created_on

    @property
    def created_by(self):
        """Gets the created_by of this OrganizationResponse.  # noqa: E501


        :return: The created_by of this OrganizationResponse.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this OrganizationResponse.


        :param created_by: The created_by of this OrganizationResponse.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def last_modified_on(self):
        """Gets the last_modified_on of this OrganizationResponse.  # noqa: E501


        :return: The last_modified_on of this OrganizationResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified_on

    @last_modified_on.setter
    def last_modified_on(self, last_modified_on):
        """Sets the last_modified_on of this OrganizationResponse.


        :param last_modified_on: The last_modified_on of this OrganizationResponse.  # noqa: E501
        :type: datetime
        """

        self._last_modified_on = last_modified_on

    @property
    def last_modified_by(self):
        """Gets the last_modified_by of this OrganizationResponse.  # noqa: E501


        :return: The last_modified_by of this OrganizationResponse.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_by

    @last_modified_by.setter
    def last_modified_by(self, last_modified_by):
        """Sets the last_modified_by of this OrganizationResponse.


        :param last_modified_by: The last_modified_by of this OrganizationResponse.  # noqa: E501
        :type: str
        """

        self._last_modified_by = last_modified_by

    @property
    def accounts(self):
        """Gets the accounts of this OrganizationResponse.  # noqa: E501


        :return: The accounts of this OrganizationResponse.  # noqa: E501
        :rtype: list[OrganizationAccountResponse]
        """
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        """Sets the accounts of this OrganizationResponse.


        :param accounts: The accounts of this OrganizationResponse.  # noqa: E501
        :type: list[OrganizationAccountResponse]
        """

        self._accounts = accounts

    @property
    def users(self):
        """Gets the users of this OrganizationResponse.  # noqa: E501


        :return: The users of this OrganizationResponse.  # noqa: E501
        :rtype: list[OrganizationSimpleIdObject]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this OrganizationResponse.


        :param users: The users of this OrganizationResponse.  # noqa: E501
        :type: list[OrganizationSimpleIdObject]
        """

        self._users = users

    @property
    def reserved_domains(self):
        """Gets the reserved_domains of this OrganizationResponse.  # noqa: E501


        :return: The reserved_domains of this OrganizationResponse.  # noqa: E501
        :rtype: list[DomainResponse]
        """
        return self._reserved_domains

    @reserved_domains.setter
    def reserved_domains(self, reserved_domains):
        """Sets the reserved_domains of this OrganizationResponse.


        :param reserved_domains: The reserved_domains of this OrganizationResponse.  # noqa: E501
        :type: list[DomainResponse]
        """

        self._reserved_domains = reserved_domains

    @property
    def identity_providers(self):
        """Gets the identity_providers of this OrganizationResponse.  # noqa: E501


        :return: The identity_providers of this OrganizationResponse.  # noqa: E501
        :rtype: list[IdentityProvidersResponse]
        """
        return self._identity_providers

    @identity_providers.setter
    def identity_providers(self, identity_providers):
        """Sets the identity_providers of this OrganizationResponse.


        :param identity_providers: The identity_providers of this OrganizationResponse.  # noqa: E501
        :type: list[IdentityProvidersResponse]
        """

        self._identity_providers = identity_providers

    @property
    def links(self):
        """Gets the links of this OrganizationResponse.  # noqa: E501


        :return: The links of this OrganizationResponse.  # noqa: E501
        :rtype: list[LinkResponse]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this OrganizationResponse.


        :param links: The links of this OrganizationResponse.  # noqa: E501
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
        if issubclass(OrganizationResponse, dict):
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
        if not isinstance(other, OrganizationResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrganizationResponse):
            return True

        return self.to_dict() != other.to_dict()
