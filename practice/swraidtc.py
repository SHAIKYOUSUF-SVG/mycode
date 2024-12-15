import pytest
import paramiko
import os
import re
@pytest.fixture
def connect2server():
    client=paramiko.client.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect("192.168.0.112",username="root",password="Winteck@2024")
    yield client
    client.close()
def test_connect(connect2server):
    client=connect2server
    a,b,c=client.exec_command("whoami")
    out=b.read().decode().strip()
    if out=="root":
        assert True
    else:
        assert False


def test_connect1(connect2server):
    client=connect2server
    a,b,c=client.exec_command("lsblk")
    out=b.read().decode().strip()
    if out:
        assert True
        print(out)
    else:
        assert Fasle





def test_sw(connect2server):
    client=connect2server
    out1=os.popen("mdadm --create /dev/md1 --level=1 --raid-devices=2 /dev/sdb /dev/sdc")
    print(out1)
    a=client.exec_command("lsblk")
    exp=""
    out=re.search(exp,a)
    if out:
        assert True
    else:
        assert False


