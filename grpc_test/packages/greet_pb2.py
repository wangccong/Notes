# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: greet.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bgreet.proto\x12\x08packages\"\x1c\n\x0chelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1c\n\rhelloResponse\x12\x0b\n\x03msg\x18\x01 \x01(\t2M\n\x0cGreetService\x12=\n\x08sayHello\x12\x16.packages.helloRequest\x1a\x17.packages.helloResponse\"\x00\x62\x06proto3')



_HELLOREQUEST = DESCRIPTOR.message_types_by_name['helloRequest']
_HELLORESPONSE = DESCRIPTOR.message_types_by_name['helloResponse']
helloRequest = _reflection.GeneratedProtocolMessageType('helloRequest', (_message.Message,), {
  'DESCRIPTOR' : _HELLOREQUEST,
  '__module__' : 'greet_pb2'
  # @@protoc_insertion_point(class_scope:packages.helloRequest)
  })
_sym_db.RegisterMessage(helloRequest)

helloResponse = _reflection.GeneratedProtocolMessageType('helloResponse', (_message.Message,), {
  'DESCRIPTOR' : _HELLORESPONSE,
  '__module__' : 'greet_pb2'
  # @@protoc_insertion_point(class_scope:packages.helloResponse)
  })
_sym_db.RegisterMessage(helloResponse)

_GREETSERVICE = DESCRIPTOR.services_by_name['GreetService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _HELLOREQUEST._serialized_start=25
  _HELLOREQUEST._serialized_end=53
  _HELLORESPONSE._serialized_start=55
  _HELLORESPONSE._serialized_end=83
  _GREETSERVICE._serialized_start=85
  _GREETSERVICE._serialized_end=162
# @@protoc_insertion_point(module_scope)
