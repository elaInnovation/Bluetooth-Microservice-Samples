using System;
using System.Collections.Generic;
using System.Text;

/**
 * \namsespace ElaBleGui.Model
 * \brief namespace associated to the all the model to represent data through the User Interface
 */
namespace BlueBaseMicroservice_Sample.Model
{
    /**
     * \class BluetoothResults
     * \brief bluetooth result declaration
     */
    public class BluetoothResults : ControllerResultBase
    {
        /** \brief internal message */
        public string Message { get; }

        /** \brief constructor */
        public BluetoothResults(uint code, string message) : base(code)
        {
            Message = message;
        }
    }
}
