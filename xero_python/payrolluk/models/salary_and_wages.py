# coding: utf-8

"""
    Xero Payroll UK

    This is the Xero Payroll API for orgs in the UK region.  # noqa: E501

    OpenAPI spec version: 2.7.0
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class SalaryAndWages(BaseModel):
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
    openapi_types = {
        "pagination": "Pagination",
        "problem": "Problem",
        "salary_and_wages": "list[SalaryAndWage]",
    }

    attribute_map = {
        "pagination": "pagination",
        "problem": "problem",
        "salary_and_wages": "salaryAndWages",
    }

    def __init__(
        self, pagination=None, problem=None, salary_and_wages=None
    ):  # noqa: E501
        """SalaryAndWages - a model defined in OpenAPI"""  # noqa: E501

        self._pagination = None
        self._problem = None
        self._salary_and_wages = None
        self.discriminator = None

        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if salary_and_wages is not None:
            self.salary_and_wages = salary_and_wages

    @property
    def pagination(self):
        """Gets the pagination of this SalaryAndWages.  # noqa: E501


        :return: The pagination of this SalaryAndWages.  # noqa: E501
        :rtype: Pagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this SalaryAndWages.


        :param pagination: The pagination of this SalaryAndWages.  # noqa: E501
        :type: Pagination
        """

        self._pagination = pagination

    @property
    def problem(self):
        """Gets the problem of this SalaryAndWages.  # noqa: E501


        :return: The problem of this SalaryAndWages.  # noqa: E501
        :rtype: Problem
        """
        return self._problem

    @problem.setter
    def problem(self, problem):
        """Sets the problem of this SalaryAndWages.


        :param problem: The problem of this SalaryAndWages.  # noqa: E501
        :type: Problem
        """

        self._problem = problem

    @property
    def salary_and_wages(self):
        """Gets the salary_and_wages of this SalaryAndWages.  # noqa: E501


        :return: The salary_and_wages of this SalaryAndWages.  # noqa: E501
        :rtype: list[SalaryAndWage]
        """
        return self._salary_and_wages

    @salary_and_wages.setter
    def salary_and_wages(self, salary_and_wages):
        """Sets the salary_and_wages of this SalaryAndWages.


        :param salary_and_wages: The salary_and_wages of this SalaryAndWages.  # noqa: E501
        :type: list[SalaryAndWage]
        """

        self._salary_and_wages = salary_and_wages
