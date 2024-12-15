import paramiko
class sshclient:
    def __init__(self, ipaddress, username, password):
        self.ipaddress = ipaddress
        self.username = username
        self.password = password
        self.client = None

    def connect(self):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(hostname=self.ipaddress, username=self.username, password=self.password)

    def uname(self):
        if self.client is None:
            self.connect()
        stdin, stdout, stderr = self.client.exec_command("whoami")
        name = stdout.read().decode().strip()
        self.client.close()
        return name
    # def get_date(self):
    #     if self.client is None:
    #         self.connect()
    #     stdin1, stdout1, stderr1 = self.client.exec_command("date")
    #     name1 = stdout1.read().decode().strip()
    #     self.client.close()
    #     return name1

out = sshclient("192.168.0.107", "winteck", "Winteck@2024")
print(out.uname())
#print(out.get_date())