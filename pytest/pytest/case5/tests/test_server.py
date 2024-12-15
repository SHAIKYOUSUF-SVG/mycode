'''
connecting to server
'''

import paramiko
def test_connect():
    user="winteck"
    passwd="Winteck@2024"
    ip="192.168.0.108"
    client = paramiko.client.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, username=user, password=passwd)
    _stdin, _stdout, _stderr = client.exec_command("whoami")
    usr=_stdout.read().decode().strip()
    client.close()
    if usr==user:
        assert True
    else:
        assert False

def test_connect1():
    user = "winteck"
    passwd = "Winteck@2024"
    ip = "192.168.0.108"
    client = paramiko.client.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, username=user, password=passwd)
    _stdin, _stdout, _stderr = client.exec_command("uname")
    out=_stdout.read().decode().strip()
    client.close()
    if out=="Linux":
        assert True
    else:
        assert False
#
# import paramiko
# user = "winteck"
# passwd = "Winteck@2024"
# ip = "192.168.0.108"
# client = paramiko.client.SSHClient()
# client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# client.connect(ip, username=user, password=passwd)
# _stdin, _stdout, _stderr = client.exec_command("whoami")
# print(_stdout.read().decode())
# client.close()'''