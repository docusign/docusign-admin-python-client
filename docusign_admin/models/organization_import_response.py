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


class OrganizationImportResponse(object):
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
        'requestor': 'OrganizationImportResponseRequestor',
        'created': 'datetime',
        'last_modified': 'datetime',
        'status': 'str',
        'user_count': 'int',
        'processed_user_count': 'int',
        'added_user_count': 'int',
        'updated_user_count': 'int',
        'closed_user_count': 'int',
        'no_action_required_user_count': 'int',
        'error_count': 'int',
        'warning_count': 'int',
        'invalid_column_headers': 'str',
        'imports_not_found_or_not_available_for_accounts': 'str',
        'imports_failed_for_accounts': 'str',
        'imports_timed_out_for_accounts': 'str',
        'imports_not_found_or_not_available_for_sites': 'str',
        'imports_failed_for_sites': 'str',
        'imports_timed_out_for_sites': 'str',
        'file_level_error_rollups': 'list[OrganizationImportResponseErrorRollup]',
        'user_level_error_rollups': 'list[OrganizationImportResponseErrorRollup]',
        'user_level_warning_rollups': 'list[OrganizationImportResponseWarningRollup]',
        'has_csv_results': 'bool',
        'results_uri': 'str'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'requestor': 'requestor',
        'created': 'created',
        'last_modified': 'last_modified',
        'status': 'status',
        'user_count': 'user_count',
        'processed_user_count': 'processed_user_count',
        'added_user_count': 'added_user_count',
        'updated_user_count': 'updated_user_count',
        'closed_user_count': 'closed_user_count',
        'no_action_required_user_count': 'no_action_required_user_count',
        'error_count': 'error_count',
        'warning_count': 'warning_count',
        'invalid_column_headers': 'invalid_column_headers',
        'imports_not_found_or_not_available_for_accounts': 'imports_not_found_or_not_available_for_accounts',
        'imports_failed_for_accounts': 'imports_failed_for_accounts',
        'imports_timed_out_for_accounts': 'imports_timed_out_for_accounts',
        'imports_not_found_or_not_available_for_sites': 'imports_not_found_or_not_available_for_sites',
        'imports_failed_for_sites': 'imports_failed_for_sites',
        'imports_timed_out_for_sites': 'imports_timed_out_for_sites',
        'file_level_error_rollups': 'file_level_error_rollups',
        'user_level_error_rollups': 'user_level_error_rollups',
        'user_level_warning_rollups': 'user_level_warning_rollups',
        'has_csv_results': 'has_csv_results',
        'results_uri': 'results_uri'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """OrganizationImportResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._type = None
        self._requestor = None
        self._created = None
        self._last_modified = None
        self._status = None
        self._user_count = None
        self._processed_user_count = None
        self._added_user_count = None
        self._updated_user_count = None
        self._closed_user_count = None
        self._no_action_required_user_count = None
        self._error_count = None
        self._warning_count = None
        self._invalid_column_headers = None
        self._imports_not_found_or_not_available_for_accounts = None
        self._imports_failed_for_accounts = None
        self._imports_timed_out_for_accounts = None
        self._imports_not_found_or_not_available_for_sites = None
        self._imports_failed_for_sites = None
        self._imports_timed_out_for_sites = None
        self._file_level_error_rollups = None
        self._user_level_error_rollups = None
        self._user_level_warning_rollups = None
        self._has_csv_results = None
        self._results_uri = None
        self.discriminator = None

        setattr(self, "_{}".format('id'), kwargs.get('id', None))
        setattr(self, "_{}".format('type'), kwargs.get('type', None))
        setattr(self, "_{}".format('requestor'), kwargs.get('requestor', None))
        setattr(self, "_{}".format('created'), kwargs.get('created', None))
        setattr(self, "_{}".format('last_modified'), kwargs.get('last_modified', None))
        setattr(self, "_{}".format('status'), kwargs.get('status', None))
        setattr(self, "_{}".format('user_count'), kwargs.get('user_count', None))
        setattr(self, "_{}".format('processed_user_count'), kwargs.get('processed_user_count', None))
        setattr(self, "_{}".format('added_user_count'), kwargs.get('added_user_count', None))
        setattr(self, "_{}".format('updated_user_count'), kwargs.get('updated_user_count', None))
        setattr(self, "_{}".format('closed_user_count'), kwargs.get('closed_user_count', None))
        setattr(self, "_{}".format('no_action_required_user_count'), kwargs.get('no_action_required_user_count', None))
        setattr(self, "_{}".format('error_count'), kwargs.get('error_count', None))
        setattr(self, "_{}".format('warning_count'), kwargs.get('warning_count', None))
        setattr(self, "_{}".format('invalid_column_headers'), kwargs.get('invalid_column_headers', None))
        setattr(self, "_{}".format('imports_not_found_or_not_available_for_accounts'), kwargs.get('imports_not_found_or_not_available_for_accounts', None))
        setattr(self, "_{}".format('imports_failed_for_accounts'), kwargs.get('imports_failed_for_accounts', None))
        setattr(self, "_{}".format('imports_timed_out_for_accounts'), kwargs.get('imports_timed_out_for_accounts', None))
        setattr(self, "_{}".format('imports_not_found_or_not_available_for_sites'), kwargs.get('imports_not_found_or_not_available_for_sites', None))
        setattr(self, "_{}".format('imports_failed_for_sites'), kwargs.get('imports_failed_for_sites', None))
        setattr(self, "_{}".format('imports_timed_out_for_sites'), kwargs.get('imports_timed_out_for_sites', None))
        setattr(self, "_{}".format('file_level_error_rollups'), kwargs.get('file_level_error_rollups', None))
        setattr(self, "_{}".format('user_level_error_rollups'), kwargs.get('user_level_error_rollups', None))
        setattr(self, "_{}".format('user_level_warning_rollups'), kwargs.get('user_level_warning_rollups', None))
        setattr(self, "_{}".format('has_csv_results'), kwargs.get('has_csv_results', None))
        setattr(self, "_{}".format('results_uri'), kwargs.get('results_uri', None))

    @property
    def id(self):
        """Gets the id of this OrganizationImportResponse.  # noqa: E501


        :return: The id of this OrganizationImportResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OrganizationImportResponse.


        :param id: The id of this OrganizationImportResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this OrganizationImportResponse.  # noqa: E501


        :return: The type of this OrganizationImportResponse.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OrganizationImportResponse.


        :param type: The type of this OrganizationImportResponse.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def requestor(self):
        """Gets the requestor of this OrganizationImportResponse.  # noqa: E501


        :return: The requestor of this OrganizationImportResponse.  # noqa: E501
        :rtype: OrganizationImportResponseRequestor
        """
        return self._requestor

    @requestor.setter
    def requestor(self, requestor):
        """Sets the requestor of this OrganizationImportResponse.


        :param requestor: The requestor of this OrganizationImportResponse.  # noqa: E501
        :type: OrganizationImportResponseRequestor
        """

        self._requestor = requestor

    @property
    def created(self):
        """Gets the created of this OrganizationImportResponse.  # noqa: E501


        :return: The created of this OrganizationImportResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this OrganizationImportResponse.


        :param created: The created of this OrganizationImportResponse.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def last_modified(self):
        """Gets the last_modified of this OrganizationImportResponse.  # noqa: E501


        :return: The last_modified of this OrganizationImportResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this OrganizationImportResponse.


        :param last_modified: The last_modified of this OrganizationImportResponse.  # noqa: E501
        :type: datetime
        """

        self._last_modified = last_modified

    @property
    def status(self):
        """Gets the status of this OrganizationImportResponse.  # noqa: E501


        :return: The status of this OrganizationImportResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this OrganizationImportResponse.


        :param status: The status of this OrganizationImportResponse.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def user_count(self):
        """Gets the user_count of this OrganizationImportResponse.  # noqa: E501


        :return: The user_count of this OrganizationImportResponse.  # noqa: E501
        :rtype: int
        """
        return self._user_count

    @user_count.setter
    def user_count(self, user_count):
        """Sets the user_count of this OrganizationImportResponse.


        :param user_count: The user_count of this OrganizationImportResponse.  # noqa: E501
        :type: int
        """

        self._user_count = user_count

    @property
    def processed_user_count(self):
        """Gets the processed_user_count of this OrganizationImportResponse.  # noqa: E501


        :return: The processed_user_count of this OrganizationImportResponse.  # noqa: E501
        :rtype: int
        """
        return self._processed_user_count

    @processed_user_count.setter
    def processed_user_count(self, processed_user_count):
        """Sets the processed_user_count of this OrganizationImportResponse.


        :param processed_user_count: The processed_user_count of this OrganizationImportResponse.  # noqa: E501
        :type: int
        """

        self._processed_user_count = processed_user_count

    @property
    def added_user_count(self):
        """Gets the added_user_count of this OrganizationImportResponse.  # noqa: E501


        :return: The added_user_count of this OrganizationImportResponse.  # noqa: E501
        :rtype: int
        """
        return self._added_user_count

    @added_user_count.setter
    def added_user_count(self, added_user_count):
        """Sets the added_user_count of this OrganizationImportResponse.


        :param added_user_count: The added_user_count of this OrganizationImportResponse.  # noqa: E501
        :type: int
        """

        self._added_user_count = added_user_count

    @property
    def updated_user_count(self):
        """Gets the updated_user_count of this OrganizationImportResponse.  # noqa: E501


        :return: The updated_user_count of this OrganizationImportResponse.  # noqa: E501
        :rtype: int
        """
        return self._updated_user_count

    @updated_user_count.setter
    def updated_user_count(self, updated_user_count):
        """Sets the updated_user_count of this OrganizationImportResponse.


        :param updated_user_count: The updated_user_count of this OrganizationImportResponse.  # noqa: E501
        :type: int
        """

        self._updated_user_count = updated_user_count

    @property
    def closed_user_count(self):
        """Gets the closed_user_count of this OrganizationImportResponse.  # noqa: E501


        :return: The closed_user_count of this OrganizationImportResponse.  # noqa: E501
        :rtype: int
        """
        return self._closed_user_count

    @closed_user_count.setter
    def closed_user_count(self, closed_user_count):
        """Sets the closed_user_count of this OrganizationImportResponse.


        :param closed_user_count: The closed_user_count of this OrganizationImportResponse.  # noqa: E501
        :type: int
        """

        self._closed_user_count = closed_user_count

    @property
    def no_action_required_user_count(self):
        """Gets the no_action_required_user_count of this OrganizationImportResponse.  # noqa: E501


        :return: The no_action_required_user_count of this OrganizationImportResponse.  # noqa: E501
        :rtype: int
        """
        return self._no_action_required_user_count

    @no_action_required_user_count.setter
    def no_action_required_user_count(self, no_action_required_user_count):
        """Sets the no_action_required_user_count of this OrganizationImportResponse.


        :param no_action_required_user_count: The no_action_required_user_count of this OrganizationImportResponse.  # noqa: E501
        :type: int
        """

        self._no_action_required_user_count = no_action_required_user_count

    @property
    def error_count(self):
        """Gets the error_count of this OrganizationImportResponse.  # noqa: E501


        :return: The error_count of this OrganizationImportResponse.  # noqa: E501
        :rtype: int
        """
        return self._error_count

    @error_count.setter
    def error_count(self, error_count):
        """Sets the error_count of this OrganizationImportResponse.


        :param error_count: The error_count of this OrganizationImportResponse.  # noqa: E501
        :type: int
        """

        self._error_count = error_count

    @property
    def warning_count(self):
        """Gets the warning_count of this OrganizationImportResponse.  # noqa: E501


        :return: The warning_count of this OrganizationImportResponse.  # noqa: E501
        :rtype: int
        """
        return self._warning_count

    @warning_count.setter
    def warning_count(self, warning_count):
        """Sets the warning_count of this OrganizationImportResponse.


        :param warning_count: The warning_count of this OrganizationImportResponse.  # noqa: E501
        :type: int
        """

        self._warning_count = warning_count

    @property
    def invalid_column_headers(self):
        """Gets the invalid_column_headers of this OrganizationImportResponse.  # noqa: E501


        :return: The invalid_column_headers of this OrganizationImportResponse.  # noqa: E501
        :rtype: str
        """
        return self._invalid_column_headers

    @invalid_column_headers.setter
    def invalid_column_headers(self, invalid_column_headers):
        """Sets the invalid_column_headers of this OrganizationImportResponse.


        :param invalid_column_headers: The invalid_column_headers of this OrganizationImportResponse.  # noqa: E501
        :type: str
        """

        self._invalid_column_headers = invalid_column_headers

    @property
    def imports_not_found_or_not_available_for_accounts(self):
        """Gets the imports_not_found_or_not_available_for_accounts of this OrganizationImportResponse.  # noqa: E501


        :return: The imports_not_found_or_not_available_for_accounts of this OrganizationImportResponse.  # noqa: E501
        :rtype: str
        """
        return self._imports_not_found_or_not_available_for_accounts

    @imports_not_found_or_not_available_for_accounts.setter
    def imports_not_found_or_not_available_for_accounts(self, imports_not_found_or_not_available_for_accounts):
        """Sets the imports_not_found_or_not_available_for_accounts of this OrganizationImportResponse.


        :param imports_not_found_or_not_available_for_accounts: The imports_not_found_or_not_available_for_accounts of this OrganizationImportResponse.  # noqa: E501
        :type: str
        """

        self._imports_not_found_or_not_available_for_accounts = imports_not_found_or_not_available_for_accounts

    @property
    def imports_failed_for_accounts(self):
        """Gets the imports_failed_for_accounts of this OrganizationImportResponse.  # noqa: E501


        :return: The imports_failed_for_accounts of this OrganizationImportResponse.  # noqa: E501
        :rtype: str
        """
        return self._imports_failed_for_accounts

    @imports_failed_for_accounts.setter
    def imports_failed_for_accounts(self, imports_failed_for_accounts):
        """Sets the imports_failed_for_accounts of this OrganizationImportResponse.


        :param imports_failed_for_accounts: The imports_failed_for_accounts of this OrganizationImportResponse.  # noqa: E501
        :type: str
        """

        self._imports_failed_for_accounts = imports_failed_for_accounts

    @property
    def imports_timed_out_for_accounts(self):
        """Gets the imports_timed_out_for_accounts of this OrganizationImportResponse.  # noqa: E501


        :return: The imports_timed_out_for_accounts of this OrganizationImportResponse.  # noqa: E501
        :rtype: str
        """
        return self._imports_timed_out_for_accounts

    @imports_timed_out_for_accounts.setter
    def imports_timed_out_for_accounts(self, imports_timed_out_for_accounts):
        """Sets the imports_timed_out_for_accounts of this OrganizationImportResponse.


        :param imports_timed_out_for_accounts: The imports_timed_out_for_accounts of this OrganizationImportResponse.  # noqa: E501
        :type: str
        """

        self._imports_timed_out_for_accounts = imports_timed_out_for_accounts

    @property
    def imports_not_found_or_not_available_for_sites(self):
        """Gets the imports_not_found_or_not_available_for_sites of this OrganizationImportResponse.  # noqa: E501


        :return: The imports_not_found_or_not_available_for_sites of this OrganizationImportResponse.  # noqa: E501
        :rtype: str
        """
        return self._imports_not_found_or_not_available_for_sites

    @imports_not_found_or_not_available_for_sites.setter
    def imports_not_found_or_not_available_for_sites(self, imports_not_found_or_not_available_for_sites):
        """Sets the imports_not_found_or_not_available_for_sites of this OrganizationImportResponse.


        :param imports_not_found_or_not_available_for_sites: The imports_not_found_or_not_available_for_sites of this OrganizationImportResponse.  # noqa: E501
        :type: str
        """

        self._imports_not_found_or_not_available_for_sites = imports_not_found_or_not_available_for_sites

    @property
    def imports_failed_for_sites(self):
        """Gets the imports_failed_for_sites of this OrganizationImportResponse.  # noqa: E501


        :return: The imports_failed_for_sites of this OrganizationImportResponse.  # noqa: E501
        :rtype: str
        """
        return self._imports_failed_for_sites

    @imports_failed_for_sites.setter
    def imports_failed_for_sites(self, imports_failed_for_sites):
        """Sets the imports_failed_for_sites of this OrganizationImportResponse.


        :param imports_failed_for_sites: The imports_failed_for_sites of this OrganizationImportResponse.  # noqa: E501
        :type: str
        """

        self._imports_failed_for_sites = imports_failed_for_sites

    @property
    def imports_timed_out_for_sites(self):
        """Gets the imports_timed_out_for_sites of this OrganizationImportResponse.  # noqa: E501


        :return: The imports_timed_out_for_sites of this OrganizationImportResponse.  # noqa: E501
        :rtype: str
        """
        return self._imports_timed_out_for_sites

    @imports_timed_out_for_sites.setter
    def imports_timed_out_for_sites(self, imports_timed_out_for_sites):
        """Sets the imports_timed_out_for_sites of this OrganizationImportResponse.


        :param imports_timed_out_for_sites: The imports_timed_out_for_sites of this OrganizationImportResponse.  # noqa: E501
        :type: str
        """

        self._imports_timed_out_for_sites = imports_timed_out_for_sites

    @property
    def file_level_error_rollups(self):
        """Gets the file_level_error_rollups of this OrganizationImportResponse.  # noqa: E501


        :return: The file_level_error_rollups of this OrganizationImportResponse.  # noqa: E501
        :rtype: list[OrganizationImportResponseErrorRollup]
        """
        return self._file_level_error_rollups

    @file_level_error_rollups.setter
    def file_level_error_rollups(self, file_level_error_rollups):
        """Sets the file_level_error_rollups of this OrganizationImportResponse.


        :param file_level_error_rollups: The file_level_error_rollups of this OrganizationImportResponse.  # noqa: E501
        :type: list[OrganizationImportResponseErrorRollup]
        """

        self._file_level_error_rollups = file_level_error_rollups

    @property
    def user_level_error_rollups(self):
        """Gets the user_level_error_rollups of this OrganizationImportResponse.  # noqa: E501


        :return: The user_level_error_rollups of this OrganizationImportResponse.  # noqa: E501
        :rtype: list[OrganizationImportResponseErrorRollup]
        """
        return self._user_level_error_rollups

    @user_level_error_rollups.setter
    def user_level_error_rollups(self, user_level_error_rollups):
        """Sets the user_level_error_rollups of this OrganizationImportResponse.


        :param user_level_error_rollups: The user_level_error_rollups of this OrganizationImportResponse.  # noqa: E501
        :type: list[OrganizationImportResponseErrorRollup]
        """

        self._user_level_error_rollups = user_level_error_rollups

    @property
    def user_level_warning_rollups(self):
        """Gets the user_level_warning_rollups of this OrganizationImportResponse.  # noqa: E501


        :return: The user_level_warning_rollups of this OrganizationImportResponse.  # noqa: E501
        :rtype: list[OrganizationImportResponseWarningRollup]
        """
        return self._user_level_warning_rollups

    @user_level_warning_rollups.setter
    def user_level_warning_rollups(self, user_level_warning_rollups):
        """Sets the user_level_warning_rollups of this OrganizationImportResponse.


        :param user_level_warning_rollups: The user_level_warning_rollups of this OrganizationImportResponse.  # noqa: E501
        :type: list[OrganizationImportResponseWarningRollup]
        """

        self._user_level_warning_rollups = user_level_warning_rollups

    @property
    def has_csv_results(self):
        """Gets the has_csv_results of this OrganizationImportResponse.  # noqa: E501


        :return: The has_csv_results of this OrganizationImportResponse.  # noqa: E501
        :rtype: bool
        """
        return self._has_csv_results

    @has_csv_results.setter
    def has_csv_results(self, has_csv_results):
        """Sets the has_csv_results of this OrganizationImportResponse.


        :param has_csv_results: The has_csv_results of this OrganizationImportResponse.  # noqa: E501
        :type: bool
        """

        self._has_csv_results = has_csv_results

    @property
    def results_uri(self):
        """Gets the results_uri of this OrganizationImportResponse.  # noqa: E501


        :return: The results_uri of this OrganizationImportResponse.  # noqa: E501
        :rtype: str
        """
        return self._results_uri

    @results_uri.setter
    def results_uri(self, results_uri):
        """Sets the results_uri of this OrganizationImportResponse.


        :param results_uri: The results_uri of this OrganizationImportResponse.  # noqa: E501
        :type: str
        """

        self._results_uri = results_uri

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
        if issubclass(OrganizationImportResponse, dict):
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
        if not isinstance(other, OrganizationImportResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrganizationImportResponse):
            return True

        return self.to_dict() != other.to_dict()
