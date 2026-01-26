import paramiko,argparse

parser=argparse.ArgumentParser()
parser.add_argument('ipaddress')
parser.add_argument('username')
parser.add_argument('password')

args=parser.parse_args()

ipaddress=args.ipaddress
username=args.username
password=args.password

def exec_command(cmd):
    client=paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=ipaddress,username=username,password=password)
    a,b,c=client.exec_command(cmd)
    out=b.read().decode()
    return out

print(exec_command('ls -l'))
print(exec_command('lsblk'))


