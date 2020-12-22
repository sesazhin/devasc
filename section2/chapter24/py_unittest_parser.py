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


if __name__ == '__main__':
    unittest.main()
