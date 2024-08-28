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


class AssetGroupAccountCloneTargetAccount(object):
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
        'region': 'str',
        'country_code': 'str',
        'site': 'str',
        'admin': 'AssetGroupAccountCloneTargetAccountAdmin'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'region': 'region',
        'country_code': 'countryCode',
        'site': 'site',
        'admin': 'admin'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """AssetGroupAccountCloneTargetAccount - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._name = None
        self._region = None
        self._country_code = None
        self._site = None
        self._admin = None
        self.discriminator = None

        setattr(self, "_{}".format('id'), kwargs.get('id', None))
        setattr(self, "_{}".format('name'), kwargs.get('name', None))
        setattr(self, "_{}".format('region'), kwargs.get('region', None))
        setattr(self, "_{}".format('country_code'), kwargs.get('country_code', None))
        setattr(self, "_{}".format('site'), kwargs.get('site', None))
        setattr(self, "_{}".format('admin'), kwargs.get('admin', None))

    @property
    def id(self):
        """Gets the id of this AssetGroupAccountCloneTargetAccount.  # noqa: E501

        The target account id to clone to. It will be empty Guid if account not yet created.  # noqa: E501

        :return: The id of this AssetGroupAccountCloneTargetAccount.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AssetGroupAccountCloneTargetAccount.

        The target account id to clone to. It will be empty Guid if account not yet created.  # noqa: E501

        :param id: The id of this AssetGroupAccountCloneTargetAccount.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this AssetGroupAccountCloneTargetAccount.  # noqa: E501

        The name of the target account.  # noqa: E501

        :return: The name of this AssetGroupAccountCloneTargetAccount.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AssetGroupAccountCloneTargetAccount.

        The name of the target account.  # noqa: E501

        :param name: The name of this AssetGroupAccountCloneTargetAccount.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def region(self):
        """Gets the region of this AssetGroupAccountCloneTargetAccount.  # noqa: E501

        The region where the target account is in.  # noqa: E501

        :return: The region of this AssetGroupAccountCloneTargetAccount.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this AssetGroupAccountCloneTargetAccount.

        The region where the target account is in.  # noqa: E501

        :param region: The region of this AssetGroupAccountCloneTargetAccount.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def country_code(self):
        """Gets the country_code of this AssetGroupAccountCloneTargetAccount.  # noqa: E501

        The country code where the target account is in. This value is ignored if region is provided.  # noqa: E501

        :return: The country_code of this AssetGroupAccountCloneTargetAccount.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this AssetGroupAccountCloneTargetAccount.

        The country code where the target account is in. This value is ignored if region is provided.  # noqa: E501

        :param country_code: The country_code of this AssetGroupAccountCloneTargetAccount.  # noqa: E501
        :type: str
        """

        self._country_code = country_code

    @property
    def site(self):
        """Gets the site of this AssetGroupAccountCloneTargetAccount.  # noqa: E501

        The site where the target account is on.  # noqa: E501

        :return: The site of this AssetGroupAccountCloneTargetAccount.  # noqa: E501
        :rtype: str
        """
        return self._site

    @site.setter
    def site(self, site):
        """Sets the site of this AssetGroupAccountCloneTargetAccount.

        The site where the target account is on.  # noqa: E501

        :param site: The site of this AssetGroupAccountCloneTargetAccount.  # noqa: E501
        :type: str
        """

        self._site = site

    @property
    def admin(self):
        """Gets the admin of this AssetGroupAccountCloneTargetAccount.  # noqa: E501

        The admin user for the target account.  # noqa: E501

        :return: The admin of this AssetGroupAccountCloneTargetAccount.  # noqa: E501
        :rtype: AssetGroupAccountCloneTargetAccountAdmin
        """
        return self._admin

    @admin.setter
    def admin(self, admin):
        """Sets the admin of this AssetGroupAccountCloneTargetAccount.

        The admin user for the target account.  # noqa: E501

        :param admin: The admin of this AssetGroupAccountCloneTargetAccount.  # noqa: E501
        :type: AssetGroupAccountCloneTargetAccountAdmin
        """

        self._admin = admin

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
        if issubclass(AssetGroupAccountCloneTargetAccount, dict):
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
        if not isinstance(other, AssetGroupAccountCloneTargetAccount):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AssetGroupAccountCloneTargetAccount):
            return True

        return self.to_dict() != other.to_dict()
