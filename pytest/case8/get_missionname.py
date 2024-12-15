
#to get the mission name of the servercith your
    # server's information
host = "192.168.0.150"
username = "winteck"
password = "Winteck@2024"

client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=username, password=password)
_stdin, _stdout, _stderr = client.exec_command("uname")
print(_stdout.read().decode().strip())
client.close()