# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flyteidl/plugins/sagemaker/training_job.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='flyteidl/plugins/sagemaker/training_job.proto',
  package='flyteidl.plugins.sagemaker',
  syntax='proto3',
  serialized_options=_b('Z3github.com/lyft/flyteidl/gen/pb-go/flyteidl/plugins'),
  serialized_pb=_b('\n-flyteidl/plugins/sagemaker/training_job.proto\x12\x1a\x66lyteidl.plugins.sagemaker\x1a\x1egoogle/protobuf/duration.proto\"(\n\tInputMode\"\x1b\n\x05Value\x12\x08\n\x04\x46ILE\x10\x00\x12\x08\n\x04PIPE\x10\x01\"1\n\rAlgorithmName\" \n\x05Value\x12\n\n\x06\x43USTOM\x10\x00\x12\x0b\n\x07XGBOOST\x10\x01\"7\n\rInputFileType\"&\n\x05Value\x12\x0c\n\x08TEXT_CSV\x10\x00\x12\x0f\n\x0bTEXT_LIBSVM\x10\x01\"/\n\x10MetricDefinition\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05regex\x18\x02 \x01(\t\"\xd1\x02\n\x16\x41lgorithmSpecification\x12?\n\ninput_mode\x18\x01 \x01(\x0e\x32+.flyteidl.plugins.sagemaker.InputMode.Value\x12G\n\x0e\x61lgorithm_name\x18\x02 \x01(\x0e\x32/.flyteidl.plugins.sagemaker.AlgorithmName.Value\x12\x19\n\x11\x61lgorithm_version\x18\x03 \x01(\t\x12H\n\x12metric_definitions\x18\x04 \x03(\x0b\x32,.flyteidl.plugins.sagemaker.MetricDefinition\x12H\n\x0finput_file_type\x18\x05 \x01(\x0e\x32/.flyteidl.plugins.sagemaker.InputFileType.Value\"e\n\x19TrainingJobResourceConfig\x12\x16\n\x0einstance_count\x18\x01 \x01(\x03\x12\x15\n\rinstance_type\x18\x02 \x01(\t\x12\x19\n\x11volume_size_in_gb\x18\x03 \x01(\x03\"\xbf\x01\n\x0bTrainingJob\x12S\n\x17\x61lgorithm_specification\x18\x01 \x01(\x0b\x32\x32.flyteidl.plugins.sagemaker.AlgorithmSpecification\x12[\n\x1ctraining_job_resource_config\x18\x02 \x01(\x0b\x32\x35.flyteidl.plugins.sagemaker.TrainingJobResourceConfigB5Z3github.com/lyft/flyteidl/gen/pb-go/flyteidl/pluginsb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,])



_INPUTMODE_VALUE = _descriptor.EnumDescriptor(
  name='Value',
  full_name='flyteidl.plugins.sagemaker.InputMode.Value',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FILE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PIPE', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=122,
  serialized_end=149,
)
_sym_db.RegisterEnumDescriptor(_INPUTMODE_VALUE)

_ALGORITHMNAME_VALUE = _descriptor.EnumDescriptor(
  name='Value',
  full_name='flyteidl.plugins.sagemaker.AlgorithmName.Value',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CUSTOM', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='XGBOOST', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=168,
  serialized_end=200,
)
_sym_db.RegisterEnumDescriptor(_ALGORITHMNAME_VALUE)

_INPUTFILETYPE_VALUE = _descriptor.EnumDescriptor(
  name='Value',
  full_name='flyteidl.plugins.sagemaker.InputFileType.Value',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TEXT_CSV', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEXT_LIBSVM', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=219,
  serialized_end=257,
)
_sym_db.RegisterEnumDescriptor(_INPUTFILETYPE_VALUE)


_INPUTMODE = _descriptor.Descriptor(
  name='InputMode',
  full_name='flyteidl.plugins.sagemaker.InputMode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _INPUTMODE_VALUE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=109,
  serialized_end=149,
)


_ALGORITHMNAME = _descriptor.Descriptor(
  name='AlgorithmName',
  full_name='flyteidl.plugins.sagemaker.AlgorithmName',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ALGORITHMNAME_VALUE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=151,
  serialized_end=200,
)


_INPUTFILETYPE = _descriptor.Descriptor(
  name='InputFileType',
  full_name='flyteidl.plugins.sagemaker.InputFileType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _INPUTFILETYPE_VALUE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=202,
  serialized_end=257,
)


_METRICDEFINITION = _descriptor.Descriptor(
  name='MetricDefinition',
  full_name='flyteidl.plugins.sagemaker.MetricDefinition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='flyteidl.plugins.sagemaker.MetricDefinition.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='regex', full_name='flyteidl.plugins.sagemaker.MetricDefinition.regex', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=259,
  serialized_end=306,
)


_ALGORITHMSPECIFICATION = _descriptor.Descriptor(
  name='AlgorithmSpecification',
  full_name='flyteidl.plugins.sagemaker.AlgorithmSpecification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='input_mode', full_name='flyteidl.plugins.sagemaker.AlgorithmSpecification.input_mode', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='algorithm_name', full_name='flyteidl.plugins.sagemaker.AlgorithmSpecification.algorithm_name', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='algorithm_version', full_name='flyteidl.plugins.sagemaker.AlgorithmSpecification.algorithm_version', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metric_definitions', full_name='flyteidl.plugins.sagemaker.AlgorithmSpecification.metric_definitions', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='input_file_type', full_name='flyteidl.plugins.sagemaker.AlgorithmSpecification.input_file_type', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=309,
  serialized_end=646,
)


_TRAININGJOBRESOURCECONFIG = _descriptor.Descriptor(
  name='TrainingJobResourceConfig',
  full_name='flyteidl.plugins.sagemaker.TrainingJobResourceConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance_count', full_name='flyteidl.plugins.sagemaker.TrainingJobResourceConfig.instance_count', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instance_type', full_name='flyteidl.plugins.sagemaker.TrainingJobResourceConfig.instance_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='volume_size_in_gb', full_name='flyteidl.plugins.sagemaker.TrainingJobResourceConfig.volume_size_in_gb', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=648,
  serialized_end=749,
)


_TRAININGJOB = _descriptor.Descriptor(
  name='TrainingJob',
  full_name='flyteidl.plugins.sagemaker.TrainingJob',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='algorithm_specification', full_name='flyteidl.plugins.sagemaker.TrainingJob.algorithm_specification', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='training_job_resource_config', full_name='flyteidl.plugins.sagemaker.TrainingJob.training_job_resource_config', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=752,
  serialized_end=943,
)

_INPUTMODE_VALUE.containing_type = _INPUTMODE
_ALGORITHMNAME_VALUE.containing_type = _ALGORITHMNAME
_INPUTFILETYPE_VALUE.containing_type = _INPUTFILETYPE
_ALGORITHMSPECIFICATION.fields_by_name['input_mode'].enum_type = _INPUTMODE_VALUE
_ALGORITHMSPECIFICATION.fields_by_name['algorithm_name'].enum_type = _ALGORITHMNAME_VALUE
_ALGORITHMSPECIFICATION.fields_by_name['metric_definitions'].message_type = _METRICDEFINITION
_ALGORITHMSPECIFICATION.fields_by_name['input_file_type'].enum_type = _INPUTFILETYPE_VALUE
_TRAININGJOB.fields_by_name['algorithm_specification'].message_type = _ALGORITHMSPECIFICATION
_TRAININGJOB.fields_by_name['training_job_resource_config'].message_type = _TRAININGJOBRESOURCECONFIG
DESCRIPTOR.message_types_by_name['InputMode'] = _INPUTMODE
DESCRIPTOR.message_types_by_name['AlgorithmName'] = _ALGORITHMNAME
DESCRIPTOR.message_types_by_name['InputFileType'] = _INPUTFILETYPE
DESCRIPTOR.message_types_by_name['MetricDefinition'] = _METRICDEFINITION
DESCRIPTOR.message_types_by_name['AlgorithmSpecification'] = _ALGORITHMSPECIFICATION
DESCRIPTOR.message_types_by_name['TrainingJobResourceConfig'] = _TRAININGJOBRESOURCECONFIG
DESCRIPTOR.message_types_by_name['TrainingJob'] = _TRAININGJOB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InputMode = _reflection.GeneratedProtocolMessageType('InputMode', (_message.Message,), dict(
  DESCRIPTOR = _INPUTMODE,
  __module__ = 'flyteidl.plugins.sagemaker.training_job_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.plugins.sagemaker.InputMode)
  ))
_sym_db.RegisterMessage(InputMode)

AlgorithmName = _reflection.GeneratedProtocolMessageType('AlgorithmName', (_message.Message,), dict(
  DESCRIPTOR = _ALGORITHMNAME,
  __module__ = 'flyteidl.plugins.sagemaker.training_job_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.plugins.sagemaker.AlgorithmName)
  ))
_sym_db.RegisterMessage(AlgorithmName)

InputFileType = _reflection.GeneratedProtocolMessageType('InputFileType', (_message.Message,), dict(
  DESCRIPTOR = _INPUTFILETYPE,
  __module__ = 'flyteidl.plugins.sagemaker.training_job_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.plugins.sagemaker.InputFileType)
  ))
_sym_db.RegisterMessage(InputFileType)

MetricDefinition = _reflection.GeneratedProtocolMessageType('MetricDefinition', (_message.Message,), dict(
  DESCRIPTOR = _METRICDEFINITION,
  __module__ = 'flyteidl.plugins.sagemaker.training_job_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.plugins.sagemaker.MetricDefinition)
  ))
_sym_db.RegisterMessage(MetricDefinition)

AlgorithmSpecification = _reflection.GeneratedProtocolMessageType('AlgorithmSpecification', (_message.Message,), dict(
  DESCRIPTOR = _ALGORITHMSPECIFICATION,
  __module__ = 'flyteidl.plugins.sagemaker.training_job_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.plugins.sagemaker.AlgorithmSpecification)
  ))
_sym_db.RegisterMessage(AlgorithmSpecification)

TrainingJobResourceConfig = _reflection.GeneratedProtocolMessageType('TrainingJobResourceConfig', (_message.Message,), dict(
  DESCRIPTOR = _TRAININGJOBRESOURCECONFIG,
  __module__ = 'flyteidl.plugins.sagemaker.training_job_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.plugins.sagemaker.TrainingJobResourceConfig)
  ))
_sym_db.RegisterMessage(TrainingJobResourceConfig)

TrainingJob = _reflection.GeneratedProtocolMessageType('TrainingJob', (_message.Message,), dict(
  DESCRIPTOR = _TRAININGJOB,
  __module__ = 'flyteidl.plugins.sagemaker.training_job_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.plugins.sagemaker.TrainingJob)
  ))
_sym_db.RegisterMessage(TrainingJob)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
