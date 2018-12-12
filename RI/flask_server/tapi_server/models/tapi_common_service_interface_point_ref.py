# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server import util


class TapiCommonServiceInterfacePointRef(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, service_interface_point_uuid=None):  # noqa: E501
        """TapiCommonServiceInterfacePointRef - a model defined in OpenAPI

        :param service_interface_point_uuid: The service_interface_point_uuid of this TapiCommonServiceInterfacePointRef.  # noqa: E501
        :type service_interface_point_uuid: str
        """
        self.openapi_types = {
            'service_interface_point_uuid': str
        }

        self.attribute_map = {
            'service_interface_point_uuid': 'service-interface-point-uuid'
        }

        self._service_interface_point_uuid = service_interface_point_uuid

    @classmethod
    def from_dict(cls, dikt) -> 'TapiCommonServiceInterfacePointRef':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.common.ServiceInterfacePointRef of this TapiCommonServiceInterfacePointRef.  # noqa: E501
        :rtype: TapiCommonServiceInterfacePointRef
        """
        return util.deserialize_model(dikt, cls)

    @property
    def service_interface_point_uuid(self):
        """Gets the service_interface_point_uuid of this TapiCommonServiceInterfacePointRef.

        none  # noqa: E501

        :return: The service_interface_point_uuid of this TapiCommonServiceInterfacePointRef.
        :rtype: str
        """
        return self._service_interface_point_uuid

    @service_interface_point_uuid.setter
    def service_interface_point_uuid(self, service_interface_point_uuid):
        """Sets the service_interface_point_uuid of this TapiCommonServiceInterfacePointRef.

        none  # noqa: E501

        :param service_interface_point_uuid: The service_interface_point_uuid of this TapiCommonServiceInterfacePointRef.
        :type service_interface_point_uuid: str
        """

        self._service_interface_point_uuid = service_interface_point_uuid
