#!/usr/bin/python
# -*- coding: utf-8 -*-
"""This example shows how to connect three controllers on a daisy chain."""

# (c)2016 Physik Instrumente (PI) GmbH & Co. KG
# Software products that are provided by PI are subject to the
# General Software License Agreement of Physik Instrumente (PI) GmbH & Co. KG
# and may incorporate and/or make use of third-party software components.
# For more information, please read the General Software License Agreement
# and the Third Party Software Note linked below.
# General Software License Agreement:
# http://www.physikinstrumente.com/download/EULA_PhysikInstrumenteGmbH_Co_KG.pdf
# Third Party Software Note:
# http://www.physikinstrumente.com/download/TPSWNote_PhysikInstrumenteGmbH_Co_KG.pdf

from pipython import GCSDevice

def main():
    """Connect three controllers on a daisy chain."""
    dev = GCSDevice()
    usbname = dev.EnumerateUSB()  # Connect the interface to the controller
    daisyname = dev.OpenUSBDaisyChain(usbname[0]) # Use interface connection as daisy chain

    dev2 = GCSDevice() # Create a new device object

    dev.ConnectDaisyChainDevice(1, daisyname) # connect dev 1 object to daisy chain
    dev2.ConnectDaisyChainDevice(2, daisyname) # connect dev 2 object to daisy chain
    print('\n{}:\n{}'.format(dev.GetInterfaceDescription(), dev.qIDN())) # use dev1 to get identification for device 1
    print('\n{}:\n{}'.format(dev2.GetInterfaceDescription(), dev2.qIDN())) # use dev2 to get identification for device 2

    # you can now use dev1 and dev2 as controllers and command motions for axis on the controller
    # please note each device has 1 axis which will be usually named '1'

if __name__ == '__main__':
    # from pipython import PIlogger, DEBUG, INFO, WARNING, ERROR, CRITICAL
    # PIlogger.setLevel(DEBUG)
    main()