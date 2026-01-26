import paramiko
class sshconnect:
    def __init__(self,ipaddress,username,password):
        self.ipaddress=ipaddress
        self.username=username
        self.password=password
        self.client=None


    def connect(self,cmd):
        self.client=paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(self.ipaddress,username=self.username,password=self.password)
        a,b,c=self.client.exec_command(cmd)
        out=b.read().decode().strip()
        self.client.close()
        return out




connection=sshconnect("192.168.0.112","root","Winteck@2024")
# out=connection.connect("whoami")
# out=connection.connect("lsblk")
# print(out)

import paramiko
class sshconnect:
    def __init__(self,ipaddress,username,password):
        self.ipaddress=ipaddress
        self.username=username
        self.password=password
        self.client=None
    def connect(self,cmd):
        self.client=paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(self.ipaddress,username=self.username,password=self.password)
        a,b,c=self.client.exec_command(cmd)
        out=b.read().decode().strip()
        self.client.close()
        return out
connection=sshconnect("192.168.0.109","winteck","Winteck@2024")




