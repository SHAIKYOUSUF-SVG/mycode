# import paramiko
# a=paramiko.client.SSHClient()
# a.set_missing_host_key_policy(paramiko.AutoAddPolicy)
# a.connect("192.168.0.124",username="winteck",password="Winteck@2024")
# x,y,z=a.exec_command("whoami")
# print(y.read().decode().strip())
# a.close()

import paramiko

#command = ("ps")
#command = ("dmidecode")
#command = ("uname -a")
#command = ("uname")
#command = ("whoami")
#command = ("ls")
#command = ("ps")
command = ("lsblk")

# Update the next three lines with your
# server's information

host = "192.168.0.124"

username = "root "
password = "Winteck@2024"

client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=username, password=password)
_stdin, _stdout,_stderr = client.exec_command(command)
print(_stdout.read().decode())
client.close()