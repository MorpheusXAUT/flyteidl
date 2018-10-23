// Code generated by protoc-gen-go. DO NOT EDIT.
// source: flyteidl/plugins/array_job.proto

package plugins // import "github.com/lyft/flyteidl/gen/pb-go/plugins"

import proto "github.com/golang/protobuf/proto"
import fmt "fmt"
import math "math"

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

// This is a compile-time assertion to ensure that this generated file
// is compatible with the proto package it is being compiled against.
// A compilation error at this line likely means your copy of the
// proto package needs to be updated.
const _ = proto.ProtoPackageIsVersion2 // please upgrade the proto package

// Describes a job that can process independent pieces of data concurrently. Multiple copies of the runnable component
// will be executed concurrently.
type ArrayJob struct {
	// Defines the maximum number of instances to bring up concurrently at any given point.
	Slots int64 `protobuf:"varint,1,opt,name=slots,proto3" json:"slots,omitempty"`
	// Defines the number of successful completions needed to mark the job as success. This number should match
	// the size of the input if the job requires processing of all input data.
	Completions int64 `protobuf:"varint,2,opt,name=completions,proto3" json:"completions,omitempty"`
	// An absolute number of the minimum number of successful completions of subtasks. As soon as this criteria is met,
	// the array job will be marked as successful and outputs will be computed.
	MinSuccesses int64 `protobuf:"varint,3,opt,name=min_successes,json=minSuccesses,proto3" json:"min_successes,omitempty"`
	// The location for where the input will be. The usage of this location is engine-dependent.
	// AWS_Batch & K8s_Batch: This location will be passed in to each task in the array job. Each job is responsible for
	// processing only the portion of the input it's meant to based on an environment variable passed into the container
	// . The algorithm for figuring that out is as follows:
	// - Read environment variable: BATCH_JOB_ARRAY_INDEX_VAR_NAME if it exists, this will contain the name of another
	//   environment variable that actually contain the index (e.g. AWS_BATCH_JOB_ARRAY_INDEX for AWS batch).
	// - Read environment variable: BATCH_JOB_ARRAY_INDEX_OFFSET if it exists, this will contain an offset to add to the
	//   index obtained above.
	// - The input location is then: <input_ref>/<final_index>/inputs.pb
	// For example, in AWS_Batch, BATCH_JOB_ARRAY_INDEX_VAR_NAME will be set to AWS_BATCH_JOB_ARRAY_INDEX. The job can
	// then look at AWS_BATCH_JOB_ARRAY_INDEX to know the index of the job (e.g. 5), then let's say BATCH_JOB_ARRAY_INDEX_OFFSET
	// contains the value 2. The final output location is then: <input_ref>/7/inputs.pb
	// P.S for Azure: The execution engine will have to process the input and slice it for each task. It'll then pass an
	// absolute location to each task for where it can find its input.
	InputRef             string   `protobuf:"bytes,4,opt,name=input_ref,json=inputRef,proto3" json:"input_ref,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *ArrayJob) Reset()         { *m = ArrayJob{} }
func (m *ArrayJob) String() string { return proto.CompactTextString(m) }
func (*ArrayJob) ProtoMessage()    {}
func (*ArrayJob) Descriptor() ([]byte, []int) {
	return fileDescriptor_array_job_db93e73db6b41249, []int{0}
}
func (m *ArrayJob) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_ArrayJob.Unmarshal(m, b)
}
func (m *ArrayJob) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_ArrayJob.Marshal(b, m, deterministic)
}
func (dst *ArrayJob) XXX_Merge(src proto.Message) {
	xxx_messageInfo_ArrayJob.Merge(dst, src)
}
func (m *ArrayJob) XXX_Size() int {
	return xxx_messageInfo_ArrayJob.Size(m)
}
func (m *ArrayJob) XXX_DiscardUnknown() {
	xxx_messageInfo_ArrayJob.DiscardUnknown(m)
}

var xxx_messageInfo_ArrayJob proto.InternalMessageInfo

func (m *ArrayJob) GetSlots() int64 {
	if m != nil {
		return m.Slots
	}
	return 0
}

func (m *ArrayJob) GetCompletions() int64 {
	if m != nil {
		return m.Completions
	}
	return 0
}

func (m *ArrayJob) GetMinSuccesses() int64 {
	if m != nil {
		return m.MinSuccesses
	}
	return 0
}

func (m *ArrayJob) GetInputRef() string {
	if m != nil {
		return m.InputRef
	}
	return ""
}

func init() {
	proto.RegisterType((*ArrayJob)(nil), "flyteidl.plugins.ArrayJob")
}

func init() {
	proto.RegisterFile("flyteidl/plugins/array_job.proto", fileDescriptor_array_job_db93e73db6b41249)
}

var fileDescriptor_array_job_db93e73db6b41249 = []byte{
	// 202 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0x4c, 0x8f, 0xb1, 0x4e, 0x04, 0x21,
	0x14, 0x45, 0x83, 0xab, 0x66, 0x17, 0x35, 0x31, 0xc4, 0x82, 0xc4, 0x86, 0x68, 0xb3, 0x31, 0x3a,
	0x14, 0x7e, 0x81, 0x96, 0x96, 0x63, 0x67, 0x33, 0x19, 0x10, 0x10, 0x03, 0x3c, 0xc2, 0x83, 0x62,
	0x7a, 0x3f, 0xdc, 0x88, 0x8e, 0xd9, 0xf2, 0x9e, 0x7b, 0x9a, 0x43, 0x85, 0x0d, 0x4b, 0x35, 0xfe,
	0x3d, 0xc8, 0x1c, 0x9a, 0xf3, 0x09, 0xe5, 0x5c, 0xca, 0xbc, 0x4c, 0x9f, 0xa0, 0x86, 0x5c, 0xa0,
	0x02, 0xbb, 0x5c, 0x8d, 0xe1, 0xcf, 0xb8, 0xf9, 0x22, 0x74, 0xfb, 0xf4, 0x63, 0xbd, 0x80, 0x62,
	0x57, 0xf4, 0x04, 0x03, 0x54, 0xe4, 0x44, 0x90, 0xfd, 0x66, 0xfc, 0x1d, 0x4c, 0xd0, 0x33, 0x0d,
	0x31, 0x07, 0x53, 0x3d, 0x24, 0xe4, 0x47, 0xfd, 0x3b, 0x44, 0xec, 0x96, 0x5e, 0x44, 0x9f, 0x26,
	0x6c, 0x5a, 0x1b, 0x44, 0x83, 0x7c, 0xd3, 0x9d, 0xf3, 0xe8, 0xd3, 0xeb, 0xca, 0xd8, 0x35, 0xdd,
	0xf9, 0x94, 0x5b, 0x9d, 0x8a, 0xb1, 0xfc, 0x58, 0x90, 0xfd, 0x6e, 0xdc, 0x76, 0x30, 0x1a, 0xfb,
	0x7c, 0xff, 0x76, 0xe7, 0x7c, 0xfd, 0x68, 0x6a, 0xd0, 0x10, 0x65, 0x58, 0x6c, 0x95, 0xff, 0x31,
	0xce, 0x24, 0x99, 0xd5, 0x83, 0x83, 0x35, 0x4b, 0x9d, 0xf6, 0x9a, 0xc7, 0xef, 0x00, 0x00, 0x00,
	0xff, 0xff, 0x9d, 0x4a, 0xa2, 0x01, 0xf1, 0x00, 0x00, 0x00,
}