'''
connecting to server
setting ficxtures
in fixtures we use setup and teardown

'''
import paramiko
import pytest
def test_connect(connect2server):
    client=connect2server
    a,b,c=client.exec_command("whoami")
    user=b.read().decode().strip()
    if user=="winteck":
        assert True
    else:
        assert False
def test_connect1(connect2server):
    client=connect2server
    a,b,c= client.exec_command("whoami")
    out=b.read().decode().strip()
    #client.close()
    if out=="Linux":
        assert True
    else:
        assert False


