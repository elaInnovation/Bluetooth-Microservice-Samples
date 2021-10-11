# System import
import grpc
from concurrent import futures
import time
import threading

# Protos import
from bluetooth.Protos.Bluetooth import ElaBluetoothPublicAPI_pb2
from bluetooth.Protos.Bluetooth import ElaBluetoothPublicAPI_pb2_grpc
from bluetooth.Protos.Authentication import ElaAuthenticationCommon_pb2
from bluetooth.Protos.Bluetooth import ElaBluetoothCommon_pb2
from BaseAuthen import ClientBase

class BluetoothClient():
    """
    Bluetooth Client Class
    """
    channel = None
    stub = None
    
    filter = ElaBluetoothCommon_pb2.ElaBluetoothFilter(
            filter_match_string="",
            filter_white_list="",
            filter_maximum_rssi=0,
            filter_only_manufacturer_id=False,
            filter_only_connectable=False,
            filter_type=ElaBluetoothCommon_pb2.ElaBluetoothFilter.FilterType.No_Option)
            
    #ELA_LOGIN = "elainnovation"
    #ELA_CERTIFICATE = "{\"data\":\"4e2aaabf6d91030218dc624821d38a6b2bbbfd329e8543af1ce1882589aa3e7ad640bc03e91033ddce426e7deba6548536de0f647760635090eaed9b1264701f4cf498c14007daec747f59ff6b5b5ee88d7563b49455fa51d45e9c89ee8ac03ad27a83e307b5301aa508bbad78ab512759c3ad95ee24187e097c797c638d105d\",\"sign\":\"bdee89baafa0a6f2db0206f16e0d14a657d8d6e10221571f9b998ca4c47d3b0ff5b8de770d046d52b1fa271908c61c0df6e4db83c3c217a233a8e74c5524a85f9affdd6d522588a167a0e7936e857f77c85c1da61f98a0461c8e6c80b836142a1f88115f74fdfb4de80b497bbe40a996b2172462482466493c636abe4099e500\"}"
    ELA_LOGIN = "admin"
    ELA_CERTIFICATE = "ElaSuperUser42"
        
    def __init__(self):
        """
        Init grpc connection
        """
        self.channel = grpc.insecure_channel('127.0.0.1:50051')
        self.stub = ElaBluetoothPublicAPI_pb2_grpc.ElaBluetoothPublicServiceStub(self.channel)
        self.data_list = []

    def startDataFlow(self):
        try:
          stream = self.stub.StartBluetoothDataFlow(ClientBase.getInstance().getRequest())

          def _cancel_after_a_while():
              time.sleep(5)
              stream.cancel()

          cancellation_thread = threading.Thread(target=_cancel_after_a_while)
          cancellation_thread.start()

          if(stream.is_active()):
            for event in stream:
              #print(event)
              self.data_list.append(event)
          return True
        except grpc.RpcError as rpc_error:
          if rpc_error.code() == grpc.StatusCode.CANCELLED:
            return True
          else:
            return False
          
        
    def login(self):
        """
        Connect and get sessionId of server
        """
        try:
            print("hello login")
            request = ElaAuthenticationCommon_pb2.ElaAuthenticationRequest(
                request = ClientBase.getInstance().getRequest(),
                login = self.ELA_LOGIN,
                certificate = self.ELA_CERTIFICATE)
                
            print("hello connect")
            status = self.stub.Connect(request)            
            ClientBase.getInstance().setSessionId(status)
            print(status)
            return True
        except Exception as e:
            print(e)
            return False

    def logout(self):
        """
        Disconnect from server  
        """
        try:
            status = self.stub.Disconnect(ClientBase.getInstance().getRequest())
            return True
        except Exception as e:
            return False

    def scan(self):
        """
        Start scan Bluetooth
        """
        try:
            request = ElaBluetoothPublicAPI_pb2.ElaBluetoothScanningRequest(
                request = ClientBase.getInstance().getRequest(),
                filter = self.filter,
                define_scan_time = False,
                scan_time_seconds = 0)
            
            status = self.stub.StartBluetoothListening(request = request)
            return True
        except Exception as e:
            return False
        
    def stopScan(self):
        """
        Stop scan bluetooth scan
        """
        try:
            status = self.stub.StopBluetoothListening(request = ClientBase.getInstance().getRequest())
            return True
        except Exception as e:
            return False
        
    def askData(self):
        """
        Get Data from the micro-servicer
        """
        try:
            data = self.stub.GetScannedDevices(ClientBase.getInstance().getRequest())
            return data
        except Exception as e:
            return False

    def updateFilterToNoFilter(self):
        """
        Remove all filter
        """
        try:
            self.filter.filter_type = ElaBluetoothCommon_pb2.ElaBluetoothFilter.FilterType.No_Option
            return True
        except Exception as e:
            return False
        
    def updateFilterToName(self,arg):
        """
        Update filter String
        """
        try:
            self.filter.filter_match_string = arg
            self.filter.filter_type = ElaBluetoothCommon_pb2.ElaBluetoothFilter.FilterType.Match_String
            return True
        except Exception as e:
            return False
        
    def updateFilterRssi(self,arg):
        """
        Update filter Rssi max
        """
        try:
            self.filter.filter_maximum_rssi = arg
            self.filter.filter_type = ElaBluetoothCommon_pb2.ElaBluetoothFilter.FilterType.Maximum_Rssi
            return True
        except Exception as e:
            return False
        
    def updateFilterMfrId(self):
        """
        Update filter Rssi max
        """
        try:
            self.filter.filter_only_manufacturer_id = True
            self.filter.filter_type = ElaBluetoothCommon_pb2.ElaBluetoothFilter.FilterType.Manufacturer_ID
            return True
        except Exception as e:
            return False

    def sendCommand(self,mac,cmd,pwd):
        """
        Connect to a tag and send a command to him
        """ 
        try:
            requestData = ElaBluetoothPublicAPI_pb2.ElaBluetoothConnectRequest(
                request = ClientBase.getInstance().getRequest(),
                target_mac_address = mac,
                ela_command = cmd,
                ela_command_password = pwd,
                ela_command_arguments = "",
                isLongWaitCommand = True)
            data = self.stub.SendElaBluetoothCommand(requestData)
            return data.result
        except Exception as e:
            return False

    

