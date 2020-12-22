import re
import os

class ConfigurationParser:
    def parseCustomerNames(self):
        '''
        files = os.listdir(os.curdir)
        print(files)
        '''

        # config_filename = os.path.join('section2', 'chapter24', 'config.txt')
        config_filename = 'config.txt'

        with open(config_filename, 'r') as config_fp:
            deviceConfig = config_fp.read()
            customerNamePattern = r'ip vrf ([a-zA-Z_]+)\n'
            customerNames = re.findall(customerNamePattern, deviceConfig)
            return customerNames