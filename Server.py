import os
import paramiko

class Server:
    """ Server class for representing and manipulating servers. """

    def __init__(self, server_ip):
        self.ip = server_ip

    def ping(self):
        address = self.ip
        response = os.system("ping " + address)
        return response
    
    def connect(self):
        server, usr_name, pwd = ('3.15.229.69', 'ubuntu', "")
        remote = paramiko.SSHClient()
        remote.load_system_host_keys()
        remote.connect(hostname=server, username=usr_name, password=pwd)
        if remote.get_transport() is not None:
            is_actv = remote.get_transport().is_active()
            print("transport active:", is_actv)
        cmd_a = "sudo apt-get update -y"
        a_in, a_out, a_err = remote.exec_command(cmd_a)
        a_in.flush()
        data_a = a_out.read().splitlines()
        for line in data_a:
            print(line)
        cmd_b = "sudo apt-get upgrade -y"
        b_in, b_out, b_err = remote.exec_command(cmd_b)
        b_in.flush()
        data_b = b_out.read().splitlines()
        for line in data_b:
            print(line)
        remote.close()
