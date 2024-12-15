import paramiko
import re
import logging as log

def connectingserver():
    command = "lsblk"
    host = "192.168.0.113"
    username = "winteck"
    password = "Winteck@2024"
    client = paramiko.client.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=username, password=password)
    _stdin, _stdout, _stderr = client.exec_command(command)
    out=_stdout.read().decode().strip()
    #print(out)
    client.close()
    #exp=("\w+\s\d+\:\d+\
    # s\d+\s\d+\.\w+\s\d?\t\w+\s\/\w+\/\w+\/\d+")
    #exp=("loop\d+\s+.\:.+")
    exp=("loop.+")
    out=re.findall(exp,out)
    if out:
        print(out)
        for i in out:
            i=i.strip()
            out=re.search("0",i)
            print(out)
    else:
        print("not found")
connectingserver()
