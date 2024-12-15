from para2 import sshclient
import re
class mainlib:
    def __init__(self):
        self.ssh=sshclient('192.168.0.124','root','Winteck@2023')
    def get_drives(self):
        return self.ssh.connect("lsblk")

    def get_cpuinfo(self):
        return self.ssh.connect('lscpu')

    def get_bios(self):
        return self.ssh.connect('dmidecode -t bios')

    def get_bmc(self):
        return self.ssh.connect('lspci')
    def get_ip(self):
        return self.ssh.connect('ifconfig')
    def get_users(self,cmd):
        return self.ssh.connect(cmd)
    def drive_capacity(self,drive_name):
        capacity=self.ssh.connect(f"lsblk {drive_name}")
        out1=re.search('[a-z]{3}.+([0-9]{3}\.[0-9]*G)',capacity)
        if out1:
            return out1.group(1)
    def get_drivefw(self,drive_name):
        fw=self.ssh.connect(f'smartctl -a {drive_name}')
        out2=re.search("Revision:\s+(.+)",fw)
        if out2:
            return out2.group(1)
    def raid_create(self,raidname,raidlevel,no_of_drives,*drives):
        drives_str = ' '.join(drives)
        raid=self.ssh.connect(f'mdadm --create {raidname} --force --level={raidlevel} --raid-devices={no_of_drives} {drives_str}')
        if raid:
            return self.ssh.connect('lsblk')



if __name__=="__main__":
    out=mainlib()
    print(out.get_drives())
    # print(get_cpuinfo())
    # print(get_bios())
    # print(get_bmc())
    # print(out.get_ip())
    # print(out.get_users("users"))
    #print(out.drive_capacity("/dev/sdc"))
    #print(out.get_drivefw("/dev/sda"))
    #print(out.raid_create('raid0',0,1,'/dev/sdd'))
