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


class EmployeePayTemplateObject(BaseModel):
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
        "pay_template": "EmployeePayTemplate",
    }

    attribute_map = {
        "pagination": "pagination",
        "problem": "problem",
        "pay_template": "payTemplate",
    }

    def __init__(self, pagination=None, problem=None, pay_template=None):  # noqa: E501
        """EmployeePayTemplateObject - a model defined in OpenAPI"""  # noqa: E501

        self._pagination = None
        self._problem = None
        self._pay_template = None
        self.discriminator = None

        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if pay_template is not None:
            self.pay_template = pay_template

    @property
    def pagination(self):
        """Gets the pagination of this EmployeePayTemplateObject.  # noqa: E501


        :return: The pagination of this EmployeePayTemplateObject.  # noqa: E501
        :rtype: Pagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this EmployeePayTemplateObject.


        :param pagination: The pagination of this EmployeePayTemplateObject.  # noqa: E501
        :type: Pagination
        """

        self._pagination = pagination

    @property
    def problem(self):
        """Gets the problem of this EmployeePayTemplateObject.  # noqa: E501


        :return: The problem of this EmployeePayTemplateObject.  # noqa: E501
        :rtype: Problem
        """
        return self._problem

    @problem.setter
    def problem(self, problem):
        """Sets the problem of this EmployeePayTemplateObject.


        :param problem: The problem of this EmployeePayTemplateObject.  # noqa: E501
        :type: Problem
        """

        self._problem = problem

    @property
    def pay_template(self):
        """Gets the pay_template of this EmployeePayTemplateObject.  # noqa: E501


        :return: The pay_template of this EmployeePayTemplateObject.  # noqa: E501
        :rtype: EmployeePayTemplate
        """
        return self._pay_template

    @pay_template.setter
    def pay_template(self, pay_template):
        """Sets the pay_template of this EmployeePayTemplateObject.


        :param pay_template: The pay_template of this EmployeePayTemplateObject.  # noqa: E501
        :type: EmployeePayTemplate
        """

        self._pay_template = pay_template
