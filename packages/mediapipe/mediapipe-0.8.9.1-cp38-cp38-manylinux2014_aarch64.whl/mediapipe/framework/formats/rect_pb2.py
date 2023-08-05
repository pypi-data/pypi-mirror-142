# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/framework/formats/rect.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='mediapipe/framework/formats/rect.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_options=_b('\n\"com.google.mediapipe.formats.protoB\tRectProto'),
  serialized_pb=_b('\n&mediapipe/framework/formats/rect.proto\x12\tmediapipe\"o\n\x04Rect\x12\x10\n\x08x_center\x18\x01 \x02(\x05\x12\x10\n\x08y_center\x18\x02 \x02(\x05\x12\x0e\n\x06height\x18\x03 \x02(\x05\x12\r\n\x05width\x18\x04 \x02(\x05\x12\x13\n\x08rotation\x18\x05 \x01(\x02:\x01\x30\x12\x0f\n\x07rect_id\x18\x06 \x01(\x03\"y\n\x0eNormalizedRect\x12\x10\n\x08x_center\x18\x01 \x02(\x02\x12\x10\n\x08y_center\x18\x02 \x02(\x02\x12\x0e\n\x06height\x18\x03 \x02(\x02\x12\r\n\x05width\x18\x04 \x02(\x02\x12\x13\n\x08rotation\x18\x05 \x01(\x02:\x01\x30\x12\x0f\n\x07rect_id\x18\x06 \x01(\x03\x42/\n\"com.google.mediapipe.formats.protoB\tRectProto')
)




_RECT = _descriptor.Descriptor(
  name='Rect',
  full_name='mediapipe.Rect',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x_center', full_name='mediapipe.Rect.x_center', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y_center', full_name='mediapipe.Rect.y_center', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='mediapipe.Rect.height', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='width', full_name='mediapipe.Rect.width', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rotation', full_name='mediapipe.Rect.rotation', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rect_id', full_name='mediapipe.Rect.rect_id', index=5,
      number=6, type=3, cpp_type=2, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=53,
  serialized_end=164,
)


_NORMALIZEDRECT = _descriptor.Descriptor(
  name='NormalizedRect',
  full_name='mediapipe.NormalizedRect',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x_center', full_name='mediapipe.NormalizedRect.x_center', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y_center', full_name='mediapipe.NormalizedRect.y_center', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='mediapipe.NormalizedRect.height', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='width', full_name='mediapipe.NormalizedRect.width', index=3,
      number=4, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rotation', full_name='mediapipe.NormalizedRect.rotation', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rect_id', full_name='mediapipe.NormalizedRect.rect_id', index=5,
      number=6, type=3, cpp_type=2, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=166,
  serialized_end=287,
)

DESCRIPTOR.message_types_by_name['Rect'] = _RECT
DESCRIPTOR.message_types_by_name['NormalizedRect'] = _NORMALIZEDRECT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Rect = _reflection.GeneratedProtocolMessageType('Rect', (_message.Message,), dict(
  DESCRIPTOR = _RECT,
  __module__ = 'mediapipe.framework.formats.rect_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.Rect)
  ))
_sym_db.RegisterMessage(Rect)

NormalizedRect = _reflection.GeneratedProtocolMessageType('NormalizedRect', (_message.Message,), dict(
  DESCRIPTOR = _NORMALIZEDRECT,
  __module__ = 'mediapipe.framework.formats.rect_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.NormalizedRect)
  ))
_sym_db.RegisterMessage(NormalizedRect)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
