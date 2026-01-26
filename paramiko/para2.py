
'''
how to connect to server using python
'''


import paramiko
host="ipaddress"
username="username"
password=""


a=paramiko.client.SSHClient()
a.set_missing_host_key_policy(paramiko.AutoAddPolicy())
a.connect(host,username=username,password=password)
x,y,z=a.exec_command("pwd")