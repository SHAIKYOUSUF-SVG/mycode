
from common import *
import re


def list_drives(connection):
    drives_output = connection.connect("lsblk")
    pattern = r"sd\w{1}"
    drive_list = re.findall(pattern, drives_output)
    drives = []
    for drive in drive_list:
        drives.append(f"/dev/{drive}")
    return drives
def cpu_info(connection):
    output=connection.connect("lscpu")
    return output
def get_drivefw(connection):
    output = connection.connect("smartctl -a /dev/sda")
    # Adjust the regex pattern as needed based on the expected firmware output format
    exp = "Revision:\s*([A-Z0-9]+)"
    out = re.search(exp, output)
    if out:
        #print(out.group(1))
        return out.group(1)

    output1 = connection.connect("smartctl -a /dev/sdb")
    # Adjust the regex pattern as needed based on the expected firmware output format
    exp = "Revision:\s*([A-Z0-9]+)"
    out1 = re.search(exp, output1)
    if out1:
        #print(out1.group(1))
        return out1.group(1)
def get_logfiles(connection):
    #connection.connect("cd /var/log")

    output1=connection.connect("ls")
    return output1

def get_biosinfo(connection):
    output=connection.connect("dmidecode -t bios")
    return output

drives = list_drives(connection)
cpu=cpu_info(connection)
fwversion=get_drivefw(connection)
bios=get_biosinfo(connection)
logs=get_logfiles(connection)
print(logs)



