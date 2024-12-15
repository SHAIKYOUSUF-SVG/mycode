from un5 import SSHConnection

class SSHConnectionExpansion(SSHConnection):
    def get_cpu_info(self,cmd):
        # if not self.client:
        #     self.connect()
        if self.client:
            a,b,c=self.client.exec_command(cmd)
            output=b.read().decode().strip()
            return output
        # else:
        #     self.connect()
        #     if self.client:
        #         a, b, c = self.client.exec_command(cmd)
        #         output = b.read().decode().strip()
        #         return output
        else:
            return None
    def get_date(self,cmd):
        if self.client:
            a, b, c = self.client.exec_command(cmd)
            output1 = b.read().decode().strip()
            return output1
        else:
            return None

    def get_drive_info(self,cmd):
        if self.client:
            a,b,c=self.client.exec_command(cmd)
            output2=b.read().decode().strip()
            return output2
        else:
            return None
    def creat_raid(self,cmd):
        if self.client:
            a,b,c=self.client.exec_command(cmd)
            output3=b.read().decode().strip()
            return output3
        else:
            return None

if __name__=='__main__':
    out=SSHConnectionExpansion('192.168.0.107','winteck','Winteck@2024')
    cpu_info=out.get_cpu_info('lscpu')
    print(cpu_info)
    print(out.get_date('date'))
    print(out.get_drive_info('smartctl -a /dev/sda'))
    print(out.creat_raid('mdadm --create raid0 --state=0 --raid-devices=2 /dev/sdd /dev/sdc '))