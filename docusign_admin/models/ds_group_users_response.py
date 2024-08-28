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


class DSGroupUsersResponse(object):
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
        'page': 'int',
        'page_size': 'int',
        'total_count': 'int',
        'users': 'list[DSGroupUserResponse]'
    }

    attribute_map = {
        'page': 'page',
        'page_size': 'page_size',
        'total_count': 'total_count',
        'users': 'users'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """DSGroupUsersResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._page = None
        self._page_size = None
        self._total_count = None
        self._users = None
        self.discriminator = None

        setattr(self, "_{}".format('page'), kwargs.get('page', None))
        setattr(self, "_{}".format('page_size'), kwargs.get('page_size', None))
        setattr(self, "_{}".format('total_count'), kwargs.get('total_count', None))
        setattr(self, "_{}".format('users'), kwargs.get('users', None))

    @property
    def page(self):
        """Gets the page of this DSGroupUsersResponse.  # noqa: E501


        :return: The page of this DSGroupUsersResponse.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this DSGroupUsersResponse.


        :param page: The page of this DSGroupUsersResponse.  # noqa: E501
        :type: int
        """

        self._page = page

    @property
    def page_size(self):
        """Gets the page_size of this DSGroupUsersResponse.  # noqa: E501


        :return: The page_size of this DSGroupUsersResponse.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this DSGroupUsersResponse.


        :param page_size: The page_size of this DSGroupUsersResponse.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def total_count(self):
        """Gets the total_count of this DSGroupUsersResponse.  # noqa: E501


        :return: The total_count of this DSGroupUsersResponse.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this DSGroupUsersResponse.


        :param total_count: The total_count of this DSGroupUsersResponse.  # noqa: E501
        :type: int
        """

        self._total_count = total_count

    @property
    def users(self):
        """Gets the users of this DSGroupUsersResponse.  # noqa: E501


        :return: The users of this DSGroupUsersResponse.  # noqa: E501
        :rtype: list[DSGroupUserResponse]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this DSGroupUsersResponse.


        :param users: The users of this DSGroupUsersResponse.  # noqa: E501
        :type: list[DSGroupUserResponse]
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
        if issubclass(DSGroupUsersResponse, dict):
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
        if not isinstance(other, DSGroupUsersResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DSGroupUsersResponse):
            return True

        return self.to_dict() != other.to_dict()
