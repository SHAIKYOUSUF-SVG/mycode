from un4 import SSHConnection
import datetime
import re
class SSHConnectionExpansion(SSHConnection):
    def get_ip(self,cmd):
        if self.client:
            a,b,c=self.client.exec_command(cmd)
            output=b.read().decode()
            return output
        else:
            self.connect()
            if self.connect:
                a,b,c=self.client.exec_command(cmd)
                output=b.read().decode()
                return output
            else:
                return None
    def get_drives(self,cmd):
        if self.client:
            a,b,c=self.client.exec_command(cmd)
            out=b.read().decode().strip()
            return out
    def create_raid(self,cmd):
        a,b,c=self.client.exec_command(cmd)
        out1=b.read().decode().strip()
        return out1

a=SSHConnectionExpansion('192.168.0.107', 'winteck', 'Winteck@2024')
ip_output=a.get_ip('ifconfig')
print(ip_output)
print(a.get_date('date'))
print(a.create_raid('lsblk'))

a.disconnect()