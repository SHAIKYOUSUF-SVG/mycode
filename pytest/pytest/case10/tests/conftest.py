import pytest
import paramiko
#run the fixture for every function
#@pytest.fixture(scope="function")
#run the fixture for every module
#@pytest.fixture(scope="module")
#run the fixture for every class
#@pytest.fixture(scope="class")
#run the fixture for entire session

@pytest.fixture(scope="session")
def connect2server():
    #this setup
    client = paramiko.client.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect("192.168.0.108", username="winteck", password="Winteck@2024")
    yield client
    #this is teardown
    client.close()