# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/protobuf/unittest_import.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import google.protobuf.unittest_import_public_pb2

from google.protobuf.unittest_import_public_pb2 import *

DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/protobuf/unittest_import.proto',
  package='protobuf_unittest_import',
  serialized_pb=_b('\n%google/protobuf/unittest_import.proto\x12\x18protobuf_unittest_import\x1a,google/protobuf/unittest_import_public.proto\"\x1a\n\rImportMessage\x12\t\n\x01\x64\x18\x01 \x01(\x05*<\n\nImportEnum\x12\x0e\n\nIMPORT_FOO\x10\x07\x12\x0e\n\nIMPORT_BAR\x10\x08\x12\x0e\n\nIMPORT_BAZ\x10\tB\x1c\n\x18\x63om.google.protobuf.testH\x01P\x00')
  ,
  dependencies=[google.protobuf.unittest_import_public_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_IMPORTENUM = _descriptor.EnumDescriptor(
  name='ImportEnum',
  full_name='protobuf_unittest_import.ImportEnum',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='IMPORT_FOO', index=0, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IMPORT_BAR', index=1, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IMPORT_BAZ', index=2, number=9,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=141,
  serialized_end=201,
)
_sym_db.RegisterEnumDescriptor(_IMPORTENUM)

ImportEnum = enum_type_wrapper.EnumTypeWrapper(_IMPORTENUM)
IMPORT_FOO = 7
IMPORT_BAR = 8
IMPORT_BAZ = 9



_IMPORTMESSAGE = _descriptor.Descriptor(
  name='ImportMessage',
  full_name='protobuf_unittest_import.ImportMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='d', full_name='protobuf_unittest_import.ImportMessage.d', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=113,
  serialized_end=139,
)

DESCRIPTOR.message_types_by_name['ImportMessage'] = _IMPORTMESSAGE
DESCRIPTOR.enum_types_by_name['ImportEnum'] = _IMPORTENUM

ImportMessage = _reflection.GeneratedProtocolMessageType('ImportMessage', (_message.Message,), dict(
  DESCRIPTOR = _IMPORTMESSAGE,
  __module__ = 'google.protobuf.unittest_import_pb2'
  # @@protoc_insertion_point(class_scope:protobuf_unittest_import.ImportMessage)
  ))
_sym_db.RegisterMessage(ImportMessage)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\030com.google.protobuf.testH\001'))
# @@protoc_insertion_point(module_scope)
