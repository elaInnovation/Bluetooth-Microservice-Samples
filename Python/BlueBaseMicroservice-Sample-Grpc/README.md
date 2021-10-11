# Python samples

This repository provide to you a sample to interrac with Bluetooth Base Microservice, a service developped by ELA Innovation. To have more information about this service, you can find it by following [this link][here_ela_sdk] on our Github. To find more information about our Devices, please consult our [website][here_ela_website]. The Bluetooth Base Microservice help you to interract with our Devices, the Blue product line.

## Purpose
The sample present here propose you an implementation of a Bluetooth base Client based on our [gRPC][here_grpc] interface. you can find more information about the gRPC interface developped by ELA Innovation [here][here_ela_grpc_interface].

## Prerequist
If you want to implement your first client, you need to install some tools to developp your client side logic. First of all, ensure that gRPC and all the relative tools are well installed in Python.
```bash
    $ sudo pip3 install grpcio
    $ sudo pip3 install grpcio-tools
```

First create in the file system the different folder where grpc tools will generate all the client side code.
```bash
   $ mkdir -p bluetooth/Protos/Authentication
   $ mkdir -p bluetooth/Protos/Bluetooth
   $ mkdir -p bluetooth/Protos/Common
```

In this sample, we add the folder **bluetooth/ExtElaMicroserviceGrpc** as an external from repository [elaMicroserviceGrpc][here_ela_grpc_interface]. From there, we make a copy of the important proto file in the file system of the sample.
```bash
    $ cp bluetooth/ExtElaMicroserviceGrpc/Protos/Common/ElaCommon.proto ./bluetooth/Protos/Common
    $ cp bluetooth/ExtElaMicroserviceGrpc/Protos/Bluetooth/ElaBluetoothPublicAPI.proto ./bluetooth/Protos/Bluetooth
    $ cp bluetooth/ExtElaMicroserviceGrpc/Protos/Bluetooth/ElaBluetoothCommon.proto ./bluetooth/Protos/Bluetooth
    $ cp bluetooth/ExtElaMicroserviceGrpc/Protos/Authentication/ElaAuthenticationCommon.proto ./bluetooth/Protos/Authentication
```

Then, generate your interface and object files according to the proto files. From repository origin folder, go to the Server folder and then execute and use grpc_tools:
```bash
    $ cd bluetooth
    $ python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./Protos/Common/ElaCommon.proto
    $ python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./Protos/Authentication/ElaAuthenticationCommon.proto
    $ python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./Protos/Bluetooth/ElaBluetoothCommon.proto
    $ python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./Protos/Bluetooth/ElaBluetoothPublicAPI.proto
```

## Execution
You can run the sample by directly by calling the following command:
```bash
     $ python3 .\ElaBleBaseClientSample.py
 ```

[here_ela_website]: https://elainnovation.com

[here_ela_sdk]:https://github.com/elaInnovation/ELA-Microservices

[here_ela_grpc_interface]: https://github.com/elaInnovation/elaMicroserviceGrpc

[here_grpc]: https://grpc.io