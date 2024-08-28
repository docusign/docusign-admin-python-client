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


class SubscriptionProvisionModelAccountCreateAccountAdmin(object):
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
        'email_address': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'locale': 'str',
        'address': 'DocuSignAccountDomainModelAddress'
    }

    attribute_map = {
        'email_address': 'EmailAddress',
        'first_name': 'FirstName',
        'last_name': 'LastName',
        'locale': 'Locale',
        'address': 'Address'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """SubscriptionProvisionModelAccountCreateAccountAdmin - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._email_address = None
        self._first_name = None
        self._last_name = None
        self._locale = None
        self._address = None
        self.discriminator = None

        setattr(self, "_{}".format('email_address'), kwargs.get('email_address', None))
        setattr(self, "_{}".format('first_name'), kwargs.get('first_name', None))
        setattr(self, "_{}".format('last_name'), kwargs.get('last_name', None))
        setattr(self, "_{}".format('locale'), kwargs.get('locale', None))
        setattr(self, "_{}".format('address'), kwargs.get('address', None))

    @property
    def email_address(self):
        """Gets the email_address of this SubscriptionProvisionModelAccountCreateAccountAdmin.  # noqa: E501


        :return: The email_address of this SubscriptionProvisionModelAccountCreateAccountAdmin.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this SubscriptionProvisionModelAccountCreateAccountAdmin.


        :param email_address: The email_address of this SubscriptionProvisionModelAccountCreateAccountAdmin.  # noqa: E501
        :type: str
        """

        self._email_address = email_address

    @property
    def first_name(self):
        """Gets the first_name of this SubscriptionProvisionModelAccountCreateAccountAdmin.  # noqa: E501


        :return: The first_name of this SubscriptionProvisionModelAccountCreateAccountAdmin.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this SubscriptionProvisionModelAccountCreateAccountAdmin.


        :param first_name: The first_name of this SubscriptionProvisionModelAccountCreateAccountAdmin.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this SubscriptionProvisionModelAccountCreateAccountAdmin.  # noqa: E501


        :return: The last_name of this SubscriptionProvisionModelAccountCreateAccountAdmin.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this SubscriptionProvisionModelAccountCreateAccountAdmin.


        :param last_name: The last_name of this SubscriptionProvisionModelAccountCreateAccountAdmin.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def locale(self):
        """Gets the locale of this SubscriptionProvisionModelAccountCreateAccountAdmin.  # noqa: E501


        :return: The locale of this SubscriptionProvisionModelAccountCreateAccountAdmin.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this SubscriptionProvisionModelAccountCreateAccountAdmin.


        :param locale: The locale of this SubscriptionProvisionModelAccountCreateAccountAdmin.  # noqa: E501
        :type: str
        """
        allowed_values = ["None", "zh_cn", "zh_tw", "nl", "en", "fr", "de", "it", "ja", "ko", "pt", "pt_br", "ru", "es", "pl"]  # noqa: E501
        if (self._configuration.client_side_validation and
                locale not in allowed_values):
            raise ValueError(
                "Invalid value for `locale` ({0}), must be one of {1}"  # noqa: E501
                .format(locale, allowed_values)
            )

        self._locale = locale

    @property
    def address(self):
        """Gets the address of this SubscriptionProvisionModelAccountCreateAccountAdmin.  # noqa: E501


        :return: The address of this SubscriptionProvisionModelAccountCreateAccountAdmin.  # noqa: E501
        :rtype: DocuSignAccountDomainModelAddress
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this SubscriptionProvisionModelAccountCreateAccountAdmin.


        :param address: The address of this SubscriptionProvisionModelAccountCreateAccountAdmin.  # noqa: E501
        :type: DocuSignAccountDomainModelAddress
        """

        self._address = address

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
        if issubclass(SubscriptionProvisionModelAccountCreateAccountAdmin, dict):
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
        if not isinstance(other, SubscriptionProvisionModelAccountCreateAccountAdmin):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SubscriptionProvisionModelAccountCreateAccountAdmin):
            return True

        return self.to_dict() != other.to_dict()