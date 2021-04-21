// Code generated by protoc-gen-go. DO NOT EDIT.
// source: flyteidl/admin/node_execution.proto

package admin

import (
	fmt "fmt"
	core "github.com/flyteorg/flyteidl/gen/pb-go/flyteidl/core"
	proto "github.com/golang/protobuf/proto"
	duration "github.com/golang/protobuf/ptypes/duration"
	timestamp "github.com/golang/protobuf/ptypes/timestamp"
	math "math"
)

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

// This is a compile-time assertion to ensure that this generated file
// is compatible with the proto package it is being compiled against.
// A compilation error at this line likely means your copy of the
// proto package needs to be updated.
const _ = proto.ProtoPackageIsVersion3 // please upgrade the proto package

// A message used to fetch a single node execution entity.
type NodeExecutionGetRequest struct {
	// Uniquely identifies an individual node execution.
	Id                   *core.NodeExecutionIdentifier `protobuf:"bytes,1,opt,name=id,proto3" json:"id,omitempty"`
	XXX_NoUnkeyedLiteral struct{}                      `json:"-"`
	XXX_unrecognized     []byte                        `json:"-"`
	XXX_sizecache        int32                         `json:"-"`
}

func (m *NodeExecutionGetRequest) Reset()         { *m = NodeExecutionGetRequest{} }
func (m *NodeExecutionGetRequest) String() string { return proto.CompactTextString(m) }
func (*NodeExecutionGetRequest) ProtoMessage()    {}
func (*NodeExecutionGetRequest) Descriptor() ([]byte, []int) {
	return fileDescriptor_f73b3eae493fd736, []int{0}
}

func (m *NodeExecutionGetRequest) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_NodeExecutionGetRequest.Unmarshal(m, b)
}
func (m *NodeExecutionGetRequest) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_NodeExecutionGetRequest.Marshal(b, m, deterministic)
}
func (m *NodeExecutionGetRequest) XXX_Merge(src proto.Message) {
	xxx_messageInfo_NodeExecutionGetRequest.Merge(m, src)
}
func (m *NodeExecutionGetRequest) XXX_Size() int {
	return xxx_messageInfo_NodeExecutionGetRequest.Size(m)
}
func (m *NodeExecutionGetRequest) XXX_DiscardUnknown() {
	xxx_messageInfo_NodeExecutionGetRequest.DiscardUnknown(m)
}

var xxx_messageInfo_NodeExecutionGetRequest proto.InternalMessageInfo

func (m *NodeExecutionGetRequest) GetId() *core.NodeExecutionIdentifier {
	if m != nil {
		return m.Id
	}
	return nil
}

// Represents a request structure to retrieve a list of node execution entities.
type NodeExecutionListRequest struct {
	// Indicates the workflow execution to filter by.
	WorkflowExecutionId *core.WorkflowExecutionIdentifier `protobuf:"bytes,1,opt,name=workflow_execution_id,json=workflowExecutionId,proto3" json:"workflow_execution_id,omitempty"`
	// Indicates the number of resources to be returned.
	Limit uint32 `protobuf:"varint,2,opt,name=limit,proto3" json:"limit,omitempty"`
	// In the case of multiple pages of results, the, server-provided token can be used to fetch the next page
	// in a query.
	// +optional
	Token string `protobuf:"bytes,3,opt,name=token,proto3" json:"token,omitempty"`
	// Indicates a list of filters passed as string.
	// More info on constructing filters : <Link>
	// +optional
	Filters string `protobuf:"bytes,4,opt,name=filters,proto3" json:"filters,omitempty"`
	// Sort ordering.
	// +optional
	SortBy *Sort `protobuf:"bytes,5,opt,name=sort_by,json=sortBy,proto3" json:"sort_by,omitempty"`
	// Unique identifier of the parent node in the execution
	// +optional
	UniqueParentId       string   `protobuf:"bytes,6,opt,name=unique_parent_id,json=uniqueParentId,proto3" json:"unique_parent_id,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *NodeExecutionListRequest) Reset()         { *m = NodeExecutionListRequest{} }
func (m *NodeExecutionListRequest) String() string { return proto.CompactTextString(m) }
func (*NodeExecutionListRequest) ProtoMessage()    {}
func (*NodeExecutionListRequest) Descriptor() ([]byte, []int) {
	return fileDescriptor_f73b3eae493fd736, []int{1}
}

func (m *NodeExecutionListRequest) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_NodeExecutionListRequest.Unmarshal(m, b)
}
func (m *NodeExecutionListRequest) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_NodeExecutionListRequest.Marshal(b, m, deterministic)
}
func (m *NodeExecutionListRequest) XXX_Merge(src proto.Message) {
	xxx_messageInfo_NodeExecutionListRequest.Merge(m, src)
}
func (m *NodeExecutionListRequest) XXX_Size() int {
	return xxx_messageInfo_NodeExecutionListRequest.Size(m)
}
func (m *NodeExecutionListRequest) XXX_DiscardUnknown() {
	xxx_messageInfo_NodeExecutionListRequest.DiscardUnknown(m)
}

var xxx_messageInfo_NodeExecutionListRequest proto.InternalMessageInfo

func (m *NodeExecutionListRequest) GetWorkflowExecutionId() *core.WorkflowExecutionIdentifier {
	if m != nil {
		return m.WorkflowExecutionId
	}
	return nil
}

func (m *NodeExecutionListRequest) GetLimit() uint32 {
	if m != nil {
		return m.Limit
	}
	return 0
}

func (m *NodeExecutionListRequest) GetToken() string {
	if m != nil {
		return m.Token
	}
	return ""
}

func (m *NodeExecutionListRequest) GetFilters() string {
	if m != nil {
		return m.Filters
	}
	return ""
}

func (m *NodeExecutionListRequest) GetSortBy() *Sort {
	if m != nil {
		return m.SortBy
	}
	return nil
}

func (m *NodeExecutionListRequest) GetUniqueParentId() string {
	if m != nil {
		return m.UniqueParentId
	}
	return ""
}

// Represents a request structure to retrieve a list of node execution entities launched by a specific task.
type NodeExecutionForTaskListRequest struct {
	// Indicates the node execution to filter by.
	TaskExecutionId *core.TaskExecutionIdentifier `protobuf:"bytes,1,opt,name=task_execution_id,json=taskExecutionId,proto3" json:"task_execution_id,omitempty"`
	// Indicates the number of resources to be returned.
	Limit uint32 `protobuf:"varint,2,opt,name=limit,proto3" json:"limit,omitempty"`
	// In the case of multiple pages of results, the, server-provided token can be used to fetch the next page
	// in a query.
	// +optional
	Token string `protobuf:"bytes,3,opt,name=token,proto3" json:"token,omitempty"`
	// Indicates a list of filters passed as string.
	// More info on constructing filters : <Link>
	// +optional
	Filters string `protobuf:"bytes,4,opt,name=filters,proto3" json:"filters,omitempty"`
	// Sort ordering.
	// +optional
	SortBy               *Sort    `protobuf:"bytes,5,opt,name=sort_by,json=sortBy,proto3" json:"sort_by,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *NodeExecutionForTaskListRequest) Reset()         { *m = NodeExecutionForTaskListRequest{} }
func (m *NodeExecutionForTaskListRequest) String() string { return proto.CompactTextString(m) }
func (*NodeExecutionForTaskListRequest) ProtoMessage()    {}
func (*NodeExecutionForTaskListRequest) Descriptor() ([]byte, []int) {
	return fileDescriptor_f73b3eae493fd736, []int{2}
}

func (m *NodeExecutionForTaskListRequest) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_NodeExecutionForTaskListRequest.Unmarshal(m, b)
}
func (m *NodeExecutionForTaskListRequest) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_NodeExecutionForTaskListRequest.Marshal(b, m, deterministic)
}
func (m *NodeExecutionForTaskListRequest) XXX_Merge(src proto.Message) {
	xxx_messageInfo_NodeExecutionForTaskListRequest.Merge(m, src)
}
func (m *NodeExecutionForTaskListRequest) XXX_Size() int {
	return xxx_messageInfo_NodeExecutionForTaskListRequest.Size(m)
}
func (m *NodeExecutionForTaskListRequest) XXX_DiscardUnknown() {
	xxx_messageInfo_NodeExecutionForTaskListRequest.DiscardUnknown(m)
}

var xxx_messageInfo_NodeExecutionForTaskListRequest proto.InternalMessageInfo

func (m *NodeExecutionForTaskListRequest) GetTaskExecutionId() *core.TaskExecutionIdentifier {
	if m != nil {
		return m.TaskExecutionId
	}
	return nil
}

func (m *NodeExecutionForTaskListRequest) GetLimit() uint32 {
	if m != nil {
		return m.Limit
	}
	return 0
}

func (m *NodeExecutionForTaskListRequest) GetToken() string {
	if m != nil {
		return m.Token
	}
	return ""
}

func (m *NodeExecutionForTaskListRequest) GetFilters() string {
	if m != nil {
		return m.Filters
	}
	return ""
}

func (m *NodeExecutionForTaskListRequest) GetSortBy() *Sort {
	if m != nil {
		return m.SortBy
	}
	return nil
}

// Encapsulates all details for a single node execution entity.
// A node represents a component in the overall workflow graph. A node launch a task, multiple tasks, an entire nested
// sub-workflow, or even a separate child-workflow execution.
// The same task can be called repeatedly in a single workflow but each node is unique.
type NodeExecution struct {
	// Uniquely identifies an individual node execution.
	Id *core.NodeExecutionIdentifier `protobuf:"bytes,1,opt,name=id,proto3" json:"id,omitempty"`
	// Path to remote data store where input blob is stored.
	InputUri string `protobuf:"bytes,2,opt,name=input_uri,json=inputUri,proto3" json:"input_uri,omitempty"`
	// Computed results associated with this node execution.
	Closure *NodeExecutionClosure `protobuf:"bytes,3,opt,name=closure,proto3" json:"closure,omitempty"`
	// Metadata for Node Execution
	Metadata             *NodeExecutionMetaData `protobuf:"bytes,4,opt,name=metadata,proto3" json:"metadata,omitempty"`
	XXX_NoUnkeyedLiteral struct{}               `json:"-"`
	XXX_unrecognized     []byte                 `json:"-"`
	XXX_sizecache        int32                  `json:"-"`
}

func (m *NodeExecution) Reset()         { *m = NodeExecution{} }
func (m *NodeExecution) String() string { return proto.CompactTextString(m) }
func (*NodeExecution) ProtoMessage()    {}
func (*NodeExecution) Descriptor() ([]byte, []int) {
	return fileDescriptor_f73b3eae493fd736, []int{3}
}

func (m *NodeExecution) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_NodeExecution.Unmarshal(m, b)
}
func (m *NodeExecution) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_NodeExecution.Marshal(b, m, deterministic)
}
func (m *NodeExecution) XXX_Merge(src proto.Message) {
	xxx_messageInfo_NodeExecution.Merge(m, src)
}
func (m *NodeExecution) XXX_Size() int {
	return xxx_messageInfo_NodeExecution.Size(m)
}
func (m *NodeExecution) XXX_DiscardUnknown() {
	xxx_messageInfo_NodeExecution.DiscardUnknown(m)
}

var xxx_messageInfo_NodeExecution proto.InternalMessageInfo

func (m *NodeExecution) GetId() *core.NodeExecutionIdentifier {
	if m != nil {
		return m.Id
	}
	return nil
}

func (m *NodeExecution) GetInputUri() string {
	if m != nil {
		return m.InputUri
	}
	return ""
}

func (m *NodeExecution) GetClosure() *NodeExecutionClosure {
	if m != nil {
		return m.Closure
	}
	return nil
}

func (m *NodeExecution) GetMetadata() *NodeExecutionMetaData {
	if m != nil {
		return m.Metadata
	}
	return nil
}

// Represents additional attributes related to a Node Execution
type NodeExecutionMetaData struct {
	// Node executions are grouped depending on retries of the parent
	// Retry group is unique within the context of a parent node.
	RetryGroup string `protobuf:"bytes,1,opt,name=retry_group,json=retryGroup,proto3" json:"retry_group,omitempty"`
	// Boolean flag indicating if the node has child nodes under it
	IsParentNode bool `protobuf:"varint,2,opt,name=is_parent_node,json=isParentNode,proto3" json:"is_parent_node,omitempty"`
	// Node id of the node in the original workflow
	// This maps to value of WorkflowTemplate.nodes[X].id
	SpecNodeId           string   `protobuf:"bytes,3,opt,name=spec_node_id,json=specNodeId,proto3" json:"spec_node_id,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *NodeExecutionMetaData) Reset()         { *m = NodeExecutionMetaData{} }
func (m *NodeExecutionMetaData) String() string { return proto.CompactTextString(m) }
func (*NodeExecutionMetaData) ProtoMessage()    {}
func (*NodeExecutionMetaData) Descriptor() ([]byte, []int) {
	return fileDescriptor_f73b3eae493fd736, []int{4}
}

func (m *NodeExecutionMetaData) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_NodeExecutionMetaData.Unmarshal(m, b)
}
func (m *NodeExecutionMetaData) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_NodeExecutionMetaData.Marshal(b, m, deterministic)
}
func (m *NodeExecutionMetaData) XXX_Merge(src proto.Message) {
	xxx_messageInfo_NodeExecutionMetaData.Merge(m, src)
}
func (m *NodeExecutionMetaData) XXX_Size() int {
	return xxx_messageInfo_NodeExecutionMetaData.Size(m)
}
func (m *NodeExecutionMetaData) XXX_DiscardUnknown() {
	xxx_messageInfo_NodeExecutionMetaData.DiscardUnknown(m)
}

var xxx_messageInfo_NodeExecutionMetaData proto.InternalMessageInfo

func (m *NodeExecutionMetaData) GetRetryGroup() string {
	if m != nil {
		return m.RetryGroup
	}
	return ""
}

func (m *NodeExecutionMetaData) GetIsParentNode() bool {
	if m != nil {
		return m.IsParentNode
	}
	return false
}

func (m *NodeExecutionMetaData) GetSpecNodeId() string {
	if m != nil {
		return m.SpecNodeId
	}
	return ""
}

// Request structure to retrieve a list of node execution entities.
type NodeExecutionList struct {
	NodeExecutions []*NodeExecution `protobuf:"bytes,1,rep,name=node_executions,json=nodeExecutions,proto3" json:"node_executions,omitempty"`
	// In the case of multiple pages of results, the server-provided token can be used to fetch the next page
	// in a query. If there are no more results, this value will be empty.
	Token                string   `protobuf:"bytes,2,opt,name=token,proto3" json:"token,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *NodeExecutionList) Reset()         { *m = NodeExecutionList{} }
func (m *NodeExecutionList) String() string { return proto.CompactTextString(m) }
func (*NodeExecutionList) ProtoMessage()    {}
func (*NodeExecutionList) Descriptor() ([]byte, []int) {
	return fileDescriptor_f73b3eae493fd736, []int{5}
}

func (m *NodeExecutionList) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_NodeExecutionList.Unmarshal(m, b)
}
func (m *NodeExecutionList) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_NodeExecutionList.Marshal(b, m, deterministic)
}
func (m *NodeExecutionList) XXX_Merge(src proto.Message) {
	xxx_messageInfo_NodeExecutionList.Merge(m, src)
}
func (m *NodeExecutionList) XXX_Size() int {
	return xxx_messageInfo_NodeExecutionList.Size(m)
}
func (m *NodeExecutionList) XXX_DiscardUnknown() {
	xxx_messageInfo_NodeExecutionList.DiscardUnknown(m)
}

var xxx_messageInfo_NodeExecutionList proto.InternalMessageInfo

func (m *NodeExecutionList) GetNodeExecutions() []*NodeExecution {
	if m != nil {
		return m.NodeExecutions
	}
	return nil
}

func (m *NodeExecutionList) GetToken() string {
	if m != nil {
		return m.Token
	}
	return ""
}

// Container for node execution details and results.
type NodeExecutionClosure struct {
	// Only a node in a terminal state will have a non-empty output_result.
	//
	// Types that are valid to be assigned to OutputResult:
	//	*NodeExecutionClosure_OutputUri
	//	*NodeExecutionClosure_Error
	OutputResult isNodeExecutionClosure_OutputResult `protobuf_oneof:"output_result"`
	// The last recorded phase for this node execution.
	Phase core.NodeExecution_Phase `protobuf:"varint,3,opt,name=phase,proto3,enum=flyteidl.core.NodeExecution_Phase" json:"phase,omitempty"`
	// Time at which the node execution began running.
	StartedAt *timestamp.Timestamp `protobuf:"bytes,4,opt,name=started_at,json=startedAt,proto3" json:"started_at,omitempty"`
	// The amount of time the node execution spent running.
	Duration *duration.Duration `protobuf:"bytes,5,opt,name=duration,proto3" json:"duration,omitempty"`
	// Time at which the node execution was created.
	CreatedAt *timestamp.Timestamp `protobuf:"bytes,6,opt,name=created_at,json=createdAt,proto3" json:"created_at,omitempty"`
	// Time at which the node execution was last updated.
	UpdatedAt *timestamp.Timestamp `protobuf:"bytes,7,opt,name=updated_at,json=updatedAt,proto3" json:"updated_at,omitempty"`
	// Store metadata for what the node launched.
	// for ex: if this is a workflow node, we store information for the launched workflow.
	//
	// Types that are valid to be assigned to TargetMetadata:
	//	*NodeExecutionClosure_WorkflowNodeMetadata
	//	*NodeExecutionClosure_TaskNodeMetadata
	TargetMetadata       isNodeExecutionClosure_TargetMetadata `protobuf_oneof:"target_metadata"`
	XXX_NoUnkeyedLiteral struct{}                              `json:"-"`
	XXX_unrecognized     []byte                                `json:"-"`
	XXX_sizecache        int32                                 `json:"-"`
}

func (m *NodeExecutionClosure) Reset()         { *m = NodeExecutionClosure{} }
func (m *NodeExecutionClosure) String() string { return proto.CompactTextString(m) }
func (*NodeExecutionClosure) ProtoMessage()    {}
func (*NodeExecutionClosure) Descriptor() ([]byte, []int) {
	return fileDescriptor_f73b3eae493fd736, []int{6}
}

func (m *NodeExecutionClosure) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_NodeExecutionClosure.Unmarshal(m, b)
}
func (m *NodeExecutionClosure) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_NodeExecutionClosure.Marshal(b, m, deterministic)
}
func (m *NodeExecutionClosure) XXX_Merge(src proto.Message) {
	xxx_messageInfo_NodeExecutionClosure.Merge(m, src)
}
func (m *NodeExecutionClosure) XXX_Size() int {
	return xxx_messageInfo_NodeExecutionClosure.Size(m)
}
func (m *NodeExecutionClosure) XXX_DiscardUnknown() {
	xxx_messageInfo_NodeExecutionClosure.DiscardUnknown(m)
}

var xxx_messageInfo_NodeExecutionClosure proto.InternalMessageInfo

type isNodeExecutionClosure_OutputResult interface {
	isNodeExecutionClosure_OutputResult()
}

type NodeExecutionClosure_OutputUri struct {
	OutputUri string `protobuf:"bytes,1,opt,name=output_uri,json=outputUri,proto3,oneof"`
}

type NodeExecutionClosure_Error struct {
	Error *core.ExecutionError `protobuf:"bytes,2,opt,name=error,proto3,oneof"`
}

func (*NodeExecutionClosure_OutputUri) isNodeExecutionClosure_OutputResult() {}

func (*NodeExecutionClosure_Error) isNodeExecutionClosure_OutputResult() {}

func (m *NodeExecutionClosure) GetOutputResult() isNodeExecutionClosure_OutputResult {
	if m != nil {
		return m.OutputResult
	}
	return nil
}

func (m *NodeExecutionClosure) GetOutputUri() string {
	if x, ok := m.GetOutputResult().(*NodeExecutionClosure_OutputUri); ok {
		return x.OutputUri
	}
	return ""
}

func (m *NodeExecutionClosure) GetError() *core.ExecutionError {
	if x, ok := m.GetOutputResult().(*NodeExecutionClosure_Error); ok {
		return x.Error
	}
	return nil
}

func (m *NodeExecutionClosure) GetPhase() core.NodeExecution_Phase {
	if m != nil {
		return m.Phase
	}
	return core.NodeExecution_UNDEFINED
}

func (m *NodeExecutionClosure) GetStartedAt() *timestamp.Timestamp {
	if m != nil {
		return m.StartedAt
	}
	return nil
}

func (m *NodeExecutionClosure) GetDuration() *duration.Duration {
	if m != nil {
		return m.Duration
	}
	return nil
}

func (m *NodeExecutionClosure) GetCreatedAt() *timestamp.Timestamp {
	if m != nil {
		return m.CreatedAt
	}
	return nil
}

func (m *NodeExecutionClosure) GetUpdatedAt() *timestamp.Timestamp {
	if m != nil {
		return m.UpdatedAt
	}
	return nil
}

type isNodeExecutionClosure_TargetMetadata interface {
	isNodeExecutionClosure_TargetMetadata()
}

type NodeExecutionClosure_WorkflowNodeMetadata struct {
	WorkflowNodeMetadata *WorkflowNodeMetadata `protobuf:"bytes,8,opt,name=workflow_node_metadata,json=workflowNodeMetadata,proto3,oneof"`
}

type NodeExecutionClosure_TaskNodeMetadata struct {
	TaskNodeMetadata *TaskNodeMetadata `protobuf:"bytes,9,opt,name=task_node_metadata,json=taskNodeMetadata,proto3,oneof"`
}

func (*NodeExecutionClosure_WorkflowNodeMetadata) isNodeExecutionClosure_TargetMetadata() {}

func (*NodeExecutionClosure_TaskNodeMetadata) isNodeExecutionClosure_TargetMetadata() {}

func (m *NodeExecutionClosure) GetTargetMetadata() isNodeExecutionClosure_TargetMetadata {
	if m != nil {
		return m.TargetMetadata
	}
	return nil
}

func (m *NodeExecutionClosure) GetWorkflowNodeMetadata() *WorkflowNodeMetadata {
	if x, ok := m.GetTargetMetadata().(*NodeExecutionClosure_WorkflowNodeMetadata); ok {
		return x.WorkflowNodeMetadata
	}
	return nil
}

func (m *NodeExecutionClosure) GetTaskNodeMetadata() *TaskNodeMetadata {
	if x, ok := m.GetTargetMetadata().(*NodeExecutionClosure_TaskNodeMetadata); ok {
		return x.TaskNodeMetadata
	}
	return nil
}

// XXX_OneofWrappers is for the internal use of the proto package.
func (*NodeExecutionClosure) XXX_OneofWrappers() []interface{} {
	return []interface{}{
		(*NodeExecutionClosure_OutputUri)(nil),
		(*NodeExecutionClosure_Error)(nil),
		(*NodeExecutionClosure_WorkflowNodeMetadata)(nil),
		(*NodeExecutionClosure_TaskNodeMetadata)(nil),
	}
}

// Metadata for a WorkflowNode
type WorkflowNodeMetadata struct {
	ExecutionId          *core.WorkflowExecutionIdentifier `protobuf:"bytes,1,opt,name=executionId,proto3" json:"executionId,omitempty"`
	XXX_NoUnkeyedLiteral struct{}                          `json:"-"`
	XXX_unrecognized     []byte                            `json:"-"`
	XXX_sizecache        int32                             `json:"-"`
}

func (m *WorkflowNodeMetadata) Reset()         { *m = WorkflowNodeMetadata{} }
func (m *WorkflowNodeMetadata) String() string { return proto.CompactTextString(m) }
func (*WorkflowNodeMetadata) ProtoMessage()    {}
func (*WorkflowNodeMetadata) Descriptor() ([]byte, []int) {
	return fileDescriptor_f73b3eae493fd736, []int{7}
}

func (m *WorkflowNodeMetadata) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_WorkflowNodeMetadata.Unmarshal(m, b)
}
func (m *WorkflowNodeMetadata) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_WorkflowNodeMetadata.Marshal(b, m, deterministic)
}
func (m *WorkflowNodeMetadata) XXX_Merge(src proto.Message) {
	xxx_messageInfo_WorkflowNodeMetadata.Merge(m, src)
}
func (m *WorkflowNodeMetadata) XXX_Size() int {
	return xxx_messageInfo_WorkflowNodeMetadata.Size(m)
}
func (m *WorkflowNodeMetadata) XXX_DiscardUnknown() {
	xxx_messageInfo_WorkflowNodeMetadata.DiscardUnknown(m)
}

var xxx_messageInfo_WorkflowNodeMetadata proto.InternalMessageInfo

func (m *WorkflowNodeMetadata) GetExecutionId() *core.WorkflowExecutionIdentifier {
	if m != nil {
		return m.ExecutionId
	}
	return nil
}

// Metadata for the case in which the node is a TaskNode
type TaskNodeMetadata struct {
	// Captures the status of caching for this execution.
	CacheStatus core.CatalogCacheStatus `protobuf:"varint,1,opt,name=cache_status,json=cacheStatus,proto3,enum=flyteidl.core.CatalogCacheStatus" json:"cache_status,omitempty"`
	// This structure carries the catalog artifact information
	CatalogKey           *core.CatalogMetadata `protobuf:"bytes,2,opt,name=catalog_key,json=catalogKey,proto3" json:"catalog_key,omitempty"`
	XXX_NoUnkeyedLiteral struct{}              `json:"-"`
	XXX_unrecognized     []byte                `json:"-"`
	XXX_sizecache        int32                 `json:"-"`
}

func (m *TaskNodeMetadata) Reset()         { *m = TaskNodeMetadata{} }
func (m *TaskNodeMetadata) String() string { return proto.CompactTextString(m) }
func (*TaskNodeMetadata) ProtoMessage()    {}
func (*TaskNodeMetadata) Descriptor() ([]byte, []int) {
	return fileDescriptor_f73b3eae493fd736, []int{8}
}

func (m *TaskNodeMetadata) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_TaskNodeMetadata.Unmarshal(m, b)
}
func (m *TaskNodeMetadata) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_TaskNodeMetadata.Marshal(b, m, deterministic)
}
func (m *TaskNodeMetadata) XXX_Merge(src proto.Message) {
	xxx_messageInfo_TaskNodeMetadata.Merge(m, src)
}
func (m *TaskNodeMetadata) XXX_Size() int {
	return xxx_messageInfo_TaskNodeMetadata.Size(m)
}
func (m *TaskNodeMetadata) XXX_DiscardUnknown() {
	xxx_messageInfo_TaskNodeMetadata.DiscardUnknown(m)
}

var xxx_messageInfo_TaskNodeMetadata proto.InternalMessageInfo

func (m *TaskNodeMetadata) GetCacheStatus() core.CatalogCacheStatus {
	if m != nil {
		return m.CacheStatus
	}
	return core.CatalogCacheStatus_CACHE_DISABLED
}

func (m *TaskNodeMetadata) GetCatalogKey() *core.CatalogMetadata {
	if m != nil {
		return m.CatalogKey
	}
	return nil
}

// For dynamic workflow nodes we capture information about the dynamic workflow definition that gets generated.
type DynamicWorkflowNodeMetadata struct {
	// id represents the unique identifier of the workflow.
	Id *core.Identifier `protobuf:"bytes,1,opt,name=id,proto3" json:"id,omitempty"`
	// Represents the compiled representation of the embedded dynamic workflow.
	CompiledWorkflow     *core.CompiledWorkflowClosure `protobuf:"bytes,2,opt,name=compiled_workflow,json=compiledWorkflow,proto3" json:"compiled_workflow,omitempty"`
	XXX_NoUnkeyedLiteral struct{}                      `json:"-"`
	XXX_unrecognized     []byte                        `json:"-"`
	XXX_sizecache        int32                         `json:"-"`
}

func (m *DynamicWorkflowNodeMetadata) Reset()         { *m = DynamicWorkflowNodeMetadata{} }
func (m *DynamicWorkflowNodeMetadata) String() string { return proto.CompactTextString(m) }
func (*DynamicWorkflowNodeMetadata) ProtoMessage()    {}
func (*DynamicWorkflowNodeMetadata) Descriptor() ([]byte, []int) {
	return fileDescriptor_f73b3eae493fd736, []int{9}
}

func (m *DynamicWorkflowNodeMetadata) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_DynamicWorkflowNodeMetadata.Unmarshal(m, b)
}
func (m *DynamicWorkflowNodeMetadata) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_DynamicWorkflowNodeMetadata.Marshal(b, m, deterministic)
}
func (m *DynamicWorkflowNodeMetadata) XXX_Merge(src proto.Message) {
	xxx_messageInfo_DynamicWorkflowNodeMetadata.Merge(m, src)
}
func (m *DynamicWorkflowNodeMetadata) XXX_Size() int {
	return xxx_messageInfo_DynamicWorkflowNodeMetadata.Size(m)
}
func (m *DynamicWorkflowNodeMetadata) XXX_DiscardUnknown() {
	xxx_messageInfo_DynamicWorkflowNodeMetadata.DiscardUnknown(m)
}

var xxx_messageInfo_DynamicWorkflowNodeMetadata proto.InternalMessageInfo

func (m *DynamicWorkflowNodeMetadata) GetId() *core.Identifier {
	if m != nil {
		return m.Id
	}
	return nil
}

func (m *DynamicWorkflowNodeMetadata) GetCompiledWorkflow() *core.CompiledWorkflowClosure {
	if m != nil {
		return m.CompiledWorkflow
	}
	return nil
}

// Request structure to fetch inputs and output urls for a node execution.
type NodeExecutionGetDataRequest struct {
	// The identifier of the node execution for which to fetch inputs and outputs.
	Id                   *core.NodeExecutionIdentifier `protobuf:"bytes,1,opt,name=id,proto3" json:"id,omitempty"`
	XXX_NoUnkeyedLiteral struct{}                      `json:"-"`
	XXX_unrecognized     []byte                        `json:"-"`
	XXX_sizecache        int32                         `json:"-"`
}

func (m *NodeExecutionGetDataRequest) Reset()         { *m = NodeExecutionGetDataRequest{} }
func (m *NodeExecutionGetDataRequest) String() string { return proto.CompactTextString(m) }
func (*NodeExecutionGetDataRequest) ProtoMessage()    {}
func (*NodeExecutionGetDataRequest) Descriptor() ([]byte, []int) {
	return fileDescriptor_f73b3eae493fd736, []int{10}
}

func (m *NodeExecutionGetDataRequest) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_NodeExecutionGetDataRequest.Unmarshal(m, b)
}
func (m *NodeExecutionGetDataRequest) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_NodeExecutionGetDataRequest.Marshal(b, m, deterministic)
}
func (m *NodeExecutionGetDataRequest) XXX_Merge(src proto.Message) {
	xxx_messageInfo_NodeExecutionGetDataRequest.Merge(m, src)
}
func (m *NodeExecutionGetDataRequest) XXX_Size() int {
	return xxx_messageInfo_NodeExecutionGetDataRequest.Size(m)
}
func (m *NodeExecutionGetDataRequest) XXX_DiscardUnknown() {
	xxx_messageInfo_NodeExecutionGetDataRequest.DiscardUnknown(m)
}

var xxx_messageInfo_NodeExecutionGetDataRequest proto.InternalMessageInfo

func (m *NodeExecutionGetDataRequest) GetId() *core.NodeExecutionIdentifier {
	if m != nil {
		return m.Id
	}
	return nil
}

// Response structure for NodeExecutionGetDataRequest which contains inputs and outputs for a node execution.
type NodeExecutionGetDataResponse struct {
	// Signed url to fetch a core.LiteralMap of node execution inputs.
	Inputs *UrlBlob `protobuf:"bytes,1,opt,name=inputs,proto3" json:"inputs,omitempty"`
	// Signed url to fetch a core.LiteralMap of node execution outputs.
	Outputs *UrlBlob `protobuf:"bytes,2,opt,name=outputs,proto3" json:"outputs,omitempty"`
	// Optional, full_inputs will only be populated if they are under a configured size threshold.
	FullInputs *core.LiteralMap `protobuf:"bytes,3,opt,name=full_inputs,json=fullInputs,proto3" json:"full_inputs,omitempty"`
	// Optional, full_outputs will only be populated if they are under a configured size threshold.
	FullOutputs *core.LiteralMap `protobuf:"bytes,4,opt,name=full_outputs,json=fullOutputs,proto3" json:"full_outputs,omitempty"`
	// Optional Workflow closure for a dynamically generated workflow, in the case this node yields a dynamic workflow we return its structure here.
	DynamicWorkflow      *DynamicWorkflowNodeMetadata `protobuf:"bytes,16,opt,name=dynamic_workflow,json=dynamicWorkflow,proto3" json:"dynamic_workflow,omitempty"`
	XXX_NoUnkeyedLiteral struct{}                     `json:"-"`
	XXX_unrecognized     []byte                       `json:"-"`
	XXX_sizecache        int32                        `json:"-"`
}

func (m *NodeExecutionGetDataResponse) Reset()         { *m = NodeExecutionGetDataResponse{} }
func (m *NodeExecutionGetDataResponse) String() string { return proto.CompactTextString(m) }
func (*NodeExecutionGetDataResponse) ProtoMessage()    {}
func (*NodeExecutionGetDataResponse) Descriptor() ([]byte, []int) {
	return fileDescriptor_f73b3eae493fd736, []int{11}
}

func (m *NodeExecutionGetDataResponse) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_NodeExecutionGetDataResponse.Unmarshal(m, b)
}
func (m *NodeExecutionGetDataResponse) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_NodeExecutionGetDataResponse.Marshal(b, m, deterministic)
}
func (m *NodeExecutionGetDataResponse) XXX_Merge(src proto.Message) {
	xxx_messageInfo_NodeExecutionGetDataResponse.Merge(m, src)
}
func (m *NodeExecutionGetDataResponse) XXX_Size() int {
	return xxx_messageInfo_NodeExecutionGetDataResponse.Size(m)
}
func (m *NodeExecutionGetDataResponse) XXX_DiscardUnknown() {
	xxx_messageInfo_NodeExecutionGetDataResponse.DiscardUnknown(m)
}

var xxx_messageInfo_NodeExecutionGetDataResponse proto.InternalMessageInfo

func (m *NodeExecutionGetDataResponse) GetInputs() *UrlBlob {
	if m != nil {
		return m.Inputs
	}
	return nil
}

func (m *NodeExecutionGetDataResponse) GetOutputs() *UrlBlob {
	if m != nil {
		return m.Outputs
	}
	return nil
}

func (m *NodeExecutionGetDataResponse) GetFullInputs() *core.LiteralMap {
	if m != nil {
		return m.FullInputs
	}
	return nil
}

func (m *NodeExecutionGetDataResponse) GetFullOutputs() *core.LiteralMap {
	if m != nil {
		return m.FullOutputs
	}
	return nil
}

func (m *NodeExecutionGetDataResponse) GetDynamicWorkflow() *DynamicWorkflowNodeMetadata {
	if m != nil {
		return m.DynamicWorkflow
	}
	return nil
}

func init() {
	proto.RegisterType((*NodeExecutionGetRequest)(nil), "flyteidl.admin.NodeExecutionGetRequest")
	proto.RegisterType((*NodeExecutionListRequest)(nil), "flyteidl.admin.NodeExecutionListRequest")
	proto.RegisterType((*NodeExecutionForTaskListRequest)(nil), "flyteidl.admin.NodeExecutionForTaskListRequest")
	proto.RegisterType((*NodeExecution)(nil), "flyteidl.admin.NodeExecution")
	proto.RegisterType((*NodeExecutionMetaData)(nil), "flyteidl.admin.NodeExecutionMetaData")
	proto.RegisterType((*NodeExecutionList)(nil), "flyteidl.admin.NodeExecutionList")
	proto.RegisterType((*NodeExecutionClosure)(nil), "flyteidl.admin.NodeExecutionClosure")
	proto.RegisterType((*WorkflowNodeMetadata)(nil), "flyteidl.admin.WorkflowNodeMetadata")
	proto.RegisterType((*TaskNodeMetadata)(nil), "flyteidl.admin.TaskNodeMetadata")
	proto.RegisterType((*DynamicWorkflowNodeMetadata)(nil), "flyteidl.admin.DynamicWorkflowNodeMetadata")
	proto.RegisterType((*NodeExecutionGetDataRequest)(nil), "flyteidl.admin.NodeExecutionGetDataRequest")
	proto.RegisterType((*NodeExecutionGetDataResponse)(nil), "flyteidl.admin.NodeExecutionGetDataResponse")
}

func init() {
	proto.RegisterFile("flyteidl/admin/node_execution.proto", fileDescriptor_f73b3eae493fd736)
}

var fileDescriptor_f73b3eae493fd736 = []byte{
	// 1053 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0xc4, 0x56, 0xed, 0x6e, 0xe3, 0x44,
	0x17, 0x5e, 0xa7, 0x9f, 0x39, 0x69, 0xd3, 0x74, 0xde, 0xee, 0xbb, 0xd9, 0x76, 0x77, 0x1b, 0xcc,
	0x82, 0x0a, 0x68, 0x1d, 0x11, 0x54, 0xbe, 0x84, 0x40, 0xfd, 0xd8, 0xdd, 0x56, 0xb4, 0x50, 0xa6,
	0x5b, 0x90, 0x10, 0xc2, 0x9a, 0xd8, 0x93, 0x74, 0x14, 0xc7, 0xe3, 0xce, 0x8c, 0x55, 0xf2, 0x8f,
	0xdb, 0xd8, 0x1f, 0xdc, 0x15, 0x97, 0x80, 0x84, 0xc4, 0x55, 0x20, 0x8f, 0xc7, 0x4e, 0xec, 0x9a,
	0x56, 0x5a, 0x7e, 0xf0, 0x73, 0xce, 0x79, 0xce, 0x73, 0xe6, 0x7c, 0xf8, 0xf1, 0xc0, 0xdb, 0x83,
	0x60, 0xa2, 0x28, 0xf3, 0x83, 0x2e, 0xf1, 0xc7, 0x2c, 0xec, 0x86, 0xdc, 0xa7, 0x2e, 0xfd, 0x85,
	0x7a, 0xb1, 0x62, 0x3c, 0x74, 0x22, 0xc1, 0x15, 0x47, 0xcd, 0x0c, 0xe4, 0x68, 0xd0, 0xe6, 0x56,
	0x29, 0xc8, 0xe3, 0xe3, 0x71, 0x06, 0xde, 0x7c, 0x9c, 0x3b, 0x3d, 0x2e, 0x68, 0xb7, 0xc4, 0x35,
	0x13, 0xab, 0xdd, 0x1e, 0x51, 0x24, 0xe0, 0x43, 0xe3, 0x7c, 0x54, 0x72, 0xf2, 0x71, 0xc4, 0x02,
	0x2a, 0x8c, 0xf7, 0x49, 0xd1, 0xcb, 0x7c, 0x1a, 0x2a, 0x36, 0x60, 0xb9, 0xbf, 0x14, 0x1d, 0x30,
	0x45, 0x05, 0x09, 0xa4, 0xf1, 0x6e, 0x0f, 0x39, 0x1f, 0x06, 0xb4, 0xab, 0x4f, 0xfd, 0x78, 0xd0,
	0x55, 0x6c, 0x4c, 0xa5, 0x22, 0xe3, 0x28, 0xa3, 0x2f, 0x03, 0xfc, 0x58, 0x90, 0xe9, 0xcd, 0xed,
	0xef, 0xe0, 0xc1, 0x37, 0xdc, 0xa7, 0xcf, 0xb3, 0x82, 0x5e, 0x52, 0x85, 0xe9, 0x55, 0x4c, 0xa5,
	0x42, 0x1f, 0x43, 0x8d, 0xf9, 0x6d, 0xab, 0x63, 0xed, 0x34, 0x7a, 0xef, 0x3a, 0x79, 0xb7, 0x92,
	0x6b, 0x38, 0x85, 0x98, 0xe3, 0xfc, 0xce, 0xb8, 0xc6, 0x7c, 0xfb, 0x75, 0x0d, 0xda, 0x05, 0xff,
	0x09, 0x93, 0x39, 0xe9, 0xcf, 0x70, 0xff, 0x9a, 0x8b, 0xd1, 0x20, 0xe0, 0xd7, 0xd3, 0x89, 0xb8,
	0x79, 0x9e, 0xf7, 0x4b, 0x79, 0x7e, 0x30, 0xd8, 0xaa, 0x5c, 0xff, 0xbb, 0xbe, 0xe9, 0x44, 0x1b,
	0xb0, 0x10, 0xb0, 0x31, 0x53, 0xed, 0x5a, 0xc7, 0xda, 0x59, 0xc5, 0xe9, 0x21, 0xb1, 0x2a, 0x3e,
	0xa2, 0x61, 0x7b, 0xae, 0x63, 0xed, 0xd4, 0x71, 0x7a, 0x40, 0x6d, 0x58, 0x1a, 0xb0, 0x40, 0x51,
	0x21, 0xdb, 0xf3, 0xda, 0x9e, 0x1d, 0xd1, 0x33, 0x58, 0x92, 0x5c, 0x28, 0xb7, 0x3f, 0x69, 0x2f,
	0xe8, 0x7b, 0x6d, 0x38, 0xc5, 0x6d, 0x71, 0xce, 0xb9, 0x50, 0x78, 0x31, 0x01, 0xed, 0x4f, 0xd0,
	0x0e, 0xb4, 0xe2, 0x90, 0x5d, 0xc5, 0xd4, 0x8d, 0x88, 0xa0, 0xa1, 0x4a, 0xea, 0x59, 0xd4, 0x8c,
	0xcd, 0xd4, 0x7e, 0xa6, 0xcd, 0xc7, 0xbe, 0xfd, 0x97, 0x05, 0xdb, 0x85, 0xde, 0xbc, 0xe0, 0xe2,
	0x15, 0x91, 0xa3, 0xd9, 0x16, 0x61, 0x58, 0x57, 0x44, 0x8e, 0xaa, 0xda, 0x53, 0x1e, 0x43, 0x12,
	0x5a, 0xd5, 0x9a, 0x35, 0x55, 0x74, 0xfc, 0x27, 0x6d, 0xb1, 0xff, 0xb4, 0x60, 0xb5, 0x50, 0xec,
	0x9b, 0xae, 0x14, 0xda, 0x82, 0x3a, 0x0b, 0xa3, 0x58, 0xb9, 0xb1, 0x60, 0xba, 0x84, 0x3a, 0x5e,
	0xd6, 0x86, 0x0b, 0xc1, 0xd0, 0x97, 0xb0, 0xe4, 0x05, 0x5c, 0xc6, 0x82, 0xea, 0x3a, 0x1a, 0xbd,
	0xa7, 0xe5, 0x5b, 0x15, 0xa8, 0x0f, 0x52, 0x2c, 0xce, 0x82, 0xd0, 0x1e, 0x2c, 0x8f, 0xa9, 0x22,
	0x3e, 0x51, 0x44, 0x17, 0xdc, 0xe8, 0xbd, 0x73, 0x2b, 0xc1, 0x29, 0x55, 0xe4, 0x90, 0x28, 0x82,
	0xf3, 0x30, 0xfb, 0x57, 0x0b, 0xee, 0x57, 0x62, 0xd0, 0x36, 0x34, 0x04, 0x55, 0x62, 0xe2, 0x0e,
	0x05, 0x8f, 0x23, 0x5d, 0x7a, 0x1d, 0x83, 0x36, 0xbd, 0x4c, 0x2c, 0xe8, 0x29, 0x34, 0x99, 0xcc,
	0xf6, 0x26, 0x11, 0x2a, 0x5d, 0xdf, 0x32, 0x5e, 0x61, 0x32, 0xdd, 0x9a, 0x84, 0x17, 0x75, 0x60,
	0x45, 0x46, 0xd4, 0xd3, 0x80, 0x64, 0x1d, 0xd2, 0x81, 0x41, 0x62, 0x4b, 0xfc, 0xc7, 0xbe, 0x7d,
	0x05, 0xeb, 0x37, 0x3e, 0x3a, 0xf4, 0x02, 0xd6, 0x8a, 0xda, 0x27, 0xdb, 0x56, 0x67, 0x6e, 0xa7,
	0xd1, 0x7b, 0x7c, 0x6b, 0x85, 0xb8, 0x19, 0xce, 0x1e, 0xe5, 0x74, 0x51, 0x6a, 0x33, 0x8b, 0x62,
	0xff, 0x31, 0x0f, 0x1b, 0x55, 0xad, 0x45, 0xdb, 0x00, 0x3c, 0x56, 0xd9, 0xbc, 0x74, 0xcd, 0x47,
	0xf7, 0x70, 0x3d, 0xb5, 0x25, 0x23, 0xdb, 0x85, 0x05, 0x2a, 0x04, 0x17, 0x9a, 0xaf, 0x70, 0x1b,
	0xbd, 0x0a, 0x39, 0xe1, 0xf3, 0x04, 0x74, 0x74, 0x0f, 0xa7, 0x68, 0xf4, 0x29, 0x2c, 0x44, 0x97,
	0x44, 0xa6, 0x73, 0x6e, 0xf6, 0xec, 0xdb, 0x36, 0xc8, 0x39, 0x4b, 0x90, 0x38, 0x0d, 0x40, 0x9f,
	0x01, 0x48, 0x45, 0x84, 0xa2, 0xbe, 0x4b, 0x94, 0x99, 0xf2, 0xa6, 0x93, 0x6a, 0xa3, 0x93, 0x69,
	0xa3, 0xf3, 0x2a, 0x13, 0x4f, 0x5c, 0x37, 0xe8, 0x3d, 0x85, 0x76, 0x61, 0x39, 0xd3, 0x4c, 0xb3,
	0xf5, 0x0f, 0x6f, 0x04, 0x1e, 0x1a, 0x00, 0xce, 0xa1, 0x49, 0x46, 0x4f, 0x50, 0x62, 0x32, 0x2e,
	0xde, 0x9d, 0xd1, 0xa0, 0xf7, 0x54, 0x12, 0x1a, 0x47, 0x7e, 0x16, 0xba, 0x74, 0x77, 0xa8, 0x41,
	0xef, 0x29, 0xf4, 0x13, 0xfc, 0x3f, 0x97, 0x57, 0x3d, 0xf9, 0x7c, 0xb3, 0x97, 0xab, 0x3f, 0x8d,
	0x4c, 0x60, 0x93, 0xde, 0x9d, 0x1a, 0xec, 0x91, 0x85, 0x37, 0xae, 0x2b, 0xec, 0xe8, 0x0c, 0x90,
	0x56, 0xa6, 0x22, 0x73, 0x5d, 0x33, 0x77, 0xca, 0xcc, 0x89, 0x36, 0x95, 0x58, 0x5b, 0xaa, 0x64,
	0xdb, 0x5f, 0x83, 0x55, 0xb3, 0x29, 0x82, 0xca, 0x38, 0x50, 0xfb, 0xeb, 0xb0, 0xa6, 0x88, 0x18,
	0x52, 0x95, 0xf3, 0xdb, 0x3e, 0x6c, 0x54, 0xdd, 0x12, 0x9d, 0x40, 0x83, 0x4e, 0xf5, 0xe2, 0x0d,
	0x7e, 0x20, 0xb3, 0xe1, 0xf6, 0x6b, 0x0b, 0x5a, 0xe5, 0x2b, 0xa3, 0x43, 0x58, 0xf1, 0x88, 0x77,
	0x49, 0x5d, 0xa9, 0x88, 0x8a, 0xa5, 0xce, 0xd1, 0xec, 0xbd, 0x55, 0xca, 0x71, 0x90, 0xfe, 0xee,
	0x0f, 0x12, 0xe4, 0xb9, 0x06, 0xe2, 0x86, 0x37, 0x3d, 0xa0, 0xaf, 0xa0, 0x61, 0x5e, 0x04, 0xee,
	0x88, 0x4e, 0xcc, 0xce, 0x3f, 0xa9, 0x26, 0xc9, 0x52, 0x63, 0x30, 0x21, 0x5f, 0xd3, 0x89, 0xfd,
	0x9b, 0x05, 0x5b, 0x87, 0x93, 0x90, 0x8c, 0x99, 0x57, 0xd9, 0x89, 0xf7, 0x66, 0x64, 0xf5, 0x61,
	0x89, 0xb7, 0xa4, 0xa4, 0xe7, 0xb0, 0x6e, 0x1e, 0x20, 0xbe, 0x9b, 0xcd, 0xd8, 0xdc, 0xa8, 0x2c,
	0xc8, 0x07, 0x06, 0x97, 0xa5, 0xcc, 0x84, 0xb3, 0xe5, 0x95, 0x1c, 0xf6, 0x05, 0x6c, 0x95, 0x1f,
	0x11, 0x5a, 0x20, 0xff, 0xe5, 0x43, 0xe2, 0xf7, 0x1a, 0x3c, 0xaa, 0xe6, 0x95, 0x11, 0x0f, 0x25,
	0x45, 0x5d, 0x58, 0xd4, 0x7f, 0x01, 0x69, 0xc8, 0x1f, 0x94, 0x77, 0xf0, 0x42, 0x04, 0xfb, 0x01,
	0xef, 0x63, 0x03, 0x43, 0x1f, 0xc2, 0x52, 0xba, 0x6e, 0xd2, 0xd4, 0xfc, 0x8f, 0x11, 0x19, 0x0e,
	0x7d, 0x0e, 0x8d, 0x41, 0x1c, 0x04, 0xae, 0x49, 0x34, 0x57, 0xd9, 0xe4, 0x93, 0xf4, 0x55, 0x76,
	0x4a, 0x22, 0x0c, 0x09, 0xfa, 0x38, 0x4d, 0xf7, 0x05, 0xac, 0xe8, 0xd8, 0x2c, 0xe7, 0xfc, 0x5d,
	0xc1, 0x3a, 0xd5, 0xb7, 0x26, 0xf3, 0xf7, 0xd0, 0xf2, 0xd3, 0xa1, 0x4f, 0x27, 0xd5, 0xd2, 0x0c,
	0x1f, 0x94, 0x6f, 0x7d, 0xcb, 0x72, 0xe0, 0x35, 0xbf, 0xe8, 0xdc, 0xff, 0xe4, 0xc7, 0xdd, 0x21,
	0x53, 0x97, 0x71, 0xdf, 0xf1, 0xf8, 0xb8, 0xab, 0x99, 0xb8, 0x18, 0x76, 0xf3, 0x77, 0xe6, 0x90,
	0x86, 0xdd, 0xa8, 0xff, 0x6c, 0xc8, 0xbb, 0xc5, 0x17, 0x71, 0x7f, 0x51, 0x6b, 0xcf, 0x47, 0x7f,
	0x07, 0x00, 0x00, 0xff, 0xff, 0x54, 0x65, 0xd1, 0xc2, 0x5f, 0x0b, 0x00, 0x00,
}
