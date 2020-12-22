import re
import os


class ConfigurationParser:
    def __init__(self):
        config_filename = 'config.txt'

        with open(config_filename, 'r') as config_fp:
            self.deviceConfig = config_fp.read()

    def parseCustomerNames(self):
        '''
        files = os.listdir(os.curdir)
        print(files)
        '''

        # config_filename = os.path.join('section2', 'chapter24', 'config.txt')

        customerNamePattern = r'ip vrf ([a-zA-Z_]+)\n'
        customerNames = re.findall(customerNamePattern, self.deviceConfig)
        return customerNames

    def parseCustomerVlan(self, customerName):
        '''
        files = os.listdir(os.curdir)
        print(files)
        '''

        # config_filename = os.path.join('section2', 'chapter24', 'config.txt')

        '''
        interface_pattern = (
            r"interface GigabitEthernet0\/0\.([0-9]+)\n"
            rf" encapsulation dot1Q [0-9]+\n ip vrf forwarding {customerName}"
        )
        '''

        interface_pattern = (
            r"interface GigabitEthernet0\/0\.([0-9]+)\n"
            r"  encapsulation dot1Q [0-9]+\n"
            f"  ip vrf forwarding {customerName}"
        )

        print(interface_pattern)

        allCustomerSubInterfaces = re.search(interface_pattern, self.deviceConfig)

        # customerVlanPattern = r'encapsulation dot1Q ([0-9]+)\n'
        # customerVlans = re.findall(customerVlanPattern, self.deviceConfig)
        print(allCustomerSubInterfaces.group(0))
        return int(allCustomerSubInterfaces.group(1))

    def parseCustomerIp(self, customer_vlan):
        ip_pattern = (
            rf"GigabitEthernet0/0\.{customer_vlan}[ ]+([0-9\.]+)"
        )
        print(ip_pattern)
        ip_addr = re.search(ip_pattern, self.deviceConfig)
        print(ip_addr.group(0))
        return ip_addr.group(1)

    def parseCustomerData(self):
        customerData = {}
        customerNames = self.parseCustomerNames()
        for customerName in customerNames:
            vlan = self.parseCustomerVlan(customerName)
            ip_address = self.parseCustomerIp(vlan)
            customerData[customerName] = [vlan, ip_address]

            print(customerData)

        return customerData

