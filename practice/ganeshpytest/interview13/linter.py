# linters_are:black,pycodestyle
#pycodestyle:used to check any errors [pycodestyle linter.py]
#black linter will check and re -erange the code in correct manner [black linetr.py]


import paramiko


class sshconnect:
    client = paramiko.client.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    client.connect("192.168.0.143", username="winteck", password="Winteck@2024")

    def get_username(self):
        a, b, c = client.exec_command("whoami")
        out = b.read().decode().strip()
        print(out)

    def get_driveslist(self):
        a, b, c = client.exec_command("lsblk")
        out = b.read().decode().strip()
        print(out)

    def get_diskfree(self):
        a, b, c = client.exec_command("df -h")
        out = b.read().decode().strip()
        print(out)


out = sshconnect()
print(out.get_username())
