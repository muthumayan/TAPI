# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.tapi_common_getserviceinterfacepointdetails_input import TapiCommonGetserviceinterfacepointdetailsInput  # noqa: F401,E501
from tapi_server import util


class InlineObject24(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, input=None):  # noqa: E501
        """InlineObject24 - a model defined in OpenAPI

        :param input: The input of this InlineObject24.  # noqa: E501
        :type input: TapiCommonGetserviceinterfacepointdetailsInput
        """
        self.openapi_types = {
            'input': TapiCommonGetserviceinterfacepointdetailsInput
        }

        self.attribute_map = {
            'input': 'input'
        }

        self._input = input

    @classmethod
    def from_dict(cls, dikt) -> 'InlineObject24':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_object_24 of this InlineObject24.  # noqa: E501
        :rtype: InlineObject24
        """
        return util.deserialize_model(dikt, cls)

    @property
    def input(self):
        """Gets the input of this InlineObject24.


        :return: The input of this InlineObject24.
        :rtype: TapiCommonGetserviceinterfacepointdetailsInput
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this InlineObject24.


        :param input: The input of this InlineObject24.
        :type input: TapiCommonGetserviceinterfacepointdetailsInput
        """

        self._input = input
