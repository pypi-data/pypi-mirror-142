# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: github.com/metaprov/modelaapi/services/cronprediction/v1/cronprediction.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from github.com.metaprov.modelaapi.pkg.apis.inference.v1alpha1 import generated_pb2 as github_dot_com_dot_metaprov_dot_modelaapi_dot_pkg_dot_apis_dot_inference_dot_v1alpha1_dot_generated__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nMgithub.com/metaprov/modelaapi/services/cronprediction/v1/cronprediction.proto\x12\x38github.com.metaprov.modelaapi.services.cronprediction.v1\x1a google/protobuf/field_mask.proto\x1a\x1cgoogle/api/annotations.proto\x1aIgithub.com/metaprov/modelaapi/pkg/apis/inference/v1alpha1/generated.proto\"\x89\x02\n\x1aListCronPredictionsRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12p\n\x06labels\x18\x02 \x03(\x0b\x32`.github.com.metaprov.modelaapi.services.cronprediction.v1.ListCronPredictionsRequest.LabelsEntry\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x9e\x01\n\x1bListCronPredictionsResponse\x12\x66\n\x0f\x63ronpredictions\x18\x01 \x01(\x0b\x32M.github.com.metaprov.modelaapi.pkg.apis.inference.v1alpha1.CronPredictionList\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\x1e\n\x1c\x43reateCronPredictionResponse\"\x80\x01\n\x1b\x43reateCronPredictionRequest\x12\x61\n\x0e\x63ronprediction\x18\x01 \x01(\x0b\x32I.github.com.metaprov.modelaapi.pkg.apis.inference.v1alpha1.CronPrediction\"\xb0\x01\n\x1bUpdateCronPredictionRequest\x12\x61\n\x0e\x63ronprediction\x18\x01 \x01(\x0b\x32I.github.com.metaprov.modelaapi.pkg.apis.inference.v1alpha1.CronPrediction\x12.\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"\x1e\n\x1cUpdateCronPredictionResponse\";\n\x18GetCronPredictionRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x8c\x01\n\x19GetCronPredictionResponse\x12\x61\n\x0e\x63ronprediction\x18\x01 \x01(\x0b\x32I.github.com.metaprov.modelaapi.pkg.apis.inference.v1alpha1.CronPrediction\x12\x0c\n\x04yaml\x18\x02 \x01(\t\">\n\x1b\x44\x65leteCronPredictionRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x1e\n\x1c\x44\x65leteCronPredictionResponse\"=\n\x1aPauseCronPredictionRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x1d\n\x1bPauseCronPredictionResponse\">\n\x1bResumeCronPredictionRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x1e\n\x1cResumeCronPredictionResponse\"}\n\x18RunCronPredictionRequest\x12\x61\n\x0e\x63ronprediction\x18\x01 \x01(\x0b\x32I.github.com.metaprov.modelaapi.pkg.apis.inference.v1alpha1.CronPrediction\"\x1b\n\x19RunCronPredictionResponse2\xa0\x0f\n\x15\x43ronPredictionService\x12\xeb\x01\n\x13ListCronPredictions\x12T.github.com.metaprov.modelaapi.services.cronprediction.v1.ListCronPredictionsRequest\x1aU.github.com.metaprov.modelaapi.services.cronprediction.v1.ListCronPredictionsResponse\"\'\x82\xd3\xe4\x93\x02!\x12\x1f/v1/cronpredictions/{namespace}\x12\xe5\x01\n\x14\x43reateCronPrediction\x12U.github.com.metaprov.modelaapi.services.cronprediction.v1.CreateCronPredictionRequest\x1aV.github.com.metaprov.modelaapi.services.cronprediction.v1.CreateCronPredictionResponse\"\x1e\x82\xd3\xe4\x93\x02\x18\"\x13/v1/cronpredictions:\x01*\x12\xe0\x01\n\x11GetCronPrediction\x12R.github.com.metaprov.modelaapi.services.cronprediction.v1.GetCronPredictionRequest\x1aS.github.com.metaprov.modelaapi.services.cronprediction.v1.GetCronPredictionResponse\"\"\x82\xd3\xe4\x93\x02\x1c\x12\x1a/v1/cronpredictions/{name}\x12\x84\x02\n\x14UpdateCronPrediction\x12U.github.com.metaprov.modelaapi.services.cronprediction.v1.UpdateCronPredictionRequest\x1aV.github.com.metaprov.modelaapi.services.cronprediction.v1.UpdateCronPredictionResponse\"=\x82\xd3\xe4\x93\x02\x37\x1a\x32/v1/cronpredictions/{cronprediction.metadata.name}:\x01*\x12\xe9\x01\n\x14\x44\x65leteCronPrediction\x12U.github.com.metaprov.modelaapi.services.cronprediction.v1.DeleteCronPredictionRequest\x1aV.github.com.metaprov.modelaapi.services.cronprediction.v1.DeleteCronPredictionResponse\"\"\x82\xd3\xe4\x93\x02\x1c*\x1a/v1/cronpredictions/{name}\x12\xec\x01\n\x13PauseCronPrediction\x12T.github.com.metaprov.modelaapi.services.cronprediction.v1.PauseCronPredictionRequest\x1aU.github.com.metaprov.modelaapi.services.cronprediction.v1.PauseCronPredictionResponse\"(\x82\xd3\xe4\x93\x02\"\" /v1/cronpredictions/{name}:pause\x12\xf0\x01\n\x14ResumeCronPrediction\x12U.github.com.metaprov.modelaapi.services.cronprediction.v1.ResumeCronPredictionRequest\x1aV.github.com.metaprov.modelaapi.services.cronprediction.v1.ResumeCronPredictionResponse\")\x82\xd3\xe4\x93\x02#\"!/v1/cronpredictions/{name}:resume\x12\xf8\x01\n\rRunPrediction\x12R.github.com.metaprov.modelaapi.services.cronprediction.v1.RunCronPredictionRequest\x1aS.github.com.metaprov.modelaapi.services.cronprediction.v1.RunCronPredictionResponse\">\x82\xd3\xe4\x93\x02\x38\"6/v1/cronpredictions/{cronprediction.metadata.name}:runB:Z8github.com/metaprov/modelaapi/services/cronprediction/v1b\x06proto3')



_LISTCRONPREDICTIONSREQUEST = DESCRIPTOR.message_types_by_name['ListCronPredictionsRequest']
_LISTCRONPREDICTIONSREQUEST_LABELSENTRY = _LISTCRONPREDICTIONSREQUEST.nested_types_by_name['LabelsEntry']
_LISTCRONPREDICTIONSRESPONSE = DESCRIPTOR.message_types_by_name['ListCronPredictionsResponse']
_CREATECRONPREDICTIONRESPONSE = DESCRIPTOR.message_types_by_name['CreateCronPredictionResponse']
_CREATECRONPREDICTIONREQUEST = DESCRIPTOR.message_types_by_name['CreateCronPredictionRequest']
_UPDATECRONPREDICTIONREQUEST = DESCRIPTOR.message_types_by_name['UpdateCronPredictionRequest']
_UPDATECRONPREDICTIONRESPONSE = DESCRIPTOR.message_types_by_name['UpdateCronPredictionResponse']
_GETCRONPREDICTIONREQUEST = DESCRIPTOR.message_types_by_name['GetCronPredictionRequest']
_GETCRONPREDICTIONRESPONSE = DESCRIPTOR.message_types_by_name['GetCronPredictionResponse']
_DELETECRONPREDICTIONREQUEST = DESCRIPTOR.message_types_by_name['DeleteCronPredictionRequest']
_DELETECRONPREDICTIONRESPONSE = DESCRIPTOR.message_types_by_name['DeleteCronPredictionResponse']
_PAUSECRONPREDICTIONREQUEST = DESCRIPTOR.message_types_by_name['PauseCronPredictionRequest']
_PAUSECRONPREDICTIONRESPONSE = DESCRIPTOR.message_types_by_name['PauseCronPredictionResponse']
_RESUMECRONPREDICTIONREQUEST = DESCRIPTOR.message_types_by_name['ResumeCronPredictionRequest']
_RESUMECRONPREDICTIONRESPONSE = DESCRIPTOR.message_types_by_name['ResumeCronPredictionResponse']
_RUNCRONPREDICTIONREQUEST = DESCRIPTOR.message_types_by_name['RunCronPredictionRequest']
_RUNCRONPREDICTIONRESPONSE = DESCRIPTOR.message_types_by_name['RunCronPredictionResponse']
ListCronPredictionsRequest = _reflection.GeneratedProtocolMessageType('ListCronPredictionsRequest', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _LISTCRONPREDICTIONSREQUEST_LABELSENTRY,
    '__module__' : 'github.com.metaprov.modelaapi.services.cronprediction.v1.cronprediction_pb2'
    # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.cronprediction.v1.ListCronPredictionsRequest.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _LISTCRONPREDICTIONSREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.cronprediction.v1.cronprediction_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.cronprediction.v1.ListCronPredictionsRequest)
  })
_sym_db.RegisterMessage(ListCronPredictionsRequest)
_sym_db.RegisterMessage(ListCronPredictionsRequest.LabelsEntry)

ListCronPredictionsResponse = _reflection.GeneratedProtocolMessageType('ListCronPredictionsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTCRONPREDICTIONSRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.cronprediction.v1.cronprediction_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.cronprediction.v1.ListCronPredictionsResponse)
  })
_sym_db.RegisterMessage(ListCronPredictionsResponse)

CreateCronPredictionResponse = _reflection.GeneratedProtocolMessageType('CreateCronPredictionResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATECRONPREDICTIONRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.cronprediction.v1.cronprediction_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.cronprediction.v1.CreateCronPredictionResponse)
  })
_sym_db.RegisterMessage(CreateCronPredictionResponse)

CreateCronPredictionRequest = _reflection.GeneratedProtocolMessageType('CreateCronPredictionRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATECRONPREDICTIONREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.cronprediction.v1.cronprediction_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.cronprediction.v1.CreateCronPredictionRequest)
  })
_sym_db.RegisterMessage(CreateCronPredictionRequest)

UpdateCronPredictionRequest = _reflection.GeneratedProtocolMessageType('UpdateCronPredictionRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATECRONPREDICTIONREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.cronprediction.v1.cronprediction_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.cronprediction.v1.UpdateCronPredictionRequest)
  })
_sym_db.RegisterMessage(UpdateCronPredictionRequest)

UpdateCronPredictionResponse = _reflection.GeneratedProtocolMessageType('UpdateCronPredictionResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATECRONPREDICTIONRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.cronprediction.v1.cronprediction_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.cronprediction.v1.UpdateCronPredictionResponse)
  })
_sym_db.RegisterMessage(UpdateCronPredictionResponse)

GetCronPredictionRequest = _reflection.GeneratedProtocolMessageType('GetCronPredictionRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCRONPREDICTIONREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.cronprediction.v1.cronprediction_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.cronprediction.v1.GetCronPredictionRequest)
  })
_sym_db.RegisterMessage(GetCronPredictionRequest)

GetCronPredictionResponse = _reflection.GeneratedProtocolMessageType('GetCronPredictionResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETCRONPREDICTIONRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.cronprediction.v1.cronprediction_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.cronprediction.v1.GetCronPredictionResponse)
  })
_sym_db.RegisterMessage(GetCronPredictionResponse)

DeleteCronPredictionRequest = _reflection.GeneratedProtocolMessageType('DeleteCronPredictionRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETECRONPREDICTIONREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.cronprediction.v1.cronprediction_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.cronprediction.v1.DeleteCronPredictionRequest)
  })
_sym_db.RegisterMessage(DeleteCronPredictionRequest)

DeleteCronPredictionResponse = _reflection.GeneratedProtocolMessageType('DeleteCronPredictionResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETECRONPREDICTIONRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.cronprediction.v1.cronprediction_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.cronprediction.v1.DeleteCronPredictionResponse)
  })
_sym_db.RegisterMessage(DeleteCronPredictionResponse)

PauseCronPredictionRequest = _reflection.GeneratedProtocolMessageType('PauseCronPredictionRequest', (_message.Message,), {
  'DESCRIPTOR' : _PAUSECRONPREDICTIONREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.cronprediction.v1.cronprediction_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.cronprediction.v1.PauseCronPredictionRequest)
  })
_sym_db.RegisterMessage(PauseCronPredictionRequest)

PauseCronPredictionResponse = _reflection.GeneratedProtocolMessageType('PauseCronPredictionResponse', (_message.Message,), {
  'DESCRIPTOR' : _PAUSECRONPREDICTIONRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.cronprediction.v1.cronprediction_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.cronprediction.v1.PauseCronPredictionResponse)
  })
_sym_db.RegisterMessage(PauseCronPredictionResponse)

ResumeCronPredictionRequest = _reflection.GeneratedProtocolMessageType('ResumeCronPredictionRequest', (_message.Message,), {
  'DESCRIPTOR' : _RESUMECRONPREDICTIONREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.cronprediction.v1.cronprediction_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.cronprediction.v1.ResumeCronPredictionRequest)
  })
_sym_db.RegisterMessage(ResumeCronPredictionRequest)

ResumeCronPredictionResponse = _reflection.GeneratedProtocolMessageType('ResumeCronPredictionResponse', (_message.Message,), {
  'DESCRIPTOR' : _RESUMECRONPREDICTIONRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.cronprediction.v1.cronprediction_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.cronprediction.v1.ResumeCronPredictionResponse)
  })
_sym_db.RegisterMessage(ResumeCronPredictionResponse)

RunCronPredictionRequest = _reflection.GeneratedProtocolMessageType('RunCronPredictionRequest', (_message.Message,), {
  'DESCRIPTOR' : _RUNCRONPREDICTIONREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.cronprediction.v1.cronprediction_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.cronprediction.v1.RunCronPredictionRequest)
  })
_sym_db.RegisterMessage(RunCronPredictionRequest)

RunCronPredictionResponse = _reflection.GeneratedProtocolMessageType('RunCronPredictionResponse', (_message.Message,), {
  'DESCRIPTOR' : _RUNCRONPREDICTIONRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.cronprediction.v1.cronprediction_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.cronprediction.v1.RunCronPredictionResponse)
  })
_sym_db.RegisterMessage(RunCronPredictionResponse)

_CRONPREDICTIONSERVICE = DESCRIPTOR.services_by_name['CronPredictionService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z8github.com/metaprov/modelaapi/services/cronprediction/v1'
  _LISTCRONPREDICTIONSREQUEST_LABELSENTRY._options = None
  _LISTCRONPREDICTIONSREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _CRONPREDICTIONSERVICE.methods_by_name['ListCronPredictions']._options = None
  _CRONPREDICTIONSERVICE.methods_by_name['ListCronPredictions']._serialized_options = b'\202\323\344\223\002!\022\037/v1/cronpredictions/{namespace}'
  _CRONPREDICTIONSERVICE.methods_by_name['CreateCronPrediction']._options = None
  _CRONPREDICTIONSERVICE.methods_by_name['CreateCronPrediction']._serialized_options = b'\202\323\344\223\002\030\"\023/v1/cronpredictions:\001*'
  _CRONPREDICTIONSERVICE.methods_by_name['GetCronPrediction']._options = None
  _CRONPREDICTIONSERVICE.methods_by_name['GetCronPrediction']._serialized_options = b'\202\323\344\223\002\034\022\032/v1/cronpredictions/{name}'
  _CRONPREDICTIONSERVICE.methods_by_name['UpdateCronPrediction']._options = None
  _CRONPREDICTIONSERVICE.methods_by_name['UpdateCronPrediction']._serialized_options = b'\202\323\344\223\0027\0322/v1/cronpredictions/{cronprediction.metadata.name}:\001*'
  _CRONPREDICTIONSERVICE.methods_by_name['DeleteCronPrediction']._options = None
  _CRONPREDICTIONSERVICE.methods_by_name['DeleteCronPrediction']._serialized_options = b'\202\323\344\223\002\034*\032/v1/cronpredictions/{name}'
  _CRONPREDICTIONSERVICE.methods_by_name['PauseCronPrediction']._options = None
  _CRONPREDICTIONSERVICE.methods_by_name['PauseCronPrediction']._serialized_options = b'\202\323\344\223\002\"\" /v1/cronpredictions/{name}:pause'
  _CRONPREDICTIONSERVICE.methods_by_name['ResumeCronPrediction']._options = None
  _CRONPREDICTIONSERVICE.methods_by_name['ResumeCronPrediction']._serialized_options = b'\202\323\344\223\002#\"!/v1/cronpredictions/{name}:resume'
  _CRONPREDICTIONSERVICE.methods_by_name['RunPrediction']._options = None
  _CRONPREDICTIONSERVICE.methods_by_name['RunPrediction']._serialized_options = b'\202\323\344\223\0028\"6/v1/cronpredictions/{cronprediction.metadata.name}:run'
  _LISTCRONPREDICTIONSREQUEST._serialized_start=279
  _LISTCRONPREDICTIONSREQUEST._serialized_end=544
  _LISTCRONPREDICTIONSREQUEST_LABELSENTRY._serialized_start=499
  _LISTCRONPREDICTIONSREQUEST_LABELSENTRY._serialized_end=544
  _LISTCRONPREDICTIONSRESPONSE._serialized_start=547
  _LISTCRONPREDICTIONSRESPONSE._serialized_end=705
  _CREATECRONPREDICTIONRESPONSE._serialized_start=707
  _CREATECRONPREDICTIONRESPONSE._serialized_end=737
  _CREATECRONPREDICTIONREQUEST._serialized_start=740
  _CREATECRONPREDICTIONREQUEST._serialized_end=868
  _UPDATECRONPREDICTIONREQUEST._serialized_start=871
  _UPDATECRONPREDICTIONREQUEST._serialized_end=1047
  _UPDATECRONPREDICTIONRESPONSE._serialized_start=1049
  _UPDATECRONPREDICTIONRESPONSE._serialized_end=1079
  _GETCRONPREDICTIONREQUEST._serialized_start=1081
  _GETCRONPREDICTIONREQUEST._serialized_end=1140
  _GETCRONPREDICTIONRESPONSE._serialized_start=1143
  _GETCRONPREDICTIONRESPONSE._serialized_end=1283
  _DELETECRONPREDICTIONREQUEST._serialized_start=1285
  _DELETECRONPREDICTIONREQUEST._serialized_end=1347
  _DELETECRONPREDICTIONRESPONSE._serialized_start=1349
  _DELETECRONPREDICTIONRESPONSE._serialized_end=1379
  _PAUSECRONPREDICTIONREQUEST._serialized_start=1381
  _PAUSECRONPREDICTIONREQUEST._serialized_end=1442
  _PAUSECRONPREDICTIONRESPONSE._serialized_start=1444
  _PAUSECRONPREDICTIONRESPONSE._serialized_end=1473
  _RESUMECRONPREDICTIONREQUEST._serialized_start=1475
  _RESUMECRONPREDICTIONREQUEST._serialized_end=1537
  _RESUMECRONPREDICTIONRESPONSE._serialized_start=1539
  _RESUMECRONPREDICTIONRESPONSE._serialized_end=1569
  _RUNCRONPREDICTIONREQUEST._serialized_start=1571
  _RUNCRONPREDICTIONREQUEST._serialized_end=1696
  _RUNCRONPREDICTIONRESPONSE._serialized_start=1698
  _RUNCRONPREDICTIONRESPONSE._serialized_end=1725
  _CRONPREDICTIONSERVICE._serialized_start=1728
  _CRONPREDICTIONSERVICE._serialized_end=3680
# @@protoc_insertion_point(module_scope)
