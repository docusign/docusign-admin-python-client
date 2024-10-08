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


class OrganizationSalesforceAccountManagersResponse(object):
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
        'account_id': 'str',
        'account_name': 'str',
        'account_type': 'str',
        'account_owner': 'OSAMRContact',
        'account_manager': 'OSAMRContact',
        'parent_account': 'OrganizationSalesforceAccountManagersResponse'
    }

    attribute_map = {
        'account_id': 'account_id',
        'account_name': 'account_name',
        'account_type': 'account_type',
        'account_owner': 'account_owner',
        'account_manager': 'account_manager',
        'parent_account': 'parent_account'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """OrganizationSalesforceAccountManagersResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account_id = None
        self._account_name = None
        self._account_type = None
        self._account_owner = None
        self._account_manager = None
        self._parent_account = None
        self.discriminator = None

        setattr(self, "_{}".format('account_id'), kwargs.get('account_id', None))
        setattr(self, "_{}".format('account_name'), kwargs.get('account_name', None))
        setattr(self, "_{}".format('account_type'), kwargs.get('account_type', None))
        setattr(self, "_{}".format('account_owner'), kwargs.get('account_owner', None))
        setattr(self, "_{}".format('account_manager'), kwargs.get('account_manager', None))
        setattr(self, "_{}".format('parent_account'), kwargs.get('parent_account', None))

    @property
    def account_id(self):
        """Gets the account_id of this OrganizationSalesforceAccountManagersResponse.  # noqa: E501


        :return: The account_id of this OrganizationSalesforceAccountManagersResponse.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this OrganizationSalesforceAccountManagersResponse.


        :param account_id: The account_id of this OrganizationSalesforceAccountManagersResponse.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def account_name(self):
        """Gets the account_name of this OrganizationSalesforceAccountManagersResponse.  # noqa: E501


        :return: The account_name of this OrganizationSalesforceAccountManagersResponse.  # noqa: E501
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this OrganizationSalesforceAccountManagersResponse.


        :param account_name: The account_name of this OrganizationSalesforceAccountManagersResponse.  # noqa: E501
        :type: str
        """

        self._account_name = account_name

    @property
    def account_type(self):
        """Gets the account_type of this OrganizationSalesforceAccountManagersResponse.  # noqa: E501


        :return: The account_type of this OrganizationSalesforceAccountManagersResponse.  # noqa: E501
        :rtype: str
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        """Sets the account_type of this OrganizationSalesforceAccountManagersResponse.


        :param account_type: The account_type of this OrganizationSalesforceAccountManagersResponse.  # noqa: E501
        :type: str
        """

        self._account_type = account_type

    @property
    def account_owner(self):
        """Gets the account_owner of this OrganizationSalesforceAccountManagersResponse.  # noqa: E501


        :return: The account_owner of this OrganizationSalesforceAccountManagersResponse.  # noqa: E501
        :rtype: OSAMRContact
        """
        return self._account_owner

    @account_owner.setter
    def account_owner(self, account_owner):
        """Sets the account_owner of this OrganizationSalesforceAccountManagersResponse.


        :param account_owner: The account_owner of this OrganizationSalesforceAccountManagersResponse.  # noqa: E501
        :type: OSAMRContact
        """

        self._account_owner = account_owner

    @property
    def account_manager(self):
        """Gets the account_manager of this OrganizationSalesforceAccountManagersResponse.  # noqa: E501


        :return: The account_manager of this OrganizationSalesforceAccountManagersResponse.  # noqa: E501
        :rtype: OSAMRContact
        """
        return self._account_manager

    @account_manager.setter
    def account_manager(self, account_manager):
        """Sets the account_manager of this OrganizationSalesforceAccountManagersResponse.


        :param account_manager: The account_manager of this OrganizationSalesforceAccountManagersResponse.  # noqa: E501
        :type: OSAMRContact
        """

        self._account_manager = account_manager

    @property
    def parent_account(self):
        """Gets the parent_account of this OrganizationSalesforceAccountManagersResponse.  # noqa: E501


        :return: The parent_account of this OrganizationSalesforceAccountManagersResponse.  # noqa: E501
        :rtype: OrganizationSalesforceAccountManagersResponse
        """
        return self._parent_account

    @parent_account.setter
    def parent_account(self, parent_account):
        """Sets the parent_account of this OrganizationSalesforceAccountManagersResponse.


        :param parent_account: The parent_account of this OrganizationSalesforceAccountManagersResponse.  # noqa: E501
        :type: OrganizationSalesforceAccountManagersResponse
        """

        self._parent_account = parent_account

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
        if issubclass(OrganizationSalesforceAccountManagersResponse, dict):
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
        if not isinstance(other, OrganizationSalesforceAccountManagersResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrganizationSalesforceAccountManagersResponse):
            return True

        return self.to_dict() != other.to_dict()
