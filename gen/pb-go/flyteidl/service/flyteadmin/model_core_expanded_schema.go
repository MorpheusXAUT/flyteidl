/*
 * flyteidl/service/admin.proto
 *
 * No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)
 *
 * API version: version not set
 * Generated by: Swagger Codegen (https://github.com/swagger-api/swagger-codegen.git)
 */

package flyteadmin

type CoreExpandedSchema struct {
	Type_ *CoreExpandedSchemaType `json:"type,omitempty"`
	Uri string `json:"uri,omitempty"`
	Metadata *CoreSchemaMetadata `json:"metadata,omitempty"`
}