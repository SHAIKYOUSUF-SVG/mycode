from un6 import connect
client=connect()
def get_drives_info():

    a,b,c=client.exec_command('lsblk')
    output=b.read().decode().strip()
    return output
out=get_drives_info()
print(out)