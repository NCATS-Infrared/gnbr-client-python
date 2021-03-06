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


class StatementsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_statement_details(self, statement_id, **kwargs):  # noqa: E501
        """get_statement_details  # noqa: E501

        Retrieves a details relating to a specified concept-relationship statement include 'is_defined_by and 'provided_by' provenance; extended edge properties exported as tag = value; and any associated annotations (publications, etc.)  cited as evidence for the given statement.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_statement_details(statement_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str statement_id: (url-encoded) CURIE identifier of the concept-relationship statement (\"assertion\", \"claim\") for which associated evidence is sought  (required)
        :param list[str] keywords: an array of keywords or substrings against which to  filter annotation names (e.g. publication titles).
        :param int offset: offset (cursor position) to next batch of annotation entries of amount 'size' to return. 
        :param int size: maximum number of evidence citation entries requested by the client; if this  argument is omitted, then the query is expected to returned all of the available annotation for this statement 
        :return: BeaconStatementWithDetails
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_statement_details_with_http_info(statement_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_statement_details_with_http_info(statement_id, **kwargs)  # noqa: E501
            return data

    def get_statement_details_with_http_info(self, statement_id, **kwargs):  # noqa: E501
        """get_statement_details  # noqa: E501

        Retrieves a details relating to a specified concept-relationship statement include 'is_defined_by and 'provided_by' provenance; extended edge properties exported as tag = value; and any associated annotations (publications, etc.)  cited as evidence for the given statement.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_statement_details_with_http_info(statement_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str statement_id: (url-encoded) CURIE identifier of the concept-relationship statement (\"assertion\", \"claim\") for which associated evidence is sought  (required)
        :param list[str] keywords: an array of keywords or substrings against which to  filter annotation names (e.g. publication titles).
        :param int offset: offset (cursor position) to next batch of annotation entries of amount 'size' to return. 
        :param int size: maximum number of evidence citation entries requested by the client; if this  argument is omitted, then the query is expected to returned all of the available annotation for this statement 
        :return: BeaconStatementWithDetails
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['statement_id', 'keywords', 'offset', 'size']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_statement_details" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'statement_id' is set
        if ('statement_id' not in params or
                params['statement_id'] is None):
            raise ValueError("Missing the required parameter `statement_id` when calling `get_statement_details`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'statement_id' in params:
            path_params['statement_id'] = params['statement_id']  # noqa: E501

        query_params = []
        if 'keywords' in params:
            query_params.append(('keywords', params['keywords']))  # noqa: E501
            collection_formats['keywords'] = 'multi'  # noqa: E501
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
            '/statements/{statement_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BeaconStatementWithDetails',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_statements(self, **kwargs):  # noqa: E501
        """get_statements  # noqa: E501

        Given a constrained set of some [CURIE-encoded](https://www.w3.org/TR/curie/)  's' ('source') concept identifiers, categories and/or keywords  (to match in the concept name or description), retrieves a list of relationship statements where either the subject or the object concept matches any of the input source concepts provided.  Optionally, a set of some 't' ('target') concept identifiers, categories and/or keywords (to match in the concept name  or description) may also be given, in which case a member of the 't' concept  set should matchthe concept opposite an 's' concept in the statement.   That is, if the 's' concept matches a subject, then the 't' concept  should match the object of a given statement (or vice versa).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_statements(async=True)
        >>> result = thread.get()

        :param async bool
        :param list[str] s: An (optional) array set of [CURIE-encoded](https://www.w3.org/TR/curie/) identifiers of  'source' ('start') concepts possibly known to the beacon. Unknown CURIES should simply be ignored (silent match failure). 
        :param list[str] s_keywords: An (optional) array of keywords or substrings against which to filter  'source' concept names and synonyms
        :param list[str] s_categories: An (optional) array set of 'source' concept categories (specified as  Biolink name labels codes gene, pathway, etc.) to which to constrain concepts matched by the main keyword search (see [Biolink Model](https://biolink.github.io/biolink-model) for the full list of codes) 
        :param str edge_label: (Optional) predicate edge label against which to constrain the search for statements ('edges') associated with the given query seed concept. The predicate edge_names for this parameter should be as published by the /predicates API endpoint and must be taken from the minimal predicate ('slot') list of the [Biolink Model](https://biolink.github.io/biolink-model). 
        :param str relation: (Optional) predicate relation against which to constrain the search for statements ('edges') associated with the given query seed concept. The predicate relations for this parameter should be as published by the /predicates API endpoint and the preferred format is a CURIE  where one exists, but strings/labels acceptable. This relation may be equivalent to the edge_label (e.g. edge_label: has_phenotype, relation: RO:0002200), or a more specific relation  in cases where the source provides more granularity (e.g. edge_label: molecularly_interacts_with, relation: RO:0002447) 
        :param list[str] t: An (optional) array set of [CURIE-encoded](https://www.w3.org/TR/curie/) identifiers of 'target' ('opposite' or 'end') concepts possibly known to the beacon. Unknown CURIEs should simply be ignored (silent match failure). 
        :param list[str] t_keywords: An (optional) array of keywords or substrings against which to filter 'target' concept names and synonyms
        :param list[str] t_categories: An (optional) array set of 'target' concept categories (specified as  Biolink name labels codes gene, pathway, etc.) to which to constrain concepts matched by the main keyword search (see [Biolink Model](https://biolink.github.io/biolink-model) for the full list of codes) 
        :param int offset: offset (cursor position) to next batch of statements of amount 'size' to return. 
        :param int size: maximum number of concept entries requested by the client; if this  argument is omitted, then the query is expected to returned all  the available data for the query 
        :return: list[BeaconStatement]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_statements_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_statements_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_statements_with_http_info(self, **kwargs):  # noqa: E501
        """get_statements  # noqa: E501

        Given a constrained set of some [CURIE-encoded](https://www.w3.org/TR/curie/)  's' ('source') concept identifiers, categories and/or keywords  (to match in the concept name or description), retrieves a list of relationship statements where either the subject or the object concept matches any of the input source concepts provided.  Optionally, a set of some 't' ('target') concept identifiers, categories and/or keywords (to match in the concept name  or description) may also be given, in which case a member of the 't' concept  set should matchthe concept opposite an 's' concept in the statement.   That is, if the 's' concept matches a subject, then the 't' concept  should match the object of a given statement (or vice versa).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_statements_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param list[str] s: An (optional) array set of [CURIE-encoded](https://www.w3.org/TR/curie/) identifiers of  'source' ('start') concepts possibly known to the beacon. Unknown CURIES should simply be ignored (silent match failure). 
        :param list[str] s_keywords: An (optional) array of keywords or substrings against which to filter  'source' concept names and synonyms
        :param list[str] s_categories: An (optional) array set of 'source' concept categories (specified as  Biolink name labels codes gene, pathway, etc.) to which to constrain concepts matched by the main keyword search (see [Biolink Model](https://biolink.github.io/biolink-model) for the full list of codes) 
        :param str edge_label: (Optional) predicate edge label against which to constrain the search for statements ('edges') associated with the given query seed concept. The predicate edge_names for this parameter should be as published by the /predicates API endpoint and must be taken from the minimal predicate ('slot') list of the [Biolink Model](https://biolink.github.io/biolink-model). 
        :param str relation: (Optional) predicate relation against which to constrain the search for statements ('edges') associated with the given query seed concept. The predicate relations for this parameter should be as published by the /predicates API endpoint and the preferred format is a CURIE  where one exists, but strings/labels acceptable. This relation may be equivalent to the edge_label (e.g. edge_label: has_phenotype, relation: RO:0002200), or a more specific relation  in cases where the source provides more granularity (e.g. edge_label: molecularly_interacts_with, relation: RO:0002447) 
        :param list[str] t: An (optional) array set of [CURIE-encoded](https://www.w3.org/TR/curie/) identifiers of 'target' ('opposite' or 'end') concepts possibly known to the beacon. Unknown CURIEs should simply be ignored (silent match failure). 
        :param list[str] t_keywords: An (optional) array of keywords or substrings against which to filter 'target' concept names and synonyms
        :param list[str] t_categories: An (optional) array set of 'target' concept categories (specified as  Biolink name labels codes gene, pathway, etc.) to which to constrain concepts matched by the main keyword search (see [Biolink Model](https://biolink.github.io/biolink-model) for the full list of codes) 
        :param int offset: offset (cursor position) to next batch of statements of amount 'size' to return. 
        :param int size: maximum number of concept entries requested by the client; if this  argument is omitted, then the query is expected to returned all  the available data for the query 
        :return: list[BeaconStatement]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['s', 's_keywords', 's_categories', 'edge_label', 'relation', 't', 't_keywords', 't_categories', 'offset', 'size']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_statements" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 's' in params:
            query_params.append(('s', params['s']))  # noqa: E501
            collection_formats['s'] = 'multi'  # noqa: E501
        if 's_keywords' in params:
            query_params.append(('s_keywords', params['s_keywords']))  # noqa: E501
            collection_formats['s_keywords'] = 'multi'  # noqa: E501
        if 's_categories' in params:
            query_params.append(('s_categories', params['s_categories']))  # noqa: E501
            collection_formats['s_categories'] = 'multi'  # noqa: E501
        if 'edge_label' in params:
            query_params.append(('edge_label', params['edge_label']))  # noqa: E501
        if 'relation' in params:
            query_params.append(('relation', params['relation']))  # noqa: E501
        if 't' in params:
            query_params.append(('t', params['t']))  # noqa: E501
            collection_formats['t'] = 'multi'  # noqa: E501
        if 't_keywords' in params:
            query_params.append(('t_keywords', params['t_keywords']))  # noqa: E501
            collection_formats['t_keywords'] = 'multi'  # noqa: E501
        if 't_categories' in params:
            query_params.append(('t_categories', params['t_categories']))  # noqa: E501
            collection_formats['t_categories'] = 'multi'  # noqa: E501
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
            '/statements', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[BeaconStatement]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
