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


class SubAccountCreateRequest(object):
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
        'subscription_details': 'SubAccountCreateRequestSubAccountCreationSubscription',
        'target_account': 'SubAccountCreateRequestSubAccountCreationTargetAccountDetails'
    }

    attribute_map = {
        'subscription_details': 'subscriptionDetails',
        'target_account': 'targetAccount'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """SubAccountCreateRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._subscription_details = None
        self._target_account = None
        self.discriminator = None

        setattr(self, "_{}".format('subscription_details'), kwargs.get('subscription_details', None))
        setattr(self, "_{}".format('target_account'), kwargs.get('target_account', None))

    @property
    def subscription_details(self):
        """Gets the subscription_details of this SubAccountCreateRequest.  # noqa: E501


        :return: The subscription_details of this SubAccountCreateRequest.  # noqa: E501
        :rtype: SubAccountCreateRequestSubAccountCreationSubscription
        """
        return self._subscription_details

    @subscription_details.setter
    def subscription_details(self, subscription_details):
        """Sets the subscription_details of this SubAccountCreateRequest.


        :param subscription_details: The subscription_details of this SubAccountCreateRequest.  # noqa: E501
        :type: SubAccountCreateRequestSubAccountCreationSubscription
        """

        self._subscription_details = subscription_details

    @property
    def target_account(self):
        """Gets the target_account of this SubAccountCreateRequest.  # noqa: E501


        :return: The target_account of this SubAccountCreateRequest.  # noqa: E501
        :rtype: SubAccountCreateRequestSubAccountCreationTargetAccountDetails
        """
        return self._target_account

    @target_account.setter
    def target_account(self, target_account):
        """Sets the target_account of this SubAccountCreateRequest.


        :param target_account: The target_account of this SubAccountCreateRequest.  # noqa: E501
        :type: SubAccountCreateRequestSubAccountCreationTargetAccountDetails
        """

        self._target_account = target_account

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
        if issubclass(SubAccountCreateRequest, dict):
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
        if not isinstance(other, SubAccountCreateRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SubAccountCreateRequest):
            return True

        return self.to_dict() != other.to_dict()