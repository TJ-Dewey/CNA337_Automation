import os

class Server:
    """ Server class for representing and manipulating servers. """

    def __init__(self, server_ip):
        self.ip = server_ip

    def ping(self):
        address = self.ip
        response = os.system("ping " + address)
        return response
