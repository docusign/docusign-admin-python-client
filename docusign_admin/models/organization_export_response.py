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


class OrganizationExportResponse(object):
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
        'type': 'str',
        'requestor': 'OrganizationExportRequestorResponse',
        'created': 'datetime',
        'last_modified': 'datetime',
        'completed': 'datetime',
        'expires': 'datetime',
        'status': 'str',
        'selected_accounts': 'list[OrgExportSelectedAccount]',
        'selected_domains': 'list[OrgExportSelectedDomain]',
        'metadata_url': 'str',
        'percent_completed': 'int',
        'number_rows': 'int',
        'size_bytes': 'int',
        'results': 'list[OrganizationExportTaskResponse]',
        'success': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'requestor': 'requestor',
        'created': 'created',
        'last_modified': 'last_modified',
        'completed': 'completed',
        'expires': 'expires',
        'status': 'status',
        'selected_accounts': 'selected_accounts',
        'selected_domains': 'selected_domains',
        'metadata_url': 'metadata_url',
        'percent_completed': 'percent_completed',
        'number_rows': 'number_rows',
        'size_bytes': 'size_bytes',
        'results': 'results',
        'success': 'success'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """OrganizationExportResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._type = None
        self._requestor = None
        self._created = None
        self._last_modified = None
        self._completed = None
        self._expires = None
        self._status = None
        self._selected_accounts = None
        self._selected_domains = None
        self._metadata_url = None
        self._percent_completed = None
        self._number_rows = None
        self._size_bytes = None
        self._results = None
        self._success = None
        self.discriminator = None

        setattr(self, "_{}".format('id'), kwargs.get('id', None))
        setattr(self, "_{}".format('type'), kwargs.get('type', None))
        setattr(self, "_{}".format('requestor'), kwargs.get('requestor', None))
        setattr(self, "_{}".format('created'), kwargs.get('created', None))
        setattr(self, "_{}".format('last_modified'), kwargs.get('last_modified', None))
        setattr(self, "_{}".format('completed'), kwargs.get('completed', None))
        setattr(self, "_{}".format('expires'), kwargs.get('expires', None))
        setattr(self, "_{}".format('status'), kwargs.get('status', None))
        setattr(self, "_{}".format('selected_accounts'), kwargs.get('selected_accounts', None))
        setattr(self, "_{}".format('selected_domains'), kwargs.get('selected_domains', None))
        setattr(self, "_{}".format('metadata_url'), kwargs.get('metadata_url', None))
        setattr(self, "_{}".format('percent_completed'), kwargs.get('percent_completed', None))
        setattr(self, "_{}".format('number_rows'), kwargs.get('number_rows', None))
        setattr(self, "_{}".format('size_bytes'), kwargs.get('size_bytes', None))
        setattr(self, "_{}".format('results'), kwargs.get('results', None))
        setattr(self, "_{}".format('success'), kwargs.get('success', None))

    @property
    def id(self):
        """Gets the id of this OrganizationExportResponse.  # noqa: E501


        :return: The id of this OrganizationExportResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OrganizationExportResponse.


        :param id: The id of this OrganizationExportResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this OrganizationExportResponse.  # noqa: E501


        :return: The type of this OrganizationExportResponse.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OrganizationExportResponse.


        :param type: The type of this OrganizationExportResponse.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def requestor(self):
        """Gets the requestor of this OrganizationExportResponse.  # noqa: E501


        :return: The requestor of this OrganizationExportResponse.  # noqa: E501
        :rtype: OrganizationExportRequestorResponse
        """
        return self._requestor

    @requestor.setter
    def requestor(self, requestor):
        """Sets the requestor of this OrganizationExportResponse.


        :param requestor: The requestor of this OrganizationExportResponse.  # noqa: E501
        :type: OrganizationExportRequestorResponse
        """

        self._requestor = requestor

    @property
    def created(self):
        """Gets the created of this OrganizationExportResponse.  # noqa: E501


        :return: The created of this OrganizationExportResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this OrganizationExportResponse.


        :param created: The created of this OrganizationExportResponse.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def last_modified(self):
        """Gets the last_modified of this OrganizationExportResponse.  # noqa: E501


        :return: The last_modified of this OrganizationExportResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this OrganizationExportResponse.


        :param last_modified: The last_modified of this OrganizationExportResponse.  # noqa: E501
        :type: datetime
        """

        self._last_modified = last_modified

    @property
    def completed(self):
        """Gets the completed of this OrganizationExportResponse.  # noqa: E501


        :return: The completed of this OrganizationExportResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._completed

    @completed.setter
    def completed(self, completed):
        """Sets the completed of this OrganizationExportResponse.


        :param completed: The completed of this OrganizationExportResponse.  # noqa: E501
        :type: datetime
        """

        self._completed = completed

    @property
    def expires(self):
        """Gets the expires of this OrganizationExportResponse.  # noqa: E501


        :return: The expires of this OrganizationExportResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._expires

    @expires.setter
    def expires(self, expires):
        """Sets the expires of this OrganizationExportResponse.


        :param expires: The expires of this OrganizationExportResponse.  # noqa: E501
        :type: datetime
        """

        self._expires = expires

    @property
    def status(self):
        """Gets the status of this OrganizationExportResponse.  # noqa: E501


        :return: The status of this OrganizationExportResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this OrganizationExportResponse.


        :param status: The status of this OrganizationExportResponse.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def selected_accounts(self):
        """Gets the selected_accounts of this OrganizationExportResponse.  # noqa: E501


        :return: The selected_accounts of this OrganizationExportResponse.  # noqa: E501
        :rtype: list[OrgExportSelectedAccount]
        """
        return self._selected_accounts

    @selected_accounts.setter
    def selected_accounts(self, selected_accounts):
        """Sets the selected_accounts of this OrganizationExportResponse.


        :param selected_accounts: The selected_accounts of this OrganizationExportResponse.  # noqa: E501
        :type: list[OrgExportSelectedAccount]
        """

        self._selected_accounts = selected_accounts

    @property
    def selected_domains(self):
        """Gets the selected_domains of this OrganizationExportResponse.  # noqa: E501


        :return: The selected_domains of this OrganizationExportResponse.  # noqa: E501
        :rtype: list[OrgExportSelectedDomain]
        """
        return self._selected_domains

    @selected_domains.setter
    def selected_domains(self, selected_domains):
        """Sets the selected_domains of this OrganizationExportResponse.


        :param selected_domains: The selected_domains of this OrganizationExportResponse.  # noqa: E501
        :type: list[OrgExportSelectedDomain]
        """

        self._selected_domains = selected_domains

    @property
    def metadata_url(self):
        """Gets the metadata_url of this OrganizationExportResponse.  # noqa: E501


        :return: The metadata_url of this OrganizationExportResponse.  # noqa: E501
        :rtype: str
        """
        return self._metadata_url

    @metadata_url.setter
    def metadata_url(self, metadata_url):
        """Sets the metadata_url of this OrganizationExportResponse.


        :param metadata_url: The metadata_url of this OrganizationExportResponse.  # noqa: E501
        :type: str
        """

        self._metadata_url = metadata_url

    @property
    def percent_completed(self):
        """Gets the percent_completed of this OrganizationExportResponse.  # noqa: E501


        :return: The percent_completed of this OrganizationExportResponse.  # noqa: E501
        :rtype: int
        """
        return self._percent_completed

    @percent_completed.setter
    def percent_completed(self, percent_completed):
        """Sets the percent_completed of this OrganizationExportResponse.


        :param percent_completed: The percent_completed of this OrganizationExportResponse.  # noqa: E501
        :type: int
        """

        self._percent_completed = percent_completed

    @property
    def number_rows(self):
        """Gets the number_rows of this OrganizationExportResponse.  # noqa: E501


        :return: The number_rows of this OrganizationExportResponse.  # noqa: E501
        :rtype: int
        """
        return self._number_rows

    @number_rows.setter
    def number_rows(self, number_rows):
        """Sets the number_rows of this OrganizationExportResponse.


        :param number_rows: The number_rows of this OrganizationExportResponse.  # noqa: E501
        :type: int
        """

        self._number_rows = number_rows

    @property
    def size_bytes(self):
        """Gets the size_bytes of this OrganizationExportResponse.  # noqa: E501


        :return: The size_bytes of this OrganizationExportResponse.  # noqa: E501
        :rtype: int
        """
        return self._size_bytes

    @size_bytes.setter
    def size_bytes(self, size_bytes):
        """Sets the size_bytes of this OrganizationExportResponse.


        :param size_bytes: The size_bytes of this OrganizationExportResponse.  # noqa: E501
        :type: int
        """

        self._size_bytes = size_bytes

    @property
    def results(self):
        """Gets the results of this OrganizationExportResponse.  # noqa: E501


        :return: The results of this OrganizationExportResponse.  # noqa: E501
        :rtype: list[OrganizationExportTaskResponse]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this OrganizationExportResponse.


        :param results: The results of this OrganizationExportResponse.  # noqa: E501
        :type: list[OrganizationExportTaskResponse]
        """

        self._results = results

    @property
    def success(self):
        """Gets the success of this OrganizationExportResponse.  # noqa: E501


        :return: The success of this OrganizationExportResponse.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this OrganizationExportResponse.


        :param success: The success of this OrganizationExportResponse.  # noqa: E501
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
        if issubclass(OrganizationExportResponse, dict):
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
        if not isinstance(other, OrganizationExportResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrganizationExportResponse):
            return True

        return self.to_dict() != other.to_dict()
