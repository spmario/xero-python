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


class EmployeeStatutoryLeaveBalanceObject(BaseModel):
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
        "leave_balance": "EmployeeStatutoryLeaveBalance",
    }

    attribute_map = {
        "pagination": "pagination",
        "problem": "problem",
        "leave_balance": "leaveBalance",
    }

    def __init__(self, pagination=None, problem=None, leave_balance=None):  # noqa: E501
        """EmployeeStatutoryLeaveBalanceObject - a model defined in OpenAPI"""  # noqa: E501

        self._pagination = None
        self._problem = None
        self._leave_balance = None
        self.discriminator = None

        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if leave_balance is not None:
            self.leave_balance = leave_balance

    @property
    def pagination(self):
        """Gets the pagination of this EmployeeStatutoryLeaveBalanceObject.  # noqa: E501


        :return: The pagination of this EmployeeStatutoryLeaveBalanceObject.  # noqa: E501
        :rtype: Pagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this EmployeeStatutoryLeaveBalanceObject.


        :param pagination: The pagination of this EmployeeStatutoryLeaveBalanceObject.  # noqa: E501
        :type: Pagination
        """

        self._pagination = pagination

    @property
    def problem(self):
        """Gets the problem of this EmployeeStatutoryLeaveBalanceObject.  # noqa: E501


        :return: The problem of this EmployeeStatutoryLeaveBalanceObject.  # noqa: E501
        :rtype: Problem
        """
        return self._problem

    @problem.setter
    def problem(self, problem):
        """Sets the problem of this EmployeeStatutoryLeaveBalanceObject.


        :param problem: The problem of this EmployeeStatutoryLeaveBalanceObject.  # noqa: E501
        :type: Problem
        """

        self._problem = problem

    @property
    def leave_balance(self):
        """Gets the leave_balance of this EmployeeStatutoryLeaveBalanceObject.  # noqa: E501


        :return: The leave_balance of this EmployeeStatutoryLeaveBalanceObject.  # noqa: E501
        :rtype: EmployeeStatutoryLeaveBalance
        """
        return self._leave_balance

    @leave_balance.setter
    def leave_balance(self, leave_balance):
        """Sets the leave_balance of this EmployeeStatutoryLeaveBalanceObject.


        :param leave_balance: The leave_balance of this EmployeeStatutoryLeaveBalanceObject.  # noqa: E501
        :type: EmployeeStatutoryLeaveBalance
        """

        self._leave_balance = leave_balance
