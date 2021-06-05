/*
 * flyteidl/service/admin.proto
 *
 * No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)
 *
 * API version: version not set
 * Generated by: Swagger Codegen (https://github.com/swagger-api/swagger-codegen.git)
 */

package flyteadmin

// A simple value. This supports any level of nesting (e.g. array of array of array of Blobs) as well as simple primitives.
type CoreLiteral struct {
	// A simple value.
	Scalar *CoreScalar `json:"scalar,omitempty"`
	// A collection of literals to allow nesting.
	Collection *CoreLiteralCollection `json:"collection,omitempty"`
	// A map of strings to literals.
	Map_ *CoreLiteralMap `json:"map,omitempty"`
	Int32Vector *CoreInt32Vector `json:"int32_vector,omitempty"`
	IntVector *CoreInt64Vector `json:"int_vector,omitempty"`
	FloatVector *CoreFloatVector `json:"float_vector,omitempty"`
	DoubleVector *CoreDoubleVector `json:"double_vector,omitempty"`
	BoolVector *CoreBoolVector `json:"bool_vector,omitempty"`
	StrVector *CoreStringVector `json:"str_vector,omitempty"`
}
