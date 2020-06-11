# Python 2.7
# Netmiko 2.4.2
# Paramiko 2.4.1

import logging
from netmiko import ConnectHandler

with open('commands_file.txt') as f:
    commands_list = f.read().splitlines()

with open('devices_file.txt') as f:
    devices_list = f.read().splitlines()
	
#Logging CLI info to a file 
# logging.basicConfig(filename="test.log", level=logging.DEBUG)
# logger = logging.getLogger('netmiko')
	

for devices in devices_list:
    print 'Connecting to device" ' + devices
    ip_address_of_device = devices
    eos_device = {
        'device_type': 'arista_eos',
        'ip': ip_address_of_device,
        'username': 'admin',
        'password': 'admin'
    }

    print "HELLO"
    net_connect = ConnectHandler(**eos_device)
    enable = net_connect.enable()
    output = net_connect.send_config_set(commands_list)
    print output
    result = open(str(devices) + "_Output", 'w')
    result.write(output)
    result.close
