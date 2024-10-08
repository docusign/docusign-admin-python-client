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


class MembershipResponse(object):
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
        'account_id': 'str',
        'external_account_id': 'str',
        'account_name': 'str',
        'is_external_account': 'bool',
        'status': 'str',
        'permission_profile': 'PermissionProfileResponse',
        'created_on': 'datetime',
        'groups': 'list[MemberGroupResponse]',
        'is_admin': 'bool'
    }

    attribute_map = {
        'email': 'email',
        'account_id': 'account_id',
        'external_account_id': 'external_account_id',
        'account_name': 'account_name',
        'is_external_account': 'is_external_account',
        'status': 'status',
        'permission_profile': 'permission_profile',
        'created_on': 'created_on',
        'groups': 'groups',
        'is_admin': 'is_admin'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """MembershipResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._email = None
        self._account_id = None
        self._external_account_id = None
        self._account_name = None
        self._is_external_account = None
        self._status = None
        self._permission_profile = None
        self._created_on = None
        self._groups = None
        self._is_admin = None
        self.discriminator = None

        setattr(self, "_{}".format('email'), kwargs.get('email', None))
        setattr(self, "_{}".format('account_id'), kwargs.get('account_id', None))
        setattr(self, "_{}".format('external_account_id'), kwargs.get('external_account_id', None))
        setattr(self, "_{}".format('account_name'), kwargs.get('account_name', None))
        setattr(self, "_{}".format('is_external_account'), kwargs.get('is_external_account', None))
        setattr(self, "_{}".format('status'), kwargs.get('status', None))
        setattr(self, "_{}".format('permission_profile'), kwargs.get('permission_profile', None))
        setattr(self, "_{}".format('created_on'), kwargs.get('created_on', None))
        setattr(self, "_{}".format('groups'), kwargs.get('groups', None))
        setattr(self, "_{}".format('is_admin'), kwargs.get('is_admin', None))

    @property
    def email(self):
        """Gets the email of this MembershipResponse.  # noqa: E501


        :return: The email of this MembershipResponse.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this MembershipResponse.


        :param email: The email of this MembershipResponse.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def account_id(self):
        """Gets the account_id of this MembershipResponse.  # noqa: E501


        :return: The account_id of this MembershipResponse.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this MembershipResponse.


        :param account_id: The account_id of this MembershipResponse.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def external_account_id(self):
        """Gets the external_account_id of this MembershipResponse.  # noqa: E501


        :return: The external_account_id of this MembershipResponse.  # noqa: E501
        :rtype: str
        """
        return self._external_account_id

    @external_account_id.setter
    def external_account_id(self, external_account_id):
        """Sets the external_account_id of this MembershipResponse.


        :param external_account_id: The external_account_id of this MembershipResponse.  # noqa: E501
        :type: str
        """

        self._external_account_id = external_account_id

    @property
    def account_name(self):
        """Gets the account_name of this MembershipResponse.  # noqa: E501


        :return: The account_name of this MembershipResponse.  # noqa: E501
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this MembershipResponse.


        :param account_name: The account_name of this MembershipResponse.  # noqa: E501
        :type: str
        """

        self._account_name = account_name

    @property
    def is_external_account(self):
        """Gets the is_external_account of this MembershipResponse.  # noqa: E501


        :return: The is_external_account of this MembershipResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_external_account

    @is_external_account.setter
    def is_external_account(self, is_external_account):
        """Sets the is_external_account of this MembershipResponse.


        :param is_external_account: The is_external_account of this MembershipResponse.  # noqa: E501
        :type: bool
        """

        self._is_external_account = is_external_account

    @property
    def status(self):
        """Gets the status of this MembershipResponse.  # noqa: E501


        :return: The status of this MembershipResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this MembershipResponse.


        :param status: The status of this MembershipResponse.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def permission_profile(self):
        """Gets the permission_profile of this MembershipResponse.  # noqa: E501


        :return: The permission_profile of this MembershipResponse.  # noqa: E501
        :rtype: PermissionProfileResponse
        """
        return self._permission_profile

    @permission_profile.setter
    def permission_profile(self, permission_profile):
        """Sets the permission_profile of this MembershipResponse.


        :param permission_profile: The permission_profile of this MembershipResponse.  # noqa: E501
        :type: PermissionProfileResponse
        """

        self._permission_profile = permission_profile

    @property
    def created_on(self):
        """Gets the created_on of this MembershipResponse.  # noqa: E501


        :return: The created_on of this MembershipResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this MembershipResponse.


        :param created_on: The created_on of this MembershipResponse.  # noqa: E501
        :type: datetime
        """

        self._created_on = created_on

    @property
    def groups(self):
        """Gets the groups of this MembershipResponse.  # noqa: E501


        :return: The groups of this MembershipResponse.  # noqa: E501
        :rtype: list[MemberGroupResponse]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this MembershipResponse.


        :param groups: The groups of this MembershipResponse.  # noqa: E501
        :type: list[MemberGroupResponse]
        """

        self._groups = groups

    @property
    def is_admin(self):
        """Gets the is_admin of this MembershipResponse.  # noqa: E501


        :return: The is_admin of this MembershipResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_admin

    @is_admin.setter
    def is_admin(self, is_admin):
        """Sets the is_admin of this MembershipResponse.


        :param is_admin: The is_admin of this MembershipResponse.  # noqa: E501
        :type: bool
        """

        self._is_admin = is_admin

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
        if issubclass(MembershipResponse, dict):
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
        if not isinstance(other, MembershipResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MembershipResponse):
            return True

        return self.to_dict() != other.to_dict()
