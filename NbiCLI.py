import telnetlib
import time


# Berlin:   telnet 10.217.156.11 31114
# Hannover: telnet 10.217.156.31 31114
# Munich:   telnet 10.217.136.141 31114
# Dresden:  telnet 10.217.136.161  31114

class FileManager:
    """"""


class Credentials:
    def __init__(self, file):
        try:
            with open(file, 'r') as self.file:
                self.user = self.file.readlines()[0]
                self.pw = self.file.readlines()[1]
                self.nename = self.file.readlines()[2]
        except:
            FileNotFoundError("Please recheck credentials file.")

    def login_command(self):
        return b'LGI:OP="' + bytes(self.__user, 'utf-8') + bytes(
            self.__pw) + b'";\n'


class TelnetNbi:
    def __init__(self, host, port, timeout):

        self.host = host
        self.port = port
        self.timeout = timeout
        self.session = telnetlib.Telnet(self.host, self.port, self.timeout)

    def connect(self, connect_command):
        try:
            self.session.write(connect_command + b'\r\n')
        except:
            ConnectionRefusedError("LGI session not connected")

    def register(self, reg_command):
        self.session.write(reg_command + b'\r\n')

    def send_mml_command(self, mml_command):
        self.session.write(mml_command + b'\r\n')

    def script_activate(self, script_path):
        self.session.write(b'S_ACTIVATE: FILE="' + script_path + b'";\r\n')

    def read(self):
        print(self.session.read_very_eager())

    def close_connection(self):
        self.session.close()
        print('Connection closed')


# credentials = Credentials('login.txt')


socket = TelnetNbi('10.217.136.161', '31114', 30)
socket.connect(b'LGI:OP="vmihai1",PWD="Huawei2020!";')
# socket.register(b'REG NE:IP="2a01:8f1:e065:2:0:0:0:2";')
socket.register(b'REG NE:NAME="OB1055";')
socket.send_mml_command(b'LST CELL:;')
socket.send_mml_command(b'LST RET:;')
socket.send_mml_command(b'LST TMA:;')
socket.script_activate(b'mmlscriptNBItest1.txt')
# socket.read()
socket.close_connection()
print(socket)

# write/import scripts to the path for script execution
# write commands to command file