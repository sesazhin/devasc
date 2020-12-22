import unittest
from section2.chapter24.main import ConfigurationParser


class TestParse(unittest.TestCase):
    def test_parse_customer_name(self):
        cp = ConfigurationParser()
        expected_names = ['CUSTOMER_A', 'CUSTOMER_B']
        # print(expected_names)
        parsed_names = cp.parseCustomerNames()
        self.assertEqual(list, type(parsed_names))
        self.assertEqual(expected_names, parsed_names)

    def test_parse_customer_vlan(self):
        cp = ConfigurationParser()
        expected_vlans = {'CUSTOMER_A': 100, 'CUSTOMER_B': 101}
        customer_name = 'CUSTOMER_A'
        parsed_vlan = cp.parseCustomerVlan(customer_name)
        print(parsed_vlan)
        # self.assertEqual(int, type(parsed_vlan))
        self.assertEqual(expected_vlans[customer_name], parsed_vlan)

    def test_parse_customer_ip(self):
        cp = ConfigurationParser()
        expected_ips = {'100': '10.10.100.1', '101': '10.10.101.1'}
        customer_vlan = '100'
        parsed_ip = cp.parseCustomerIp(customer_vlan)
        print(parsed_ip)
        # self.assertEqual(int, type(parsed_vlan))
        self.assertEqual(expected_ips[customer_vlan], parsed_ip)

    def test_parse_customer_data(self):
        cp = ConfigurationParser()
        expected_data = {'CUSTOMER_A': [100, '10.10.100.1'],
                         'CUSTOMER_B': [101, '10.10.101.1']}

        parsed_data = cp.parseCustomerData()
        self.assertEqual(expected_data, parsed_data)


if __name__ == '__main__':
    unittest.main()
