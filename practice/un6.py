import paramiko

def connect():
    client=paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname='192.168.0.115',username='winteck',password='Winteck@2022')
    return client


def get_mission_info():
    client=connect()
    a,b,c=client.exec_command('uname')
    output1=b.read().decode()
    client.close()
    return output1

def get_cpu_info():
    client=connect()
    a,b,c=client.exec_command('whoami')
    output=b.read().decode().strip()
    client.close()
    return output

def get_users_list():
    client=connect()
    a,b,c=client.exec_command('users')
    output2=b.read().decode().strip()
    return output2

if __name__=='__main__':
    out=get_cpu_info()
    print(out)
    out1=get_mission_info()
    print(out1)
    out2=get_users_list()
    print(out2)