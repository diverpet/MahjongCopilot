# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: config.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x63onfig.proto\x12\tlq.config\"T\n\x05\x46ield\x12\x12\n\nfield_name\x18\x01 \x01(\t\x12\x14\n\x0c\x61rray_length\x18\x02 \x01(\r\x12\x0f\n\x07pb_type\x18\x03 \x01(\t\x12\x10\n\x08pb_index\x18\x04 \x01(\r\"*\n\tSheetMeta\x12\x10\n\x08\x63\x61tegory\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\"a\n\x0bSheetSchema\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\"\n\x04meta\x18\x02 \x01(\x0b\x32\x14.lq.config.SheetMeta\x12 \n\x06\x66ields\x18\x03 \x03(\x0b\x32\x10.lq.config.Field\"C\n\x0bTableSchema\x12\x0c\n\x04name\x18\x01 \x01(\t\x12&\n\x06sheets\x18\x02 \x03(\x0b\x32\x16.lq.config.SheetSchema\"7\n\tSheetData\x12\r\n\x05table\x18\x01 \x01(\t\x12\r\n\x05sheet\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x03 \x03(\x0c\"\x82\x01\n\x0c\x43onfigTables\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x13\n\x0bheader_hash\x18\x02 \x01(\t\x12\'\n\x07schemas\x18\x03 \x03(\x0b\x32\x16.lq.config.TableSchema\x12#\n\x05\x64\x61tas\x18\x04 \x03(\x0b\x32\x14.lq.config.SheetDatab\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'config_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _FIELD._serialized_start=27
  _FIELD._serialized_end=111
  _SHEETMETA._serialized_start=113
  _SHEETMETA._serialized_end=155
  _SHEETSCHEMA._serialized_start=157
  _SHEETSCHEMA._serialized_end=254
  _TABLESCHEMA._serialized_start=256
  _TABLESCHEMA._serialized_end=323
  _SHEETDATA._serialized_start=325
  _SHEETDATA._serialized_end=380
  _CONFIGTABLES._serialized_start=383
  _CONFIGTABLES._serialized_end=513
# @@protoc_insertion_point(module_scope)