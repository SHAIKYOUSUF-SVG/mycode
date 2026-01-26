import paramiko
import sys

import datetime

class SSHConnect:
    if len(sys.argv)!=4:
        sys.exit()
    def connect(self):
        self.client=paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(hostname=sys.argv[1],username=sys.argv[2],password=sys.argv[3])
    def get_ip(self,cmd):
        if self.client:
            a,b,c=self.client.exec_command(cmd)
            ip=b.read().decode().strip()
            self.client.close()
            return ip
    def get_uname(self,cmd):
        if self.client:
            a,b,c=self.client.exec_command(cmd)
            un=b.read().decode().strip()
            self.client.close()
            return un
    def get_date(self,cmd):
        if self.client:
            a, b, c = self.client.exec_command(cmd)
            un = b.read().decode().strip()
            self.client.close()
            return un





out=SSHConnect()
out.connect()
# print(out.get_ip('ifconfig')
print(out.get_uname('uname-a'))
print(out.get_date('date'))