# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pydgraph/proto/api.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18pydgraph/proto/api.proto\x12\x03\x61pi\"\xb8\x02\n\x07Request\x12\x10\n\x08start_ts\x18\x01 \x01(\x04\x12\r\n\x05query\x18\x04 \x01(\t\x12$\n\x04vars\x18\x05 \x03(\x0b\x32\x16.api.Request.VarsEntry\x12\x11\n\tread_only\x18\x06 \x01(\x08\x12\x13\n\x0b\x62\x65st_effort\x18\x07 \x01(\x08\x12 \n\tmutations\x18\x0c \x03(\x0b\x32\r.api.Mutation\x12\x12\n\ncommit_now\x18\r \x01(\x08\x12,\n\x0bresp_format\x18\x0e \x01(\x0e\x32\x17.api.Request.RespFormat\x12\x0c\n\x04hash\x18\x0f \x01(\t\x1a+\n\tVarsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x1f\n\nRespFormat\x12\x08\n\x04JSON\x10\x00\x12\x07\n\x03RDF\x10\x01\"\x14\n\x04Uids\x12\x0c\n\x04uids\x18\x01 \x03(\t\"\x1d\n\x0cListOfString\x12\r\n\x05value\x18\x01 \x03(\t\"\xbc\x02\n\x08Response\x12\x0c\n\x04json\x18\x01 \x01(\x0c\x12\x1c\n\x03txn\x18\x02 \x01(\x0b\x32\x0f.api.TxnContext\x12\x1d\n\x07latency\x18\x03 \x01(\x0b\x32\x0c.api.Latency\x12\x1d\n\x07metrics\x18\x04 \x01(\x0b\x32\x0c.api.Metrics\x12%\n\x04uids\x18\x0c \x03(\x0b\x32\x17.api.Response.UidsEntry\x12\x0b\n\x03rdf\x18\r \x01(\x0c\x12%\n\x04hdrs\x18\x0e \x03(\x0b\x32\x17.api.Response.HdrsEntry\x1a+\n\tUidsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a>\n\tHdrsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12 \n\x05value\x18\x02 \x01(\x0b\x32\x11.api.ListOfString:\x02\x38\x01\"\xad\x01\n\x08Mutation\x12\x10\n\x08set_json\x18\x01 \x01(\x0c\x12\x13\n\x0b\x64\x65lete_json\x18\x02 \x01(\x0c\x12\x12\n\nset_nquads\x18\x03 \x01(\x0c\x12\x12\n\ndel_nquads\x18\x04 \x01(\x0c\x12\x17\n\x03set\x18\x05 \x03(\x0b\x32\n.api.NQuad\x12\x17\n\x03\x64\x65l\x18\x06 \x03(\x0b\x32\n.api.NQuad\x12\x0c\n\x04\x63ond\x18\t \x01(\t\x12\x12\n\ncommit_now\x18\x0e \x01(\x08\"\xd2\x01\n\tOperation\x12\x0e\n\x06schema\x18\x01 \x01(\t\x12\x11\n\tdrop_attr\x18\x02 \x01(\t\x12\x10\n\x08\x64rop_all\x18\x03 \x01(\x08\x12&\n\x07\x64rop_op\x18\x04 \x01(\x0e\x32\x15.api.Operation.DropOp\x12\x12\n\ndrop_value\x18\x05 \x01(\t\x12\x19\n\x11run_in_background\x18\x06 \x01(\x08\"9\n\x06\x44ropOp\x12\x08\n\x04NONE\x10\x00\x12\x07\n\x03\x41LL\x10\x01\x12\x08\n\x04\x44\x41TA\x10\x02\x12\x08\n\x04\x41TTR\x10\x03\x12\x08\n\x04TYPE\x10\x04\"\x17\n\x07Payload\x12\x0c\n\x04\x44\x61ta\x18\x01 \x01(\x0c\"m\n\nTxnContext\x12\x10\n\x08start_ts\x18\x01 \x01(\x04\x12\x11\n\tcommit_ts\x18\x02 \x01(\x04\x12\x0f\n\x07\x61\x62orted\x18\x03 \x01(\x08\x12\x0c\n\x04keys\x18\x04 \x03(\t\x12\r\n\x05preds\x18\x05 \x03(\t\x12\x0c\n\x04hash\x18\x06 \x01(\t\"\x07\n\x05\x43heck\"\x16\n\x07Version\x12\x0b\n\x03tag\x18\x01 \x01(\t\"x\n\x07Latency\x12\x12\n\nparsing_ns\x18\x01 \x01(\x04\x12\x15\n\rprocessing_ns\x18\x02 \x01(\x04\x12\x13\n\x0b\x65ncoding_ns\x18\x03 \x01(\x04\x12\x1b\n\x13\x61ssign_timestamp_ns\x18\x04 \x01(\x04\x12\x10\n\x08total_ns\x18\x05 \x01(\x04\"f\n\x07Metrics\x12+\n\x08num_uids\x18\x01 \x03(\x0b\x32\x19.api.Metrics.NumUidsEntry\x1a.\n\x0cNumUidsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x04:\x02\x38\x01\"\xa3\x01\n\x05NQuad\x12\x0f\n\x07subject\x18\x01 \x01(\t\x12\x11\n\tpredicate\x18\x02 \x01(\t\x12\x11\n\tobject_id\x18\x03 \x01(\t\x12 \n\x0cobject_value\x18\x04 \x01(\x0b\x32\n.api.Value\x12\x0c\n\x04lang\x18\x06 \x01(\t\x12\x1a\n\x06\x66\x61\x63\x65ts\x18\x07 \x03(\x0b\x32\n.api.Facet\x12\x11\n\tnamespace\x18\x08 \x01(\x04J\x04\x08\x05\x10\x06\"\x8c\x02\n\x05Value\x12\x15\n\x0b\x64\x65\x66\x61ult_val\x18\x01 \x01(\tH\x00\x12\x13\n\tbytes_val\x18\x02 \x01(\x0cH\x00\x12\x11\n\x07int_val\x18\x03 \x01(\x03H\x00\x12\x12\n\x08\x62ool_val\x18\x04 \x01(\x08H\x00\x12\x11\n\x07str_val\x18\x05 \x01(\tH\x00\x12\x14\n\ndouble_val\x18\x06 \x01(\x01H\x00\x12\x11\n\x07geo_val\x18\x07 \x01(\x0cH\x00\x12\x12\n\x08\x64\x61te_val\x18\x08 \x01(\x0cH\x00\x12\x16\n\x0c\x64\x61tetime_val\x18\t \x01(\x0cH\x00\x12\x16\n\x0cpassword_val\x18\n \x01(\tH\x00\x12\x11\n\x07uid_val\x18\x0b \x01(\x04H\x00\x12\x16\n\x0cvfloat32_val\x18\r \x01(\x0cH\x00\x42\x05\n\x03val\"\xab\x01\n\x05\x46\x61\x63\x65t\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c\x12$\n\x08val_type\x18\x03 \x01(\x0e\x32\x12.api.Facet.ValType\x12\x0e\n\x06tokens\x18\x04 \x03(\t\x12\r\n\x05\x61lias\x18\x05 \x01(\t\"A\n\x07ValType\x12\n\n\x06STRING\x10\x00\x12\x07\n\x03INT\x10\x01\x12\t\n\x05\x46LOAT\x10\x02\x12\x08\n\x04\x42OOL\x10\x03\x12\x0c\n\x08\x44\x41TETIME\x10\x04\"Z\n\x0cLoginRequest\x12\x0e\n\x06userid\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\x15\n\rrefresh_token\x18\x03 \x01(\t\x12\x11\n\tnamespace\x18\x04 \x01(\x04\".\n\x03Jwt\x12\x12\n\naccess_jwt\x18\x01 \x01(\t\x12\x13\n\x0brefresh_jwt\x18\x02 \x01(\t2\xe7\x01\n\x06\x44graph\x12+\n\x05Login\x12\x11.api.LoginRequest\x1a\r.api.Response\"\x00\x12&\n\x05Query\x12\x0c.api.Request\x1a\r.api.Response\"\x00\x12\'\n\x05\x41lter\x12\x0e.api.Operation\x1a\x0c.api.Payload\"\x00\x12\x33\n\rCommitOrAbort\x12\x0f.api.TxnContext\x1a\x0f.api.TxnContext\"\x00\x12*\n\x0c\x43heckVersion\x12\n.api.Check\x1a\x0c.api.Version\"\x00\x42\x18\n\tio.dgraphB\x0b\x44graphProtob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pydgraph.proto.api_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\tio.dgraphB\013DgraphProto'
  _globals['_REQUEST_VARSENTRY']._loaded_options = None
  _globals['_REQUEST_VARSENTRY']._serialized_options = b'8\001'
  _globals['_RESPONSE_UIDSENTRY']._loaded_options = None
  _globals['_RESPONSE_UIDSENTRY']._serialized_options = b'8\001'
  _globals['_RESPONSE_HDRSENTRY']._loaded_options = None
  _globals['_RESPONSE_HDRSENTRY']._serialized_options = b'8\001'
  _globals['_METRICS_NUMUIDSENTRY']._loaded_options = None
  _globals['_METRICS_NUMUIDSENTRY']._serialized_options = b'8\001'
  _globals['_REQUEST']._serialized_start=34
  _globals['_REQUEST']._serialized_end=346
  _globals['_REQUEST_VARSENTRY']._serialized_start=270
  _globals['_REQUEST_VARSENTRY']._serialized_end=313
  _globals['_REQUEST_RESPFORMAT']._serialized_start=315
  _globals['_REQUEST_RESPFORMAT']._serialized_end=346
  _globals['_UIDS']._serialized_start=348
  _globals['_UIDS']._serialized_end=368
  _globals['_LISTOFSTRING']._serialized_start=370
  _globals['_LISTOFSTRING']._serialized_end=399
  _globals['_RESPONSE']._serialized_start=402
  _globals['_RESPONSE']._serialized_end=718
  _globals['_RESPONSE_UIDSENTRY']._serialized_start=611
  _globals['_RESPONSE_UIDSENTRY']._serialized_end=654
  _globals['_RESPONSE_HDRSENTRY']._serialized_start=656
  _globals['_RESPONSE_HDRSENTRY']._serialized_end=718
  _globals['_MUTATION']._serialized_start=721
  _globals['_MUTATION']._serialized_end=894
  _globals['_OPERATION']._serialized_start=897
  _globals['_OPERATION']._serialized_end=1107
  _globals['_OPERATION_DROPOP']._serialized_start=1050
  _globals['_OPERATION_DROPOP']._serialized_end=1107
  _globals['_PAYLOAD']._serialized_start=1109
  _globals['_PAYLOAD']._serialized_end=1132
  _globals['_TXNCONTEXT']._serialized_start=1134
  _globals['_TXNCONTEXT']._serialized_end=1243
  _globals['_CHECK']._serialized_start=1245
  _globals['_CHECK']._serialized_end=1252
  _globals['_VERSION']._serialized_start=1254
  _globals['_VERSION']._serialized_end=1276
  _globals['_LATENCY']._serialized_start=1278
  _globals['_LATENCY']._serialized_end=1398
  _globals['_METRICS']._serialized_start=1400
  _globals['_METRICS']._serialized_end=1502
  _globals['_METRICS_NUMUIDSENTRY']._serialized_start=1456
  _globals['_METRICS_NUMUIDSENTRY']._serialized_end=1502
  _globals['_NQUAD']._serialized_start=1505
  _globals['_NQUAD']._serialized_end=1668
  _globals['_VALUE']._serialized_start=1671
  _globals['_VALUE']._serialized_end=1939
  _globals['_FACET']._serialized_start=1942
  _globals['_FACET']._serialized_end=2113
  _globals['_FACET_VALTYPE']._serialized_start=2048
  _globals['_FACET_VALTYPE']._serialized_end=2113
  _globals['_LOGINREQUEST']._serialized_start=2115
  _globals['_LOGINREQUEST']._serialized_end=2205
  _globals['_JWT']._serialized_start=2207
  _globals['_JWT']._serialized_end=2253
  _globals['_DGRAPH']._serialized_start=2256
  _globals['_DGRAPH']._serialized_end=2487
# @@protoc_insertion_point(module_scope)
