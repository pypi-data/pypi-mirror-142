# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/modules/face_geometry/protos/environment.proto

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
  name='mediapipe/modules/face_geometry/protos/environment.proto',
  package='mediapipe.face_geometry',
  syntax='proto2',
  serialized_options=_b('\n)com.google.mediapipe.modules.facegeometryB\020EnvironmentProto'),
  serialized_pb=_b('\n8mediapipe/modules/face_geometry/protos/environment.proto\x12\x17mediapipe.face_geometry\"L\n\x11PerspectiveCamera\x12\x1c\n\x14vertical_fov_degrees\x18\x01 \x01(\x02\x12\x0c\n\x04near\x18\x02 \x01(\x02\x12\x0b\n\x03\x66\x61r\x18\x03 \x01(\x02\"\xa2\x01\n\x0b\x45nvironment\x12K\n\x15origin_point_location\x18\x01 \x01(\x0e\x32,.mediapipe.face_geometry.OriginPointLocation\x12\x46\n\x12perspective_camera\x18\x02 \x01(\x0b\x32*.mediapipe.face_geometry.PerspectiveCamera*B\n\x13OriginPointLocation\x12\x16\n\x12\x42OTTOM_LEFT_CORNER\x10\x01\x12\x13\n\x0fTOP_LEFT_CORNER\x10\x02\x42=\n)com.google.mediapipe.modules.facegeometryB\x10\x45nvironmentProto')
)

_ORIGINPOINTLOCATION = _descriptor.EnumDescriptor(
  name='OriginPointLocation',
  full_name='mediapipe.face_geometry.OriginPointLocation',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BOTTOM_LEFT_CORNER', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TOP_LEFT_CORNER', index=1, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=328,
  serialized_end=394,
)
_sym_db.RegisterEnumDescriptor(_ORIGINPOINTLOCATION)

OriginPointLocation = enum_type_wrapper.EnumTypeWrapper(_ORIGINPOINTLOCATION)
BOTTOM_LEFT_CORNER = 1
TOP_LEFT_CORNER = 2



_PERSPECTIVECAMERA = _descriptor.Descriptor(
  name='PerspectiveCamera',
  full_name='mediapipe.face_geometry.PerspectiveCamera',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vertical_fov_degrees', full_name='mediapipe.face_geometry.PerspectiveCamera.vertical_fov_degrees', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='near', full_name='mediapipe.face_geometry.PerspectiveCamera.near', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='far', full_name='mediapipe.face_geometry.PerspectiveCamera.far', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=85,
  serialized_end=161,
)


_ENVIRONMENT = _descriptor.Descriptor(
  name='Environment',
  full_name='mediapipe.face_geometry.Environment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='origin_point_location', full_name='mediapipe.face_geometry.Environment.origin_point_location', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='perspective_camera', full_name='mediapipe.face_geometry.Environment.perspective_camera', index=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=164,
  serialized_end=326,
)

_ENVIRONMENT.fields_by_name['origin_point_location'].enum_type = _ORIGINPOINTLOCATION
_ENVIRONMENT.fields_by_name['perspective_camera'].message_type = _PERSPECTIVECAMERA
DESCRIPTOR.message_types_by_name['PerspectiveCamera'] = _PERSPECTIVECAMERA
DESCRIPTOR.message_types_by_name['Environment'] = _ENVIRONMENT
DESCRIPTOR.enum_types_by_name['OriginPointLocation'] = _ORIGINPOINTLOCATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PerspectiveCamera = _reflection.GeneratedProtocolMessageType('PerspectiveCamera', (_message.Message,), dict(
  DESCRIPTOR = _PERSPECTIVECAMERA,
  __module__ = 'mediapipe.modules.face_geometry.protos.environment_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.face_geometry.PerspectiveCamera)
  ))
_sym_db.RegisterMessage(PerspectiveCamera)

Environment = _reflection.GeneratedProtocolMessageType('Environment', (_message.Message,), dict(
  DESCRIPTOR = _ENVIRONMENT,
  __module__ = 'mediapipe.modules.face_geometry.protos.environment_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.face_geometry.Environment)
  ))
_sym_db.RegisterMessage(Environment)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
