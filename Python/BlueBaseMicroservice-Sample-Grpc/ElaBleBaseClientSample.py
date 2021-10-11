## import package
import time

from bluetooth.BluetoothController import BluetoothController

controller = BluetoothController()
 
## @brief Main application entry point
def mainApp():
    # initialize and connect to client
    print("### Starting test Client Ble Base application ###")
    
    controller.Login()
    #
    # start and get data 
    controller.StartScanner()
    time.sleep(5)
    datas = controller.GetData()
    print(datas)
    #
    # stop scanner
    controller.StopScanner()
    controller.Logout()
    print("### Leaving test Client Ble Base application ###")

## @brief Main function
if __name__ == '__main__':
    mainApp()