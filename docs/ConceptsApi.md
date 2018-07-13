# swagger_client.ConceptsApi

All URIs are relative to *https://reference-beacon.ncats.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_concept_details**](ConceptsApi.md#get_concept_details) | **GET** /concepts/{conceptId} | 
[**get_concepts**](ConceptsApi.md#get_concepts) | **GET** /concepts | 
[**get_exact_matches_to_concept**](ConceptsApi.md#get_exact_matches_to_concept) | **GET** /exactmatches/{conceptId} | 
[**get_exact_matches_to_concept_list**](ConceptsApi.md#get_exact_matches_to_concept_list) | **GET** /exactmatches | 


# **get_concept_details**
> list[BeaconConceptWithDetails] get_concept_details(concept_id)



Retrieves details for a specified concepts in the system, as specified by a (url-encoded) CURIE identifier of a concept known the given knowledge source. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConceptsApi()
concept_id = 'concept_id_example' # str | (url-encoded) CURIE identifier of concept of interest

try:
    api_response = api_instance.get_concept_details(concept_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConceptsApi->get_concept_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **concept_id** | **str**| (url-encoded) CURIE identifier of concept of interest | 

### Return type

[**list[BeaconConceptWithDetails]**](BeaconConceptWithDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_concepts**
> list[BeaconConcept] get_concepts(keywords, types=types, page_number=page_number, page_size=page_size)



Retrieves a (paged) list of whose concept in the  beacon knowledge base with names and/or synonyms  matching a set of keywords or substrings.  The (possibly paged) results returned should generally  be returned in order of the quality of the match,  that is, the highest ranked concepts should exactly  match the most keywords, in the same order as the  keywords were given. Lower quality hits with fewer  keyword matches or out-of-order keyword matches,  should be returned lower in the list. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConceptsApi()
keywords = 'keywords_example' # str | a (urlencoded) space delimited set of keywords or substrings against which to match concept names and synonyms
types = 'types_example' # str | a (url-encoded) space-delimited set of semantic groups (specified as codes gene, pathway, etc.) to which to constrain concepts matched by the main keyword search (see [Biolink Model](https://biolink.github.io/biolink-model) for the full list of codes)  (optional)
page_number = 56 # int | (1-based) number of the page to be returned in a paged set of query results  (optional)
page_size = 56 # int | number of concepts per page to be returned in a paged set of query results  (optional)

try:
    api_response = api_instance.get_concepts(keywords, types=types, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConceptsApi->get_concepts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keywords** | **str**| a (urlencoded) space delimited set of keywords or substrings against which to match concept names and synonyms | 
 **types** | **str**| a (url-encoded) space-delimited set of semantic groups (specified as codes gene, pathway, etc.) to which to constrain concepts matched by the main keyword search (see [Biolink Model](https://biolink.github.io/biolink-model) for the full list of codes)  | [optional] 
 **page_number** | **int**| (1-based) number of the page to be returned in a paged set of query results  | [optional] 
 **page_size** | **int**| number of concepts per page to be returned in a paged set of query results  | [optional] 

### Return type

[**list[BeaconConcept]**](BeaconConcept.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_exact_matches_to_concept**
> list[str] get_exact_matches_to_concept(concept_id)



Retrieves a list of qualified identifiers of \"exact match\" concepts, [sensa SKOS](http://www.w3.org/2004/02/skos/core#exactMatch) associated with a specified (url-encoded) CURIE (without brackets) concept object identifier,  typically, of a concept selected from the list of concepts originally returned by a /concepts API call on a given KS.  

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConceptsApi()
concept_id = 'concept_id_example' # str | (url-encoded) CURIE identifier of the concept to be matched

try:
    api_response = api_instance.get_exact_matches_to_concept(concept_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConceptsApi->get_exact_matches_to_concept: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **concept_id** | **str**| (url-encoded) CURIE identifier of the concept to be matched | 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_exact_matches_to_concept_list**
> list[str] get_exact_matches_to_concept_list(c)



Given an input list of [CURIE](https://www.w3.org/TR/curie/) identifiers of known exactly matched concepts [*sensa*-SKOS](http://www.w3.org/2004/02/skos/core#exactMatch), retrieves the list of [CURIE](https://www.w3.org/TR/curie/) identifiers of additional concepts that are deemed by the given knowledge source to be exact matches to one or more of the input concepts **plus** whichever identifiers from the input list which specifically matched these new additional concepts.  If an empty set is returned, the it can be assumed that the given  knowledge source does not know of any new equivalent concepts matching the input set. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConceptsApi()
c = ['c_example'] # list[str] | set of [CURIE-encoded](https://www.w3.org/TR/curie/) identifiers of exactly matching concepts, to be used in a search for additional exactly matching concepts [*sensa*-SKOS](http://www.w3.org/2004/02/skos/core#exactMatch). 

try:
    api_response = api_instance.get_exact_matches_to_concept_list(c)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConceptsApi->get_exact_matches_to_concept_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **c** | [**list[str]**](str.md)| set of [CURIE-encoded](https://www.w3.org/TR/curie/) identifiers of exactly matching concepts, to be used in a search for additional exactly matching concepts [*sensa*-SKOS](http://www.w3.org/2004/02/skos/core#exactMatch).  | 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

