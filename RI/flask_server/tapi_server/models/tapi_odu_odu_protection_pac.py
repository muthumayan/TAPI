# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server import util


class TapiOduOduProtectionPac(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, aps_enable=True, aps_level=None):  # noqa: E501
        """TapiOduOduProtectionPac - a model defined in OpenAPI

        :param aps_enable: The aps_enable of this TapiOduOduProtectionPac.  # noqa: E501
        :type aps_enable: bool
        :param aps_level: The aps_level of this TapiOduOduProtectionPac.  # noqa: E501
        :type aps_level: int
        """
        self.openapi_types = {
            'aps_enable': bool,
            'aps_level': int
        }

        self.attribute_map = {
            'aps_enable': 'aps-enable',
            'aps_level': 'aps-level'
        }

        self._aps_enable = aps_enable
        self._aps_level = aps_level

    @classmethod
    def from_dict(cls, dikt) -> 'TapiOduOduProtectionPac':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.odu.OduProtectionPac of this TapiOduOduProtectionPac.  # noqa: E501
        :rtype: TapiOduOduProtectionPac
        """
        return util.deserialize_model(dikt, cls)

    @property
    def aps_enable(self):
        """Gets the aps_enable of this TapiOduOduProtectionPac.

        This attribute is for enabling/disabling the automatic protection switching (APS) capability at the transport adaptation function that is represented by the ODU_ConnectionTerminationPoint object class. It triggers the MI_APS_EN signal to the transport adaptation function.  # noqa: E501

        :return: The aps_enable of this TapiOduOduProtectionPac.
        :rtype: bool
        """
        return self._aps_enable

    @aps_enable.setter
    def aps_enable(self, aps_enable):
        """Sets the aps_enable of this TapiOduOduProtectionPac.

        This attribute is for enabling/disabling the automatic protection switching (APS) capability at the transport adaptation function that is represented by the ODU_ConnectionTerminationPoint object class. It triggers the MI_APS_EN signal to the transport adaptation function.  # noqa: E501

        :param aps_enable: The aps_enable of this TapiOduOduProtectionPac.
        :type aps_enable: bool
        """

        self._aps_enable = aps_enable

    @property
    def aps_level(self):
        """Gets the aps_level of this TapiOduOduProtectionPac.

        This attribute is for configuring the automatic protection switching (APS) level that should operate at the transport adaptation function that is represented by the ODU_ConnectionTerminationPoint object class. It triggers the MI_APS_LVL signal to the transport adaptation function. The value 0 means path and the values 1 through 6 mean TCM level 1 through 6 respectively.  # noqa: E501

        :return: The aps_level of this TapiOduOduProtectionPac.
        :rtype: int
        """
        return self._aps_level

    @aps_level.setter
    def aps_level(self, aps_level):
        """Sets the aps_level of this TapiOduOduProtectionPac.

        This attribute is for configuring the automatic protection switching (APS) level that should operate at the transport adaptation function that is represented by the ODU_ConnectionTerminationPoint object class. It triggers the MI_APS_LVL signal to the transport adaptation function. The value 0 means path and the values 1 through 6 mean TCM level 1 through 6 respectively.  # noqa: E501

        :param aps_level: The aps_level of this TapiOduOduProtectionPac.
        :type aps_level: int
        """

        self._aps_level = aps_level
