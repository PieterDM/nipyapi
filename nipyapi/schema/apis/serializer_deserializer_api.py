# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0.0

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class SerializerDeserializerApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def add_ser_des(self, body, **kwargs):
        """
        Add a Serializer/Deserializer into the Schema Registry

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.add_ser_des(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param SerDesPair body: Serializer/Deserializer information to be registered (required)
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.add_ser_des_with_http_info(body, **kwargs)
        else:
            (data) = self.add_ser_des_with_http_info(body, **kwargs)
            return data

    def add_ser_des_with_http_info(self, body, **kwargs):
        """
        Add a Serializer/Deserializer into the Schema Registry

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.add_ser_des_with_http_info(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param SerDesPair body: Serializer/Deserializer information to be registered (required)
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_ser_des" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `add_ser_des`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['tokenAuth']

        return self.api_client.call_api('/api/v1/schemaregistry/serdes', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='int',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_ser_des(self, id, **kwargs):
        """
        Get a Serializer for the given serializer id

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_ser_des(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: Serializer identifier (required)
        :return: SerDesInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_ser_des_with_http_info(id, **kwargs)
        else:
            (data) = self.get_ser_des_with_http_info(id, **kwargs)
            return data

    def get_ser_des_with_http_info(self, id, **kwargs):
        """
        Get a Serializer for the given serializer id

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_ser_des_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: Serializer identifier (required)
        :return: SerDesInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_ser_des" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_ser_des`")


        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['tokenAuth']

        return self.api_client.call_api('/api/v1/schemaregistry/serdes/{id}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='SerDesInfo',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_serializers(self, name, **kwargs):
        """
        Get list of Serializers registered for the given schema name

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_serializers(name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str name: Schema name (required)
        :return: list[SerDesInfo]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_serializers_with_http_info(name, **kwargs)
        else:
            (data) = self.get_serializers_with_http_info(name, **kwargs)
            return data

    def get_serializers_with_http_info(self, name, **kwargs):
        """
        Get list of Serializers registered for the given schema name

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_serializers_with_http_info(name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str name: Schema name (required)
        :return: list[SerDesInfo]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_serializers" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params) or (params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `get_serializers`")


        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['tokenAuth']

        return self.api_client.call_api('/api/v1/schemaregistry/schemas/{name}/serdes', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[SerDesInfo]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def map_schema_with_ser_des(self, name, ser_des_id, **kwargs):
        """
        Bind the given Serializer/Deserializer to the schema identified by the schema name

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.map_schema_with_ser_des(name, ser_des_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str name: Schema name (required)
        :param int ser_des_id: Serializer/deserializer identifier (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.map_schema_with_ser_des_with_http_info(name, ser_des_id, **kwargs)
        else:
            (data) = self.map_schema_with_ser_des_with_http_info(name, ser_des_id, **kwargs)
            return data

    def map_schema_with_ser_des_with_http_info(self, name, ser_des_id, **kwargs):
        """
        Bind the given Serializer/Deserializer to the schema identified by the schema name

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.map_schema_with_ser_des_with_http_info(name, ser_des_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str name: Schema name (required)
        :param int ser_des_id: Serializer/deserializer identifier (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'ser_des_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method map_schema_with_ser_des" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params) or (params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `map_schema_with_ser_des`")
        # verify the required parameter 'ser_des_id' is set
        if ('ser_des_id' not in params) or (params['ser_des_id'] is None):
            raise ValueError("Missing the required parameter `ser_des_id` when calling `map_schema_with_ser_des`")


        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']
        if 'ser_des_id' in params:
            path_params['serDesId'] = params['ser_des_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['tokenAuth']

        return self.api_client.call_api('/api/v1/schemaregistry/schemas/{name}/mapping/{serDesId}', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
