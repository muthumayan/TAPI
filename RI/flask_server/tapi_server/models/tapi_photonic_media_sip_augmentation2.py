# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.tapi_photonic_media_otsi_service_interface_point_spec import TapiPhotonicMediaOtsiServiceInterfacePointSpec  # noqa: F401,E501
from tapi_server import util


class TapiPhotonicMediaSipAugmentation2(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, otsi_service_interface_point_spec=None):  # noqa: E501
        """TapiPhotonicMediaSipAugmentation2 - a model defined in OpenAPI

        :param otsi_service_interface_point_spec: The otsi_service_interface_point_spec of this TapiPhotonicMediaSipAugmentation2.  # noqa: E501
        :type otsi_service_interface_point_spec: TapiPhotonicMediaOtsiServiceInterfacePointSpec
        """
        self.openapi_types = {
            'otsi_service_interface_point_spec': TapiPhotonicMediaOtsiServiceInterfacePointSpec
        }

        self.attribute_map = {
            'otsi_service_interface_point_spec': 'otsi-service-interface-point-spec'
        }

        self._otsi_service_interface_point_spec = otsi_service_interface_point_spec

    @classmethod
    def from_dict(cls, dikt) -> 'TapiPhotonicMediaSipAugmentation2':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.photonic.media.SipAugmentation2 of this TapiPhotonicMediaSipAugmentation2.  # noqa: E501
        :rtype: TapiPhotonicMediaSipAugmentation2
        """
        return util.deserialize_model(dikt, cls)

    @property
    def otsi_service_interface_point_spec(self):
        """Gets the otsi_service_interface_point_spec of this TapiPhotonicMediaSipAugmentation2.


        :return: The otsi_service_interface_point_spec of this TapiPhotonicMediaSipAugmentation2.
        :rtype: TapiPhotonicMediaOtsiServiceInterfacePointSpec
        """
        return self._otsi_service_interface_point_spec

    @otsi_service_interface_point_spec.setter
    def otsi_service_interface_point_spec(self, otsi_service_interface_point_spec):
        """Sets the otsi_service_interface_point_spec of this TapiPhotonicMediaSipAugmentation2.


        :param otsi_service_interface_point_spec: The otsi_service_interface_point_spec of this TapiPhotonicMediaSipAugmentation2.
        :type otsi_service_interface_point_spec: TapiPhotonicMediaOtsiServiceInterfacePointSpec
        """

        self._otsi_service_interface_point_spec = otsi_service_interface_point_spec
