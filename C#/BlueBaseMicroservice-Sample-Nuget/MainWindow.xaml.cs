using BlueBaseMicroservice_Sample.Configuration;
using BlueBaseMicroservice_Sample.Views;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace BlueBaseMicroservice_Sample
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        /** \brief constructor */
        public MainWindow()
        {
            InitializeComponent();
            initializeInternalComponents();
            localizeComponents();
        }

        #region implement IuserControlBase interface
        public void initializeInternalComponents()
        {
            TabItem settingsTab = new TabItem();
            //
            if (true == ElaMicroConfiguration.getInstance().Settings?.BluetoothConfiguration?.UserAllowed)
            {
                TabItem blueTab = new TabItem();
                blueTab.Header = ElaMicroConfiguration.getInstance().Settings?.BluetoothConfiguration.GrpcServiceName;
                blueTab.Content = new MicroBlueManager() { Tag = ElaMicroConfiguration.getInstance().Settings?.BluetoothConfiguration.GrpcServiceName };
                this.tabMain.Items.Add(blueTab);
            }
            //
        }

        public void localizeComponents()
        {

        }
        #endregion
    }
}
