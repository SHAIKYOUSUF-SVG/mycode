

import paramiko
import sys
# ipaddress=sys.argv[1]
# username=sys.argv[2]
# password=sys.argv[3]
port=22
def exec_command(cmd):
    client=paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=sys.argv[1],username=sys.argv[2],password=sys.argv[3])
    a,b,c=client.exec_command(cmd)
    out=b.read().decode()
    return out
if __name__=='__main__':
    print(exec_command('whoami'))
    print(exec_command('lsblk'))

