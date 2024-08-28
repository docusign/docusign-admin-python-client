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


class SubAccountCreateRequestSubAccountCreationTargetAccountDetails(object):
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
        'address': 'AddressInformation',
        'admin': 'SubAccountCreateRequestSubAccountCreationTargetAccountAdmin',
        'name': 'str',
        'country_code': 'str',
        'region': 'str',
        'site': 'str'
    }

    attribute_map = {
        'id': 'id',
        'address': 'address',
        'admin': 'admin',
        'name': 'name',
        'country_code': 'countryCode',
        'region': 'region',
        'site': 'site'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """SubAccountCreateRequestSubAccountCreationTargetAccountDetails - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._address = None
        self._admin = None
        self._name = None
        self._country_code = None
        self._region = None
        self._site = None
        self.discriminator = None

        setattr(self, "_{}".format('id'), kwargs.get('id', None))
        setattr(self, "_{}".format('address'), kwargs.get('address', None))
        setattr(self, "_{}".format('admin'), kwargs.get('admin', None))
        setattr(self, "_{}".format('name'), kwargs.get('name', None))
        setattr(self, "_{}".format('country_code'), kwargs.get('country_code', None))
        setattr(self, "_{}".format('region'), kwargs.get('region', None))
        setattr(self, "_{}".format('site'), kwargs.get('site', None))

    @property
    def id(self):
        """Gets the id of this SubAccountCreateRequestSubAccountCreationTargetAccountDetails.  # noqa: E501


        :return: The id of this SubAccountCreateRequestSubAccountCreationTargetAccountDetails.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SubAccountCreateRequestSubAccountCreationTargetAccountDetails.


        :param id: The id of this SubAccountCreateRequestSubAccountCreationTargetAccountDetails.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def address(self):
        """Gets the address of this SubAccountCreateRequestSubAccountCreationTargetAccountDetails.  # noqa: E501


        :return: The address of this SubAccountCreateRequestSubAccountCreationTargetAccountDetails.  # noqa: E501
        :rtype: AddressInformation
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this SubAccountCreateRequestSubAccountCreationTargetAccountDetails.


        :param address: The address of this SubAccountCreateRequestSubAccountCreationTargetAccountDetails.  # noqa: E501
        :type: AddressInformation
        """

        self._address = address

    @property
    def admin(self):
        """Gets the admin of this SubAccountCreateRequestSubAccountCreationTargetAccountDetails.  # noqa: E501


        :return: The admin of this SubAccountCreateRequestSubAccountCreationTargetAccountDetails.  # noqa: E501
        :rtype: SubAccountCreateRequestSubAccountCreationTargetAccountAdmin
        """
        return self._admin

    @admin.setter
    def admin(self, admin):
        """Sets the admin of this SubAccountCreateRequestSubAccountCreationTargetAccountDetails.


        :param admin: The admin of this SubAccountCreateRequestSubAccountCreationTargetAccountDetails.  # noqa: E501
        :type: SubAccountCreateRequestSubAccountCreationTargetAccountAdmin
        """

        self._admin = admin

    @property
    def name(self):
        """Gets the name of this SubAccountCreateRequestSubAccountCreationTargetAccountDetails.  # noqa: E501


        :return: The name of this SubAccountCreateRequestSubAccountCreationTargetAccountDetails.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SubAccountCreateRequestSubAccountCreationTargetAccountDetails.


        :param name: The name of this SubAccountCreateRequestSubAccountCreationTargetAccountDetails.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def country_code(self):
        """Gets the country_code of this SubAccountCreateRequestSubAccountCreationTargetAccountDetails.  # noqa: E501


        :return: The country_code of this SubAccountCreateRequestSubAccountCreationTargetAccountDetails.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this SubAccountCreateRequestSubAccountCreationTargetAccountDetails.


        :param country_code: The country_code of this SubAccountCreateRequestSubAccountCreationTargetAccountDetails.  # noqa: E501
        :type: str
        """

        self._country_code = country_code

    @property
    def region(self):
        """Gets the region of this SubAccountCreateRequestSubAccountCreationTargetAccountDetails.  # noqa: E501


        :return: The region of this SubAccountCreateRequestSubAccountCreationTargetAccountDetails.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this SubAccountCreateRequestSubAccountCreationTargetAccountDetails.


        :param region: The region of this SubAccountCreateRequestSubAccountCreationTargetAccountDetails.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def site(self):
        """Gets the site of this SubAccountCreateRequestSubAccountCreationTargetAccountDetails.  # noqa: E501


        :return: The site of this SubAccountCreateRequestSubAccountCreationTargetAccountDetails.  # noqa: E501
        :rtype: str
        """
        return self._site

    @site.setter
    def site(self, site):
        """Sets the site of this SubAccountCreateRequestSubAccountCreationTargetAccountDetails.


        :param site: The site of this SubAccountCreateRequestSubAccountCreationTargetAccountDetails.  # noqa: E501
        :type: str
        """

        self._site = site

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
        if issubclass(SubAccountCreateRequestSubAccountCreationTargetAccountDetails, dict):
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
        if not isinstance(other, SubAccountCreateRequestSubAccountCreationTargetAccountDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SubAccountCreateRequestSubAccountCreationTargetAccountDetails):
            return True

        return self.to_dict() != other.to_dict()
