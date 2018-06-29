from getpass import getpass
from netmiko import ConnectHandler

import time


user = input("Enter your SSH username: ")
password = getpass()


# Create a file named "pots_lines_file" which will be a list of POTS lines to be dialed out
with open('pots_lines_file') as f:
    pots_lines = f.read().splitlines()


# Device definition
modempool = {
    'device_type': 'cisco_ios',
    'ip': '10.1.2.3',
    'username': user,
    'password': password,
}


net_connect = ConnectHandler(**modempool)


for line in pots_lines:
    config_commands = ['modem1', 'atdt 1' + line] # Commands to dial to the modem
    output = net_connect.send_config_set(config_commands) # Dial out to destination modem
    time.sleep(30) # A delay of 30 seconds to wait for a response from the destination modem

    if output:
        net_connect.read_until("CONNECT") # Not sure if this is how to read_until in Netmiko
        print(output) # Prints the prompt of successful OOB connections and continue loop
    else:
        print('Connection failed to ', line, '.\n')
        <input keystrokes here: ctrl+shift+6 then x> # Needed keystores for break sequence
        break_commands = ['disco', 'exit']
        break = net_connect.send_config_set(break_commands) # Exits out of the router (modempool)
