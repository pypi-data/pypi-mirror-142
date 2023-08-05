# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: github.com/metaprov/modelaapi/services/publisherd/v1/publisherd.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from github.com.metaprov.modelaapi.pkg.apis.training.v1alpha1 import generated_pb2 as github_dot_com_dot_metaprov_dot_modelaapi_dot_pkg_dot_apis_dot_training_dot_v1alpha1_dot_generated__pb2
from github.com.metaprov.modelaapi.pkg.apis.data.v1alpha1 import generated_pb2 as github_dot_com_dot_metaprov_dot_modelaapi_dot_pkg_dot_apis_dot_data_dot_v1alpha1_dot_generated__pb2
from github.com.metaprov.modelaapi.pkg.apis.infra.v1alpha1 import generated_pb2 as github_dot_com_dot_metaprov_dot_modelaapi_dot_pkg_dot_apis_dot_infra_dot_v1alpha1_dot_generated__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nEgithub.com/metaprov/modelaapi/services/publisherd/v1/publisherd.proto\x12\x34github.com.metaprov.modelaapi.services.publisherd.v1\x1aHgithub.com/metaprov/modelaapi/pkg/apis/training/v1alpha1/generated.proto\x1a\x44github.com/metaprov/modelaapi/pkg/apis/data/v1alpha1/generated.proto\x1a\x45github.com/metaprov/modelaapi/pkg/apis/infra/v1alpha1/generated.proto\"\xff\x02\n\x16PublishNotebookRequest\x12\x14\n\x0cnotebookName\x18\x01 \x01(\t\x12\x19\n\x11notebookNamespace\x18\x02 \x01(\t\x12\\\n\x0cnotebookSpec\x18\x03 \x01(\x0b\x32\x46.github.com.metaprov.modelaapi.pkg.apis.training.v1alpha1.NotebookSpec\x12\x17\n\x0fNotebookContent\x18\x04 \x01(\t\x12\x12\n\nDockerfile\x18\x05 \x01(\t\x12\x10\n\x08provider\x18\x06 \x01(\t\x12h\n\x06secret\x18\x07 \x03(\x0b\x32X.github.com.metaprov.modelaapi.services.publisherd.v1.PublishNotebookRequest.SecretEntry\x1a-\n\x0bSecretEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\",\n\x17PublishNotebookResponse\x12\x11\n\tImageName\x18\x01 \x01(\t\"\xe9\t\n\x13PublishModelRequest\x12V\n\x0b\x64\x61taproduct\x18\x01 \x01(\x0b\x32\x41.github.com.metaprov.modelaapi.pkg.apis.data.v1alpha1.DataProduct\x12\x64\n\x12\x64\x61taproductversion\x18\x02 \x01(\x0b\x32H.github.com.metaprov.modelaapi.pkg.apis.data.v1alpha1.DataProductVersion\x12N\n\x05model\x18\x03 \x01(\x0b\x32?.github.com.metaprov.modelaapi.pkg.apis.training.v1alpha1.Model\x12N\n\x05study\x18\x04 \x01(\x0b\x32?.github.com.metaprov.modelaapi.pkg.apis.training.v1alpha1.Study\x12T\n\ndatasource\x18\x05 \x01(\x0b\x32@.github.com.metaprov.modelaapi.pkg.apis.data.v1alpha1.DataSource\x12N\n\x07\x64\x61taset\x18\x06 \x01(\x0b\x32=.github.com.metaprov.modelaapi.pkg.apis.data.v1alpha1.Dataset\x12\x10\n\x08provider\x18\x07 \x01(\t\x12\x11\n\timagename\x18\x08 \x01(\t\x12\x1c\n\x14imagenameWithVersion\x18\t \x01(\t\x12\x0c\n\x04push\x18\n \x01(\x08\x12T\n\x06\x62ucket\x18\x0b \x01(\x0b\x32\x44.github.com.metaprov.modelaapi.pkg.apis.infra.v1alpha1.VirtualBucket\x12T\n\tcloudConn\x18\x0c \x01(\x0b\x32\x41.github.com.metaprov.modelaapi.pkg.apis.infra.v1alpha1.Connection\x12o\n\x0b\x63loudSecret\x18\r \x03(\x0b\x32Z.github.com.metaprov.modelaapi.services.publisherd.v1.PublishModelRequest.CloudSecretEntry\x12[\n\x10\x64ockerConnection\x18\x0e \x01(\x0b\x32\x41.github.com.metaprov.modelaapi.pkg.apis.infra.v1alpha1.Connection\x12\x81\x01\n\x14\x64ockerRegistrySecret\x18\x0f \x03(\x0b\x32\x63.github.com.metaprov.modelaapi.services.publisherd.v1.PublishModelRequest.DockerRegistrySecretEntry\x12\x0e\n\x06kaniko\x18\x13 \x01(\x08\x1a\x32\n\x10\x43loudSecretEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\x1a;\n\x19\x44ockerRegistrySecretEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\"7\n\x14PublishModelResponse\x12\x11\n\tImageName\x18\x01 \x01(\t\x12\x0c\n\x04hash\x18\x02 \x01(\t\"\xea\x06\n\x13PackageModelRequest\x12V\n\x0b\x64\x61taproduct\x18\x01 \x01(\x0b\x32\x41.github.com.metaprov.modelaapi.pkg.apis.data.v1alpha1.DataProduct\x12\x64\n\x12\x64\x61taproductversion\x18\x02 \x01(\x0b\x32H.github.com.metaprov.modelaapi.pkg.apis.data.v1alpha1.DataProductVersion\x12N\n\x05model\x18\x03 \x01(\x0b\x32?.github.com.metaprov.modelaapi.pkg.apis.training.v1alpha1.Model\x12N\n\x05study\x18\x04 \x01(\x0b\x32?.github.com.metaprov.modelaapi.pkg.apis.training.v1alpha1.Study\x12T\n\ndatasource\x18\x05 \x01(\x0b\x32@.github.com.metaprov.modelaapi.pkg.apis.data.v1alpha1.DataSource\x12N\n\x07\x64\x61taset\x18\x06 \x01(\x0b\x32=.github.com.metaprov.modelaapi.pkg.apis.data.v1alpha1.Dataset\x12T\n\x06\x62ucket\x18\x07 \x01(\x0b\x32\x44.github.com.metaprov.modelaapi.pkg.apis.infra.v1alpha1.VirtualBucket\x12T\n\tcloudConn\x18\x08 \x01(\x0b\x32\x41.github.com.metaprov.modelaapi.pkg.apis.infra.v1alpha1.Connection\x12o\n\x0b\x63loudSecret\x18\t \x03(\x0b\x32Z.github.com.metaprov.modelaapi.services.publisherd.v1.PackageModelRequest.CloudSecretEntry\x1a\x32\n\x10\x43loudSecretEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\"4\n\x14PackageModelResponse\x12\x0e\n\x06tarUri\x18\x01 \x01(\t\x12\x0c\n\x04hash\x18\x02 \x01(\t\"\x11\n\x0fShutdownRequest\"\x12\n\x10ShutdownResponse2\xb8\x05\n\x11PublisherdService\x12\xa7\x01\n\x0cPackageModel\x12I.github.com.metaprov.modelaapi.services.publisherd.v1.PackageModelRequest\x1aJ.github.com.metaprov.modelaapi.services.publisherd.v1.PackageModelResponse\"\x00\x12\xa7\x01\n\x0cPublishModel\x12I.github.com.metaprov.modelaapi.services.publisherd.v1.PublishModelRequest\x1aJ.github.com.metaprov.modelaapi.services.publisherd.v1.PublishModelResponse\"\x00\x12\xb0\x01\n\x0fPublishNotebook\x12L.github.com.metaprov.modelaapi.services.publisherd.v1.PublishNotebookRequest\x1aM.github.com.metaprov.modelaapi.services.publisherd.v1.PublishNotebookResponse\"\x00\x12\x9b\x01\n\x08Shutdown\x12\x45.github.com.metaprov.modelaapi.services.publisherd.v1.ShutdownRequest\x1a\x46.github.com.metaprov.modelaapi.services.publisherd.v1.ShutdownResponse\"\x00\x42\x36Z4github.com/metaprov/modelaapi/services/publisherd/v1b\x06proto3')



_PUBLISHNOTEBOOKREQUEST = DESCRIPTOR.message_types_by_name['PublishNotebookRequest']
_PUBLISHNOTEBOOKREQUEST_SECRETENTRY = _PUBLISHNOTEBOOKREQUEST.nested_types_by_name['SecretEntry']
_PUBLISHNOTEBOOKRESPONSE = DESCRIPTOR.message_types_by_name['PublishNotebookResponse']
_PUBLISHMODELREQUEST = DESCRIPTOR.message_types_by_name['PublishModelRequest']
_PUBLISHMODELREQUEST_CLOUDSECRETENTRY = _PUBLISHMODELREQUEST.nested_types_by_name['CloudSecretEntry']
_PUBLISHMODELREQUEST_DOCKERREGISTRYSECRETENTRY = _PUBLISHMODELREQUEST.nested_types_by_name['DockerRegistrySecretEntry']
_PUBLISHMODELRESPONSE = DESCRIPTOR.message_types_by_name['PublishModelResponse']
_PACKAGEMODELREQUEST = DESCRIPTOR.message_types_by_name['PackageModelRequest']
_PACKAGEMODELREQUEST_CLOUDSECRETENTRY = _PACKAGEMODELREQUEST.nested_types_by_name['CloudSecretEntry']
_PACKAGEMODELRESPONSE = DESCRIPTOR.message_types_by_name['PackageModelResponse']
_SHUTDOWNREQUEST = DESCRIPTOR.message_types_by_name['ShutdownRequest']
_SHUTDOWNRESPONSE = DESCRIPTOR.message_types_by_name['ShutdownResponse']
PublishNotebookRequest = _reflection.GeneratedProtocolMessageType('PublishNotebookRequest', (_message.Message,), {

  'SecretEntry' : _reflection.GeneratedProtocolMessageType('SecretEntry', (_message.Message,), {
    'DESCRIPTOR' : _PUBLISHNOTEBOOKREQUEST_SECRETENTRY,
    '__module__' : 'github.com.metaprov.modelaapi.services.publisherd.v1.publisherd_pb2'
    # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.publisherd.v1.PublishNotebookRequest.SecretEntry)
    })
  ,
  'DESCRIPTOR' : _PUBLISHNOTEBOOKREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.publisherd.v1.publisherd_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.publisherd.v1.PublishNotebookRequest)
  })
_sym_db.RegisterMessage(PublishNotebookRequest)
_sym_db.RegisterMessage(PublishNotebookRequest.SecretEntry)

PublishNotebookResponse = _reflection.GeneratedProtocolMessageType('PublishNotebookResponse', (_message.Message,), {
  'DESCRIPTOR' : _PUBLISHNOTEBOOKRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.publisherd.v1.publisherd_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.publisherd.v1.PublishNotebookResponse)
  })
_sym_db.RegisterMessage(PublishNotebookResponse)

PublishModelRequest = _reflection.GeneratedProtocolMessageType('PublishModelRequest', (_message.Message,), {

  'CloudSecretEntry' : _reflection.GeneratedProtocolMessageType('CloudSecretEntry', (_message.Message,), {
    'DESCRIPTOR' : _PUBLISHMODELREQUEST_CLOUDSECRETENTRY,
    '__module__' : 'github.com.metaprov.modelaapi.services.publisherd.v1.publisherd_pb2'
    # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.publisherd.v1.PublishModelRequest.CloudSecretEntry)
    })
  ,

  'DockerRegistrySecretEntry' : _reflection.GeneratedProtocolMessageType('DockerRegistrySecretEntry', (_message.Message,), {
    'DESCRIPTOR' : _PUBLISHMODELREQUEST_DOCKERREGISTRYSECRETENTRY,
    '__module__' : 'github.com.metaprov.modelaapi.services.publisherd.v1.publisherd_pb2'
    # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.publisherd.v1.PublishModelRequest.DockerRegistrySecretEntry)
    })
  ,
  'DESCRIPTOR' : _PUBLISHMODELREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.publisherd.v1.publisherd_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.publisherd.v1.PublishModelRequest)
  })
_sym_db.RegisterMessage(PublishModelRequest)
_sym_db.RegisterMessage(PublishModelRequest.CloudSecretEntry)
_sym_db.RegisterMessage(PublishModelRequest.DockerRegistrySecretEntry)

PublishModelResponse = _reflection.GeneratedProtocolMessageType('PublishModelResponse', (_message.Message,), {
  'DESCRIPTOR' : _PUBLISHMODELRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.publisherd.v1.publisherd_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.publisherd.v1.PublishModelResponse)
  })
_sym_db.RegisterMessage(PublishModelResponse)

PackageModelRequest = _reflection.GeneratedProtocolMessageType('PackageModelRequest', (_message.Message,), {

  'CloudSecretEntry' : _reflection.GeneratedProtocolMessageType('CloudSecretEntry', (_message.Message,), {
    'DESCRIPTOR' : _PACKAGEMODELREQUEST_CLOUDSECRETENTRY,
    '__module__' : 'github.com.metaprov.modelaapi.services.publisherd.v1.publisherd_pb2'
    # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.publisherd.v1.PackageModelRequest.CloudSecretEntry)
    })
  ,
  'DESCRIPTOR' : _PACKAGEMODELREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.publisherd.v1.publisherd_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.publisherd.v1.PackageModelRequest)
  })
_sym_db.RegisterMessage(PackageModelRequest)
_sym_db.RegisterMessage(PackageModelRequest.CloudSecretEntry)

PackageModelResponse = _reflection.GeneratedProtocolMessageType('PackageModelResponse', (_message.Message,), {
  'DESCRIPTOR' : _PACKAGEMODELRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.publisherd.v1.publisherd_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.publisherd.v1.PackageModelResponse)
  })
_sym_db.RegisterMessage(PackageModelResponse)

ShutdownRequest = _reflection.GeneratedProtocolMessageType('ShutdownRequest', (_message.Message,), {
  'DESCRIPTOR' : _SHUTDOWNREQUEST,
  '__module__' : 'github.com.metaprov.modelaapi.services.publisherd.v1.publisherd_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.publisherd.v1.ShutdownRequest)
  })
_sym_db.RegisterMessage(ShutdownRequest)

ShutdownResponse = _reflection.GeneratedProtocolMessageType('ShutdownResponse', (_message.Message,), {
  'DESCRIPTOR' : _SHUTDOWNRESPONSE,
  '__module__' : 'github.com.metaprov.modelaapi.services.publisherd.v1.publisherd_pb2'
  # @@protoc_insertion_point(class_scope:github.com.metaprov.modelaapi.services.publisherd.v1.ShutdownResponse)
  })
_sym_db.RegisterMessage(ShutdownResponse)

_PUBLISHERDSERVICE = DESCRIPTOR.services_by_name['PublisherdService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z4github.com/metaprov/modelaapi/services/publisherd/v1'
  _PUBLISHNOTEBOOKREQUEST_SECRETENTRY._options = None
  _PUBLISHNOTEBOOKREQUEST_SECRETENTRY._serialized_options = b'8\001'
  _PUBLISHMODELREQUEST_CLOUDSECRETENTRY._options = None
  _PUBLISHMODELREQUEST_CLOUDSECRETENTRY._serialized_options = b'8\001'
  _PUBLISHMODELREQUEST_DOCKERREGISTRYSECRETENTRY._options = None
  _PUBLISHMODELREQUEST_DOCKERREGISTRYSECRETENTRY._serialized_options = b'8\001'
  _PACKAGEMODELREQUEST_CLOUDSECRETENTRY._options = None
  _PACKAGEMODELREQUEST_CLOUDSECRETENTRY._serialized_options = b'8\001'
  _PUBLISHNOTEBOOKREQUEST._serialized_start=343
  _PUBLISHNOTEBOOKREQUEST._serialized_end=726
  _PUBLISHNOTEBOOKREQUEST_SECRETENTRY._serialized_start=681
  _PUBLISHNOTEBOOKREQUEST_SECRETENTRY._serialized_end=726
  _PUBLISHNOTEBOOKRESPONSE._serialized_start=728
  _PUBLISHNOTEBOOKRESPONSE._serialized_end=772
  _PUBLISHMODELREQUEST._serialized_start=775
  _PUBLISHMODELREQUEST._serialized_end=2032
  _PUBLISHMODELREQUEST_CLOUDSECRETENTRY._serialized_start=1921
  _PUBLISHMODELREQUEST_CLOUDSECRETENTRY._serialized_end=1971
  _PUBLISHMODELREQUEST_DOCKERREGISTRYSECRETENTRY._serialized_start=1973
  _PUBLISHMODELREQUEST_DOCKERREGISTRYSECRETENTRY._serialized_end=2032
  _PUBLISHMODELRESPONSE._serialized_start=2034
  _PUBLISHMODELRESPONSE._serialized_end=2089
  _PACKAGEMODELREQUEST._serialized_start=2092
  _PACKAGEMODELREQUEST._serialized_end=2966
  _PACKAGEMODELREQUEST_CLOUDSECRETENTRY._serialized_start=1921
  _PACKAGEMODELREQUEST_CLOUDSECRETENTRY._serialized_end=1971
  _PACKAGEMODELRESPONSE._serialized_start=2968
  _PACKAGEMODELRESPONSE._serialized_end=3020
  _SHUTDOWNREQUEST._serialized_start=3022
  _SHUTDOWNREQUEST._serialized_end=3039
  _SHUTDOWNRESPONSE._serialized_start=3041
  _SHUTDOWNRESPONSE._serialized_end=3059
  _PUBLISHERDSERVICE._serialized_start=3062
  _PUBLISHERDSERVICE._serialized_end=3758
# @@protoc_insertion_point(module_scope)
