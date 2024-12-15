import paramiko
class sshclient:
    def __init__(self,ipaddress,username,password):
        self.ipaddress=ipaddress
        self.username=username
        self.passwrod=password

    def connect(self):
        client=paramiko.client.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=self.ipaddress,username=self.username,password=self.passwrod)
        a,b,c=client.exec_command("whoami")
        out=b.read().decode().strip()
        client.close()
        return out
obj=sshclient('192.168.0.124','root','Winteck@2023')

print(obj.__dict__)
print(obj.connect())