/*
 * flyteidl/service/admin.proto
 *
 * No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)
 *
 * API version: version not set
 * Generated by: Swagger Codegen (https://github.com/swagger-api/swagger-codegen.git)
 */

package flyteadmin

// Adds defaults for customizable workflow-execution specifications and overrides.
type AdminWorkflowExecutionConfig struct {
	// Can be used to control the number of parallel nodes to run within the workflow. This is useful to achieve fairness.
	MaxParallelism int32 `json:"max_parallelism,omitempty"`
	// Indicates security context permissions for executions triggered with this matchable attribute.
	SecurityContext *CoreSecurityContext `json:"security_context,omitempty"`
	// Encapsulates user settings pertaining to offloaded data (i.e. Blobs, Schema, query data, etc.).
	RawOutputDataConfig *AdminRawOutputDataConfig `json:"raw_output_data_config,omitempty"`
	// Custom labels to be applied to a triggered execution resource.
	Labels *AdminLabels `json:"labels,omitempty"`
	// Custom annotations to be applied to a triggered execution resource.
	Annotations *AdminAnnotations `json:"annotations,omitempty"`
}
