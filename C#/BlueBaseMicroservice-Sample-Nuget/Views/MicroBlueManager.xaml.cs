using BlueBaseMicroservice_Sample.Configuration;
using BlueBaseMicroservice_Sample.Model;
using ElaBluetooth;
using elaMicroserviceClient.Core.Bluetooth.Single.Implement;
using ElaSoftwareCommon.Log;
using System;
using System.Collections.Generic;
using System.Text;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using static ElaBluetooth.ElaBluetoothFilter.Types;

namespace BlueBaseMicroservice_Sample.Views
{
    /// <summary>
    /// Logique d'interaction pour MicroBlueManager.xaml
    /// </summary>
    public partial class MicroBlueManager : UserControl
    {
        /** \brief target bluetooth client */
        private ElaBluetoothClient m_client = new ElaBluetoothClient();

        /** \brief constructor */
        public MicroBlueManager()
        {
            InitializeComponent();
            initializeConfiguration();
        }

        /** \brief initialize configuration */
        private void initializeConfiguration()
        {
            //
            this.cbbFilterOptions.Items.Add(FilterType.NoOption);
            this.cbbFilterOptions.Items.Add(FilterType.MatchString);
            this.cbbFilterOptions.Items.Add(FilterType.WhiteList);
            this.cbbFilterOptions.Items.Add(FilterType.MaximumRssi);
            //this.cbbFilterOptions.Items.Add(FilterType.ConnectableOnly);
            this.cbbFilterOptions.Items.Add(FilterType.ManufacturerId);
            this.cbbFilterOptions.SelectedIndex = 0;
        }

        /**
         * \fn getConfiguration
         * \brief getter on the tag configuration used 
         */
        public TagTemplaceMsData getConfiguration()
        {
            TagTemplaceMsData tag = new TagTemplaceMsData();
            //
            tag.mac = this.tbTag.Text;
            tag.password = this.tbPassword.Text;
            tag.command = this.tbCommand.Text;
            tag.arguments = this.tbTagArgumentsLabel.Text;
            //
            return tag;
        }

        #region event definition
        /**
         * \fn btnConnect_Click
         * \brief event on connect button
         */
        private void btnConnect_Click(object sender, RoutedEventArgs e)
        {
            try
            {
                uint errorCode = this.m_client.connect(ElaMicroConfiguration.getInstance().Settings.BluetoothConfiguration.GrpcHostName, ElaMicroConfiguration.getInstance().Settings.BluetoothConfiguration.GrpcPort);
                if (0 != errorCode)
                {
                    ElaMicroConfiguration.getInstance().Logger.add(new LogItem(String.Format("An error occur during connection : error code {0}", errorCode)));
                }
                else ElaMicroConfiguration.getInstance().Logger.add(new LogItem("Connection Established"));
            }
            catch (Exception ex)
            {
                ElaMicroConfiguration.getInstance().Logger.add(new LogItem(ex));
            }
        }

        /**
         * \fn btnConnectAuthen_Click
         * \brief event on connect with authentication button
         */
        private void btnConnectAuthen_Click(object sender, RoutedEventArgs e)
        {
            try
            {
                uint errorCode = this.m_client.login(this.tbUserName.Text, this.pwdUser.Password);
                if (0 != errorCode)
                {
                    ElaMicroConfiguration.getInstance().Logger.add(new LogItem(String.Format("Authentication Connect failed : error code {0}", errorCode)));
                }
                else ElaMicroConfiguration.getInstance().Logger.add(new LogItem("Authenticate Connect with Bluetooth Authentication Established"));
            }
            catch (Exception ex)
            {
                ElaMicroConfiguration.getInstance().Logger.add(new LogItem(ex));
            }
        }

        /**
         * \fn btnDisconnectAuthent_Click
         * \brief event on disconnect without authentication
         */
        private void btnDisconnectAuthent_Click(object sender, RoutedEventArgs e)
        {
            try
            {
                uint errorCode = this.m_client.logout();
                if (0 != errorCode)
                {
                    ElaMicroConfiguration.getInstance().Logger.add(new LogItem(String.Format("Authentication Disconnect failed : error code {0}", errorCode)));
                }
                else ElaMicroConfiguration.getInstance().Logger.add(new LogItem("Authenticate Disconnection with Bluetooth Service Success"));
            }
            catch (Exception ex)
            {
                ElaMicroConfiguration.getInstance().Logger.add(new LogItem(ex));
            }
        }

        /**
         * \fn btnStart_Click
         * \brief event start bluetooth listening
         */
        private void btnStart_Click(object sender, RoutedEventArgs e)
        {
            try
            {
                ElaBluetoothFilter bleFilter = new ElaBluetoothFilter();
                bleFilter.FilterType = (FilterType)this.cbbFilterOptions.SelectedItem;
                if (false == this.cbbFilterOptions.SelectedItem.Equals(FilterType.NoOption))
                {
                    if (this.cbbFilterOptions.SelectedItem.Equals(FilterType.MatchString)) bleFilter.FilterMatchString = this.tbMatchString.Text;
                    else if (this.cbbFilterOptions.SelectedItem.Equals(FilterType.WhiteList))
                    {
                        String[] whiteList = this.tbWhiteList.Text.Split(';');
                        foreach (String item in whiteList) if (false == item.Equals(String.Empty)) bleFilter.FilterWhiteList.Add(item);
                    }
                    else if (this.cbbFilterOptions.SelectedItem.Equals(FilterType.MaximumRssi))
                    {
                        int rssiMaxFilter = -99;
                        if (int.TryParse(this.tbRssiMaxRssi.Text, out rssiMaxFilter))
                        {
                            bleFilter.FilterMaximumRssi = rssiMaxFilter;
                        }
                    }
                    else if (this.cbbFilterOptions.SelectedItem.Equals(FilterType.ManufacturerId)) bleFilter.FilterOnlyManufacturerId = true;
                }

                uint errorCode = this.m_client.StartListening(bleFilter);
                if (0 != errorCode)
                {
                    ElaMicroConfiguration.getInstance().Logger.add(new LogItem(String.Format("Start Bluetooth Scanner failed : error code {0}", errorCode)));
                }
                else ElaMicroConfiguration.getInstance().Logger.add(new LogItem("Bluetooth Scanner Started with Success"));
            }
            catch (Exception ex)
            {
                ElaMicroConfiguration.getInstance().Logger.add(new LogItem(ex));
            }
        }

        /**
         * \fn btnStop_Click
         * \brief event stop bluetooth listening
         */
        private void btnStop_Click(object sender, RoutedEventArgs e)
        {
            try
            {
                uint errorCode = this.m_client.StopListening();
                if (0 != errorCode)
                {
                    ElaMicroConfiguration.getInstance().Logger.add(new LogItem(String.Format("Stop Bluetooth Scanner failed :  error code {0}", errorCode)));
                }
                else ElaMicroConfiguration.getInstance().Logger.add(new LogItem("Bluetooth Scanner Stoppped with Success"));
            }
            catch (Exception ex)
            {
                ElaMicroConfiguration.getInstance().Logger.add(new LogItem(ex));
            }
        }

        private void btnConnectTag_Click(object sender, RoutedEventArgs e)
        {
            //
            try
            {
                var result = this.m_client.SendCommand(this.tbTag.Text, this.tbCommand.Text, this.tbPassword.Text, this.tbArguments.Text, this.cbIsLongWaitCommand.IsChecked.Value);
                if (0 == result.ErrorCode)
                {
                    ElaMicroConfiguration.getInstance().Logger.add(new LogItem(String.Format("Result of sending command : {0}", result.Message)));
                }
                else ElaMicroConfiguration.getInstance().Logger.add(new LogItem(String.Format("An error occurs while service is sending a command to the tag  : {0} error code = {1}", this.tbTag.Text, result.ErrorCode)));
            }
            catch (Exception ex)
            {
                ElaMicroConfiguration.getInstance().Logger.add(new LogItem(ex));
            }
        }

        private void btnGetScanData_Click(object sender, RoutedEventArgs e)
        {
            try
            {
                List<ElaBluetoothScanResultItem> scan_result = this.m_client.GetScannedDevices();
                ElaMicroConfiguration.getInstance().Logger.add(new LogItem(String.Format("Number of object scanned : {0}", scan_result.Count)));
                int count = 0;
                foreach (ElaBluetoothScanResultItem item in scan_result)
                {
                    ElaMicroConfiguration.getInstance().Logger.add(new LogItem(String.Format("Item scanned {0} : timestamp={1}; mac address={2}; localname={3}; rssi={4}", count, item.TimeStamp, item.MacAddress, item.LocalName, item.Rssi)));
                    count++;
                }
            }
            catch (Exception ex)
            {
                ElaMicroConfiguration.getInstance().Logger.add(new LogItem(ex));
            }
        }

        private void btnGetStatus_Click(object sender, RoutedEventArgs e)
        {
            try
            {
                ElaBluetoothMicroserviceStatus status = this.m_client.GetStatusService();
                ElaMicroConfiguration.getInstance().Logger.add(new LogItem("**************************************************"));
                ElaMicroConfiguration.getInstance().Logger.add(new LogItem($"Service State : {status.ScannerStatus.ToString()}"));
                if (null != status.MicroserviceInfos) ElaMicroConfiguration.getInstance().Logger.add(new LogItem($"Version Service : {status.MicroserviceInfos.ServiceVersion.ToString()}"));
                if (null != status.MicroserviceInfos) ElaMicroConfiguration.getInstance().Logger.add(new LogItem($"Version Proto : {status.MicroserviceInfos.ProtoVersion.ToString()}"));
                if (null != status.MicroserviceInfos) ElaMicroConfiguration.getInstance().Logger.add(new LogItem($"Service Name : {status.MicroserviceInfos.ServiceName.ToString()}"));
                if (null != status.MicroserviceInfos) ElaMicroConfiguration.getInstance().Logger.add(new LogItem($"Target OS : {status.MicroserviceInfos.TargetOS.ToString()}"));
                if (null != status.MicroserviceInfos) ElaMicroConfiguration.getInstance().Logger.add(new LogItem($"Connector Name : {status.MicroserviceInfos.ConnectorName.ToString()}"));
                //
                if (null != status.StatisticsSummary) ElaMicroConfiguration.getInstance().Logger.add(new LogItem($"Stats Functions : {status.StatisticsSummary.StatsFunctionCall.ToString()}"));
                if (null != status.StatisticsSummary) ElaMicroConfiguration.getInstance().Logger.add(new LogItem($"Stats Timing : {status.StatisticsSummary.StatsTiming.ToString()}"));
                //
                if (null != status.CurrentFilter) ElaMicroConfiguration.getInstance().Logger.add(new LogItem($"Current Filter Type : {status.CurrentFilter.FilterType.ToString()}"));
            }
            catch (Exception ex)
            {
                ElaMicroConfiguration.getInstance().Logger.add(new LogItem(ex));
            }
        }
        #endregion

        private void btnStartDataFlow_Click(object sender, RoutedEventArgs e)
        {
            try
            {
                ElaBluetoothFilter bleFilter = new ElaBluetoothFilter();
                bleFilter.FilterType = (FilterType)this.cbbFilterOptions.SelectedItem;
                if (false == this.cbbFilterOptions.SelectedItem.Equals(FilterType.NoOption))
                {
                    if (this.cbbFilterOptions.SelectedItem.Equals(FilterType.MatchString)) bleFilter.FilterMatchString = this.tbMatchString.Text;
                    else if (this.cbbFilterOptions.SelectedItem.Equals(FilterType.WhiteList))
                    {
                        String[] whiteList = this.tbWhiteList.Text.Split(';');
                        foreach (String item in whiteList) if (false == item.Equals(String.Empty)) bleFilter.FilterWhiteList.Add(item);
                    }
                    else if (this.cbbFilterOptions.SelectedItem.Equals(FilterType.MaximumRssi))
                    {
                        int rssiMaxFilter = -99;
                        if (int.TryParse(this.tbRssiMaxRssi.Text, out rssiMaxFilter))
                        {
                            bleFilter.FilterMaximumRssi = rssiMaxFilter;
                        }
                    }
                    //else if (this.cbbFilterOptions.SelectedItem.Equals(FilterType.ConnectableOnly)) bleFilter.FilterOnlyConnectable = true;
                    else if (this.cbbFilterOptions.SelectedItem.Equals(FilterType.ManufacturerId)) bleFilter.FilterOnlyManufacturerId = true;
                }

                uint errorCode = this.m_client.StartBluetoothDataFlow(bleFilter);
                if (0 != errorCode)
                {
                    ElaMicroConfiguration.getInstance().Logger.add(new LogItem(String.Format("Start Bluetooth streaming failed : error code {0}", errorCode)));
                }
                else
                {
                    ElaMicroConfiguration.getInstance().Logger.add(new LogItem("Bluetooth streaming started successfully"));
                    m_client.evBluetoothPacketReceived += M_client_evBluetoothPacketReceived;
                }
            }
            catch (Exception ex)
            {
                ElaMicroConfiguration.getInstance().Logger.add(new LogItem(ex));
            }
        }

        private void M_client_evBluetoothPacketReceived(object sender, ElaBluetoothScanResultItem item)
        {
            ElaMicroConfiguration.getInstance().Logger.add(new LogItem($"Timestamp={item.TimeStamp}; mac address={item.MacAddress}; localname={item.LocalName}; rssi={item.Rssi}"));
        }

        private void btnStopDataFlow_Click(object sender, RoutedEventArgs e)
        {
            try
            {
                uint errorCode = this.m_client.StopBluetoothDataFlow();
                if (0 != errorCode)
                {
                    ElaMicroConfiguration.getInstance().Logger.add(new LogItem(String.Format("Stop Bluetooth streaming failed :  error code {0}", errorCode)));
                }
                else
                {
                    m_client.evBluetoothPacketReceived -= M_client_evBluetoothPacketReceived;
                    ElaMicroConfiguration.getInstance().Logger.add(new LogItem("Bluetooth streaming stoppped with Success"));
                }
            }
            catch (Exception ex)
            {
                ElaMicroConfiguration.getInstance().Logger.add(new LogItem(ex));
            }
        }

    }
}
