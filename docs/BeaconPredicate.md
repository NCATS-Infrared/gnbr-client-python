# BeaconPredicate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | CURIE-encoded identifier of predicate relation  | [optional] 
**uri** | **str** | The predicate URI which should generally resolves to the  full semantic description of the predicate relation | [optional] 
**edge_label** | **str** | A predicate edge label which must be taken from the minimal predicate (&#39;slot&#39;) list of the [Biolink Model](https://biolink.github.io/biolink-model).  | [optional] 
**relation** | **str** | The predicate relation, with the preferred format being a CURIE where one exists, but strings/labels acceptable. This relation  may be equivalent to the edge_label (e.g. edge_label: has_phenotype, relation: RO:0002200), or a more specific relation in cases where the source provides more granularity  (e.g. edge_label: molecularly_interacts_with, relation: RO:0002447)  | [optional] 
**local_id** | **str** | CURIE-encoded identifier of the locally defined predicate relation. Such terms should be formally documented as mappings in the [Biolink Model](https://biolink.github.io/biolink-model)  | [optional] 
**local_uri** | **str** | The predicate URI which should generally resolves  to the local predicate relation | [optional] 
**local_relation** | **str** | human readable name of the locally defined predicate relation  | [optional] 
**description** | **str** | human readable definition of predicate relation  provided by this beacon  | [optional] 
**frequency** | **int** | the number of statement entries using the specified predicate in the given beacon knowledge base | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


