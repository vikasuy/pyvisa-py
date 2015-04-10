# -*- coding: utf-8 -*-



from pyvisa import constants
from pyvisa.compat import unittest
from pyvisa.testsuite import BaseTestCase

pyvisapy = __import__('pyvisa-py')

parse = pyvisapy.common.parse_resource_name


class TestParsers(BaseTestCase):

    def _parse_test(self, rn, **kwargs):
        result = dict(resource_name=rn, **kwargs)
        self.assertEqual(parse(rn), result)

    @unittest.expectedFailure
    def test_asrl_ethernet(self):
        self._parse_test('ASRL::1.2.3.4::2::INSTR',
                         interface_type=constants.InterfaceType.asrl,
                         resource_class='INSTR',
                         port='2',
                         address='1.2.3.4')

    def test_asrl(self):
        self._parse_test('ASRL1::INSTR',
                         interface_type=constants.InterfaceType.asrl,
                         resource_class='INSTR',
                         board='1',
                         canonical_resource_name='ASRL1::INSTR')

        self._parse_test('ASRL1',
                         interface_type=constants.InterfaceType.asrl,
                         resource_class='INSTR',
                         board='1',
                         canonical_resource_name='ASRL1::INSTR')

    def test_gpib_instr(self):
        self._parse_test('GPIB::1::0::INSTR',
                         interface_type=constants.InterfaceType.gpib,
                         resource_class='INSTR',
                         board='0',
                         primary_address='1',
                         secondary_address='0',
                         canonical_resource_name='GPIB0::1::0::INSTR')

        self._parse_test('GPIB::1::INSTR',
                         interface_type=constants.InterfaceType.gpib,
                         resource_class='INSTR',
                         board='0',
                         primary_address='1',
                         secondary_address=65535,
                         canonical_resource_name='GPIB0::1::65535::INSTR')

        self._parse_test('GPIB1::1::INSTR',
                         interface_type=constants.InterfaceType.gpib,
                         resource_class='INSTR',
                         board='1',
                         primary_address='1',
                         secondary_address=65535,
                         canonical_resource_name='GPIB1::1::65535::INSTR')

        self._parse_test('GPIB1::1',
                         interface_type=constants.InterfaceType.gpib,
                         resource_class='INSTR',
                         board='1',
                         primary_address='1',
                         secondary_address=65535,
                         canonical_resource_name='GPIB1::1::65535::INSTR')

    def test_gpib_intf(self):
        self._parse_test('GPIB::INTFC',
                         interface_type=constants.InterfaceType.gpib,
                         resource_class='INTFC',
                         board='0',
                         canonical_resource_name='GPIB0::INTFC')

        self._parse_test('GPIB3::INTFC',
                         interface_type=constants.InterfaceType.gpib,
                         resource_class='INTFC',
                         board='3',
                         canonical_resource_name='GPIB3::INTFC')

    def test_tcpip_intr(self):

        self._parse_test('TCPIP::192.168.134.102',
                         interface_type=constants.InterfaceType.tcpip,
                         resource_class='INSTR',
                         host_address='192.168.134.102',
                         board='0',
                         lan_device_name='inst0',
                         canonical_resource_name='TCPIP0::192.168.134.102::inst0::INSTR')

        self._parse_test('TCPIP::dev.company.com::INSTR',
                         interface_type=constants.InterfaceType.tcpip,
                         resource_class='INSTR',
                         host_address='dev.company.com',
                         board='0',
                         lan_device_name='inst0',
                         canonical_resource_name='TCPIP0::dev.company.com::inst0::INSTR')

        self._parse_test('TCPIP3::dev.company.com::inst3::INSTR',
                         interface_type=constants.InterfaceType.tcpip,
                         resource_class='INSTR',
                         host_address='dev.company.com',
                         board='3',
                         lan_device_name='inst3',
                         canonical_resource_name='TCPIP3::dev.company.com::inst3::INSTR')

        self._parse_test('TCPIP3::1.2.3.4::inst3::INSTR',
                         interface_type=constants.InterfaceType.tcpip,
                         resource_class='INSTR',
                         host_address='1.2.3.4',
                         board='3',
                         lan_device_name='inst3',
                         canonical_resource_name='TCPIP3::1.2.3.4::inst3::INSTR')

    def test_tcpip_socket(self):
        self._parse_test('TCPIP::1.2.3.4::999::SOCKET',
                         interface_type=constants.InterfaceType.tcpip,
                         resource_class='SOCKET',
                         host_address='1.2.3.4',
                         board='0',
                         port='999',
                         canonical_resource_name='TCPIP0::1.2.3.4::999::SOCKET')

        self._parse_test('TCPIP2::1.2.3.4::999::SOCKET',
                         interface_type=constants.InterfaceType.tcpip,
                         resource_class='SOCKET',
                         host_address='1.2.3.4',
                         board='2',
                         port='999',
                         canonical_resource_name='TCPIP2::1.2.3.4::999::SOCKET')

    def test_usb_instr(self):
        self._parse_test('USB::0x1234::125::A22-5::INSTR',
                         interface_type=constants.InterfaceType.usb,
                         resource_class='INSTR',
                         manufacturer_id='0x1234',
                         model_code='125',
                         serial_number='A22-5',
                         board='0',
                         usb_interface_number='0',
                         canonical_resource_name='USB0::0x1234::125::A22-5::0::INSTR')

        self._parse_test('USB2::0x1234::125::A22-5::INSTR',
                         interface_type=constants.InterfaceType.usb,
                         resource_class='INSTR',
                         manufacturer_id='0x1234',
                         model_code='125',
                         serial_number='A22-5',
                         board='2',
                         usb_interface_number='0',
                         canonical_resource_name='USB2::0x1234::125::A22-5::0::INSTR')

        self._parse_test('USB::0x1234::125::A22-5',
                         interface_type=constants.InterfaceType.usb,
                         resource_class='INSTR',
                         manufacturer_id='0x1234',
                         model_code='125',
                         serial_number='A22-5',
                         board='0',
                         usb_interface_number='0',
                         canonical_resource_name='USB0::0x1234::125::A22-5::0::INSTR')

        self._parse_test('USB::0x1234::125::A22-5::3::INSTR',
                         interface_type=constants.InterfaceType.usb,
                         resource_class='INSTR',
                         manufacturer_id='0x1234',
                         model_code='125',
                         serial_number='A22-5',
                         board='0',
                         usb_interface_number='3',
                         canonical_resource_name='USB0::0x1234::125::A22-5::3::INSTR')

        self._parse_test('USB2::0x1234::125::A22-5::3::INSTR',
                         interface_type=constants.InterfaceType.usb,
                         resource_class='INSTR',
                         manufacturer_id='0x1234',
                         model_code='125',
                         serial_number='A22-5',
                         board='2',
                         usb_interface_number='3',
                         canonical_resource_name='USB2::0x1234::125::A22-5::3::INSTR')

        self._parse_test('USB1::0x1234::125::A22-5::3',
                         interface_type=constants.InterfaceType.usb,
                         resource_class='INSTR',
                         manufacturer_id='0x1234',
                         model_code='125',
                         serial_number='A22-5',
                         board='1',
                         usb_interface_number='3',
                         canonical_resource_name='USB1::0x1234::125::A22-5::3::INSTR')

    def test_usb_raw(self):
        self._parse_test('USB::0x1234::125::A22-5::RAW',
                         interface_type=constants.InterfaceType.usb,
                         resource_class='RAW',
                         manufacturer_id='0x1234',
                         model_code='125',
                         serial_number='A22-5',
                         board='0',
                         usb_interface_number='0',
                         canonical_resource_name='USB0::0x1234::125::A22-5::0::RAW')

        self._parse_test('USB2::0x1234::125::A22-5::RAW',
                         interface_type=constants.InterfaceType.usb,
                         resource_class='RAW',
                         manufacturer_id='0x1234',
                         model_code='125',
                         serial_number='A22-5',
                         board='2',
                         usb_interface_number='0',
                         canonical_resource_name='USB2::0x1234::125::A22-5::0::RAW')

        self._parse_test('USB2::0x1234::125::A22-5::3::RAW',
                         interface_type=constants.InterfaceType.usb,
                         resource_class='RAW',
                         manufacturer_id='0x1234',
                         model_code='125',
                         serial_number='A22-5',
                         board='2',
                         usb_interface_number='3',
                         canonical_resource_name='USB2::0x1234::125::A22-5::3::RAW')
