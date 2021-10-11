
from bluetooth.BluetoothClient import BluetoothClient
import threading

class BluetoothController():
    """description of class"""

    # Bluetooth client
    bluetoothClient = BluetoothClient()

    IsScanning = False

    def Login(self):
        """
        Login to the µS
        """
        if(self.bluetoothClient.login()):
            return True
        else:
            return False

    def Logout(self):
        """
        Logout to the µS
        """
        if(self.bluetoothClient.logout()):
            return True
        else:
            return False

    def StartScanner(self):
        """
        Start scanner
        """
        if(self.IsScanning):
            return False
        if(self.bluetoothClient.scan()):
            self.IsScanning = True
            return True
        else:
            return False

    def StopScanner(self):
        """
        Stop scanner
        """
        if(self.IsScanning == False):
            return False
        if(self.bluetoothClient.stopScan()):
            self.IsScanning = False
            return True
        else:
            return False

    def GetData(self):
        """
        Get data frm µS
        """
        if(self.IsScanning == False):
            return False
        data = self.bluetoothClient.askData()
        if(data != False):
            return data
        else:
            return False
            
    def UpdateFilterName(self,filter):
        """
        Update filter name
        """
        if(self.bluetoothClient.updateFilterToName(filter)):
            return True
        else:
            return False

    def SendCommand(self,mac,cmd,pwd):
        """
        Send a command to the tag
        """
        data = self.bluetoothClient.sendCommand(mac,cmd,pwd)
        if(data != False):
            return data
        else:
            return False

    def StartScanStreaming(self):
      """
      Start a streaming data flow
      """
      if(self.IsScanning == False):
            return False
      if(self.bluetoothClient.startDataFlow()):
            return True
      else:
          return False

    def getDataFlow(self):
      """
      Get all data in the streaming
      """
      return self.bluetoothClient.data_list
      
