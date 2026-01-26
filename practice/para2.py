import paramiko
class sshclient:
    def __init__(self,host,username,password):
        self.host=host
        self.username=username
        self.password=password
    def connect(self,cmd):
        client = paramiko.client.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=self.host, username=self.username, password=self.password)
        _stdin, _stdout,_stderr = client.exec_command(cmd)
        result=_stdout.read().decode()
        client.close()
        return result
#out1=sshclient("192.168.0.124","root","Winteck@2023")
#print(out.connect('lsblk'))