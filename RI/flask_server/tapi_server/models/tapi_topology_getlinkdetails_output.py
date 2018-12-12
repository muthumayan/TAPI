# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.tapi_topology_link import TapiTopologyLink  # noqa: F401,E501
from tapi_server import util


class TapiTopologyGetlinkdetailsOutput(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, link=None):  # noqa: E501
        """TapiTopologyGetlinkdetailsOutput - a model defined in OpenAPI

        :param link: The link of this TapiTopologyGetlinkdetailsOutput.  # noqa: E501
        :type link: TapiTopologyLink
        """
        self.openapi_types = {
            'link': TapiTopologyLink
        }

        self.attribute_map = {
            'link': 'link'
        }

        self._link = link

    @classmethod
    def from_dict(cls, dikt) -> 'TapiTopologyGetlinkdetailsOutput':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.topology.getlinkdetails.Output of this TapiTopologyGetlinkdetailsOutput.  # noqa: E501
        :rtype: TapiTopologyGetlinkdetailsOutput
        """
        return util.deserialize_model(dikt, cls)

    @property
    def link(self):
        """Gets the link of this TapiTopologyGetlinkdetailsOutput.


        :return: The link of this TapiTopologyGetlinkdetailsOutput.
        :rtype: TapiTopologyLink
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this TapiTopologyGetlinkdetailsOutput.


        :param link: The link of this TapiTopologyGetlinkdetailsOutput.
        :type link: TapiTopologyLink
        """

        self._link = link
