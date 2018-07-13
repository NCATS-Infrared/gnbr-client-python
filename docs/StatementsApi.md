# swagger_client.StatementsApi

All URIs are relative to *https://reference-beacon.ncats.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_evidence**](StatementsApi.md#get_evidence) | **GET** /evidence/{statementId} | 
[**get_statements**](StatementsApi.md#get_statements) | **GET** /statements | 


# **get_evidence**
> list[BeaconAnnotation] get_evidence(statement_id, keywords=keywords, page_number=page_number, page_size=page_size)



Retrieves a (paged) list of annotations cited as evidence for a specified concept-relationship statement 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatementsApi()
statement_id = 'statement_id_example' # str | (url-encoded) CURIE identifier of the concept-relationship statement (\"assertion\", \"claim\") for which associated evidence is sought 
keywords = 'keywords_example' # str | (url-encoded, space delimited) keyword filter to apply against the label field of the annotation  (optional)
page_number = 56 # int | (1-based) number of the page to be returned in a paged set of query results  (optional)
page_size = 56 # int | number of cited references per page to be returned in a paged set of query results  (optional)

try:
    api_response = api_instance.get_evidence(statement_id, keywords=keywords, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatementsApi->get_evidence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **statement_id** | **str**| (url-encoded) CURIE identifier of the concept-relationship statement (\&quot;assertion\&quot;, \&quot;claim\&quot;) for which associated evidence is sought  | 
 **keywords** | **str**| (url-encoded, space delimited) keyword filter to apply against the label field of the annotation  | [optional] 
 **page_number** | **int**| (1-based) number of the page to be returned in a paged set of query results  | [optional] 
 **page_size** | **int**| number of cited references per page to be returned in a paged set of query results  | [optional] 

### Return type

[**list[BeaconAnnotation]**](BeaconAnnotation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_statements**
> list[BeaconStatement] get_statements(s, relations=relations, t=t, keywords=keywords, types=types, page_number=page_number, page_size=page_size)



Given a specified set of [CURIE-encoded](https://www.w3.org/TR/curie/)  'source' ('s') concept identifiers,  retrieves a paged list of relationship statements where either the subject or object concept matches any of the input 'source' concepts provided.  Optionally, a set of 'target' ('t') concept  identifiers may also be given, in which case a member of the 'target' identifier set should match the concept opposing the 'source' in the  statement, that is, if the'source' matches a subject, then the  'target' should match the object of a given statement (or vice versa). 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatementsApi()
s = ['s_example'] # list[str] | a set of [CURIE-encoded](https://www.w3.org/TR/curie/) identifiers of  'source' concepts possibly known to the beacon. Unknown CURIES should simply be ignored (silent match failure). 
relations = 'relations_example' # str | a (url-encoded, space-delimited) string of predicate relation identifiers with which to constrain the statement relations retrieved  for the given query seed concept. The predicate ids sent should  be as published by the beacon-aggregator by the /predicates API endpoint.  (optional)
t = ['t_example'] # list[str] | (optional) an array set of [CURIE-encoded](https://www.w3.org/TR/curie/)  identifiers of 'target' concepts possibly known to the beacon.  Unknown CURIEs should simply be ignored (silent match failure).  (optional)
keywords = 'keywords_example' # str | a (url-encoded, space-delimited) string of keywords or substrings against which to match the subject, predicate or object names of the set of concept-relations matched by any of the input exact matching concepts  (optional)
types = 'types_example' # str | a (url-encoded, space-delimited) string of concept types (specified as codes gene, pathway, etc.) to which to constrain the subject or object concepts associated with the query seed concept (see [Biolink Model](https://biolink.github.io/biolink-model) for the full list of codes)  (optional)
page_number = 56 # int | (1-based) number of the page to be returned in a paged set of query results  (optional)
page_size = 56 # int | number of concepts per page to be returned in a paged set of query results  (optional)

try:
    api_response = api_instance.get_statements(s, relations=relations, t=t, keywords=keywords, types=types, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatementsApi->get_statements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **s** | [**list[str]**](str.md)| a set of [CURIE-encoded](https://www.w3.org/TR/curie/) identifiers of  &#39;source&#39; concepts possibly known to the beacon. Unknown CURIES should simply be ignored (silent match failure).  | 
 **relations** | **str**| a (url-encoded, space-delimited) string of predicate relation identifiers with which to constrain the statement relations retrieved  for the given query seed concept. The predicate ids sent should  be as published by the beacon-aggregator by the /predicates API endpoint.  | [optional] 
 **t** | [**list[str]**](str.md)| (optional) an array set of [CURIE-encoded](https://www.w3.org/TR/curie/)  identifiers of &#39;target&#39; concepts possibly known to the beacon.  Unknown CURIEs should simply be ignored (silent match failure).  | [optional] 
 **keywords** | **str**| a (url-encoded, space-delimited) string of keywords or substrings against which to match the subject, predicate or object names of the set of concept-relations matched by any of the input exact matching concepts  | [optional] 
 **types** | **str**| a (url-encoded, space-delimited) string of concept types (specified as codes gene, pathway, etc.) to which to constrain the subject or object concepts associated with the query seed concept (see [Biolink Model](https://biolink.github.io/biolink-model) for the full list of codes)  | [optional] 
 **page_number** | **int**| (1-based) number of the page to be returned in a paged set of query results  | [optional] 
 **page_size** | **int**| number of concepts per page to be returned in a paged set of query results  | [optional] 

### Return type

[**list[BeaconStatement]**](BeaconStatement.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

