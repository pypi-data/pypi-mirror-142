# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protoc-gen-swagger/options/annotations.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2
from protoc_gen_swagger.options import openapiv2_pb2 as protoc__gen__swagger_dot_options_dot_openapiv2__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='protoc-gen-swagger/options/annotations.proto',
  package='grpc.gateway.protoc_gen_swagger.options',
  syntax='proto3',
  serialized_options=_b('ZAgithub.com/grpc-ecosystem/grpc-gateway/protoc-gen-swagger/options'),
  serialized_pb=_b('\n,protoc-gen-swagger/options/annotations.proto\x12\'grpc.gateway.protoc_gen_swagger.options\x1a google/protobuf/descriptor.proto\x1a*protoc-gen-swagger/options/openapiv2.proto:j\n\x11openapiv2_swagger\x12\x1c.google.protobuf.FileOptions\x18\x92\x08 \x01(\x0b\x32\x30.grpc.gateway.protoc_gen_swagger.options.Swagger:p\n\x13openapiv2_operation\x12\x1e.google.protobuf.MethodOptions\x18\x92\x08 \x01(\x0b\x32\x32.grpc.gateway.protoc_gen_swagger.options.Operation:k\n\x10openapiv2_schema\x12\x1f.google.protobuf.MessageOptions\x18\x92\x08 \x01(\x0b\x32/.grpc.gateway.protoc_gen_swagger.options.Schema:e\n\ropenapiv2_tag\x12\x1f.google.protobuf.ServiceOptions\x18\x92\x08 \x01(\x0b\x32,.grpc.gateway.protoc_gen_swagger.options.Tag:l\n\x0fopenapiv2_field\x12\x1d.google.protobuf.FieldOptions\x18\x92\x08 \x01(\x0b\x32\x33.grpc.gateway.protoc_gen_swagger.options.JSONSchemaBCZAgithub.com/grpc-ecosystem/grpc-gateway/protoc-gen-swagger/optionsb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR,protoc__gen__swagger_dot_options_dot_openapiv2__pb2.DESCRIPTOR,])


OPENAPIV2_SWAGGER_FIELD_NUMBER = 1042
openapiv2_swagger = _descriptor.FieldDescriptor(
  name='openapiv2_swagger', full_name='grpc.gateway.protoc_gen_swagger.options.openapiv2_swagger', index=0,
  number=1042, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
OPENAPIV2_OPERATION_FIELD_NUMBER = 1042
openapiv2_operation = _descriptor.FieldDescriptor(
  name='openapiv2_operation', full_name='grpc.gateway.protoc_gen_swagger.options.openapiv2_operation', index=1,
  number=1042, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
OPENAPIV2_SCHEMA_FIELD_NUMBER = 1042
openapiv2_schema = _descriptor.FieldDescriptor(
  name='openapiv2_schema', full_name='grpc.gateway.protoc_gen_swagger.options.openapiv2_schema', index=2,
  number=1042, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
OPENAPIV2_TAG_FIELD_NUMBER = 1042
openapiv2_tag = _descriptor.FieldDescriptor(
  name='openapiv2_tag', full_name='grpc.gateway.protoc_gen_swagger.options.openapiv2_tag', index=3,
  number=1042, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
OPENAPIV2_FIELD_FIELD_NUMBER = 1042
openapiv2_field = _descriptor.FieldDescriptor(
  name='openapiv2_field', full_name='grpc.gateway.protoc_gen_swagger.options.openapiv2_field', index=4,
  number=1042, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)

DESCRIPTOR.extensions_by_name['openapiv2_swagger'] = openapiv2_swagger
DESCRIPTOR.extensions_by_name['openapiv2_operation'] = openapiv2_operation
DESCRIPTOR.extensions_by_name['openapiv2_schema'] = openapiv2_schema
DESCRIPTOR.extensions_by_name['openapiv2_tag'] = openapiv2_tag
DESCRIPTOR.extensions_by_name['openapiv2_field'] = openapiv2_field
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

openapiv2_swagger.message_type = protoc__gen__swagger_dot_options_dot_openapiv2__pb2._SWAGGER
google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(openapiv2_swagger)
openapiv2_operation.message_type = protoc__gen__swagger_dot_options_dot_openapiv2__pb2._OPERATION
google_dot_protobuf_dot_descriptor__pb2.MethodOptions.RegisterExtension(openapiv2_operation)
openapiv2_schema.message_type = protoc__gen__swagger_dot_options_dot_openapiv2__pb2._SCHEMA
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(openapiv2_schema)
openapiv2_tag.message_type = protoc__gen__swagger_dot_options_dot_openapiv2__pb2._TAG
google_dot_protobuf_dot_descriptor__pb2.ServiceOptions.RegisterExtension(openapiv2_tag)
openapiv2_field.message_type = protoc__gen__swagger_dot_options_dot_openapiv2__pb2._JSONSCHEMA
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(openapiv2_field)

DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
