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


class AddUserResponseAccountProperties(object):
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
        'site_id': 'int',
        'product_permission_profiles': 'list[ProductPermissionProfileResponse]',
        'ds_groups': 'list[DSGroupResponse]',
        'company_name': 'str',
        'job_title': 'str'
    }

    attribute_map = {
        'id': 'id',
        'site_id': 'site_id',
        'product_permission_profiles': 'product_permission_profiles',
        'ds_groups': 'ds_groups',
        'company_name': 'company_name',
        'job_title': 'job_title'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """AddUserResponseAccountProperties - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._site_id = None
        self._product_permission_profiles = None
        self._ds_groups = None
        self._company_name = None
        self._job_title = None
        self.discriminator = None

        setattr(self, "_{}".format('id'), kwargs.get('id', None))
        setattr(self, "_{}".format('site_id'), kwargs.get('site_id', None))
        setattr(self, "_{}".format('product_permission_profiles'), kwargs.get('product_permission_profiles', None))
        setattr(self, "_{}".format('ds_groups'), kwargs.get('ds_groups', None))
        setattr(self, "_{}".format('company_name'), kwargs.get('company_name', None))
        setattr(self, "_{}".format('job_title'), kwargs.get('job_title', None))

    @property
    def id(self):
        """Gets the id of this AddUserResponseAccountProperties.  # noqa: E501


        :return: The id of this AddUserResponseAccountProperties.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AddUserResponseAccountProperties.


        :param id: The id of this AddUserResponseAccountProperties.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def site_id(self):
        """Gets the site_id of this AddUserResponseAccountProperties.  # noqa: E501


        :return: The site_id of this AddUserResponseAccountProperties.  # noqa: E501
        :rtype: int
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this AddUserResponseAccountProperties.


        :param site_id: The site_id of this AddUserResponseAccountProperties.  # noqa: E501
        :type: int
        """

        self._site_id = site_id

    @property
    def product_permission_profiles(self):
        """Gets the product_permission_profiles of this AddUserResponseAccountProperties.  # noqa: E501


        :return: The product_permission_profiles of this AddUserResponseAccountProperties.  # noqa: E501
        :rtype: list[ProductPermissionProfileResponse]
        """
        return self._product_permission_profiles

    @product_permission_profiles.setter
    def product_permission_profiles(self, product_permission_profiles):
        """Sets the product_permission_profiles of this AddUserResponseAccountProperties.


        :param product_permission_profiles: The product_permission_profiles of this AddUserResponseAccountProperties.  # noqa: E501
        :type: list[ProductPermissionProfileResponse]
        """

        self._product_permission_profiles = product_permission_profiles

    @property
    def ds_groups(self):
        """Gets the ds_groups of this AddUserResponseAccountProperties.  # noqa: E501


        :return: The ds_groups of this AddUserResponseAccountProperties.  # noqa: E501
        :rtype: list[DSGroupResponse]
        """
        return self._ds_groups

    @ds_groups.setter
    def ds_groups(self, ds_groups):
        """Sets the ds_groups of this AddUserResponseAccountProperties.


        :param ds_groups: The ds_groups of this AddUserResponseAccountProperties.  # noqa: E501
        :type: list[DSGroupResponse]
        """

        self._ds_groups = ds_groups

    @property
    def company_name(self):
        """Gets the company_name of this AddUserResponseAccountProperties.  # noqa: E501


        :return: The company_name of this AddUserResponseAccountProperties.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this AddUserResponseAccountProperties.


        :param company_name: The company_name of this AddUserResponseAccountProperties.  # noqa: E501
        :type: str
        """

        self._company_name = company_name

    @property
    def job_title(self):
        """Gets the job_title of this AddUserResponseAccountProperties.  # noqa: E501


        :return: The job_title of this AddUserResponseAccountProperties.  # noqa: E501
        :rtype: str
        """
        return self._job_title

    @job_title.setter
    def job_title(self, job_title):
        """Sets the job_title of this AddUserResponseAccountProperties.


        :param job_title: The job_title of this AddUserResponseAccountProperties.  # noqa: E501
        :type: str
        """

        self._job_title = job_title

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
        if issubclass(AddUserResponseAccountProperties, dict):
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
        if not isinstance(other, AddUserResponseAccountProperties):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AddUserResponseAccountProperties):
            return True

        return self.to_dict() != other.to_dict()
