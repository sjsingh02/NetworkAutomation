from netmiko import ConnectHandler

with open('commands_file.txt') as f:
    commands_list = f.read().splitlines()

with open('devices_file.txt') as f:
    devices_list = f.read().splitlines()

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
    conft=net_connect.config_mode()
    output = net_connect.send_config_set(commands_list)
    print output
