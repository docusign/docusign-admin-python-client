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


class DomainResponse(object):
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
        'status': 'str',
        'host_name': 'str',
        'txt_token': 'str',
        'identity_provider_id': 'str',
        'settings': 'list[SettingResponse]',
        'links': 'list[LinkResponse]'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'host_name': 'host_name',
        'txt_token': 'txt_token',
        'identity_provider_id': 'identity_provider_id',
        'settings': 'settings',
        'links': 'links'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """DomainResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._status = None
        self._host_name = None
        self._txt_token = None
        self._identity_provider_id = None
        self._settings = None
        self._links = None
        self.discriminator = None

        setattr(self, "_{}".format('id'), kwargs.get('id', None))
        setattr(self, "_{}".format('status'), kwargs.get('status', None))
        setattr(self, "_{}".format('host_name'), kwargs.get('host_name', None))
        setattr(self, "_{}".format('txt_token'), kwargs.get('txt_token', None))
        setattr(self, "_{}".format('identity_provider_id'), kwargs.get('identity_provider_id', None))
        setattr(self, "_{}".format('settings'), kwargs.get('settings', None))
        setattr(self, "_{}".format('links'), kwargs.get('links', None))

    @property
    def id(self):
        """Gets the id of this DomainResponse.  # noqa: E501


        :return: The id of this DomainResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DomainResponse.


        :param id: The id of this DomainResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def status(self):
        """Gets the status of this DomainResponse.  # noqa: E501


        :return: The status of this DomainResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DomainResponse.


        :param status: The status of this DomainResponse.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def host_name(self):
        """Gets the host_name of this DomainResponse.  # noqa: E501


        :return: The host_name of this DomainResponse.  # noqa: E501
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this DomainResponse.


        :param host_name: The host_name of this DomainResponse.  # noqa: E501
        :type: str
        """

        self._host_name = host_name

    @property
    def txt_token(self):
        """Gets the txt_token of this DomainResponse.  # noqa: E501


        :return: The txt_token of this DomainResponse.  # noqa: E501
        :rtype: str
        """
        return self._txt_token

    @txt_token.setter
    def txt_token(self, txt_token):
        """Sets the txt_token of this DomainResponse.


        :param txt_token: The txt_token of this DomainResponse.  # noqa: E501
        :type: str
        """

        self._txt_token = txt_token

    @property
    def identity_provider_id(self):
        """Gets the identity_provider_id of this DomainResponse.  # noqa: E501


        :return: The identity_provider_id of this DomainResponse.  # noqa: E501
        :rtype: str
        """
        return self._identity_provider_id

    @identity_provider_id.setter
    def identity_provider_id(self, identity_provider_id):
        """Sets the identity_provider_id of this DomainResponse.


        :param identity_provider_id: The identity_provider_id of this DomainResponse.  # noqa: E501
        :type: str
        """

        self._identity_provider_id = identity_provider_id

    @property
    def settings(self):
        """Gets the settings of this DomainResponse.  # noqa: E501


        :return: The settings of this DomainResponse.  # noqa: E501
        :rtype: list[SettingResponse]
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this DomainResponse.


        :param settings: The settings of this DomainResponse.  # noqa: E501
        :type: list[SettingResponse]
        """

        self._settings = settings

    @property
    def links(self):
        """Gets the links of this DomainResponse.  # noqa: E501


        :return: The links of this DomainResponse.  # noqa: E501
        :rtype: list[LinkResponse]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this DomainResponse.


        :param links: The links of this DomainResponse.  # noqa: E501
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
        if issubclass(DomainResponse, dict):
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
        if not isinstance(other, DomainResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DomainResponse):
            return True

        return self.to_dict() != other.to_dict()
