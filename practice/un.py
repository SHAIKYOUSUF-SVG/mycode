import os
import re
import paramiko
def uname():
    client = paramiko.client.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname="192.168.0.112", username="winteck", password="Winteck@2024")
    a, b, c = client.exec_command("whoami")
    name= b.read().decode().strip()
    client.close()
    return name
out=uname()
print(out)
##############################################
class sshconnect:
    def __init__(self,ipaddress,username,password):
        self.ipaddress=ipaddress
        self.username=username
        self.password=password
    def get_username(self):
        return self.username

    def connect1(self):
        client=paramiko.client.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname="192.168.0.112", username="winteck", password="Winteck@2024")
        a,b,c=client.exec_command("whoami")
        out=b.read().decode().strip()
        print('############')
        return out


    def connect2(self):
        client=paramiko.client.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname="192.168.0.112", username="winteck", password="Winteck@2024")
        a,b,c=client.exec_command("lsblk")
        out=b.read().decode().strip()
        print(out)


    def connect3(self):
        client = paramiko.client.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname="192.168.0.112", username="winteck", password="Winteck@2024")
        out1=os.system("mdadm --create /dev/md1 --level=1 --raid-devices=2 /dev/sdb /dev/sdc")
        print(out1)
        a=client.exec_command("df -h")
        exp="md1"
        out=re.search(exp,a)
        if out:
            print(out)
    def connect3(self):
        client = paramiko.client.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname="192.168.0.112", username="winteck", password="Winteck@2024")
        


obj=sshconnect("192.168.0.136","winteck","Winteck@2024")
print(obj.__dict__)
print(obj.get_username())

print(obj.connect1())
print(obj.connect2())
print(obj.connect3())