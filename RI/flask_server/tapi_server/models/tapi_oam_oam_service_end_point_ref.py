# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.tapi_oam_oam_service_ref import TapiOamOamServiceRef  # noqa: F401,E501
from tapi_server import util


class TapiOamOamServiceEndPointRef(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, oam_service_uuid=None, oam_service_end_point_local_id=None):  # noqa: E501
        """TapiOamOamServiceEndPointRef - a model defined in OpenAPI

        :param oam_service_uuid: The oam_service_uuid of this TapiOamOamServiceEndPointRef.  # noqa: E501
        :type oam_service_uuid: str
        :param oam_service_end_point_local_id: The oam_service_end_point_local_id of this TapiOamOamServiceEndPointRef.  # noqa: E501
        :type oam_service_end_point_local_id: str
        """
        self.openapi_types = {
            'oam_service_uuid': str,
            'oam_service_end_point_local_id': str
        }

        self.attribute_map = {
            'oam_service_uuid': 'oam-service-uuid',
            'oam_service_end_point_local_id': 'oam-service-end-point-local-id'
        }

        self._oam_service_uuid = oam_service_uuid
        self._oam_service_end_point_local_id = oam_service_end_point_local_id

    @classmethod
    def from_dict(cls, dikt) -> 'TapiOamOamServiceEndPointRef':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.oam.OamServiceEndPointRef of this TapiOamOamServiceEndPointRef.  # noqa: E501
        :rtype: TapiOamOamServiceEndPointRef
        """
        return util.deserialize_model(dikt, cls)

    @property
    def oam_service_uuid(self):
        """Gets the oam_service_uuid of this TapiOamOamServiceEndPointRef.

        none  # noqa: E501

        :return: The oam_service_uuid of this TapiOamOamServiceEndPointRef.
        :rtype: str
        """
        return self._oam_service_uuid

    @oam_service_uuid.setter
    def oam_service_uuid(self, oam_service_uuid):
        """Sets the oam_service_uuid of this TapiOamOamServiceEndPointRef.

        none  # noqa: E501

        :param oam_service_uuid: The oam_service_uuid of this TapiOamOamServiceEndPointRef.
        :type oam_service_uuid: str
        """

        self._oam_service_uuid = oam_service_uuid

    @property
    def oam_service_end_point_local_id(self):
        """Gets the oam_service_end_point_local_id of this TapiOamOamServiceEndPointRef.

        none  # noqa: E501

        :return: The oam_service_end_point_local_id of this TapiOamOamServiceEndPointRef.
        :rtype: str
        """
        return self._oam_service_end_point_local_id

    @oam_service_end_point_local_id.setter
    def oam_service_end_point_local_id(self, oam_service_end_point_local_id):
        """Sets the oam_service_end_point_local_id of this TapiOamOamServiceEndPointRef.

        none  # noqa: E501

        :param oam_service_end_point_local_id: The oam_service_end_point_local_id of this TapiOamOamServiceEndPointRef.
        :type oam_service_end_point_local_id: str
        """

        self._oam_service_end_point_local_id = oam_service_end_point_local_id
