# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flyteidl/service/dataproxy.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from protoc_gen_swagger.options import annotations_pb2 as protoc__gen__swagger_dot_options_dot_annotations__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='flyteidl/service/dataproxy.proto',
  package='flyteidl.service',
  syntax='proto3',
  serialized_options=_b('Z7github.com/flyteorg/flyteidl/gen/pb-go/flyteidl/service'),
  serialized_pb=_b('\n flyteidl/service/dataproxy.proto\x12\x10\x66lyteidl.service\x1a\x1cgoogle/api/annotations.proto\x1a,protoc-gen-swagger/options/annotations.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"v\n\x1c\x43reateUploadLocationResponse\x12\x12\n\nsigned_url\x18\x01 \x01(\t\x12\x12\n\nnative_url\x18\x02 \x01(\t\x12.\n\nexpires_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x94\x01\n\x1b\x43reateUploadLocationRequest\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\x0e\n\x06\x64omain\x18\x02 \x01(\t\x12\x10\n\x08\x66ilename\x18\x03 \x01(\t\x12-\n\nexpires_in\x18\x04 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x13\n\x0b\x63ontent_md5\x18\x05 \x01(\x0c\x32\x85\x02\n\x10\x44\x61taProxyService\x12\xf0\x01\n\x14\x43reateUploadLocation\x12-.flyteidl.service.CreateUploadLocationRequest\x1a..flyteidl.service.CreateUploadLocationResponse\"y\x82\xd3\xe4\x93\x02#\"\x1e/api/v1/dataproxy/artifact_urn:\x01*\x92\x41M\x1aKCreates a write-only http location that is accessible for tasks at runtime.B9Z7github.com/flyteorg/flyteidl/gen/pb-go/flyteidl/serviceb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,protoc__gen__swagger_dot_options_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_CREATEUPLOADLOCATIONRESPONSE = _descriptor.Descriptor(
  name='CreateUploadLocationResponse',
  full_name='flyteidl.service.CreateUploadLocationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='signed_url', full_name='flyteidl.service.CreateUploadLocationResponse.signed_url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='native_url', full_name='flyteidl.service.CreateUploadLocationResponse.native_url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expires_at', full_name='flyteidl.service.CreateUploadLocationResponse.expires_at', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=195,
  serialized_end=313,
)


_CREATEUPLOADLOCATIONREQUEST = _descriptor.Descriptor(
  name='CreateUploadLocationRequest',
  full_name='flyteidl.service.CreateUploadLocationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='project', full_name='flyteidl.service.CreateUploadLocationRequest.project', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='domain', full_name='flyteidl.service.CreateUploadLocationRequest.domain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filename', full_name='flyteidl.service.CreateUploadLocationRequest.filename', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expires_in', full_name='flyteidl.service.CreateUploadLocationRequest.expires_in', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content_md5', full_name='flyteidl.service.CreateUploadLocationRequest.content_md5', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=316,
  serialized_end=464,
)

_CREATEUPLOADLOCATIONRESPONSE.fields_by_name['expires_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_CREATEUPLOADLOCATIONREQUEST.fields_by_name['expires_in'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
DESCRIPTOR.message_types_by_name['CreateUploadLocationResponse'] = _CREATEUPLOADLOCATIONRESPONSE
DESCRIPTOR.message_types_by_name['CreateUploadLocationRequest'] = _CREATEUPLOADLOCATIONREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateUploadLocationResponse = _reflection.GeneratedProtocolMessageType('CreateUploadLocationResponse', (_message.Message,), dict(
  DESCRIPTOR = _CREATEUPLOADLOCATIONRESPONSE,
  __module__ = 'flyteidl.service.dataproxy_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.service.CreateUploadLocationResponse)
  ))
_sym_db.RegisterMessage(CreateUploadLocationResponse)

CreateUploadLocationRequest = _reflection.GeneratedProtocolMessageType('CreateUploadLocationRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATEUPLOADLOCATIONREQUEST,
  __module__ = 'flyteidl.service.dataproxy_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.service.CreateUploadLocationRequest)
  ))
_sym_db.RegisterMessage(CreateUploadLocationRequest)


DESCRIPTOR._options = None

_DATAPROXYSERVICE = _descriptor.ServiceDescriptor(
  name='DataProxyService',
  full_name='flyteidl.service.DataProxyService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=467,
  serialized_end=728,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateUploadLocation',
    full_name='flyteidl.service.DataProxyService.CreateUploadLocation',
    index=0,
    containing_service=None,
    input_type=_CREATEUPLOADLOCATIONREQUEST,
    output_type=_CREATEUPLOADLOCATIONRESPONSE,
    serialized_options=_b('\202\323\344\223\002#\"\036/api/v1/dataproxy/artifact_urn:\001*\222AM\032KCreates a write-only http location that is accessible for tasks at runtime.'),
  ),
])
_sym_db.RegisterServiceDescriptor(_DATAPROXYSERVICE)

DESCRIPTOR.services_by_name['DataProxyService'] = _DATAPROXYSERVICE

# @@protoc_insertion_point(module_scope)
