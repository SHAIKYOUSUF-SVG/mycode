import paramiko

class ServerDrives:
    def _init_(self, hostname, username, password):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.client=None

    def connect(self):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            self.client.connect(hostname=self.hostname, username=self.username, password=self.password)
        except Exception as e:
            print(e)

    def get_drives(self,cmd):
        try:
            stdin, stdout, stderr = self.client.exec_command(cmd)
            output = stdout.read().decode().strip()
            headers = output[0].split()
            return headers
        except Exception as e:
            return None
    def close(self):
        if self.client:
            self.client.close()

out=ServerDrives('192.168.0.112','winteck','Winteck@2024')
print(out.__dict__)