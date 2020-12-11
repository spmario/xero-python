# coding: utf-8

"""
    Xero Payroll NZ

    This is the Xero Payroll API for orgs in the NZ region.  # noqa: E501

    OpenAPI spec version: 2.7.0
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class EmployeeObject(BaseModel):
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
        "employee": "Employee",
        "problem": "Problem",
    }

    attribute_map = {
        "pagination": "pagination",
        "employee": "employee",
        "problem": "problem",
    }

    def __init__(self, pagination=None, employee=None, problem=None):  # noqa: E501
        """EmployeeObject - a model defined in OpenAPI"""  # noqa: E501

        self._pagination = None
        self._employee = None
        self._problem = None
        self.discriminator = None

        if pagination is not None:
            self.pagination = pagination
        if employee is not None:
            self.employee = employee
        if problem is not None:
            self.problem = problem

    @property
    def pagination(self):
        """Gets the pagination of this EmployeeObject.  # noqa: E501


        :return: The pagination of this EmployeeObject.  # noqa: E501
        :rtype: Pagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this EmployeeObject.


        :param pagination: The pagination of this EmployeeObject.  # noqa: E501
        :type: Pagination
        """

        self._pagination = pagination

    @property
    def employee(self):
        """Gets the employee of this EmployeeObject.  # noqa: E501


        :return: The employee of this EmployeeObject.  # noqa: E501
        :rtype: Employee
        """
        return self._employee

    @employee.setter
    def employee(self, employee):
        """Sets the employee of this EmployeeObject.


        :param employee: The employee of this EmployeeObject.  # noqa: E501
        :type: Employee
        """

        self._employee = employee

    @property
    def problem(self):
        """Gets the problem of this EmployeeObject.  # noqa: E501


        :return: The problem of this EmployeeObject.  # noqa: E501
        :rtype: Problem
        """
        return self._problem

    @problem.setter
    def problem(self, problem):
        """Sets the problem of this EmployeeObject.


        :param problem: The problem of this EmployeeObject.  # noqa: E501
        :type: Problem
        """

        self._problem = problem
