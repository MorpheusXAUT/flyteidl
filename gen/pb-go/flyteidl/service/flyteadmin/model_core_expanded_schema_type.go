/*
 * flyteidl/service/admin.proto
 *
 * No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)
 *
 * API version: version not set
 * Generated by: Swagger Codegen (https://github.com/swagger-api/swagger-codegen.git)
 */

package flyteadmin

type CoreExpandedSchemaType struct {
	// A list of ordered columns this schema comprises of.
	Columns []CoreLiteralType `json:"columns,omitempty"`
	Names []string `json:"names,omitempty"`
}