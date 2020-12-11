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


class LeaveTypes(BaseModel):
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
        "leave_types": "list[LeaveType]",
    }

    attribute_map = {
        "pagination": "pagination",
        "problem": "problem",
        "leave_types": "leaveTypes",
    }

    def __init__(self, pagination=None, problem=None, leave_types=None):  # noqa: E501
        """LeaveTypes - a model defined in OpenAPI"""  # noqa: E501

        self._pagination = None
        self._problem = None
        self._leave_types = None
        self.discriminator = None

        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if leave_types is not None:
            self.leave_types = leave_types

    @property
    def pagination(self):
        """Gets the pagination of this LeaveTypes.  # noqa: E501


        :return: The pagination of this LeaveTypes.  # noqa: E501
        :rtype: Pagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this LeaveTypes.


        :param pagination: The pagination of this LeaveTypes.  # noqa: E501
        :type: Pagination
        """

        self._pagination = pagination

    @property
    def problem(self):
        """Gets the problem of this LeaveTypes.  # noqa: E501


        :return: The problem of this LeaveTypes.  # noqa: E501
        :rtype: Problem
        """
        return self._problem

    @problem.setter
    def problem(self, problem):
        """Sets the problem of this LeaveTypes.


        :param problem: The problem of this LeaveTypes.  # noqa: E501
        :type: Problem
        """

        self._problem = problem

    @property
    def leave_types(self):
        """Gets the leave_types of this LeaveTypes.  # noqa: E501


        :return: The leave_types of this LeaveTypes.  # noqa: E501
        :rtype: list[LeaveType]
        """
        return self._leave_types

    @leave_types.setter
    def leave_types(self, leave_types):
        """Sets the leave_types of this LeaveTypes.


        :param leave_types: The leave_types of this LeaveTypes.  # noqa: E501
        :type: list[LeaveType]
        """

        self._leave_types = leave_types
