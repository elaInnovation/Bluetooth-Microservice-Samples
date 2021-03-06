# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from bluetooth.Protos.Authentication import ElaAuthenticationCommon_pb2 as Protos_dot_Authentication_dot_ElaAuthenticationCommon__pb2
from bluetooth.Protos.Bluetooth import ElaBluetoothCommon_pb2 as Protos_dot_Bluetooth_dot_ElaBluetoothCommon__pb2
from bluetooth.Protos.Bluetooth import ElaBluetoothPublicAPI_pb2 as Protos_dot_Bluetooth_dot_ElaBluetoothPublicAPI__pb2
from bluetooth.Protos.Common import ElaCommon_pb2 as Protos_dot_Common_dot_ElaCommon__pb2


class ElaBluetoothPublicServiceStub(object):
    """The BackendConfig service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Connect = channel.unary_unary(
                '/ElaBluetooth.ElaBluetoothPublicService/Connect',
                request_serializer=Protos_dot_Authentication_dot_ElaAuthenticationCommon__pb2.ElaAuthenticationRequest.SerializeToString,
                response_deserializer=Protos_dot_Authentication_dot_ElaAuthenticationCommon__pb2.ElaAuthenticationResponse.FromString,
                )
        self.Disconnect = channel.unary_unary(
                '/ElaBluetooth.ElaBluetoothPublicService/Disconnect',
                request_serializer=Protos_dot_Common_dot_ElaCommon__pb2.ElaInputBaseRequest.SerializeToString,
                response_deserializer=Protos_dot_Common_dot_ElaCommon__pb2.ElaError.FromString,
                )
        self.StartBluetoothListening = channel.unary_unary(
                '/ElaBluetooth.ElaBluetoothPublicService/StartBluetoothListening',
                request_serializer=Protos_dot_Bluetooth_dot_ElaBluetoothPublicAPI__pb2.ElaBluetoothScanningRequest.SerializeToString,
                response_deserializer=Protos_dot_Common_dot_ElaCommon__pb2.ElaError.FromString,
                )
        self.GetScannedDevices = channel.unary_unary(
                '/ElaBluetooth.ElaBluetoothPublicService/GetScannedDevices',
                request_serializer=Protos_dot_Common_dot_ElaCommon__pb2.ElaInputBaseRequest.SerializeToString,
                response_deserializer=Protos_dot_Bluetooth_dot_ElaBluetoothCommon__pb2.ElaBluetoothScanResults.FromString,
                )
        self.StopBluetoothListening = channel.unary_unary(
                '/ElaBluetooth.ElaBluetoothPublicService/StopBluetoothListening',
                request_serializer=Protos_dot_Common_dot_ElaCommon__pb2.ElaInputBaseRequest.SerializeToString,
                response_deserializer=Protos_dot_Common_dot_ElaCommon__pb2.ElaError.FromString,
                )
        self.StartBluetoothDataFlow = channel.unary_stream(
                '/ElaBluetooth.ElaBluetoothPublicService/StartBluetoothDataFlow',
                request_serializer=Protos_dot_Bluetooth_dot_ElaBluetoothPublicAPI__pb2.ElaBluetoothScanningRequest.SerializeToString,
                response_deserializer=Protos_dot_Bluetooth_dot_ElaBluetoothCommon__pb2.ElaBluetoothScanResultItem.FromString,
                )
        self.StopBluetoothDataFlow = channel.unary_unary(
                '/ElaBluetooth.ElaBluetoothPublicService/StopBluetoothDataFlow',
                request_serializer=Protos_dot_Common_dot_ElaCommon__pb2.ElaInputBaseRequest.SerializeToString,
                response_deserializer=Protos_dot_Common_dot_ElaCommon__pb2.ElaError.FromString,
                )
        self.SendElaBluetoothCommand = channel.unary_unary(
                '/ElaBluetooth.ElaBluetoothPublicService/SendElaBluetoothCommand',
                request_serializer=Protos_dot_Bluetooth_dot_ElaBluetoothPublicAPI__pb2.ElaBluetoothConnectRequest.SerializeToString,
                response_deserializer=Protos_dot_Bluetooth_dot_ElaBluetoothPublicAPI__pb2.ElaBluetoothConnectResult.FromString,
                )
        self.GetServiceStatus = channel.unary_unary(
                '/ElaBluetooth.ElaBluetoothPublicService/GetServiceStatus',
                request_serializer=Protos_dot_Common_dot_ElaCommon__pb2.ElaInputBaseRequest.SerializeToString,
                response_deserializer=Protos_dot_Bluetooth_dot_ElaBluetoothPublicAPI__pb2.ElaBluetoothMicroserviceStatus.FromString,
                )
        self.GetLogInformations = channel.unary_unary(
                '/ElaBluetooth.ElaBluetoothPublicService/GetLogInformations',
                request_serializer=Protos_dot_Common_dot_ElaCommon__pb2.ElaLogRequest.SerializeToString,
                response_deserializer=Protos_dot_Common_dot_ElaCommon__pb2.ElaLogResponse.FromString,
                )
        self.SetUserInformations = channel.unary_unary(
                '/ElaBluetooth.ElaBluetoothPublicService/SetUserInformations',
                request_serializer=Protos_dot_Common_dot_ElaCommon__pb2.ElaUserInformationsRequest.SerializeToString,
                response_deserializer=Protos_dot_Common_dot_ElaCommon__pb2.ElaError.FromString,
                )
        self.SetConfiguration = channel.unary_unary(
                '/ElaBluetooth.ElaBluetoothPublicService/SetConfiguration',
                request_serializer=Protos_dot_Common_dot_ElaCommon__pb2.ElaConfigurationRequest.SerializeToString,
                response_deserializer=Protos_dot_Common_dot_ElaCommon__pb2.ElaError.FromString,
                )


class ElaBluetoothPublicServiceServicer(object):
    """The BackendConfig service definition.
    """

    def Connect(self, request, context):
        """authentication functions
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Disconnect(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StartBluetoothListening(self, request, context):
        """bluetooth scanning
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetScannedDevices(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StopBluetoothListening(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StartBluetoothDataFlow(self, request, context):
        """bluetooth scanning streaming
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StopBluetoothDataFlow(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendElaBluetoothCommand(self, request, context):
        """bluetooth connections
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetServiceStatus(self, request, context):
        """monitoring
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLogInformations(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetUserInformations(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetConfiguration(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ElaBluetoothPublicServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Connect': grpc.unary_unary_rpc_method_handler(
                    servicer.Connect,
                    request_deserializer=Protos_dot_Authentication_dot_ElaAuthenticationCommon__pb2.ElaAuthenticationRequest.FromString,
                    response_serializer=Protos_dot_Authentication_dot_ElaAuthenticationCommon__pb2.ElaAuthenticationResponse.SerializeToString,
            ),
            'Disconnect': grpc.unary_unary_rpc_method_handler(
                    servicer.Disconnect,
                    request_deserializer=Protos_dot_Common_dot_ElaCommon__pb2.ElaInputBaseRequest.FromString,
                    response_serializer=Protos_dot_Common_dot_ElaCommon__pb2.ElaError.SerializeToString,
            ),
            'StartBluetoothListening': grpc.unary_unary_rpc_method_handler(
                    servicer.StartBluetoothListening,
                    request_deserializer=Protos_dot_Bluetooth_dot_ElaBluetoothPublicAPI__pb2.ElaBluetoothScanningRequest.FromString,
                    response_serializer=Protos_dot_Common_dot_ElaCommon__pb2.ElaError.SerializeToString,
            ),
            'GetScannedDevices': grpc.unary_unary_rpc_method_handler(
                    servicer.GetScannedDevices,
                    request_deserializer=Protos_dot_Common_dot_ElaCommon__pb2.ElaInputBaseRequest.FromString,
                    response_serializer=Protos_dot_Bluetooth_dot_ElaBluetoothCommon__pb2.ElaBluetoothScanResults.SerializeToString,
            ),
            'StopBluetoothListening': grpc.unary_unary_rpc_method_handler(
                    servicer.StopBluetoothListening,
                    request_deserializer=Protos_dot_Common_dot_ElaCommon__pb2.ElaInputBaseRequest.FromString,
                    response_serializer=Protos_dot_Common_dot_ElaCommon__pb2.ElaError.SerializeToString,
            ),
            'StartBluetoothDataFlow': grpc.unary_stream_rpc_method_handler(
                    servicer.StartBluetoothDataFlow,
                    request_deserializer=Protos_dot_Bluetooth_dot_ElaBluetoothPublicAPI__pb2.ElaBluetoothScanningRequest.FromString,
                    response_serializer=Protos_dot_Bluetooth_dot_ElaBluetoothCommon__pb2.ElaBluetoothScanResultItem.SerializeToString,
            ),
            'StopBluetoothDataFlow': grpc.unary_unary_rpc_method_handler(
                    servicer.StopBluetoothDataFlow,
                    request_deserializer=Protos_dot_Common_dot_ElaCommon__pb2.ElaInputBaseRequest.FromString,
                    response_serializer=Protos_dot_Common_dot_ElaCommon__pb2.ElaError.SerializeToString,
            ),
            'SendElaBluetoothCommand': grpc.unary_unary_rpc_method_handler(
                    servicer.SendElaBluetoothCommand,
                    request_deserializer=Protos_dot_Bluetooth_dot_ElaBluetoothPublicAPI__pb2.ElaBluetoothConnectRequest.FromString,
                    response_serializer=Protos_dot_Bluetooth_dot_ElaBluetoothPublicAPI__pb2.ElaBluetoothConnectResult.SerializeToString,
            ),
            'GetServiceStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.GetServiceStatus,
                    request_deserializer=Protos_dot_Common_dot_ElaCommon__pb2.ElaInputBaseRequest.FromString,
                    response_serializer=Protos_dot_Bluetooth_dot_ElaBluetoothPublicAPI__pb2.ElaBluetoothMicroserviceStatus.SerializeToString,
            ),
            'GetLogInformations': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLogInformations,
                    request_deserializer=Protos_dot_Common_dot_ElaCommon__pb2.ElaLogRequest.FromString,
                    response_serializer=Protos_dot_Common_dot_ElaCommon__pb2.ElaLogResponse.SerializeToString,
            ),
            'SetUserInformations': grpc.unary_unary_rpc_method_handler(
                    servicer.SetUserInformations,
                    request_deserializer=Protos_dot_Common_dot_ElaCommon__pb2.ElaUserInformationsRequest.FromString,
                    response_serializer=Protos_dot_Common_dot_ElaCommon__pb2.ElaError.SerializeToString,
            ),
            'SetConfiguration': grpc.unary_unary_rpc_method_handler(
                    servicer.SetConfiguration,
                    request_deserializer=Protos_dot_Common_dot_ElaCommon__pb2.ElaConfigurationRequest.FromString,
                    response_serializer=Protos_dot_Common_dot_ElaCommon__pb2.ElaError.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ElaBluetooth.ElaBluetoothPublicService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ElaBluetoothPublicService(object):
    """The BackendConfig service definition.
    """

    @staticmethod
    def Connect(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ElaBluetooth.ElaBluetoothPublicService/Connect',
            Protos_dot_Authentication_dot_ElaAuthenticationCommon__pb2.ElaAuthenticationRequest.SerializeToString,
            Protos_dot_Authentication_dot_ElaAuthenticationCommon__pb2.ElaAuthenticationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Disconnect(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ElaBluetooth.ElaBluetoothPublicService/Disconnect',
            Protos_dot_Common_dot_ElaCommon__pb2.ElaInputBaseRequest.SerializeToString,
            Protos_dot_Common_dot_ElaCommon__pb2.ElaError.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StartBluetoothListening(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ElaBluetooth.ElaBluetoothPublicService/StartBluetoothListening',
            Protos_dot_Bluetooth_dot_ElaBluetoothPublicAPI__pb2.ElaBluetoothScanningRequest.SerializeToString,
            Protos_dot_Common_dot_ElaCommon__pb2.ElaError.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetScannedDevices(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ElaBluetooth.ElaBluetoothPublicService/GetScannedDevices',
            Protos_dot_Common_dot_ElaCommon__pb2.ElaInputBaseRequest.SerializeToString,
            Protos_dot_Bluetooth_dot_ElaBluetoothCommon__pb2.ElaBluetoothScanResults.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StopBluetoothListening(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ElaBluetooth.ElaBluetoothPublicService/StopBluetoothListening',
            Protos_dot_Common_dot_ElaCommon__pb2.ElaInputBaseRequest.SerializeToString,
            Protos_dot_Common_dot_ElaCommon__pb2.ElaError.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StartBluetoothDataFlow(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/ElaBluetooth.ElaBluetoothPublicService/StartBluetoothDataFlow',
            Protos_dot_Bluetooth_dot_ElaBluetoothPublicAPI__pb2.ElaBluetoothScanningRequest.SerializeToString,
            Protos_dot_Bluetooth_dot_ElaBluetoothCommon__pb2.ElaBluetoothScanResultItem.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StopBluetoothDataFlow(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ElaBluetooth.ElaBluetoothPublicService/StopBluetoothDataFlow',
            Protos_dot_Common_dot_ElaCommon__pb2.ElaInputBaseRequest.SerializeToString,
            Protos_dot_Common_dot_ElaCommon__pb2.ElaError.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendElaBluetoothCommand(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ElaBluetooth.ElaBluetoothPublicService/SendElaBluetoothCommand',
            Protos_dot_Bluetooth_dot_ElaBluetoothPublicAPI__pb2.ElaBluetoothConnectRequest.SerializeToString,
            Protos_dot_Bluetooth_dot_ElaBluetoothPublicAPI__pb2.ElaBluetoothConnectResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetServiceStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ElaBluetooth.ElaBluetoothPublicService/GetServiceStatus',
            Protos_dot_Common_dot_ElaCommon__pb2.ElaInputBaseRequest.SerializeToString,
            Protos_dot_Bluetooth_dot_ElaBluetoothPublicAPI__pb2.ElaBluetoothMicroserviceStatus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetLogInformations(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ElaBluetooth.ElaBluetoothPublicService/GetLogInformations',
            Protos_dot_Common_dot_ElaCommon__pb2.ElaLogRequest.SerializeToString,
            Protos_dot_Common_dot_ElaCommon__pb2.ElaLogResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetUserInformations(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ElaBluetooth.ElaBluetoothPublicService/SetUserInformations',
            Protos_dot_Common_dot_ElaCommon__pb2.ElaUserInformationsRequest.SerializeToString,
            Protos_dot_Common_dot_ElaCommon__pb2.ElaError.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetConfiguration(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ElaBluetooth.ElaBluetoothPublicService/SetConfiguration',
            Protos_dot_Common_dot_ElaCommon__pb2.ElaConfigurationRequest.SerializeToString,
            Protos_dot_Common_dot_ElaCommon__pb2.ElaError.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
