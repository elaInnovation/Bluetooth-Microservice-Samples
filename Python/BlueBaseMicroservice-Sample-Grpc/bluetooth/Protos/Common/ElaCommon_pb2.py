# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Protos/Common/ElaCommon.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Protos/Common/ElaCommon.proto',
  package='ElaCommon',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1dProtos/Common/ElaCommon.proto\x12\tElaCommon\"k\n\x13\x45laInputBaseRequest\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12\x12\n\nsession_id\x18\x02 \x01(\t\x12\x12\n\nrequest_id\x18\x03 \x01(\t\x12\x19\n\x11\x63lient_ip_address\x18\x04 \x01(\t\"\x9e\x01\n\x13ServiceInformations\x12\x1a\n\x12user_specific_name\x18\x01 \x01(\t\x12\"\n\x1auser_specific_informations\x18\x02 \x01(\t\x12!\n\x19user_specific_description\x18\x03 \x01(\t\x12$\n\x1cuser_specific_gps_coordinate\x18\x04 \x01(\t\"\x87\x01\n\x1a\x45laUserInformationsRequest\x12/\n\x07request\x18\x01 \x01(\x0b\x32\x1e.ElaCommon.ElaInputBaseRequest\x12\x38\n\x10user_information\x18\x02 \x01(\x0b\x32\x1e.ElaCommon.ServiceInformations\"v\n\x08\x45laError\x12\r\n\x05\x65rror\x18\x01 \x01(\r\x12\x18\n\x10lastErrorMessage\x18\x02 \x01(\t\x12\x1c\n\x14lastExceptionMessage\x18\x03 \x01(\t\x12\x10\n\x08\x63lientId\x18\x04 \x01(\t\x12\x11\n\trequestId\x18\x05 \x01(\t\"\x87\x01\n\x14\x45laMicroserviceInfos\x12\x17\n\x0fservice_version\x18\x01 \x01(\t\x12\x14\n\x0cservice_name\x18\x02 \x01(\t\x12\x15\n\rproto_version\x18\x03 \x01(\t\x12\x11\n\ttarget_OS\x18\x04 \x01(\t\x12\x16\n\x0e\x63onnector_name\x18\x05 \x01(\t\"l\n\x19\x45laMicroserviceStatistics\x12\x1b\n\x13stats_function_call\x18\x01 \x01(\t\x12\x14\n\x0cstats_timing\x18\x02 \x01(\t\x12\x1c\n\x14stats_error_handling\x18\x03 \x01(\t\"\x8e\x01\n\x13\x45laMicroserviceItem\x12\x10\n\x08hostname\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\r\x12\r\n\x05login\x18\x03 \x01(\t\x12\x10\n\x08password\x18\x04 \x01(\t\x12\x1d\n\x15microservice_username\x18\x05 \x01(\t\x12\x17\n\x0fmicroservice_id\x18\x06 \x01(\t\"s\n\rElaLogRequest\x12/\n\x07request\x18\x01 \x01(\x0b\x32\x1e.ElaCommon.ElaInputBaseRequest\x12\x19\n\x11\x41llValuesRequired\x18\x02 \x01(\x08\x12\x16\n\x0emax_log_values\x18\x03 \x01(\r\"G\n\x0e\x45laLogResponse\x12\"\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x13.ElaCommon.ElaError\x12\x11\n\tlogValues\x18\x02 \x03(\t\"r\n\x18\x45laCloseStreamingRequest\x12\"\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x13.ElaCommon.ElaError\x12 \n\x18\x63lose_steaming_requiered\x18\x02 \x01(\x08\x12\x10\n\x08\x63lientId\x18\x03 \x01(\t\"j\n\x17\x45laConfigurationRequest\x12/\n\x07request\x18\x01 \x01(\x0b\x32\x1e.ElaCommon.ElaInputBaseRequest\x12\x10\n\x08hostname\x18\x02 \x01(\t\x12\x0c\n\x04port\x18\x03 \x01(\rb\x06proto3'
)




_ELAINPUTBASEREQUEST = _descriptor.Descriptor(
  name='ElaInputBaseRequest',
  full_name='ElaCommon.ElaInputBaseRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_id', full_name='ElaCommon.ElaInputBaseRequest.client_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='session_id', full_name='ElaCommon.ElaInputBaseRequest.session_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='request_id', full_name='ElaCommon.ElaInputBaseRequest.request_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='client_ip_address', full_name='ElaCommon.ElaInputBaseRequest.client_ip_address', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=44,
  serialized_end=151,
)


_SERVICEINFORMATIONS = _descriptor.Descriptor(
  name='ServiceInformations',
  full_name='ElaCommon.ServiceInformations',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_specific_name', full_name='ElaCommon.ServiceInformations.user_specific_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_specific_informations', full_name='ElaCommon.ServiceInformations.user_specific_informations', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_specific_description', full_name='ElaCommon.ServiceInformations.user_specific_description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_specific_gps_coordinate', full_name='ElaCommon.ServiceInformations.user_specific_gps_coordinate', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=154,
  serialized_end=312,
)


_ELAUSERINFORMATIONSREQUEST = _descriptor.Descriptor(
  name='ElaUserInformationsRequest',
  full_name='ElaCommon.ElaUserInformationsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='request', full_name='ElaCommon.ElaUserInformationsRequest.request', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_information', full_name='ElaCommon.ElaUserInformationsRequest.user_information', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=315,
  serialized_end=450,
)


_ELAERROR = _descriptor.Descriptor(
  name='ElaError',
  full_name='ElaCommon.ElaError',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='ElaCommon.ElaError.error', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lastErrorMessage', full_name='ElaCommon.ElaError.lastErrorMessage', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lastExceptionMessage', full_name='ElaCommon.ElaError.lastExceptionMessage', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='clientId', full_name='ElaCommon.ElaError.clientId', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='requestId', full_name='ElaCommon.ElaError.requestId', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=452,
  serialized_end=570,
)


_ELAMICROSERVICEINFOS = _descriptor.Descriptor(
  name='ElaMicroserviceInfos',
  full_name='ElaCommon.ElaMicroserviceInfos',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='service_version', full_name='ElaCommon.ElaMicroserviceInfos.service_version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='service_name', full_name='ElaCommon.ElaMicroserviceInfos.service_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='proto_version', full_name='ElaCommon.ElaMicroserviceInfos.proto_version', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='target_OS', full_name='ElaCommon.ElaMicroserviceInfos.target_OS', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='connector_name', full_name='ElaCommon.ElaMicroserviceInfos.connector_name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=573,
  serialized_end=708,
)


_ELAMICROSERVICESTATISTICS = _descriptor.Descriptor(
  name='ElaMicroserviceStatistics',
  full_name='ElaCommon.ElaMicroserviceStatistics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='stats_function_call', full_name='ElaCommon.ElaMicroserviceStatistics.stats_function_call', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='stats_timing', full_name='ElaCommon.ElaMicroserviceStatistics.stats_timing', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='stats_error_handling', full_name='ElaCommon.ElaMicroserviceStatistics.stats_error_handling', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=710,
  serialized_end=818,
)


_ELAMICROSERVICEITEM = _descriptor.Descriptor(
  name='ElaMicroserviceItem',
  full_name='ElaCommon.ElaMicroserviceItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='hostname', full_name='ElaCommon.ElaMicroserviceItem.hostname', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='port', full_name='ElaCommon.ElaMicroserviceItem.port', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='login', full_name='ElaCommon.ElaMicroserviceItem.login', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='ElaCommon.ElaMicroserviceItem.password', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='microservice_username', full_name='ElaCommon.ElaMicroserviceItem.microservice_username', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='microservice_id', full_name='ElaCommon.ElaMicroserviceItem.microservice_id', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=821,
  serialized_end=963,
)


_ELALOGREQUEST = _descriptor.Descriptor(
  name='ElaLogRequest',
  full_name='ElaCommon.ElaLogRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='request', full_name='ElaCommon.ElaLogRequest.request', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='AllValuesRequired', full_name='ElaCommon.ElaLogRequest.AllValuesRequired', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_log_values', full_name='ElaCommon.ElaLogRequest.max_log_values', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=965,
  serialized_end=1080,
)


_ELALOGRESPONSE = _descriptor.Descriptor(
  name='ElaLogResponse',
  full_name='ElaCommon.ElaLogResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='ElaCommon.ElaLogResponse.error', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='logValues', full_name='ElaCommon.ElaLogResponse.logValues', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1082,
  serialized_end=1153,
)


_ELACLOSESTREAMINGREQUEST = _descriptor.Descriptor(
  name='ElaCloseStreamingRequest',
  full_name='ElaCommon.ElaCloseStreamingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='ElaCommon.ElaCloseStreamingRequest.error', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='close_steaming_requiered', full_name='ElaCommon.ElaCloseStreamingRequest.close_steaming_requiered', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='clientId', full_name='ElaCommon.ElaCloseStreamingRequest.clientId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1155,
  serialized_end=1269,
)


_ELACONFIGURATIONREQUEST = _descriptor.Descriptor(
  name='ElaConfigurationRequest',
  full_name='ElaCommon.ElaConfigurationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='request', full_name='ElaCommon.ElaConfigurationRequest.request', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hostname', full_name='ElaCommon.ElaConfigurationRequest.hostname', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='port', full_name='ElaCommon.ElaConfigurationRequest.port', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1271,
  serialized_end=1377,
)

_ELAUSERINFORMATIONSREQUEST.fields_by_name['request'].message_type = _ELAINPUTBASEREQUEST
_ELAUSERINFORMATIONSREQUEST.fields_by_name['user_information'].message_type = _SERVICEINFORMATIONS
_ELALOGREQUEST.fields_by_name['request'].message_type = _ELAINPUTBASEREQUEST
_ELALOGRESPONSE.fields_by_name['error'].message_type = _ELAERROR
_ELACLOSESTREAMINGREQUEST.fields_by_name['error'].message_type = _ELAERROR
_ELACONFIGURATIONREQUEST.fields_by_name['request'].message_type = _ELAINPUTBASEREQUEST
DESCRIPTOR.message_types_by_name['ElaInputBaseRequest'] = _ELAINPUTBASEREQUEST
DESCRIPTOR.message_types_by_name['ServiceInformations'] = _SERVICEINFORMATIONS
DESCRIPTOR.message_types_by_name['ElaUserInformationsRequest'] = _ELAUSERINFORMATIONSREQUEST
DESCRIPTOR.message_types_by_name['ElaError'] = _ELAERROR
DESCRIPTOR.message_types_by_name['ElaMicroserviceInfos'] = _ELAMICROSERVICEINFOS
DESCRIPTOR.message_types_by_name['ElaMicroserviceStatistics'] = _ELAMICROSERVICESTATISTICS
DESCRIPTOR.message_types_by_name['ElaMicroserviceItem'] = _ELAMICROSERVICEITEM
DESCRIPTOR.message_types_by_name['ElaLogRequest'] = _ELALOGREQUEST
DESCRIPTOR.message_types_by_name['ElaLogResponse'] = _ELALOGRESPONSE
DESCRIPTOR.message_types_by_name['ElaCloseStreamingRequest'] = _ELACLOSESTREAMINGREQUEST
DESCRIPTOR.message_types_by_name['ElaConfigurationRequest'] = _ELACONFIGURATIONREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ElaInputBaseRequest = _reflection.GeneratedProtocolMessageType('ElaInputBaseRequest', (_message.Message,), {
  'DESCRIPTOR' : _ELAINPUTBASEREQUEST,
  '__module__' : 'Protos.Common.ElaCommon_pb2'
  # @@protoc_insertion_point(class_scope:ElaCommon.ElaInputBaseRequest)
  })
_sym_db.RegisterMessage(ElaInputBaseRequest)

ServiceInformations = _reflection.GeneratedProtocolMessageType('ServiceInformations', (_message.Message,), {
  'DESCRIPTOR' : _SERVICEINFORMATIONS,
  '__module__' : 'Protos.Common.ElaCommon_pb2'
  # @@protoc_insertion_point(class_scope:ElaCommon.ServiceInformations)
  })
_sym_db.RegisterMessage(ServiceInformations)

ElaUserInformationsRequest = _reflection.GeneratedProtocolMessageType('ElaUserInformationsRequest', (_message.Message,), {
  'DESCRIPTOR' : _ELAUSERINFORMATIONSREQUEST,
  '__module__' : 'Protos.Common.ElaCommon_pb2'
  # @@protoc_insertion_point(class_scope:ElaCommon.ElaUserInformationsRequest)
  })
_sym_db.RegisterMessage(ElaUserInformationsRequest)

ElaError = _reflection.GeneratedProtocolMessageType('ElaError', (_message.Message,), {
  'DESCRIPTOR' : _ELAERROR,
  '__module__' : 'Protos.Common.ElaCommon_pb2'
  # @@protoc_insertion_point(class_scope:ElaCommon.ElaError)
  })
_sym_db.RegisterMessage(ElaError)

ElaMicroserviceInfos = _reflection.GeneratedProtocolMessageType('ElaMicroserviceInfos', (_message.Message,), {
  'DESCRIPTOR' : _ELAMICROSERVICEINFOS,
  '__module__' : 'Protos.Common.ElaCommon_pb2'
  # @@protoc_insertion_point(class_scope:ElaCommon.ElaMicroserviceInfos)
  })
_sym_db.RegisterMessage(ElaMicroserviceInfos)

ElaMicroserviceStatistics = _reflection.GeneratedProtocolMessageType('ElaMicroserviceStatistics', (_message.Message,), {
  'DESCRIPTOR' : _ELAMICROSERVICESTATISTICS,
  '__module__' : 'Protos.Common.ElaCommon_pb2'
  # @@protoc_insertion_point(class_scope:ElaCommon.ElaMicroserviceStatistics)
  })
_sym_db.RegisterMessage(ElaMicroserviceStatistics)

ElaMicroserviceItem = _reflection.GeneratedProtocolMessageType('ElaMicroserviceItem', (_message.Message,), {
  'DESCRIPTOR' : _ELAMICROSERVICEITEM,
  '__module__' : 'Protos.Common.ElaCommon_pb2'
  # @@protoc_insertion_point(class_scope:ElaCommon.ElaMicroserviceItem)
  })
_sym_db.RegisterMessage(ElaMicroserviceItem)

ElaLogRequest = _reflection.GeneratedProtocolMessageType('ElaLogRequest', (_message.Message,), {
  'DESCRIPTOR' : _ELALOGREQUEST,
  '__module__' : 'Protos.Common.ElaCommon_pb2'
  # @@protoc_insertion_point(class_scope:ElaCommon.ElaLogRequest)
  })
_sym_db.RegisterMessage(ElaLogRequest)

ElaLogResponse = _reflection.GeneratedProtocolMessageType('ElaLogResponse', (_message.Message,), {
  'DESCRIPTOR' : _ELALOGRESPONSE,
  '__module__' : 'Protos.Common.ElaCommon_pb2'
  # @@protoc_insertion_point(class_scope:ElaCommon.ElaLogResponse)
  })
_sym_db.RegisterMessage(ElaLogResponse)

ElaCloseStreamingRequest = _reflection.GeneratedProtocolMessageType('ElaCloseStreamingRequest', (_message.Message,), {
  'DESCRIPTOR' : _ELACLOSESTREAMINGREQUEST,
  '__module__' : 'Protos.Common.ElaCommon_pb2'
  # @@protoc_insertion_point(class_scope:ElaCommon.ElaCloseStreamingRequest)
  })
_sym_db.RegisterMessage(ElaCloseStreamingRequest)

ElaConfigurationRequest = _reflection.GeneratedProtocolMessageType('ElaConfigurationRequest', (_message.Message,), {
  'DESCRIPTOR' : _ELACONFIGURATIONREQUEST,
  '__module__' : 'Protos.Common.ElaCommon_pb2'
  # @@protoc_insertion_point(class_scope:ElaCommon.ElaConfigurationRequest)
  })
_sym_db.RegisterMessage(ElaConfigurationRequest)


# @@protoc_insertion_point(module_scope)