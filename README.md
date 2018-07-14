# swagger-client
This is the Translator Knowledge Beacon web service application programming interface (API). 

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.16
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen
For more information, please visit [http://starinformatics.com](http://starinformatics.com)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install (Recommended)

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/NCATS-Infrared/gnbr-client-python.git
```

Then import the package:
```python
import swagger_client 
```

(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/NCATS-Infrared/gnbr-client-python.git`). Another option is to install using a virtual environment (conda or virtualenv). To do so, set up and/or activate your environment and use pip as per usual.

virtualenv
```
virtualenv env
source env/bin/activate
```
conda
```
conda create --name env
source activate env
```


### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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

## Documentation for API Endpoints

All URIs are relative to *https://reference-beacon.ncats.io*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ConceptsApi* | [**get_concept_details**](docs/ConceptsApi.md#get_concept_details) | **GET** /concepts/{conceptId} | 
*ConceptsApi* | [**get_concepts**](docs/ConceptsApi.md#get_concepts) | **GET** /concepts | 
*ConceptsApi* | [**get_exact_matches_to_concept**](docs/ConceptsApi.md#get_exact_matches_to_concept) | **GET** /exactmatches/{conceptId} | 
*ConceptsApi* | [**get_exact_matches_to_concept_list**](docs/ConceptsApi.md#get_exact_matches_to_concept_list) | **GET** /exactmatches | 
*MetadataApi* | [**get_concept_types**](docs/MetadataApi.md#get_concept_types) | **GET** /types | 
*MetadataApi* | [**get_predicates**](docs/MetadataApi.md#get_predicates) | **GET** /predicates | 
*StatementsApi* | [**get_evidence**](docs/StatementsApi.md#get_evidence) | **GET** /evidence/{statementId} | 
*StatementsApi* | [**get_statements**](docs/StatementsApi.md#get_statements) | **GET** /statements | 


## Documentation For Models

 - [BeaconAnnotation](docs/BeaconAnnotation.md)
 - [BeaconConcept](docs/BeaconConcept.md)
 - [BeaconConceptDetail](docs/BeaconConceptDetail.md)
 - [BeaconConceptType](docs/BeaconConceptType.md)
 - [BeaconConceptWithDetails](docs/BeaconConceptWithDetails.md)
 - [BeaconPredicate](docs/BeaconPredicate.md)
 - [BeaconStatement](docs/BeaconStatement.md)
 - [BeaconStatementObject](docs/BeaconStatementObject.md)
 - [BeaconStatementPredicate](docs/BeaconStatementPredicate.md)
 - [BeaconStatementSubject](docs/BeaconStatementSubject.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author

srensi@stanford.edu

