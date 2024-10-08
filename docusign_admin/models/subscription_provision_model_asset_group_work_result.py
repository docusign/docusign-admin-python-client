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


class SubscriptionProvisionModelAssetGroupWorkResult(object):
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
        'asset_group_work': 'SubscriptionProvisionModelAssetGroupWork',
        'message': 'str',
        'success': 'bool'
    }

    attribute_map = {
        'asset_group_work': 'AssetGroupWork',
        'message': 'Message',
        'success': 'Success'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """SubscriptionProvisionModelAssetGroupWorkResult - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._asset_group_work = None
        self._message = None
        self._success = None
        self.discriminator = None

        setattr(self, "_{}".format('asset_group_work'), kwargs.get('asset_group_work', None))
        setattr(self, "_{}".format('message'), kwargs.get('message', None))
        setattr(self, "_{}".format('success'), kwargs.get('success', None))

    @property
    def asset_group_work(self):
        """Gets the asset_group_work of this SubscriptionProvisionModelAssetGroupWorkResult.  # noqa: E501


        :return: The asset_group_work of this SubscriptionProvisionModelAssetGroupWorkResult.  # noqa: E501
        :rtype: SubscriptionProvisionModelAssetGroupWork
        """
        return self._asset_group_work

    @asset_group_work.setter
    def asset_group_work(self, asset_group_work):
        """Sets the asset_group_work of this SubscriptionProvisionModelAssetGroupWorkResult.


        :param asset_group_work: The asset_group_work of this SubscriptionProvisionModelAssetGroupWorkResult.  # noqa: E501
        :type: SubscriptionProvisionModelAssetGroupWork
        """

        self._asset_group_work = asset_group_work

    @property
    def message(self):
        """Gets the message of this SubscriptionProvisionModelAssetGroupWorkResult.  # noqa: E501


        :return: The message of this SubscriptionProvisionModelAssetGroupWorkResult.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this SubscriptionProvisionModelAssetGroupWorkResult.


        :param message: The message of this SubscriptionProvisionModelAssetGroupWorkResult.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def success(self):
        """Gets the success of this SubscriptionProvisionModelAssetGroupWorkResult.  # noqa: E501


        :return: The success of this SubscriptionProvisionModelAssetGroupWorkResult.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this SubscriptionProvisionModelAssetGroupWorkResult.


        :param success: The success of this SubscriptionProvisionModelAssetGroupWorkResult.  # noqa: E501
        :type: bool
        """

        self._success = success

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
        if issubclass(SubscriptionProvisionModelAssetGroupWorkResult, dict):
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
        if not isinstance(other, SubscriptionProvisionModelAssetGroupWorkResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SubscriptionProvisionModelAssetGroupWorkResult):
            return True

        return self.to_dict() != other.to_dict()
