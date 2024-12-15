import paramiko

class sshclient:
    def __init__(self, ipaddress, username, password):
        self.ipaddress = ipaddress
        self.username = username
        self.password = password

    def connect(self):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            self.client.connect(hostname=self.ipaddress, username=self.username, password=self.password)
            a, b, c = self.client.exec_command("whoami")
            name = b.read().decode().strip()
            self.client.close()
            return name
        except paramiko.AuthenticationException:
            return "Authentication failed."
        except paramiko.SSHException as sshException:
            return f"Unable to establish SSH connection: {sshException}"
        except Exception as e:
            return f"Exception in connecting to SSH: {e}"

out = sshclient("192.168.0.1o7", "winteck", "Winteck@2024")

print(out.connect())
