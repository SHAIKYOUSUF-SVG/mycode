import pytest
import paramiko

def test_connect11(connect2server):
    client=connect2server
    a,b,c= client.exec_command("whoami")
    user=b.read().decode().strip()
    #client.close()
    if user=="winteck":
        assert True
    else:
        assert False
def test_connect12(connect2server):
    client=connect2server
    a,b,c= client.exec_command("uname")
    user=b.read().decode().strip()
    #client.close()
    if user=="Linux":
        assert True
    else:
        assert False

