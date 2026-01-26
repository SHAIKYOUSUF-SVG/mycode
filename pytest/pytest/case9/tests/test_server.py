c'''
connecting to server
setting ficxtures
in fixtures we use setup and teardown

'''
import paramiko
import pytest
@pytest.fixture
def connect2server():

    client = paramiko.client.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect("192.168.0.108", username="winteck", password="Winteck@2024")
    yield client
    client.close()
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
    _stdin, _stdout, _stderr = client.exec_command("whoami")
    out=_stdout.read().decode().strip()
    client.close()
    if out=="Linux":
        assert True
    else:
        assert False


