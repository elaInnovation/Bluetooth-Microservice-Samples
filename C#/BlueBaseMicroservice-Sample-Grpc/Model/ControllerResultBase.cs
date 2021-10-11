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
     * \class ControllerResultBase
     * \brief controller result base
     */
    public class ControllerResultBase
    {
        /** \brief error code definition for the target result */
        public uint ErrorCode { get; }

        /** \brief constructor */
        public ControllerResultBase(uint code)
        {
            ErrorCode = code;
        }
    }
}
