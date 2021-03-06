# coding: utf-8

"""
    GNBR Knowledge Beacon API

    This is the GNBR Knowledge Beacon web service application programming interface (API).   # noqa: E501

    OpenAPI spec version: 1.2.0
    Contact: srensi@stanford.edu
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from gnbr_beacon.api_client import ApiClient


class ConceptsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_concept_details(self, concept_id, **kwargs):  # noqa: E501
        """get_concept_details  # noqa: E501

        Retrieves details for a specified concepts in the system, as specified by a (url-encoded) CURIE identifier of a concept known the given knowledge source.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_concept_details(concept_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str concept_id: (url-encoded) CURIE identifier of concept of interest (required)
        :return: BeaconConceptWithDetails
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_concept_details_with_http_info(concept_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_concept_details_with_http_info(concept_id, **kwargs)  # noqa: E501
            return data

    def get_concept_details_with_http_info(self, concept_id, **kwargs):  # noqa: E501
        """get_concept_details  # noqa: E501

        Retrieves details for a specified concepts in the system, as specified by a (url-encoded) CURIE identifier of a concept known the given knowledge source.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_concept_details_with_http_info(concept_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str concept_id: (url-encoded) CURIE identifier of concept of interest (required)
        :return: BeaconConceptWithDetails
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['concept_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_concept_details" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'concept_id' is set
        if ('concept_id' not in params or
                params['concept_id'] is None):
            raise ValueError("Missing the required parameter `concept_id` when calling `get_concept_details`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'concept_id' in params:
            path_params['concept_id'] = params['concept_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/concepts/{concept_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BeaconConceptWithDetails',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_concepts(self, **kwargs):  # noqa: E501
        """get_concepts  # noqa: E501

        Retrieves a list of whose concept in the  beacon knowledge base with names and/or synonyms  matching a set of keywords or substrings.  The results returned should generally  be returned in order of the quality of the match,  that is, the highest ranked concepts should exactly  match the most keywords, in the same order as the  keywords were given. Lower quality hits with fewer  keyword matches or out-of-order keyword matches,  should be returned lower in the list.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_concepts(async=True)
        >>> result = thread.get()

        :param async bool
        :param list[str] keywords: (Optional) array of keywords or substrings against which to match concept names and synonyms
        :param list[str] categories: (Optional) array set of concept categories - specified as Biolink name labels codes gene, pathway, etc. - to which to constrain concepts matched by the main keyword search (see [Biolink Model](https://biolink.github.io/biolink-model) for the full list of terms) 
        :param int offset: offset (cursor position) to next batch of statements of amount 'size' to return. 
        :param int size: maximum number of concept entries requested by the client; if this  argument is omitted, then the query is expected to returned all the available data for the query 
        :return: list[BeaconConcept]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_concepts_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_concepts_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_concepts_with_http_info(self, **kwargs):  # noqa: E501
        """get_concepts  # noqa: E501

        Retrieves a list of whose concept in the  beacon knowledge base with names and/or synonyms  matching a set of keywords or substrings.  The results returned should generally  be returned in order of the quality of the match,  that is, the highest ranked concepts should exactly  match the most keywords, in the same order as the  keywords were given. Lower quality hits with fewer  keyword matches or out-of-order keyword matches,  should be returned lower in the list.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_concepts_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param list[str] keywords: (Optional) array of keywords or substrings against which to match concept names and synonyms
        :param list[str] categories: (Optional) array set of concept categories - specified as Biolink name labels codes gene, pathway, etc. - to which to constrain concepts matched by the main keyword search (see [Biolink Model](https://biolink.github.io/biolink-model) for the full list of terms) 
        :param int offset: offset (cursor position) to next batch of statements of amount 'size' to return. 
        :param int size: maximum number of concept entries requested by the client; if this  argument is omitted, then the query is expected to returned all the available data for the query 
        :return: list[BeaconConcept]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['keywords', 'categories', 'offset', 'size']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_concepts" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keywords' in params:
            query_params.append(('keywords', params['keywords']))  # noqa: E501
            collection_formats['keywords'] = 'multi'  # noqa: E501
        if 'categories' in params:
            query_params.append(('categories', params['categories']))  # noqa: E501
            collection_formats['categories'] = 'multi'  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'size' in params:
            query_params.append(('size', params['size']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/concepts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[BeaconConcept]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_exact_matches_to_concept_list(self, c, **kwargs):  # noqa: E501
        """get_exact_matches_to_concept_list  # noqa: E501

        Given an input array of [CURIE](https://www.w3.org/TR/curie/) identifiers of known exactly matched concepts [*sensa*-SKOS](http://www.w3.org/2004/02/skos/core#exactMatch), retrieves the list of [CURIE](https://www.w3.org/TR/curie/) identifiers of additional concepts that are deemed by the given knowledge source to be exact matches to one or more of the input concepts **plus** whichever concept identifiers from the input list were specifically matched to  these additional concepts, thus giving the whole known set of equivalent concepts known to this particular knowledge source.  If an empty set is  returned, the it can be assumed that the given knowledge source does  not know of any new equivalent concepts matching the input set. The caller of this endpoint can then decide whether or not to treat  its input identifiers as its own equivalent set.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_exact_matches_to_concept_list(c, async=True)
        >>> result = thread.get()

        :param async bool
        :param list[str] c: an array set of [CURIE-encoded](https://www.w3.org/TR/curie/)  identifiers of concepts thought to be exactly matching concepts, to be used in a search for additional exactly matching concepts [*sensa*-SKOS](http://www.w3.org/2004/02/skos/core#exactMatch).  (required)
        :return: list[ExactMatchResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_exact_matches_to_concept_list_with_http_info(c, **kwargs)  # noqa: E501
        else:
            (data) = self.get_exact_matches_to_concept_list_with_http_info(c, **kwargs)  # noqa: E501
            return data

    def get_exact_matches_to_concept_list_with_http_info(self, c, **kwargs):  # noqa: E501
        """get_exact_matches_to_concept_list  # noqa: E501

        Given an input array of [CURIE](https://www.w3.org/TR/curie/) identifiers of known exactly matched concepts [*sensa*-SKOS](http://www.w3.org/2004/02/skos/core#exactMatch), retrieves the list of [CURIE](https://www.w3.org/TR/curie/) identifiers of additional concepts that are deemed by the given knowledge source to be exact matches to one or more of the input concepts **plus** whichever concept identifiers from the input list were specifically matched to  these additional concepts, thus giving the whole known set of equivalent concepts known to this particular knowledge source.  If an empty set is  returned, the it can be assumed that the given knowledge source does  not know of any new equivalent concepts matching the input set. The caller of this endpoint can then decide whether or not to treat  its input identifiers as its own equivalent set.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_exact_matches_to_concept_list_with_http_info(c, async=True)
        >>> result = thread.get()

        :param async bool
        :param list[str] c: an array set of [CURIE-encoded](https://www.w3.org/TR/curie/)  identifiers of concepts thought to be exactly matching concepts, to be used in a search for additional exactly matching concepts [*sensa*-SKOS](http://www.w3.org/2004/02/skos/core#exactMatch).  (required)
        :return: list[ExactMatchResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['c']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_exact_matches_to_concept_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'c' is set
        if ('c' not in params or
                params['c'] is None):
            raise ValueError("Missing the required parameter `c` when calling `get_exact_matches_to_concept_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'c' in params:
            query_params.append(('c', params['c']))  # noqa: E501
            collection_formats['c'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/exactmatches', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ExactMatchResponse]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
