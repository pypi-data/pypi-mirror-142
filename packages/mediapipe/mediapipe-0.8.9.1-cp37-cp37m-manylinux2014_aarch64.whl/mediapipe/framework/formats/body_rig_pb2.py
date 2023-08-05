# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/framework/formats/body_rig.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='mediapipe/framework/formats/body_rig.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n*mediapipe/framework/formats/body_rig.proto\x12\tmediapipe\"0\n\x05Joint\x12\x13\n\x0brotation_6d\x18\x01 \x03(\x02\x12\x12\n\nvisibility\x18\x02 \x01(\x02\",\n\tJointList\x12\x1f\n\x05joint\x18\x01 \x03(\x0b\x32\x10.mediapipe.Joint')
)




_JOINT = _descriptor.Descriptor(
  name='Joint',
  full_name='mediapipe.Joint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rotation_6d', full_name='mediapipe.Joint.rotation_6d', index=0,
      number=1, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='visibility', full_name='mediapipe.Joint.visibility', index=1,
      number=2, type=2, cpp_type=6, label=1,
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
  serialized_start=57,
  serialized_end=105,
)


_JOINTLIST = _descriptor.Descriptor(
  name='JointList',
  full_name='mediapipe.JointList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='joint', full_name='mediapipe.JointList.joint', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=107,
  serialized_end=151,
)

_JOINTLIST.fields_by_name['joint'].message_type = _JOINT
DESCRIPTOR.message_types_by_name['Joint'] = _JOINT
DESCRIPTOR.message_types_by_name['JointList'] = _JOINTLIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Joint = _reflection.GeneratedProtocolMessageType('Joint', (_message.Message,), dict(
  DESCRIPTOR = _JOINT,
  __module__ = 'mediapipe.framework.formats.body_rig_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.Joint)
  ))
_sym_db.RegisterMessage(Joint)

JointList = _reflection.GeneratedProtocolMessageType('JointList', (_message.Message,), dict(
  DESCRIPTOR = _JOINTLIST,
  __module__ = 'mediapipe.framework.formats.body_rig_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.JointList)
  ))
_sym_db.RegisterMessage(JointList)


# @@protoc_insertion_point(module_scope)
