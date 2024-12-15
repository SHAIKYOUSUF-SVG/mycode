import paramiko

class SSHConnect:
    def __init__(self,hostname,username,password):
        self.hostname=hostname
        self.username=username
        self.password=password

    def connect(self):
        self.client=paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(hostname=self.hostname,username=self.username,password=self.password)

    def get_ip(self):
        if self.client:
            a,b,c=self.client.exec_command('ifconfig')
            ip=b.read().decode().strip()
            self.client.close()
            return ip
if __name__=="__main__":
    out = SSHConnect('192.168.0.113', 'root', 'Winteck@2022')
    out.connect()
    print(out.get_ip())

