import paramiko
import sys

ipaddress='192.168.0.115'
username='winteck'
password='Winteck@2022'
port=22
def exec_command(cmd):
    client=paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=ipaddress,username=username,password=password)
    a,b,c=client.exec_command(cmd)
    out=b.read().decode()
    return out
if __name__=='__main__':
    print(exec_command('whoami'))
    print(exec_command('lsblk'))

