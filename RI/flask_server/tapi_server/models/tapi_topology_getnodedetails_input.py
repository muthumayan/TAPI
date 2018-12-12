# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server import util


class TapiTopologyGetnodedetailsInput(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, node_id_or_name=None, topology_id_or_name=None):  # noqa: E501
        """TapiTopologyGetnodedetailsInput - a model defined in OpenAPI

        :param node_id_or_name: The node_id_or_name of this TapiTopologyGetnodedetailsInput.  # noqa: E501
        :type node_id_or_name: str
        :param topology_id_or_name: The topology_id_or_name of this TapiTopologyGetnodedetailsInput.  # noqa: E501
        :type topology_id_or_name: str
        """
        self.openapi_types = {
            'node_id_or_name': str,
            'topology_id_or_name': str
        }

        self.attribute_map = {
            'node_id_or_name': 'node-id-or-name',
            'topology_id_or_name': 'topology-id-or-name'
        }

        self._node_id_or_name = node_id_or_name
        self._topology_id_or_name = topology_id_or_name

    @classmethod
    def from_dict(cls, dikt) -> 'TapiTopologyGetnodedetailsInput':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.topology.getnodedetails.Input of this TapiTopologyGetnodedetailsInput.  # noqa: E501
        :rtype: TapiTopologyGetnodedetailsInput
        """
        return util.deserialize_model(dikt, cls)

    @property
    def node_id_or_name(self):
        """Gets the node_id_or_name of this TapiTopologyGetnodedetailsInput.

        none  # noqa: E501

        :return: The node_id_or_name of this TapiTopologyGetnodedetailsInput.
        :rtype: str
        """
        return self._node_id_or_name

    @node_id_or_name.setter
    def node_id_or_name(self, node_id_or_name):
        """Sets the node_id_or_name of this TapiTopologyGetnodedetailsInput.

        none  # noqa: E501

        :param node_id_or_name: The node_id_or_name of this TapiTopologyGetnodedetailsInput.
        :type node_id_or_name: str
        """

        self._node_id_or_name = node_id_or_name

    @property
    def topology_id_or_name(self):
        """Gets the topology_id_or_name of this TapiTopologyGetnodedetailsInput.

        none  # noqa: E501

        :return: The topology_id_or_name of this TapiTopologyGetnodedetailsInput.
        :rtype: str
        """
        return self._topology_id_or_name

    @topology_id_or_name.setter
    def topology_id_or_name(self, topology_id_or_name):
        """Sets the topology_id_or_name of this TapiTopologyGetnodedetailsInput.

        none  # noqa: E501

        :param topology_id_or_name: The topology_id_or_name of this TapiTopologyGetnodedetailsInput.
        :type topology_id_or_name: str
        """

        self._topology_id_or_name = topology_id_or_name
