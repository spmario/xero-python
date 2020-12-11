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


class SettingsTrackingCategoriesEmployeeGroups(BaseModel):
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
    openapi_types = {"tracking_category_id": "str", "tracking_category_name": "str"}

    attribute_map = {
        "tracking_category_id": "TrackingCategoryID",
        "tracking_category_name": "TrackingCategoryName",
    }

    def __init__(
        self, tracking_category_id=None, tracking_category_name=None
    ):  # noqa: E501
        """SettingsTrackingCategoriesEmployeeGroups - a model defined in OpenAPI"""  # noqa: E501

        self._tracking_category_id = None
        self._tracking_category_name = None
        self.discriminator = None

        if tracking_category_id is not None:
            self.tracking_category_id = tracking_category_id
        if tracking_category_name is not None:
            self.tracking_category_name = tracking_category_name

    @property
    def tracking_category_id(self):
        """Gets the tracking_category_id of this SettingsTrackingCategoriesEmployeeGroups.  # noqa: E501

        The identifier for the tracking category  # noqa: E501

        :return: The tracking_category_id of this SettingsTrackingCategoriesEmployeeGroups.  # noqa: E501
        :rtype: str
        """
        return self._tracking_category_id

    @tracking_category_id.setter
    def tracking_category_id(self, tracking_category_id):
        """Sets the tracking_category_id of this SettingsTrackingCategoriesEmployeeGroups.

        The identifier for the tracking category  # noqa: E501

        :param tracking_category_id: The tracking_category_id of this SettingsTrackingCategoriesEmployeeGroups.  # noqa: E501
        :type: str
        """

        self._tracking_category_id = tracking_category_id

    @property
    def tracking_category_name(self):
        """Gets the tracking_category_name of this SettingsTrackingCategoriesEmployeeGroups.  # noqa: E501

        Name of the tracking category  # noqa: E501

        :return: The tracking_category_name of this SettingsTrackingCategoriesEmployeeGroups.  # noqa: E501
        :rtype: str
        """
        return self._tracking_category_name

    @tracking_category_name.setter
    def tracking_category_name(self, tracking_category_name):
        """Sets the tracking_category_name of this SettingsTrackingCategoriesEmployeeGroups.

        Name of the tracking category  # noqa: E501

        :param tracking_category_name: The tracking_category_name of this SettingsTrackingCategoriesEmployeeGroups.  # noqa: E501
        :type: str
        """

        self._tracking_category_name = tracking_category_name
