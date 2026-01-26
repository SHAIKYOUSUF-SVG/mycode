import re
import paramiko

class sshclient:
    def __init__(self, ipaddress, username, password):
        self.ipaddress = ipaddress
        self.username = username
        self.password = password

    def connect1(self):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(hostname=self.ipaddress, username=self.username, password=self.password)
        a, b, c = self.client.exec_command("whoami")
        name= b.read().decode().strip()
        self.client.close()
        return name
    def get_drives(self):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(hostname=self.ipaddress, username=self.username, password=self.password)
        a, b, c = self.client.exec_command("lsblk")
        name1 = b.read().decode().strip()
        self.client.close()
        return name1
    def get_cpuinfo(self):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(hostname=self.ipaddress, username=self.username, password=self.password)
        a, b, c = self.client.exec_command("lscpu")
        name2 = b.read().decode().strip()
        self.client.close()
        return name2

    def get_drivefw(self):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(hostname=self.ipaddress, username=self.username, password=self.password)
        a, b, c = self.client.exec_command("smartctl -a /dev/sda")
        name3 = b.read().decode().strip()
        #exp="Revision:\s+([a-z]{2}[0-9]{2})"
        exp="Revision:\s+([A-Z]{2}[0-9]{2})"
        out=re.search(exp,name3)
        if out:
            return out.group(1)
        # self.client.close()
        # return name3

out=sshclient("192.168.0.136","winteck","Winteck@2024")

print(out.connect1())
print(out.get_drives())

print(out.get_cpuinfo())
print(out.get_drivefw())