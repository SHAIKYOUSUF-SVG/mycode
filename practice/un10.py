import paramiko
# import os
#
#
# client=paramiko.SSHClient()
# client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# client.connect(hostname='192.168.0.136',username='winteck',password='Winteck@2024')
# client.exec_command('whoami')
# client.close()

class SSH:
    def __init__(self,hostname,username,password):
        self.hostname=hostname
        self.username=username
        self.password=password
        self.client=None

    def connect(self):
        self.client=paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(hostname=self.hostname,username=self.username,password=self.password)

    def get_uname(self):
        if not self.client:
            self.connect()
        a,b,c=self.client.exec_command('uname -a')
        out1=b.read().decode().strip()
        return out1

    def get_drives(self):
        if self.client:
            #self.connect()
            a1,b1,c1=self.client.exec_command('lsblk')
            out2=b1.read().decode().strip()
            return out2

    def get_cpu_info(self):
        if not self.client:
            self.connect()
        a,b,c=self.client.exec_command('lscpu')
        out3=b.read().decode().strip()
        return out3

    def switch_to_root(self):
        if not self.client:
            self.connect()
        a,b,c=self.client.exec_command('sudo -S whoami')
        a.write('Winteck@2024\n')
        a.flush()
        out5=b.read().decode().strip()
        error=c.read().decode().strip()
        if error and "incorrect password" in error.lower():
            raise Exception(f'Raid creation failed: Incorrect password - {error}')
        elif error:
            print(f'Warning: {error}')  # Non-fatal warnings can be logged
        if out5=='root':
            return out5
        else:
            raise Exception('failed to switch to root user')


    def create_raid(self,arg1,arg2,no,drive_names):
        if not self.client:
            self.connect()
        a,b,c=self.client.exec_command(f'sudo -s mdadm --create {arg1} --level={arg2} --force --raid-devices={no} {drive_names}')
        out4=b.read().decode().strip()
        error=c.read().decode().strip()
        if error:
            raise Exception(f'raid creation failed: {error}')
        a,b,c=self.client.exec_command('lsblk')
        lsblk_output=b.read().decode().strip()

        return lsblk_output,out4




    def close(self):
        if self.client:
            self.client.close()



out=SSH('192.168.0.136','winteck','Winteck@2024')
# print(out.get_uname())
# print(out.get_drives())
# print(out.get_cpu_info())
print(out.switch_to_root())
print(out.create_raid('/dev/md0',0,1,'/dev/sdb'))
