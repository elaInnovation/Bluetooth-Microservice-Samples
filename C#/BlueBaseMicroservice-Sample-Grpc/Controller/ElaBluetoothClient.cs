using BlueBaseMicroservice_Sample.Model;
using ElaBluetooth;
using ElaCommon;
using ElaSoftwareCommon.Error;
using System;
using System.Collections.Generic;
using System.Text;
using System.Threading;
using static ElaBluetooth.ElaBluetoothPublicService;

namespace BlueBaseMicroservice_Sample.Controller
{
    /** \brief delegate fot data received */
    public delegate void BluetoothPacketReceivedEventHandler(object sender, ElaBluetoothScanResultItem packet);

    /**
    * \class ElaBluetoothClient
    * \brief Bluetooth client implementation
    */
    public class ElaBluetoothClient : ElaGrpcClientBase
    {
        // constant definition
        private const String CONNECTED_COMMAND_FAIL = "NO_RESULT";

        /** \brief ble client definition */
        private ElaBluetoothPublicServiceClient BleClient
        {
            get => m_GrpcClient as ElaBluetoothPublicServiceClient;
        }

        /** \brief event for bluetooth device received */
        public event BluetoothPacketReceivedEventHandler evBluetoothPacketReceived;

        /** \brief streaming cancellation token **/
        private CancellationTokenSource CancellationToken = new CancellationTokenSource();

        /** \brief constructor */
        public ElaBluetoothClient() : base() { }

        protected override void CreateGrpcClient(uint channelTestResult)
        {
            if (channelTestResult == ErrorServiceHandlerBase.ERR_OK)
                m_GrpcClient = new ElaBluetoothPublicServiceClient(m_Channel);
            else
                m_GrpcClient = null;
        }

        #region bluetooth functions

        /**
        * \fn StartListening
        * \brief start bluetooth scanner on the target service
        * \return error code 
        */
        public uint StartListening(ElaBluetoothFilter bleFilter)
        {
            try
            {
                if (null == this.BleClient) throw new ElaSoftwareCommonException(ErrorServiceHandlerClient.ERR_CLIENT_NOT_CONNECTED);
                //
                ElaBluetoothScanningRequest request = new ElaBluetoothScanningRequest();
                request.Request = getBleRequest();
                //
                request.Filter = bleFilter;
                //
                request.DefineScanTime = false;
                request.ScanTimeSeconds = 15; // Todo: link to UI
                if (request.ScanTimeSeconds != 0)
                {
                    request.DefineScanTime = true;
                }
                //
                ElaError error = this.BleClient.StartBluetoothListening(request);
                if (ErrorServiceHandlerBase.ERR_OK != error.Error)
                    this.m_strLastErrorMessage = ErrorServiceHandlerBase.getErrorMessage(error.Error);
                //
                return error.Error;
            }
            catch (Exception ex)
            {
                return HandleClientException(ex);
            }
        }

        /**
        * \fn GetScannedDevices
        * \brief getter on the scan result devices
        * \return list of scan result devices
        */
        public List<ElaBluetoothScanResultItem> GetScannedDevices()
        {
            try
            {
                if (null == this.BleClient) throw new ElaSoftwareCommonException(ErrorServiceHandlerClient.ERR_CLIENT_NOT_CONNECTED);
                //
                List<ElaBluetoothScanResultItem> resuls_items = new List<ElaBluetoothScanResultItem>();
                ElaInputBaseRequest request = getBleRequest();
                //
                ElaBluetoothScanResults result = this.BleClient.GetScannedDevices(request);
                if (ErrorServiceHandlerBase.ERR_OK == result.Error.Error)
                {
                    if (null != result.Scanned)
                    {
                        foreach (ElaBluetoothScanResultItem item in result.Scanned.Results)
                        {
                            resuls_items.Add(item);
                        }
                    }
                }
                else
                    this.m_strLastErrorMessage = ErrorServiceHandlerBase.getErrorMessage(result.Error.Error);

                return resuls_items;
            }
            catch (Exception ex)
            {
                HandleClientException(ex);
                return new List<ElaBluetoothScanResultItem>();

            }
        }

        /**
        * \fn StopListening
        * \brief stop bluetooth listening 
        * \return error code
        */
        public uint StopListening()
        {
            try
            {
                if (null == this.BleClient) throw new ElaSoftwareCommonException(ErrorServiceHandlerClient.ERR_CLIENT_NOT_CONNECTED);
                //
                ElaInputBaseRequest request = new ElaInputBaseRequest();
                request = getBleRequest();

                ElaError error = this.BleClient.StopBluetoothListening(request);
                return error.Error;
            }
            catch (Exception ex)
            {
                return HandleClientException(ex);
            }
        }

        /**
        * \fn SendCommand
        * \brief send connect command to the micro service
        * \param [in] deviceID : target mac address
        * \param [in] command : formatted command
        * \return error code
        */
        public BluetoothResults SendCommand(string macAddress, string command, String password = "", String arguments = "", bool isLongWaitCommand = false)
        {
            ElaBluetoothConnectResult result = new ElaBluetoothConnectResult();

            try
            {
                if (null == this.BleClient) throw new ElaSoftwareCommonException(ErrorServiceHandlerClient.ERR_CLIENT_NOT_CONNECTED);
                if (String.IsNullOrEmpty(macAddress)) throw new ElaSoftwareCommonException(ErrorServiceHandlerClient.ERR_BLUETOOTH_EMPTY_MAC_ADDRESS);
                if (String.IsNullOrEmpty(command)) throw new ElaSoftwareCommonException(ErrorServiceHandlerClient.ERR_BLUETOOTH_COMMAND_EMPTY);
                //
                ElaBluetoothConnectRequest connectRequest = new ElaBluetoothConnectRequest();
                connectRequest.TargetMacAddress = macAddress;
                connectRequest.ElaCommand = command;
                connectRequest.ElaCommandPassword = password;
                connectRequest.ElaCommandArguments = arguments;
                connectRequest.IsLongWaitCommand = isLongWaitCommand;
                connectRequest.Request = getBleRequest();
                //
                result = this.BleClient.SendElaBluetoothCommand(connectRequest);
            }
            catch (Exception ex)
            {
                uint error = HandleClientException(ex);
                result.Result = CONNECTED_COMMAND_FAIL;
                result.Error.Error = error;
            }

            return new BluetoothResults(result.Error.Error, result.Result);
        }

        /**
        * \fn GetStatusService
        * \brief getter on the micro service status
        * \return micro service status
        */
        public ElaBluetoothMicroserviceStatus GetStatusService()
        {
            try
            {
                ElaBluetoothMicroserviceStatus status = new ElaBluetoothMicroserviceStatus();
                //
                if (null == this.BleClient) throw new ElaSoftwareCommonException(ErrorServiceHandlerClient.ERR_CLIENT_NOT_CONNECTED);
                //
                ElaInputBaseRequest request = getBleRequest();
                status = this.BleClient.GetServiceStatus(request);
                //
                return status;
            }
            catch (Exception ex)
            {
                ElaBluetoothMicroserviceStatus status = new ElaBluetoothMicroserviceStatus();
                status.LastError = new ElaError();
                status.LastError.LastErrorMessage = ex.Message;
                status.LastError.LastExceptionMessage = ex.InnerException?.Message;
                status.LastError.Error = ErrorServiceHandlerClient.ERR_UNHANDLED_EXCEPTION;
                this.m_strLastErrorMessage = ex.Message;
                return status;
            }
        }

        public uint SetUserInformation(string description, string informations, string username, string gpscoordinate)
        {
            try
            {
                if (null == this.BleClient) throw new ElaSoftwareCommonException(ErrorServiceHandlerClient.ERR_CLIENT_NOT_CONNECTED);
                //
                ElaUserInformationsRequest request = new ElaUserInformationsRequest();
                request.Request = getBleRequest();
                request.UserInformation = new ServiceInformations();
                request.UserInformation.UserSpecificDescription = description;
                request.UserInformation.UserSpecificInformations = informations;
                request.UserInformation.UserSpecificName = username;
                request.UserInformation.UserSpecificGpsCoordinate = gpscoordinate;
                //
                ElaError error = this.BleClient.SetUserInformations(request);
                //
                return error.Error;
            }
            catch (Exception ex)
            {
                return HandleClientException(ex);
            }
        }

        public List<string> getLog()
        {
            List<string> logs = new List<string>();

            try
            {
                return getLog(-1);
            }
            catch (Exception ex)
            {
                HandleClientException(ex);
                return logs;
            }
        }

        public List<string> getLog(int num_last_values_desired)
        {
            List<string> logs = new List<string>();

            try
            {
                if (null == this.BleClient) throw new ElaSoftwareCommonException(ErrorServiceHandlerClient.ERR_CLIENT_NOT_CONNECTED);
                //
                ElaLogRequest request = new ElaLogRequest();
                request.Request = getBleRequest();
                request.AllValuesRequired = num_last_values_desired < 0;
                request.MaxLogValues = (num_last_values_desired < 0) ? 0 : (uint)num_last_values_desired;
                //
                ElaLogResponse response = this.BleClient.GetLogInformations(request);
                if (ErrorServiceHandlerBase.ERR_OK == response.Error.Error)
                {
                    foreach (String line in response.LogValues)
                    {
                        logs.Add(line);
                    }
                }
                else
                {
                    logs.Add($"[ElaBluetoothClient][getLog]\tCalling the function GetLog from Ble Base Server return with error code : {response.Error.Error}");
                }
                //
                return logs;
            }
            catch (Exception ex)
            {
                HandleClientException(ex);
                return logs;
            }
        }

        public uint StartBluetoothDataFlow(ElaBluetoothFilter bleFilter)
        {
            try
            {
                if (null == this.BleClient) throw new ElaSoftwareCommonException(ErrorServiceHandlerClient.ERR_CLIENT_NOT_CONNECTED);
                //
                var request = new ElaBluetoothScanningRequest()
                {
                    Request = getBleRequest(),
                    Filter = bleFilter
                };
                //
                CancellationToken = new CancellationTokenSource();
                Thread threadLocalizationResults = new Thread(StreamBleDevices);
                threadLocalizationResults.Start(request);
                //
                return ErrorServiceHandlerBase.ERR_OK;
            }
            catch (Exception ex)
            {
                return HandleClientException(ex);
            }
        }

        /**
            * \fn HandleLocalizationResults
            * \brief thread function associated for the streaming data coming from EPE
            * \param [in] data : input object, must be ErtlsRequest
            */
        private async void StreamBleDevices(object data)
        {
            try
            {
                if (data is ElaBluetoothScanningRequest request)
                {
                    using (var serverStream = BleClient.StartBluetoothDataFlow(request))
                    {
                        while (await serverStream.ResponseStream.MoveNext(CancellationToken.Token))
                        {
                            ElaBluetoothScanResultItem bluetoothPacket = serverStream.ResponseStream.Current;
                            if (null != bluetoothPacket)
                            {
                                evBluetoothPacketReceived?.Invoke(this, bluetoothPacket);
                            }
                            Thread.Sleep(10);
                        }
                    }
                }
            }
            catch (Exception ex)
            {
                HandleClientException(ex);
            }
        }

        public uint StopBluetoothDataFlow()
        {
            try
            {
                if (null == this.BleClient) throw new ElaSoftwareCommonException(ErrorServiceHandlerClient.ERR_CLIENT_NOT_CONNECTED);

                ElaError error = BleClient.StopBluetoothDataFlow(getBleRequest());
                if (error.Error == ErrorServiceHandlerBase.ERR_OK) CancellationToken.Cancel();
                return error.Error;
            }
            catch (Exception ex)
            {
                return HandleClientException(ex);
            }
        }
        #endregion
    }
}
