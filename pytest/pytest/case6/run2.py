import paramiko
user = "winteck"
passwd = "Winteck@2024"
ip = "192.168.0.108"
client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(ip, username=user, password=passwd)
_stdin, _stdout, _stderr = client.exec_command("uname")
print(_stdout.read().decode().strip())
client.close()