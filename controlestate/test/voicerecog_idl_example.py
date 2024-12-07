﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 @file voicerecog_idl_example.py
 @brief Python example implementations generated from voicerecog.idl
 @date $Date$


"""

import omniORB
from omniORB import CORBA, PortableServer
import Library, Library__POA



class voicerecogdata_i (Library__POA.voicerecogdata):
    """
    @class voicerecogdata_i
    Example class implementing IDL interface Library.voicerecogdata
    """

    def __init__(self):
        """
        @brief standard constructor
        Initialise member variables here
        """
        pass

    # Dataset setresult(in string data)
    def setresult(self, data):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result

    # Dataset voicerecog(in Dataset data)
    def voicerecog(self, data):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result

    # Dataset voicerecogadditionalfunction(in Dataset data)
    def voicerecogadditionalfunction(self, data):
        raise CORBA.NO_IMPLEMENT(0, CORBA.COMPLETED_NO)
        # *** Implement me
        # Must return: result


if __name__ == "__main__":
    import sys
    
    # Initialise the ORB
    orb = CORBA.ORB_init(sys.argv)
    
    # As an example, we activate an object in the Root POA
    poa = orb.resolve_initial_references("RootPOA")

    # Create an instance of a servant class
    servant = voicerecogdata_i()

    # Activate it in the Root POA
    poa.activate_object(servant)

    # Get the object reference to the object
    objref = servant._this()
    
    # Print a stringified IOR for it
    print(orb.object_to_string(objref))

    # Activate the Root POA's manager
    poa._get_the_POAManager().activate()

    # Run the ORB, blocking this thread
    orb.run()

