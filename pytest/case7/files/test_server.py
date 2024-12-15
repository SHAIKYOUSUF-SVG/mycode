#set_up: also a test case before running all test case setup testcase will run
#teardown:after setup teardown will run
'''
before testcase start what to run is setup andafetr testcase stops what to run teardown
'''
import paramiko
def set_up():
    user="winteck"
    passw="Winteck@2024"
    host="192.168.0.150"
    client=paramiko.client.SSHClient()
    client.connect(host,username=user,password=passw)

def test_connect1():
    _stdin,_stdout,_stderr=client.exec_command("whoami")
    out=_stdout.read().decode().strip()
    if out==user:
        assert True
    else:
        assert False
def test_connect2():

    _stdin,_stdout,_stderr=client.exec_command("uname")
    out=_stdout.read().decode().strip()
    if out=="Linux":
        assert True
    else:
        assert False

