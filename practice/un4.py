import paramiko

class SSHConnection:
    def __init__(self,hostname,username,password,port=22):
        self.hostname=hostname
        self.username=username
        self.password=password
        self.port=port
        self.client=None

    def connect(self):
        try:
            self.client=paramiko.SSHClient()
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.client.connect(self.hostname,username=self.username,password=self.password)
            print(f'successfully conected to {self.hostname}')
        except Exception as er:
            print(f'failed to connect to {self.hostname}:{er}')

    def disconnect(self):
        if self.client:
            self.client.close()
            print(f'{self.hostname} discoenncted')
        else:
            print('no active connection to discoennct')

'''
class SSHConnection:
    def __init__(self,hostname,username,password,port=22):
        self.hostname=hostname
        self.username=username
        self.password=password
        self.client=None
        
    def connect(self):
        try:
            self.client=paramiko.SSHClient()
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.client.connect(self.hostname,username=self.username,password=self.password)
            print(f'successfully connected to {self.hostname}')
        except Exception as err:
            print(f'failed to connect to {self.hostname}:{err}')
        
        def disconnect(self):
            if self.client:
                self.client.close()
                print(f'{self.hostname} discoenncetd')
            else:
                print('no active host to disconnect')'''