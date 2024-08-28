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


class SubscriptionProvisionModelAccountCreateCreateAccountSubscriptionDetails(object):
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
        'subscription_id': 'str',
        'plan_id': 'str',
        'modules': 'list[str]'
    }

    attribute_map = {
        'subscription_id': 'SubscriptionId',
        'plan_id': 'PlanId',
        'modules': 'Modules'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """SubscriptionProvisionModelAccountCreateCreateAccountSubscriptionDetails - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._subscription_id = None
        self._plan_id = None
        self._modules = None
        self.discriminator = None

        setattr(self, "_{}".format('subscription_id'), kwargs.get('subscription_id', None))
        setattr(self, "_{}".format('plan_id'), kwargs.get('plan_id', None))
        setattr(self, "_{}".format('modules'), kwargs.get('modules', None))

    @property
    def subscription_id(self):
        """Gets the subscription_id of this SubscriptionProvisionModelAccountCreateCreateAccountSubscriptionDetails.  # noqa: E501


        :return: The subscription_id of this SubscriptionProvisionModelAccountCreateCreateAccountSubscriptionDetails.  # noqa: E501
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this SubscriptionProvisionModelAccountCreateCreateAccountSubscriptionDetails.


        :param subscription_id: The subscription_id of this SubscriptionProvisionModelAccountCreateCreateAccountSubscriptionDetails.  # noqa: E501
        :type: str
        """

        self._subscription_id = subscription_id

    @property
    def plan_id(self):
        """Gets the plan_id of this SubscriptionProvisionModelAccountCreateCreateAccountSubscriptionDetails.  # noqa: E501


        :return: The plan_id of this SubscriptionProvisionModelAccountCreateCreateAccountSubscriptionDetails.  # noqa: E501
        :rtype: str
        """
        return self._plan_id

    @plan_id.setter
    def plan_id(self, plan_id):
        """Sets the plan_id of this SubscriptionProvisionModelAccountCreateCreateAccountSubscriptionDetails.


        :param plan_id: The plan_id of this SubscriptionProvisionModelAccountCreateCreateAccountSubscriptionDetails.  # noqa: E501
        :type: str
        """

        self._plan_id = plan_id

    @property
    def modules(self):
        """Gets the modules of this SubscriptionProvisionModelAccountCreateCreateAccountSubscriptionDetails.  # noqa: E501


        :return: The modules of this SubscriptionProvisionModelAccountCreateCreateAccountSubscriptionDetails.  # noqa: E501
        :rtype: list[str]
        """
        return self._modules

    @modules.setter
    def modules(self, modules):
        """Sets the modules of this SubscriptionProvisionModelAccountCreateCreateAccountSubscriptionDetails.


        :param modules: The modules of this SubscriptionProvisionModelAccountCreateCreateAccountSubscriptionDetails.  # noqa: E501
        :type: list[str]
        """

        self._modules = modules

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
        if issubclass(SubscriptionProvisionModelAccountCreateCreateAccountSubscriptionDetails, dict):
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
        if not isinstance(other, SubscriptionProvisionModelAccountCreateCreateAccountSubscriptionDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SubscriptionProvisionModelAccountCreateCreateAccountSubscriptionDetails):
            return True

        return self.to_dict() != other.to_dict()
