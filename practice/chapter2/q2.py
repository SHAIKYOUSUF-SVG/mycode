class versions:
    def __init__(self,firmware,devicedriver,ipaddress,macaddress):
        self.firmware=firmware
        self.devicedriver=devicedriver
        self.ipaddress=ipaddress
        self.macaddress=macaddress

    def get_fw_version(self):
        #firmwareversion="3.08.11"
        return self.firmware
    def get_driver_version(self):
        return self.devicedriver
    def get_ipaddress(self):
        return self.ipaddress
    def get_macaddress(self):
        return self.macaddress


out=versions("3.08.11","14:3A","192.168.0.1","14:2A:13:1B")
print(out.get_fw_version())
print(out.get_driver_version())


import paramiko
import re
command = "whoami"
host = "192.168.0.113"
username = "winteck"
password = "Winteck@2024"
client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=username, password=password)
_stdin, _stdout,_stderr = client.exec_command(command)
print(_stdout.read().decode())
client.close()
#print(out)

import paramiko
command = "df -h"
host = "192.168.0.113"
username = "winteck"
password = "Winteck@2024"
client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=username, password=password)
_stdin, _stdout,_stderr = client.exec_command(command)
print(_stdout.read().decode())
client.close()



command = "lsblk"
host = "192.168.0.113"
username = "winteck"
password = "Winteck@2024"
client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=username, password=password)
_stdin, _stdout,_stderr = client.exec_command(command)
print(_stdout.read().decode())
client.close()