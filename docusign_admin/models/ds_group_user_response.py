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


class DSGroupUserResponse(object):
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
        'user_id': 'str',
        'account_id': 'str',
        'user_name': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'middle_name': 'str',
        'status': 'str',
        'error_details': 'ErrorDetails'
    }

    attribute_map = {
        'user_id': 'user_id',
        'account_id': 'account_id',
        'user_name': 'user_name',
        'first_name': 'first_name',
        'last_name': 'last_name',
        'middle_name': 'middle_name',
        'status': 'status',
        'error_details': 'error_details'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """DSGroupUserResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._user_id = None
        self._account_id = None
        self._user_name = None
        self._first_name = None
        self._last_name = None
        self._middle_name = None
        self._status = None
        self._error_details = None
        self.discriminator = None

        setattr(self, "_{}".format('user_id'), kwargs.get('user_id', None))
        setattr(self, "_{}".format('account_id'), kwargs.get('account_id', None))
        setattr(self, "_{}".format('user_name'), kwargs.get('user_name', None))
        setattr(self, "_{}".format('first_name'), kwargs.get('first_name', None))
        setattr(self, "_{}".format('last_name'), kwargs.get('last_name', None))
        setattr(self, "_{}".format('middle_name'), kwargs.get('middle_name', None))
        setattr(self, "_{}".format('status'), kwargs.get('status', None))
        setattr(self, "_{}".format('error_details'), kwargs.get('error_details', None))

    @property
    def user_id(self):
        """Gets the user_id of this DSGroupUserResponse.  # noqa: E501


        :return: The user_id of this DSGroupUserResponse.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this DSGroupUserResponse.


        :param user_id: The user_id of this DSGroupUserResponse.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def account_id(self):
        """Gets the account_id of this DSGroupUserResponse.  # noqa: E501


        :return: The account_id of this DSGroupUserResponse.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this DSGroupUserResponse.


        :param account_id: The account_id of this DSGroupUserResponse.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def user_name(self):
        """Gets the user_name of this DSGroupUserResponse.  # noqa: E501


        :return: The user_name of this DSGroupUserResponse.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this DSGroupUserResponse.


        :param user_name: The user_name of this DSGroupUserResponse.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

    @property
    def first_name(self):
        """Gets the first_name of this DSGroupUserResponse.  # noqa: E501


        :return: The first_name of this DSGroupUserResponse.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this DSGroupUserResponse.


        :param first_name: The first_name of this DSGroupUserResponse.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this DSGroupUserResponse.  # noqa: E501


        :return: The last_name of this DSGroupUserResponse.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this DSGroupUserResponse.


        :param last_name: The last_name of this DSGroupUserResponse.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def middle_name(self):
        """Gets the middle_name of this DSGroupUserResponse.  # noqa: E501


        :return: The middle_name of this DSGroupUserResponse.  # noqa: E501
        :rtype: str
        """
        return self._middle_name

    @middle_name.setter
    def middle_name(self, middle_name):
        """Sets the middle_name of this DSGroupUserResponse.


        :param middle_name: The middle_name of this DSGroupUserResponse.  # noqa: E501
        :type: str
        """

        self._middle_name = middle_name

    @property
    def status(self):
        """Gets the status of this DSGroupUserResponse.  # noqa: E501


        :return: The status of this DSGroupUserResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DSGroupUserResponse.


        :param status: The status of this DSGroupUserResponse.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def error_details(self):
        """Gets the error_details of this DSGroupUserResponse.  # noqa: E501


        :return: The error_details of this DSGroupUserResponse.  # noqa: E501
        :rtype: ErrorDetails
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """Sets the error_details of this DSGroupUserResponse.


        :param error_details: The error_details of this DSGroupUserResponse.  # noqa: E501
        :type: ErrorDetails
        """

        self._error_details = error_details

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
        if issubclass(DSGroupUserResponse, dict):
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
        if not isinstance(other, DSGroupUserResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DSGroupUserResponse):
            return True

        return self.to_dict() != other.to_dict()
