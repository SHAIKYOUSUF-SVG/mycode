import paramiko
import pytest
@pytest.fixture
def connect_server():
    client=paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect("192.168.0.143",username="winteck",passwd="Winteck@2024")
    yield
    client.close()
def get_hw_info(cmd):
    a, b, c = client.exec_command("dmidecode -t bios")
    out = b.read().decode().strip()


@pytest.mark.slow
def test_get_hw_info():

    if out:
        assert True
    else:
        assert False

class ssh:


