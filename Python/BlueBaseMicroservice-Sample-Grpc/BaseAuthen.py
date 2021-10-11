

# System import
import grpc
from concurrent import futures
import time
import sys

# Protos import
from bluetooth.Protos.Common import ElaCommon_pb2
from bluetooth.Protos.Authentication import ElaAuthenticationCommon_pb2

class ClientBase:
    """
    Client base Class
    """
    __instance = None
    __server = None
    
    clientId = "1"
    sessionId = "1"
    requestId = 0
    
    @staticmethod
    def getInstance():
        """
        Singleton
        """
        if(ClientBase.__instance == None):
            ClientBase()
        return ClientBase.__instance
        
    def __init__(self):
        """
        Init function of the client
        """
        if(ClientBase.__instance != None):
            raise Exception("This class is a singleton")
        else:
            ClientBase.__instance = self
            
    def getRequest(self):
        """
        Get Base Request for scan
        """
        self.requestId += 1
        request = ElaCommon_pb2.ElaInputBaseRequest(
            client_id=self.clientId,
            session_id=self.sessionId,
            request_id=str(self.requestId))
        return request
    
    def setSessionId(self, status):
        """
        Override session Id
        """
        if(None == status):
            return False
        else:
            self.sessionId = status.sessionId