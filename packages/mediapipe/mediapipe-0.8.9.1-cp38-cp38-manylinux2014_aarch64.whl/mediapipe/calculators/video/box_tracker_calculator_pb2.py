# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/calculators/video/box_tracker_calculator.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mediapipe.framework import calculator_pb2 as mediapipe_dot_framework_dot_calculator__pb2
try:
  mediapipe_dot_framework_dot_calculator__options__pb2 = mediapipe_dot_framework_dot_calculator__pb2.mediapipe_dot_framework_dot_calculator__options__pb2
except AttributeError:
  mediapipe_dot_framework_dot_calculator__options__pb2 = mediapipe_dot_framework_dot_calculator__pb2.mediapipe.framework.calculator_options_pb2
from mediapipe.util.tracking import box_tracker_pb2 as mediapipe_dot_util_dot_tracking_dot_box__tracker__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mediapipe/calculators/video/box_tracker_calculator.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n8mediapipe/calculators/video/box_tracker_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\x1a)mediapipe/util/tracking/box_tracker.proto\"\xa8\x03\n\x1b\x42oxTrackerCalculatorOptions\x12\x35\n\x0ftracker_options\x18\x01 \x01(\x0b\x32\x1c.mediapipe.BoxTrackerOptions\x12\x36\n\x10initial_position\x18\x02 \x01(\x0b\x32\x1c.mediapipe.TimedBoxProtoList\x12&\n\x17visualize_tracking_data\x18\x03 \x01(\x08:\x05\x66\x61lse\x12\x1e\n\x0fvisualize_state\x18\x04 \x01(\x08:\x05\x66\x61lse\x12\'\n\x18visualize_internal_state\x18\x05 \x01(\x08:\x05\x66\x61lse\x12*\n\x1fstreaming_track_data_cache_size\x18\x06 \x01(\x05:\x01\x30\x12&\n\x1bstart_pos_transition_frames\x18\x07 \x01(\x05:\x01\x30\x32U\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xf4\xa4\x94\x80\x01 \x01(\x0b\x32&.mediapipe.BoxTrackerCalculatorOptions')
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,mediapipe_dot_util_dot_tracking_dot_box__tracker__pb2.DESCRIPTOR,])




_BOXTRACKERCALCULATOROPTIONS = _descriptor.Descriptor(
  name='BoxTrackerCalculatorOptions',
  full_name='mediapipe.BoxTrackerCalculatorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tracker_options', full_name='mediapipe.BoxTrackerCalculatorOptions.tracker_options', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='initial_position', full_name='mediapipe.BoxTrackerCalculatorOptions.initial_position', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='visualize_tracking_data', full_name='mediapipe.BoxTrackerCalculatorOptions.visualize_tracking_data', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='visualize_state', full_name='mediapipe.BoxTrackerCalculatorOptions.visualize_state', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='visualize_internal_state', full_name='mediapipe.BoxTrackerCalculatorOptions.visualize_internal_state', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='streaming_track_data_cache_size', full_name='mediapipe.BoxTrackerCalculatorOptions.streaming_track_data_cache_size', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_pos_transition_frames', full_name='mediapipe.BoxTrackerCalculatorOptions.start_pos_transition_frames', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.BoxTrackerCalculatorOptions.ext', index=0,
      number=268767860, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=153,
  serialized_end=577,
)

_BOXTRACKERCALCULATOROPTIONS.fields_by_name['tracker_options'].message_type = mediapipe_dot_util_dot_tracking_dot_box__tracker__pb2._BOXTRACKEROPTIONS
_BOXTRACKERCALCULATOROPTIONS.fields_by_name['initial_position'].message_type = mediapipe_dot_util_dot_tracking_dot_box__tracker__pb2._TIMEDBOXPROTOLIST
DESCRIPTOR.message_types_by_name['BoxTrackerCalculatorOptions'] = _BOXTRACKERCALCULATOROPTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BoxTrackerCalculatorOptions = _reflection.GeneratedProtocolMessageType('BoxTrackerCalculatorOptions', (_message.Message,), dict(
  DESCRIPTOR = _BOXTRACKERCALCULATOROPTIONS,
  __module__ = 'mediapipe.calculators.video.box_tracker_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.BoxTrackerCalculatorOptions)
  ))
_sym_db.RegisterMessage(BoxTrackerCalculatorOptions)

_BOXTRACKERCALCULATOROPTIONS.extensions_by_name['ext'].message_type = _BOXTRACKERCALCULATOROPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_BOXTRACKERCALCULATOROPTIONS.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
