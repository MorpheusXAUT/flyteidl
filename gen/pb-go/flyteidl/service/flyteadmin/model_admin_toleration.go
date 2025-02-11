/*
 * flyteidl/service/admin.proto
 *
 * No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)
 *
 * API version: version not set
 * Generated by: Swagger Codegen (https://github.com/swagger-api/swagger-codegen.git)
 */

package flyteadmin

// Defines a set of specific label selectors that the execution can tolerate on a cluster.
type AdminToleration struct {
	// A toleration selector is similar to that of an affinity but the only valid operators are EQUALS AND EXISTS.
	Selectors []AdminSelector `json:"selectors,omitempty"`
}
