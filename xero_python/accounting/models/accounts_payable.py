# coding: utf-8

"""
    Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 2.7.0
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class AccountsPayable(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {"outstanding": "float", "overdue": "float"}

    attribute_map = {"outstanding": "Outstanding", "overdue": "Overdue"}

    def __init__(self, outstanding=None, overdue=None):  # noqa: E501
        """AccountsPayable - a model defined in OpenAPI"""  # noqa: E501

        self._outstanding = None
        self._overdue = None
        self.discriminator = None

        if outstanding is not None:
            self.outstanding = outstanding
        if overdue is not None:
            self.overdue = overdue

    @property
    def outstanding(self):
        """Gets the outstanding of this AccountsPayable.  # noqa: E501


        :return: The outstanding of this AccountsPayable.  # noqa: E501
        :rtype: float
        """
        return self._outstanding

    @outstanding.setter
    def outstanding(self, outstanding):
        """Sets the outstanding of this AccountsPayable.


        :param outstanding: The outstanding of this AccountsPayable.  # noqa: E501
        :type: float
        """

        self._outstanding = outstanding

    @property
    def overdue(self):
        """Gets the overdue of this AccountsPayable.  # noqa: E501


        :return: The overdue of this AccountsPayable.  # noqa: E501
        :rtype: float
        """
        return self._overdue

    @overdue.setter
    def overdue(self, overdue):
        """Sets the overdue of this AccountsPayable.


        :param overdue: The overdue of this AccountsPayable.  # noqa: E501
        :type: float
        """

        self._overdue = overdue
