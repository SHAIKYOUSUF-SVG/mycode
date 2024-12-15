import paramiko

class SSHConnection:
    def __init__(self,hostname,username,password):
        self.hostname=hostname
        self.username=username
        self.password=password
        self.client=None
    def connect(self):
        try:
            self.client=paramiko.SSHClient()
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.client.connect(self.hostname,username=self.username,password=self.password)
            print(f'{self.username} connected successfully')
        except Exception as er:
            print(f'failed to connect {self.username}:{er}')
    def disconnect(self):
        if self.client:
            self.client.close()
            print(f'{self.username} discoenncted successsfully')
        else:
            print('no active connection to disconent')

