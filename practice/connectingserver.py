import paramiko
import logging as log
log.basicConfig(filename="connectigserver2.log",level="WARNING")

def sshclient():
    log.info("about connecting to srevr")
    host="192.168.0.113"
    hostname="winteck"
    passwd="Winteck@2024"
    client=paramiko.client.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    client.connect(host,username=hostname,password=passwd)
    a,b,c=client.exec_command("whoami")
    #a,b1,c=client.exec_command("lsblk")
    out=b.read().decode().strip()
    #cout1=b1.read().decode().strip()
    client.close()

    if out=="winteck":
        print("connectted")

        log.info("severe is connect")
    else:
        print("not connected")
        log.critical("server is not connected")
    client.close()
sshclient()

host="192.168.0.113"
name="winteck"
passwd="Winteck@2024"
client=paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
client.connect(host,username=name,password=passwd)
a,b,c=client.exec_command("whoami")
out=b.read().decode().strip()
client.close()
if out=="winteck":
    print("connectted")
else:
   print("not connected")

