# BlueBaseMicroservice Sample using Nuget
This sample is an integration using [Bluetooth Base Microservice][here_ela_sdk] and [elaMicroserviceClient][here_ela_nuget] nuget package. We use Visual Studio 2019 Community to create a new solution. You can directly open the **sln file** to load the solution in Visual Studio environnement and run the sample. We use WPF, Framework.Net and C# to code the User Interface.

## Nugets
Two nugets package are usefull to integrate **Bluetooth Base Microservice**:
- elaMicroserviceClient: this is a precoded **Bluetooth Base Client**.
- ElaSoftwareCommon: this is the common library developped by ELA. For this sample we use log, Errors object and error handling functions.

## elaMicroserviceClient
The user interface for Bluetooth Base Microservice is available in namespace **BlueBaseMicroservice_Sample.Views**. This component use the **ElaBluetoothClient class**, the precoded client from **elaMicroserviceClient**.
```C#
	/** \brief target bluetooth client */
	private ElaBluetoothClient m_client = new ElaBluetoothClient();
```

Before calling any function, you need to connect to the **Bluetooth Base Microservice** by using the **connect** function. The connection function ty to reach the target **hostname** and **port** where the microservice is hosted.
```C#                
	uint errorCode = this.m_client.connect(ElaMicroConfiguration.getInstance().Settings.BluetoothConfiguration.GrpcHostName, ElaMicroConfiguration.getInstance().Settings.BluetoothConfiguration.GrpcPort);
	if (0 != errorCode)
	{
		ElaMicroConfiguration.getInstance().Logger.add(new LogItem(String.Format("An error occur during connection : error code {0}", errorCode)));
	}
```

In this part of code, you can (re)define your target hostname. The port for bluetooth connection is always the same for the Bluetooth Base Microservice.
```C#                
	uint errorCode = this.m_client.connect("<your_hostname>", ElaMicroConfiguration.getInstance().Settings.BluetoothConfiguration.GrpcPort);
	if (0 != errorCode)
	{
		ElaMicroConfiguration.getInstance().Logger.add(new LogItem(String.Format("An error occur during connection : error code {0}", errorCode)));
	}
```

To ensure to invoke all function from the API, you need to authenticate to the module by following the [ELA Authentication rules][here_ela_authentication]. In this sample, you will find the two main authentication function to connect to the module:
- **login** : to send your login and password information and get a session id to invoke all other function from the API
- **logout** : to release the session id and close the API

** Invoke login function**
```C#   
	uint errorCode = this.m_client.login(this.tbUserName.Text, this.pwdUser.Password);
	if (0 != errorCode)
	{
		ElaMicroConfiguration.getInstance().Logger.add(new LogItem(String.Format("Authentication Connect failed : error code {0}", errorCode)));
	}
```

** Release with logout function**
```C#   
	uint errorCode = this.m_client.logout();
	if (0 != errorCode)
	{
		ElaMicroConfiguration.getInstance().Logger.add(new LogItem(String.Format("Authentication Disconnect failed : error code {0}", errorCode)));
	}
```

Then you can invoke all other API functions. All the button and sample present show you how to use the instancied client object to communicate with **Bluetooth Base Module**

[here_ela_sdk]: https://github.com/elaInnovation/ELA-Microservices

[here_ela_nuget]: https://www.nuget.org/packages/elaMicroserviceClient/

[here_ela_authentication]: https://github.com/elaInnovation/ELA-Microservices#authentication