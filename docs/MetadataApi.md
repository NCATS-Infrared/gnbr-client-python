# swagger_client.MetadataApi

All URIs are relative to *https://reference-beacon.ncats.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_concept_types**](MetadataApi.md#get_concept_types) | **GET** /types | 
[**get_predicates**](MetadataApi.md#get_predicates) | **GET** /predicates | 


# **get_concept_types**
> list[BeaconConceptType] get_concept_types()



Get a list of types and # of instances in the knowledge source, and a link to the API call for the list of equivalent terminology 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataApi()

try:
    api_response = api_instance.get_concept_types()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->get_concept_types: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[BeaconConceptType]**](BeaconConceptType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_predicates**
> list[BeaconPredicate] get_predicates()



Get a list of predicates used in statements issued by the knowledge source 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataApi()

try:
    api_response = api_instance.get_predicates()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->get_predicates: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[BeaconPredicate]**](BeaconPredicate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

