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
    
    
    #<After sending config_commands, a delay of 30 seconds is needed to wait for the modem to respond appropriately.>

    
    #<Followed by a conditional logic code block: (1) script to read until the word "CONNECT" then print the output and continue loop>;
    #(2) print "Connection failed to <POTS line>." if the modem does not return any output and continue loop>;
    #(3) At the last item in the loop, disconnect and exit out from the modempool router.>
