"""Provide support for Nanosurf Accessory Interface Electronics
Copyright (C) Nanosurf AG - All Rights Reserved (2021)
License - MIT"""

from array import array
import nanosurf.lib.spm as spm

class AISlaveIDHeader:
    """ This class stores the information found in the id eeprom of each slave device"""

    def __init__(self, binaryarray: list = [int]):
        """ This class stores the information found in the id eeprom of each slave device

            As standart identification a bt-number is read from the device
            Optional a serial number is provided

        Parameters
        ----------
        binaryarray : array of byte data, optional
            data array (e.g. read from eeprom) to be decoded and filled into the class structure
        """

        self._version = 0
        self._bt_number = ""
        self._serial_no = ""
        self.decode_eeprom_data(binaryarray)

    def decode_eeprom_data(self, binaryarray: list[int]):
        """ This function can extract the id header information stored in a binary data stream, normally read from a id eeprom.
            The information is stored as class variables and can be ready by accessor functions

        Parameters
        ----------
        binaryarray : array of byte data, optional
            data array (e.g. read from eeprom) to be decoded and filled into the class structure

       """
        if len(binaryarray) > 10:
            self._version = binaryarray[0]
            assert self._version == 1, "AISlaveIDHeader: unknown id header version detected."
            self._bt_number = array('B', binaryarray[2:2+binaryarray[1]]).tobytes().decode()
            if binaryarray[9] > 0:
                self._serial_no = array('B', binaryarray[10:10+binaryarray[9]]).tobytes().decode()
            else:
                self._serial_no = ""

    def get_bt_number(self) -> str:
        """ Returns the slave devices identification string.
            It's usual form is "BTxxxxx"

        Returns
        -------
        bt_number: str
            identification string

        """
        return self._bt_number

    def get_serial_number(self) -> str:
        """ Return the slave devices (optional) serial number.
            It's usual form is "xxx-xx-xxx"

         Returns
         -------
            serial_number: str
                 serial number as string or empty string if no serial number is defined

        """
        return self._serial_no

class AccessoryInterface:
    """ This is the main class to get access to an accessory interface (AI) and its slave devices.

        Connect to a know AI by its serial-no, or scan first for available AIs, or connect to first found
        Then access to a slave device of this AI can be etablished by select_port()

        slave devices are identified by get_slave_device_id().
        To talk to a slave device, specific classes have to be build.

    """
    def __init__(self, spm: spm.Spm):
        """ This is the main class to get access to an accessory interface (AI) and its slave devices.

        Parameters
        ----------
        spm
            reference to the connected spm COM class

        """
        self._app = spm.application
        self._testobj = self._app.CreateTestObj
        self._ai_bus_addr = -1
        self._own_id_header = AISlaveIDHeader()

    def get_list_of_available_interfaces(self) -> list[str]:
        """ Searches for attached accessory interfaces and create list of available devices
            Have to be called at least once before a connect() can be done

         Returns
         ------
         list of str
            list of serial numbers of all found accessory interfaces

        """
        self._list_of_found_ai = []

        count_ai = self._testobj.GetAccessoryInterfaceInUseCount
        for i in range(count_ai):
            self._list_of_found_ai.append(self._testobj.GetAccessoryInterfaceInUseSerial(i))

        count_ai = self._testobj.GetAccessoryInterfaceAvailableCount
        for i in range(count_ai):
            self._list_of_found_ai.append(self._testobj.GetAccessoryInterfaceAvailableSerial(i))

        return self._list_of_found_ai

    def connect(self, serial_no: str = "") -> bool:
        """ connect this instance to a accessory interface identified by device serial-number

        Parameters
        ----------
        serial_no : str, optional
            serial-number of accessory interface to be connected to. If omitted it connects to fist AI found

        Returns
         ------
        Bool
            true if connection could be set up

        """
        self._ai_bus_addr = -1 # no connection

        # without given serial number we try auto detection
        if serial_no == "":
            self.get_list_of_available_interfaces()
            if len(self._list_of_found_ai) > 0:
                serial_no = self._list_of_found_ai[0]

        # setup connection
        try:
            self._ai_bus_addr = self.get_bus_addr_of_ai_device(serial_no)

            # if connection could be done read and store device information
            if self._ai_bus_addr > 0:
                self.select_port(0)
                self._own_id_header = self.get_slave_device_id()
            else:
                self._own_id_header = AISlaveIDHeader()
        except AssertionError:
            self._own_id_header = AISlaveIDHeader()
            self._ai_bus_addr = -1

        return self._ai_bus_addr > 0

    def get_port_count(self) -> int:
        """ return the number of slave port the connected interface has

        Returns
        -------
        int
            number of ports avaliable on this accessory interface

        """
        known_ai_devices = {"BT07172": 5}
        if self._own_id_header.get_bt_number() in known_ai_devices:
            return known_ai_devices[self._own_id_header.get_bt_number()]
        else:
            return 0

    def get_serial_number(self) -> str:
        """ returns the serial number of the connected accessory interface

        Returns
        -------
        str
            Onw serial_number as a string in the form "xxx-yy-zzz" or empty string if not connected

        """
        return self._own_id_header.get_serial_number()

    def get_bus_addr(self) -> int:
        """ returns the communication bus address. Used for further I2C communication with a slave

        Returns
        -------
        int
            bus_address - identification number to be used for I2C communication

        """
        return self._ai_bus_addr

    def select_port(self, port_nr: int):
        """ opens the port to communication with a slave device at port
            Only one port at a given time can be selected. all further slave communication goes through the selected port
            Port 0 is assigned to accessory interface internal configuration and should be used carefully

        Parameters
        ----------
        port_nr : int
            identification number of the port to be used
        """
        assert self._ai_bus_addr != -1, "Accessory Interface: Error: Slave Access, but connection not assigned"
        ret = self._testobj.I2CSetupMetaData(0,1,self._ai_bus_addr,0x70,0,1) # Setup for switch(multiplexer)
        assert ret == 0, "Accessory Interface: Error: Cannot connect to bus switch"
        ret = self._testobj.I2CIsConnected
        assert ret == 1,"Accessory Interface: Error: Bus switch is not responding"

        # activate port, port 0 is internal, port 1 to 5 are accessory ports
        ret = self._testobj.I2CWrite(0,1,[1 << port_nr])
        assert ret == 0, "Accessory Interface: Error: Write error to Bus switch"

    def is_slave_device_connected(self) -> bool:
        """ check if a slave device is connected to selected port
            It looks if the id eeprom can be found

        Returns
        -------
        bool
            returns True if a device is found on selected port, otherwise False

        """

        assert self._ai_bus_addr != -1, "Accessory Interface: Error: Slave Access, but connection not assigned"
        ret = self._testobj.I2CSetupMetaData(0,1,self._ai_bus_addr,0x57,2,1) # Setup for eeprom
        assert ret == 0, "Accessory Interface: Error: Cannot setup device metadata"
        id_eeprom_connected = self._testobj.I2CIsConnected
        return id_eeprom_connected != 0

    def get_slave_device_id(self) -> AISlaveIDHeader:
        """ read the identification information from the device on selected port
            The information is read from the id eeprom and stored in a AISlaveIDHeader class

         input:
            none
         return:
            slave_id - AISlaveIDHeader class type with the retrieved information
        """
        assert self._ai_bus_addr != -1, "Accessory Interface: Error: Slave Access, but connection not assigned"
        ret = self._testobj.I2CSetupMetaData(0,1,self._ai_bus_addr,0x57,2,1) # Setup for eeprom
        assert ret == 0, "Accessory Interface: Error: Cannot setup device metadata"
        id_eeprom_data = self._testobj.I2CReadEx(0, 19)
        return AISlaveIDHeader(id_eeprom_data)

    def get_bus_addr_of_ai_device(self, serial_no: str) -> int:
        """ returns the bus_address to a accessory interface with provided serial_no

        Parameters
        ----------
        serial_no : str
            serial-number of accessory interface to provide the bus_adr

        Returns
         ------
        bus_adr: int
            bus_adr of AI with provided serial_no or a negative number if AI was not found

        """

        found_bus_addr = -1 # init return value

        # search for bus address of given serial number in list of InUse devices
        count_ai = self._testobj.GetAccessoryInterfaceInUseCount
        for i in range(count_ai):
            if serial_no == self._testobj.GetAccessoryInterfaceInUseSerial(i):
                found_bus_addr = self._testobj.GetAccessoryInterfaceInUseI2CBus(i)
                break

        # if not found, search in list of free devices
        if found_bus_addr < 0:
            count_ai = self._testobj.GetAccessoryInterfaceAvailableCount
            for i in range(count_ai):
                if serial_no == self._testobj.GetAccessoryInterfaceAvailableSerial(i):
                    found_bus_addr = self._testobj.ActivateAccessoryInterfaceAvailable(i)
                    break

        return found_bus_addr

