/*
 * flyteidl/service/admin.proto
 *
 * No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)
 *
 * API version: version not set
 * Generated by: Swagger Codegen (https://github.com/swagger-api/swagger-codegen.git)
 */

package flyteadmin

// A map of literals. This is a workaround since oneofs in proto messages cannot contain a map field.
type CoreLiteralMap struct {
	Literals map[string]CoreLiteral `json:"literals,omitempty"`
}
