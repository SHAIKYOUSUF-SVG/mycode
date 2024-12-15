import paramiko
import pytest


def test_connect():

    # Update the next three lines with your
    # server's information

    host = "192.168.0.150"
    username = "winteck"
    password = "Winteck@2024"

    client = paramiko.client.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=username, password=password)
    _stdin, _stdout, _stderr = client.exec_command("whoami")
    usr=_stdout.read().decode().strip()
    client.close()
    if usr==username:
        assert True
    else:
        assert False

def test_connect2():

    # Update the next three lines with your
    # server's information

    host = "192.168.0.150"
    username = "winteck"
    password = "Winteck@2024"

    client = paramiko.client.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=username, password=password)
    _stdin, _stdout, _stderr = client.exec_command("uname")
    out=_stdout.read().decode().strip()
    client.close()
    if out=="Linux":
        assert True
    else:
        assert False