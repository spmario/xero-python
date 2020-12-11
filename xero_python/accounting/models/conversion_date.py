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


class ConversionDate(BaseModel):
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
    openapi_types = {"month": "int", "year": "int"}

    attribute_map = {"month": "Month", "year": "Year"}

    def __init__(self, month=None, year=None):  # noqa: E501
        """ConversionDate - a model defined in OpenAPI"""  # noqa: E501

        self._month = None
        self._year = None
        self.discriminator = None

        if month is not None:
            self.month = month
        if year is not None:
            self.year = year

    @property
    def month(self):
        """Gets the month of this ConversionDate.  # noqa: E501

        The month the organisation starts using Xero. Value is an integer between 1 and 12  # noqa: E501

        :return: The month of this ConversionDate.  # noqa: E501
        :rtype: int
        """
        return self._month

    @month.setter
    def month(self, month):
        """Sets the month of this ConversionDate.

        The month the organisation starts using Xero. Value is an integer between 1 and 12  # noqa: E501

        :param month: The month of this ConversionDate.  # noqa: E501
        :type: int
        """

        self._month = month

    @property
    def year(self):
        """Gets the year of this ConversionDate.  # noqa: E501

        The year the organisation starts using Xero. Value is an integer greater than 2006  # noqa: E501

        :return: The year of this ConversionDate.  # noqa: E501
        :rtype: int
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this ConversionDate.

        The year the organisation starts using Xero. Value is an integer greater than 2006  # noqa: E501

        :param year: The year of this ConversionDate.  # noqa: E501
        :type: int
        """

        self._year = year
