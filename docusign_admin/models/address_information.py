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


class AddressInformation(object):
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
        'street_address': 'str',
        'street_address_2': 'str',
        'locality': 'str',
        'region': 'str',
        'postal_code': 'str',
        'country': 'str',
        'phone': 'str',
        'fax': 'str'
    }

    attribute_map = {
        'street_address': 'street_address',
        'street_address_2': 'street_address_2',
        'locality': 'locality',
        'region': 'region',
        'postal_code': 'postal_code',
        'country': 'country',
        'phone': 'phone',
        'fax': 'fax'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """AddressInformation - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._street_address = None
        self._street_address_2 = None
        self._locality = None
        self._region = None
        self._postal_code = None
        self._country = None
        self._phone = None
        self._fax = None
        self.discriminator = None

        setattr(self, "_{}".format('street_address'), kwargs.get('street_address', None))
        setattr(self, "_{}".format('street_address_2'), kwargs.get('street_address_2', None))
        setattr(self, "_{}".format('locality'), kwargs.get('locality', None))
        setattr(self, "_{}".format('region'), kwargs.get('region', None))
        setattr(self, "_{}".format('postal_code'), kwargs.get('postal_code', None))
        setattr(self, "_{}".format('country'), kwargs.get('country', None))
        setattr(self, "_{}".format('phone'), kwargs.get('phone', None))
        setattr(self, "_{}".format('fax'), kwargs.get('fax', None))

    @property
    def street_address(self):
        """Gets the street_address of this AddressInformation.  # noqa: E501


        :return: The street_address of this AddressInformation.  # noqa: E501
        :rtype: str
        """
        return self._street_address

    @street_address.setter
    def street_address(self, street_address):
        """Sets the street_address of this AddressInformation.


        :param street_address: The street_address of this AddressInformation.  # noqa: E501
        :type: str
        """

        self._street_address = street_address

    @property
    def street_address_2(self):
        """Gets the street_address_2 of this AddressInformation.  # noqa: E501


        :return: The street_address_2 of this AddressInformation.  # noqa: E501
        :rtype: str
        """
        return self._street_address_2

    @street_address_2.setter
    def street_address_2(self, street_address_2):
        """Sets the street_address_2 of this AddressInformation.


        :param street_address_2: The street_address_2 of this AddressInformation.  # noqa: E501
        :type: str
        """

        self._street_address_2 = street_address_2

    @property
    def locality(self):
        """Gets the locality of this AddressInformation.  # noqa: E501


        :return: The locality of this AddressInformation.  # noqa: E501
        :rtype: str
        """
        return self._locality

    @locality.setter
    def locality(self, locality):
        """Sets the locality of this AddressInformation.


        :param locality: The locality of this AddressInformation.  # noqa: E501
        :type: str
        """

        self._locality = locality

    @property
    def region(self):
        """Gets the region of this AddressInformation.  # noqa: E501


        :return: The region of this AddressInformation.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this AddressInformation.


        :param region: The region of this AddressInformation.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def postal_code(self):
        """Gets the postal_code of this AddressInformation.  # noqa: E501


        :return: The postal_code of this AddressInformation.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this AddressInformation.


        :param postal_code: The postal_code of this AddressInformation.  # noqa: E501
        :type: str
        """

        self._postal_code = postal_code

    @property
    def country(self):
        """Gets the country of this AddressInformation.  # noqa: E501


        :return: The country of this AddressInformation.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this AddressInformation.


        :param country: The country of this AddressInformation.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def phone(self):
        """Gets the phone of this AddressInformation.  # noqa: E501


        :return: The phone of this AddressInformation.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this AddressInformation.


        :param phone: The phone of this AddressInformation.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def fax(self):
        """Gets the fax of this AddressInformation.  # noqa: E501


        :return: The fax of this AddressInformation.  # noqa: E501
        :rtype: str
        """
        return self._fax

    @fax.setter
    def fax(self, fax):
        """Sets the fax of this AddressInformation.


        :param fax: The fax of this AddressInformation.  # noqa: E501
        :type: str
        """

        self._fax = fax

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
        if issubclass(AddressInformation, dict):
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
        if not isinstance(other, AddressInformation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AddressInformation):
            return True

        return self.to_dict() != other.to_dict()
