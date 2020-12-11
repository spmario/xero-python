# coding: utf-8

"""
    Xero Payroll AU

    This is the Xero Payroll API for orgs in Australia region.  # noqa: E501

    OpenAPI spec version: 2.7.0
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class DeductionType(BaseModel):
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
        "name": "str",
        "account_code": "str",
        "reduces_tax": "bool",
        "reduces_super": "bool",
        "is_exempt_from_w1": "bool",
        "deduction_type_id": "str",
        "updated_date_utc": "datetime[ms-format]",
        "deduction_category": "str",
        "current_record": "bool",
    }

    attribute_map = {
        "name": "Name",
        "account_code": "AccountCode",
        "reduces_tax": "ReducesTax",
        "reduces_super": "ReducesSuper",
        "is_exempt_from_w1": "IsExemptFromW1",
        "deduction_type_id": "DeductionTypeID",
        "updated_date_utc": "UpdatedDateUTC",
        "deduction_category": "DeductionCategory",
        "current_record": "CurrentRecord",
    }

    def __init__(
        self,
        name=None,
        account_code=None,
        reduces_tax=None,
        reduces_super=None,
        is_exempt_from_w1=None,
        deduction_type_id=None,
        updated_date_utc=None,
        deduction_category=None,
        current_record=None,
    ):  # noqa: E501
        """DeductionType - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._account_code = None
        self._reduces_tax = None
        self._reduces_super = None
        self._is_exempt_from_w1 = None
        self._deduction_type_id = None
        self._updated_date_utc = None
        self._deduction_category = None
        self._current_record = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if account_code is not None:
            self.account_code = account_code
        if reduces_tax is not None:
            self.reduces_tax = reduces_tax
        if reduces_super is not None:
            self.reduces_super = reduces_super
        if is_exempt_from_w1 is not None:
            self.is_exempt_from_w1 = is_exempt_from_w1
        if deduction_type_id is not None:
            self.deduction_type_id = deduction_type_id
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc
        if deduction_category is not None:
            self.deduction_category = deduction_category
        if current_record is not None:
            self.current_record = current_record

    @property
    def name(self):
        """Gets the name of this DeductionType.  # noqa: E501

        Name of the earnings rate (max length = 100)  # noqa: E501

        :return: The name of this DeductionType.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeductionType.

        Name of the earnings rate (max length = 100)  # noqa: E501

        :param name: The name of this DeductionType.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 100:
            raise ValueError(
                "Invalid value for `name`, "
                "length must be less than or equal to `100`"
            )  # noqa: E501

        self._name = name

    @property
    def account_code(self):
        """Gets the account_code of this DeductionType.  # noqa: E501

        See Accounts  # noqa: E501

        :return: The account_code of this DeductionType.  # noqa: E501
        :rtype: str
        """
        return self._account_code

    @account_code.setter
    def account_code(self, account_code):
        """Sets the account_code of this DeductionType.

        See Accounts  # noqa: E501

        :param account_code: The account_code of this DeductionType.  # noqa: E501
        :type: str
        """

        self._account_code = account_code

    @property
    def reduces_tax(self):
        """Gets the reduces_tax of this DeductionType.  # noqa: E501

        Indicates that this is a pre-tax deduction that will reduce the amount of tax you withhold from an employee.  # noqa: E501

        :return: The reduces_tax of this DeductionType.  # noqa: E501
        :rtype: bool
        """
        return self._reduces_tax

    @reduces_tax.setter
    def reduces_tax(self, reduces_tax):
        """Sets the reduces_tax of this DeductionType.

        Indicates that this is a pre-tax deduction that will reduce the amount of tax you withhold from an employee.  # noqa: E501

        :param reduces_tax: The reduces_tax of this DeductionType.  # noqa: E501
        :type: bool
        """

        self._reduces_tax = reduces_tax

    @property
    def reduces_super(self):
        """Gets the reduces_super of this DeductionType.  # noqa: E501

        Most deductions don’t reduce your superannuation guarantee contribution liability, so typically you will not set any value for this.  # noqa: E501

        :return: The reduces_super of this DeductionType.  # noqa: E501
        :rtype: bool
        """
        return self._reduces_super

    @reduces_super.setter
    def reduces_super(self, reduces_super):
        """Sets the reduces_super of this DeductionType.

        Most deductions don’t reduce your superannuation guarantee contribution liability, so typically you will not set any value for this.  # noqa: E501

        :param reduces_super: The reduces_super of this DeductionType.  # noqa: E501
        :type: bool
        """

        self._reduces_super = reduces_super

    @property
    def is_exempt_from_w1(self):
        """Gets the is_exempt_from_w1 of this DeductionType.  # noqa: E501

        Boolean to determine if the deduction type is reportable or exempt from W1  # noqa: E501

        :return: The is_exempt_from_w1 of this DeductionType.  # noqa: E501
        :rtype: bool
        """
        return self._is_exempt_from_w1

    @is_exempt_from_w1.setter
    def is_exempt_from_w1(self, is_exempt_from_w1):
        """Sets the is_exempt_from_w1 of this DeductionType.

        Boolean to determine if the deduction type is reportable or exempt from W1  # noqa: E501

        :param is_exempt_from_w1: The is_exempt_from_w1 of this DeductionType.  # noqa: E501
        :type: bool
        """

        self._is_exempt_from_w1 = is_exempt_from_w1

    @property
    def deduction_type_id(self):
        """Gets the deduction_type_id of this DeductionType.  # noqa: E501

        Xero identifier  # noqa: E501

        :return: The deduction_type_id of this DeductionType.  # noqa: E501
        :rtype: str
        """
        return self._deduction_type_id

    @deduction_type_id.setter
    def deduction_type_id(self, deduction_type_id):
        """Sets the deduction_type_id of this DeductionType.

        Xero identifier  # noqa: E501

        :param deduction_type_id: The deduction_type_id of this DeductionType.  # noqa: E501
        :type: str
        """

        self._deduction_type_id = deduction_type_id

    @property
    def updated_date_utc(self):
        """Gets the updated_date_utc of this DeductionType.  # noqa: E501

        Last modified timestamp  # noqa: E501

        :return: The updated_date_utc of this DeductionType.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        """Sets the updated_date_utc of this DeductionType.

        Last modified timestamp  # noqa: E501

        :param updated_date_utc: The updated_date_utc of this DeductionType.  # noqa: E501
        :type: datetime
        """

        self._updated_date_utc = updated_date_utc

    @property
    def deduction_category(self):
        """Gets the deduction_category of this DeductionType.  # noqa: E501


        :return: The deduction_category of this DeductionType.  # noqa: E501
        :rtype: str
        """
        return self._deduction_category

    @deduction_category.setter
    def deduction_category(self, deduction_category):
        """Sets the deduction_category of this DeductionType.


        :param deduction_category: The deduction_category of this DeductionType.  # noqa: E501
        :type: str
        """
        allowed_values = ["NONE", "UNIONFEES", "WORKPLACEGIVING", "None"]  # noqa: E501
        if deduction_category not in allowed_values:
            raise ValueError(
                "Invalid value for `deduction_category` ({0}), must be one of {1}".format(  # noqa: E501
                    deduction_category, allowed_values
                )
            )

        self._deduction_category = deduction_category

    @property
    def current_record(self):
        """Gets the current_record of this DeductionType.  # noqa: E501

        Is the current record  # noqa: E501

        :return: The current_record of this DeductionType.  # noqa: E501
        :rtype: bool
        """
        return self._current_record

    @current_record.setter
    def current_record(self, current_record):
        """Sets the current_record of this DeductionType.

        Is the current record  # noqa: E501

        :param current_record: The current_record of this DeductionType.  # noqa: E501
        :type: bool
        """

        self._current_record = current_record
