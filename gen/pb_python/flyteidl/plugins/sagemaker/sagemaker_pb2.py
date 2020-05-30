# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flyteidl/plugins/sagemaker/sagemaker.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='flyteidl/plugins/sagemaker/sagemaker.proto',
  package='flyteidl.plugins.sagemaker',
  syntax='proto3',
  serialized_options=_b('Z3github.com/lyft/flyteidl/gen/pb-go/flyteidl/plugins'),
  serialized_pb=_b('\n*flyteidl/plugins/sagemaker/sagemaker.proto\x12\x1a\x66lyteidl.plugins.sagemaker\"\x98\x01\n\x18\x43ontinuousParameterRange\x12\x0c\n\x04Name\x18\x01 \x01(\t\x12\x10\n\x08MaxValue\x18\x02 \x01(\x01\x12\x10\n\x08MinValue\x18\x03 \x01(\x01\x12J\n\x0bScalingType\x18\x04 \x01(\x0e\x32\x35.flyteidl.plugins.sagemaker.HyperparameterScalingType\"\x95\x01\n\x15IntegerParameterRange\x12\x0c\n\x04Name\x18\x01 \x01(\t\x12\x10\n\x08MaxValue\x18\x02 \x01(\x02\x12\x10\n\x08MinValue\x18\x03 \x01(\x02\x12J\n\x0bScalingType\x18\x04 \x01(\x0e\x32\x35.flyteidl.plugins.sagemaker.HyperparameterScalingType\"9\n\x19\x43\x61tegoricalParameterRange\x12\x0c\n\x04Name\x18\x01 \x01(\t\x12\x0e\n\x06Values\x18\x02 \x03(\t\"\x98\x02\n\x0fParameterRanges\x12W\n\x19\x43ontinuousParameterRanges\x18\x01 \x03(\x0b\x32\x34.flyteidl.plugins.sagemaker.ContinuousParameterRange\x12Q\n\x16IntegerParameterRanges\x18\x02 \x03(\x0b\x32\x31.flyteidl.plugins.sagemaker.IntegerParameterRange\x12Y\n\x1a\x43\x61tegoricalParameterRanges\x18\x03 \x03(\x0b\x32\x35.flyteidl.plugins.sagemaker.CategoricalParameterRange\"\xf2\x01\n\x16\x41lgorithmSpecification\x12\x15\n\rTrainingImage\x18\x01 \x01(\t\x12\x19\n\x11TrainingInputMode\x18\x02 \x01(\t\x12\x15\n\rAlgorithmName\x18\x03 \x01(\t\x12^\n\x11MetricDefinitions\x18\x04 \x03(\x0b\x32\x43.flyteidl.plugins.sagemaker.AlgorithmSpecification.MetricDefinition\x1a/\n\x10MetricDefinition\x12\x0c\n\x04Name\x18\x01 \x01(\t\x12\r\n\x05Regex\x18\x02 \x01(\t\"m\n\x0eResourceConfig\x12\x14\n\x0cInstanceType\x18\x01 \x01(\t\x12\x15\n\rInstanceCount\x18\x02 \x01(\x03\x12\x16\n\x0eVolumeSizeInGB\x18\x03 \x01(\x03\x12\x16\n\x0eVolumeKmsKeyId\x18\x04 \x01(\t\"N\n\x11StoppingCondition\x12\x1b\n\x13MaxRuntimeInSeconds\x18\x01 \x01(\x03\x12\x1c\n\x14MaxWaitTimeInSeconds\x18\x02 \x01(\x03\"6\n\tVpcConfig\x12\x18\n\x10SecurityGroupIds\x18\x01 \x03(\t\x12\x0f\n\x07Subnets\x18\x02 \x03(\t\"\xef\x02\n\x14SagemakerTrainingJob\x12\x0e\n\x06Region\x18\x01 \x01(\t\x12\x0f\n\x07RoleArn\x18\x02 \x01(\t\x12R\n\x16\x41lgorithmSpecification\x18\x03 \x01(\x0b\x32\x32.flyteidl.plugins.sagemaker.AlgorithmSpecification\x12\x42\n\x0eResourceConfig\x18\x04 \x01(\x0b\x32*.flyteidl.plugins.sagemaker.ResourceConfig\x12H\n\x11StoppingCondition\x18\x05 \x01(\x0b\x32-.flyteidl.plugins.sagemaker.StoppingCondition\x12\x38\n\tVpcConfig\x18\x06 \x01(\x0b\x32%.flyteidl.plugins.sagemaker.VpcConfig\x12\x1a\n\x12\x45nableSpotTraining\x18\x07 \x01(\x08\"\xa7\x01\n\x0fHPOJobObjective\x12M\n\x04Type\x18\x01 \x01(\x0e\x32?.flyteidl.plugins.sagemaker.HPOJobObjective.HPOJobObjectiveType\x12\x12\n\nMetricName\x18\x02 \x01(\t\"1\n\x13HPOJobObjectiveType\x12\x0c\n\x08MINIMIZE\x10\x00\x12\x0c\n\x08MAXIMIZE\x10\x01\"\xb2\x02\n\x0fSagemakerHPOJob\x12\x10\n\x08Strategy\x18\x01 \x01(\t\x12>\n\tObjective\x18\x02 \x01(\x0b\x32+.flyteidl.plugins.sagemaker.HPOJobObjective\x12\x1f\n\x17MaxNumberOfTrainingJobs\x18\x03 \x01(\x03\x12\x1f\n\x17MaxParallelTrainingJobs\x18\x04 \x01(\x03\x12\x44\n\x0fParameterRanges\x18\x05 \x01(\x0b\x32+.flyteidl.plugins.sagemaker.ParameterRanges\x12\x45\n\x0bTrainingJob\x18\x06 \x01(\x0b\x32\x30.flyteidl.plugins.sagemaker.SagemakerTrainingJob*Z\n\x19HyperparameterScalingType\x12\x08\n\x04\x41UTO\x10\x00\x12\n\n\x06LINEAR\x10\x01\x12\x0f\n\x0bLOGARITHMIC\x10\x02\x12\x16\n\x12REVERSELOGARITHMIC\x10\x03\x42\x35Z3github.com/lyft/flyteidl/gen/pb-go/flyteidl/pluginsb\x06proto3')
)

_HYPERPARAMETERSCALINGTYPE = _descriptor.EnumDescriptor(
  name='HyperparameterScalingType',
  full_name='flyteidl.plugins.sagemaker.HyperparameterScalingType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='AUTO', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LINEAR', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOGARITHMIC', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REVERSELOGARITHMIC', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2064,
  serialized_end=2154,
)
_sym_db.RegisterEnumDescriptor(_HYPERPARAMETERSCALINGTYPE)

HyperparameterScalingType = enum_type_wrapper.EnumTypeWrapper(_HYPERPARAMETERSCALINGTYPE)
AUTO = 0
LINEAR = 1
LOGARITHMIC = 2
REVERSELOGARITHMIC = 3


_HPOJOBOBJECTIVE_HPOJOBOBJECTIVETYPE = _descriptor.EnumDescriptor(
  name='HPOJobObjectiveType',
  full_name='flyteidl.plugins.sagemaker.HPOJobObjective.HPOJobObjectiveType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MINIMIZE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAXIMIZE', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1704,
  serialized_end=1753,
)
_sym_db.RegisterEnumDescriptor(_HPOJOBOBJECTIVE_HPOJOBOBJECTIVETYPE)


_CONTINUOUSPARAMETERRANGE = _descriptor.Descriptor(
  name='ContinuousParameterRange',
  full_name='flyteidl.plugins.sagemaker.ContinuousParameterRange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Name', full_name='flyteidl.plugins.sagemaker.ContinuousParameterRange.Name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='MaxValue', full_name='flyteidl.plugins.sagemaker.ContinuousParameterRange.MaxValue', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='MinValue', full_name='flyteidl.plugins.sagemaker.ContinuousParameterRange.MinValue', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ScalingType', full_name='flyteidl.plugins.sagemaker.ContinuousParameterRange.ScalingType', index=3,
      number=4, type=14, cpp_type=8, label=1,
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
  serialized_start=75,
  serialized_end=227,
)


_INTEGERPARAMETERRANGE = _descriptor.Descriptor(
  name='IntegerParameterRange',
  full_name='flyteidl.plugins.sagemaker.IntegerParameterRange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Name', full_name='flyteidl.plugins.sagemaker.IntegerParameterRange.Name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='MaxValue', full_name='flyteidl.plugins.sagemaker.IntegerParameterRange.MaxValue', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='MinValue', full_name='flyteidl.plugins.sagemaker.IntegerParameterRange.MinValue', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ScalingType', full_name='flyteidl.plugins.sagemaker.IntegerParameterRange.ScalingType', index=3,
      number=4, type=14, cpp_type=8, label=1,
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
  serialized_start=230,
  serialized_end=379,
)


_CATEGORICALPARAMETERRANGE = _descriptor.Descriptor(
  name='CategoricalParameterRange',
  full_name='flyteidl.plugins.sagemaker.CategoricalParameterRange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Name', full_name='flyteidl.plugins.sagemaker.CategoricalParameterRange.Name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Values', full_name='flyteidl.plugins.sagemaker.CategoricalParameterRange.Values', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=381,
  serialized_end=438,
)


_PARAMETERRANGES = _descriptor.Descriptor(
  name='ParameterRanges',
  full_name='flyteidl.plugins.sagemaker.ParameterRanges',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ContinuousParameterRanges', full_name='flyteidl.plugins.sagemaker.ParameterRanges.ContinuousParameterRanges', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='IntegerParameterRanges', full_name='flyteidl.plugins.sagemaker.ParameterRanges.IntegerParameterRanges', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='CategoricalParameterRanges', full_name='flyteidl.plugins.sagemaker.ParameterRanges.CategoricalParameterRanges', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=441,
  serialized_end=721,
)


_ALGORITHMSPECIFICATION_METRICDEFINITION = _descriptor.Descriptor(
  name='MetricDefinition',
  full_name='flyteidl.plugins.sagemaker.AlgorithmSpecification.MetricDefinition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Name', full_name='flyteidl.plugins.sagemaker.AlgorithmSpecification.MetricDefinition.Name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Regex', full_name='flyteidl.plugins.sagemaker.AlgorithmSpecification.MetricDefinition.Regex', index=1,
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
  serialized_start=919,
  serialized_end=966,
)

_ALGORITHMSPECIFICATION = _descriptor.Descriptor(
  name='AlgorithmSpecification',
  full_name='flyteidl.plugins.sagemaker.AlgorithmSpecification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='TrainingImage', full_name='flyteidl.plugins.sagemaker.AlgorithmSpecification.TrainingImage', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='TrainingInputMode', full_name='flyteidl.plugins.sagemaker.AlgorithmSpecification.TrainingInputMode', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='AlgorithmName', full_name='flyteidl.plugins.sagemaker.AlgorithmSpecification.AlgorithmName', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='MetricDefinitions', full_name='flyteidl.plugins.sagemaker.AlgorithmSpecification.MetricDefinitions', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_ALGORITHMSPECIFICATION_METRICDEFINITION, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=724,
  serialized_end=966,
)


_RESOURCECONFIG = _descriptor.Descriptor(
  name='ResourceConfig',
  full_name='flyteidl.plugins.sagemaker.ResourceConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='InstanceType', full_name='flyteidl.plugins.sagemaker.ResourceConfig.InstanceType', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='InstanceCount', full_name='flyteidl.plugins.sagemaker.ResourceConfig.InstanceCount', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='VolumeSizeInGB', full_name='flyteidl.plugins.sagemaker.ResourceConfig.VolumeSizeInGB', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='VolumeKmsKeyId', full_name='flyteidl.plugins.sagemaker.ResourceConfig.VolumeKmsKeyId', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=968,
  serialized_end=1077,
)


_STOPPINGCONDITION = _descriptor.Descriptor(
  name='StoppingCondition',
  full_name='flyteidl.plugins.sagemaker.StoppingCondition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='MaxRuntimeInSeconds', full_name='flyteidl.plugins.sagemaker.StoppingCondition.MaxRuntimeInSeconds', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='MaxWaitTimeInSeconds', full_name='flyteidl.plugins.sagemaker.StoppingCondition.MaxWaitTimeInSeconds', index=1,
      number=2, type=3, cpp_type=2, label=1,
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
  serialized_start=1079,
  serialized_end=1157,
)


_VPCCONFIG = _descriptor.Descriptor(
  name='VpcConfig',
  full_name='flyteidl.plugins.sagemaker.VpcConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='SecurityGroupIds', full_name='flyteidl.plugins.sagemaker.VpcConfig.SecurityGroupIds', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Subnets', full_name='flyteidl.plugins.sagemaker.VpcConfig.Subnets', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1159,
  serialized_end=1213,
)


_SAGEMAKERTRAININGJOB = _descriptor.Descriptor(
  name='SagemakerTrainingJob',
  full_name='flyteidl.plugins.sagemaker.SagemakerTrainingJob',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Region', full_name='flyteidl.plugins.sagemaker.SagemakerTrainingJob.Region', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='RoleArn', full_name='flyteidl.plugins.sagemaker.SagemakerTrainingJob.RoleArn', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='AlgorithmSpecification', full_name='flyteidl.plugins.sagemaker.SagemakerTrainingJob.AlgorithmSpecification', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ResourceConfig', full_name='flyteidl.plugins.sagemaker.SagemakerTrainingJob.ResourceConfig', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='StoppingCondition', full_name='flyteidl.plugins.sagemaker.SagemakerTrainingJob.StoppingCondition', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='VpcConfig', full_name='flyteidl.plugins.sagemaker.SagemakerTrainingJob.VpcConfig', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='EnableSpotTraining', full_name='flyteidl.plugins.sagemaker.SagemakerTrainingJob.EnableSpotTraining', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=1216,
  serialized_end=1583,
)


_HPOJOBOBJECTIVE = _descriptor.Descriptor(
  name='HPOJobObjective',
  full_name='flyteidl.plugins.sagemaker.HPOJobObjective',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Type', full_name='flyteidl.plugins.sagemaker.HPOJobObjective.Type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='MetricName', full_name='flyteidl.plugins.sagemaker.HPOJobObjective.MetricName', index=1,
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
    _HPOJOBOBJECTIVE_HPOJOBOBJECTIVETYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1586,
  serialized_end=1753,
)


_SAGEMAKERHPOJOB = _descriptor.Descriptor(
  name='SagemakerHPOJob',
  full_name='flyteidl.plugins.sagemaker.SagemakerHPOJob',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Strategy', full_name='flyteidl.plugins.sagemaker.SagemakerHPOJob.Strategy', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Objective', full_name='flyteidl.plugins.sagemaker.SagemakerHPOJob.Objective', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='MaxNumberOfTrainingJobs', full_name='flyteidl.plugins.sagemaker.SagemakerHPOJob.MaxNumberOfTrainingJobs', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='MaxParallelTrainingJobs', full_name='flyteidl.plugins.sagemaker.SagemakerHPOJob.MaxParallelTrainingJobs', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ParameterRanges', full_name='flyteidl.plugins.sagemaker.SagemakerHPOJob.ParameterRanges', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='TrainingJob', full_name='flyteidl.plugins.sagemaker.SagemakerHPOJob.TrainingJob', index=5,
      number=6, type=11, cpp_type=10, label=1,
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
  serialized_start=1756,
  serialized_end=2062,
)

_CONTINUOUSPARAMETERRANGE.fields_by_name['ScalingType'].enum_type = _HYPERPARAMETERSCALINGTYPE
_INTEGERPARAMETERRANGE.fields_by_name['ScalingType'].enum_type = _HYPERPARAMETERSCALINGTYPE
_PARAMETERRANGES.fields_by_name['ContinuousParameterRanges'].message_type = _CONTINUOUSPARAMETERRANGE
_PARAMETERRANGES.fields_by_name['IntegerParameterRanges'].message_type = _INTEGERPARAMETERRANGE
_PARAMETERRANGES.fields_by_name['CategoricalParameterRanges'].message_type = _CATEGORICALPARAMETERRANGE
_ALGORITHMSPECIFICATION_METRICDEFINITION.containing_type = _ALGORITHMSPECIFICATION
_ALGORITHMSPECIFICATION.fields_by_name['MetricDefinitions'].message_type = _ALGORITHMSPECIFICATION_METRICDEFINITION
_SAGEMAKERTRAININGJOB.fields_by_name['AlgorithmSpecification'].message_type = _ALGORITHMSPECIFICATION
_SAGEMAKERTRAININGJOB.fields_by_name['ResourceConfig'].message_type = _RESOURCECONFIG
_SAGEMAKERTRAININGJOB.fields_by_name['StoppingCondition'].message_type = _STOPPINGCONDITION
_SAGEMAKERTRAININGJOB.fields_by_name['VpcConfig'].message_type = _VPCCONFIG
_HPOJOBOBJECTIVE.fields_by_name['Type'].enum_type = _HPOJOBOBJECTIVE_HPOJOBOBJECTIVETYPE
_HPOJOBOBJECTIVE_HPOJOBOBJECTIVETYPE.containing_type = _HPOJOBOBJECTIVE
_SAGEMAKERHPOJOB.fields_by_name['Objective'].message_type = _HPOJOBOBJECTIVE
_SAGEMAKERHPOJOB.fields_by_name['ParameterRanges'].message_type = _PARAMETERRANGES
_SAGEMAKERHPOJOB.fields_by_name['TrainingJob'].message_type = _SAGEMAKERTRAININGJOB
DESCRIPTOR.message_types_by_name['ContinuousParameterRange'] = _CONTINUOUSPARAMETERRANGE
DESCRIPTOR.message_types_by_name['IntegerParameterRange'] = _INTEGERPARAMETERRANGE
DESCRIPTOR.message_types_by_name['CategoricalParameterRange'] = _CATEGORICALPARAMETERRANGE
DESCRIPTOR.message_types_by_name['ParameterRanges'] = _PARAMETERRANGES
DESCRIPTOR.message_types_by_name['AlgorithmSpecification'] = _ALGORITHMSPECIFICATION
DESCRIPTOR.message_types_by_name['ResourceConfig'] = _RESOURCECONFIG
DESCRIPTOR.message_types_by_name['StoppingCondition'] = _STOPPINGCONDITION
DESCRIPTOR.message_types_by_name['VpcConfig'] = _VPCCONFIG
DESCRIPTOR.message_types_by_name['SagemakerTrainingJob'] = _SAGEMAKERTRAININGJOB
DESCRIPTOR.message_types_by_name['HPOJobObjective'] = _HPOJOBOBJECTIVE
DESCRIPTOR.message_types_by_name['SagemakerHPOJob'] = _SAGEMAKERHPOJOB
DESCRIPTOR.enum_types_by_name['HyperparameterScalingType'] = _HYPERPARAMETERSCALINGTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ContinuousParameterRange = _reflection.GeneratedProtocolMessageType('ContinuousParameterRange', (_message.Message,), dict(
  DESCRIPTOR = _CONTINUOUSPARAMETERRANGE,
  __module__ = 'flyteidl.plugins.sagemaker.sagemaker_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.plugins.sagemaker.ContinuousParameterRange)
  ))
_sym_db.RegisterMessage(ContinuousParameterRange)

IntegerParameterRange = _reflection.GeneratedProtocolMessageType('IntegerParameterRange', (_message.Message,), dict(
  DESCRIPTOR = _INTEGERPARAMETERRANGE,
  __module__ = 'flyteidl.plugins.sagemaker.sagemaker_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.plugins.sagemaker.IntegerParameterRange)
  ))
_sym_db.RegisterMessage(IntegerParameterRange)

CategoricalParameterRange = _reflection.GeneratedProtocolMessageType('CategoricalParameterRange', (_message.Message,), dict(
  DESCRIPTOR = _CATEGORICALPARAMETERRANGE,
  __module__ = 'flyteidl.plugins.sagemaker.sagemaker_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.plugins.sagemaker.CategoricalParameterRange)
  ))
_sym_db.RegisterMessage(CategoricalParameterRange)

ParameterRanges = _reflection.GeneratedProtocolMessageType('ParameterRanges', (_message.Message,), dict(
  DESCRIPTOR = _PARAMETERRANGES,
  __module__ = 'flyteidl.plugins.sagemaker.sagemaker_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.plugins.sagemaker.ParameterRanges)
  ))
_sym_db.RegisterMessage(ParameterRanges)

AlgorithmSpecification = _reflection.GeneratedProtocolMessageType('AlgorithmSpecification', (_message.Message,), dict(

  MetricDefinition = _reflection.GeneratedProtocolMessageType('MetricDefinition', (_message.Message,), dict(
    DESCRIPTOR = _ALGORITHMSPECIFICATION_METRICDEFINITION,
    __module__ = 'flyteidl.plugins.sagemaker.sagemaker_pb2'
    # @@protoc_insertion_point(class_scope:flyteidl.plugins.sagemaker.AlgorithmSpecification.MetricDefinition)
    ))
  ,
  DESCRIPTOR = _ALGORITHMSPECIFICATION,
  __module__ = 'flyteidl.plugins.sagemaker.sagemaker_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.plugins.sagemaker.AlgorithmSpecification)
  ))
_sym_db.RegisterMessage(AlgorithmSpecification)
_sym_db.RegisterMessage(AlgorithmSpecification.MetricDefinition)

ResourceConfig = _reflection.GeneratedProtocolMessageType('ResourceConfig', (_message.Message,), dict(
  DESCRIPTOR = _RESOURCECONFIG,
  __module__ = 'flyteidl.plugins.sagemaker.sagemaker_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.plugins.sagemaker.ResourceConfig)
  ))
_sym_db.RegisterMessage(ResourceConfig)

StoppingCondition = _reflection.GeneratedProtocolMessageType('StoppingCondition', (_message.Message,), dict(
  DESCRIPTOR = _STOPPINGCONDITION,
  __module__ = 'flyteidl.plugins.sagemaker.sagemaker_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.plugins.sagemaker.StoppingCondition)
  ))
_sym_db.RegisterMessage(StoppingCondition)

VpcConfig = _reflection.GeneratedProtocolMessageType('VpcConfig', (_message.Message,), dict(
  DESCRIPTOR = _VPCCONFIG,
  __module__ = 'flyteidl.plugins.sagemaker.sagemaker_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.plugins.sagemaker.VpcConfig)
  ))
_sym_db.RegisterMessage(VpcConfig)

SagemakerTrainingJob = _reflection.GeneratedProtocolMessageType('SagemakerTrainingJob', (_message.Message,), dict(
  DESCRIPTOR = _SAGEMAKERTRAININGJOB,
  __module__ = 'flyteidl.plugins.sagemaker.sagemaker_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.plugins.sagemaker.SagemakerTrainingJob)
  ))
_sym_db.RegisterMessage(SagemakerTrainingJob)

HPOJobObjective = _reflection.GeneratedProtocolMessageType('HPOJobObjective', (_message.Message,), dict(
  DESCRIPTOR = _HPOJOBOBJECTIVE,
  __module__ = 'flyteidl.plugins.sagemaker.sagemaker_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.plugins.sagemaker.HPOJobObjective)
  ))
_sym_db.RegisterMessage(HPOJobObjective)

SagemakerHPOJob = _reflection.GeneratedProtocolMessageType('SagemakerHPOJob', (_message.Message,), dict(
  DESCRIPTOR = _SAGEMAKERHPOJOB,
  __module__ = 'flyteidl.plugins.sagemaker.sagemaker_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.plugins.sagemaker.SagemakerHPOJob)
  ))
_sym_db.RegisterMessage(SagemakerHPOJob)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
