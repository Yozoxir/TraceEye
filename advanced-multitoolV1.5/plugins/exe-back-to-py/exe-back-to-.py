from pystyle import Colors, Col, Colorate, Center, System, Cursor
from py_compile import compile
from os import listdir, remove, mkdir, chdir
from os.path import isdir, isfile
from shutil import rmtree, copy
from subprocess import check_output
from etc.pyinstxtractor import extract
import os

os.system("cls")

banner = f"""
 $$$$$$\\  $$$$$$$\\  $$\\    $$\\  $$$$$$\\  $$\\   $$\\  $$$$$$\\  $$$$$$$$\\ $$$$$$$\\        $$$$$$$$\\ $$\\   $$\\ $$$$$$$$\\       $$$$$$$$\\  $$$$$$\\        $$$$$$$\\ $$\\     $$\\ 
$$  __$$\\ $$  __$$\\ $$ |   $$ |$$  __$$\\ $$$\\  $$ |$$  __$$\\ $$  _____|$$  __$$\\       $$  _____|$$ |  $$ |$$  _____|      \\__$$  __|$$  __$$\\       $$  __$$\\$$\\   $$  |
$$ /  $$ |$$ |  $$ |$$ |   $$ |$$ /  $$ |$$$$\\ $$ |$$ /  \\__|$$ |      $$ |  $$ |      $$ |      \\$$\\ $$  |$$ |               $$ |   $$ /  $$ |      $$ |  $$ |\\$$\\ $$  / 
$$$$$$$$ |$$ |  $$ |\\$$\\  $$  |$$$$$$$$ |$$ $$\\$$ |$$ |      $$$$$\\    $$ |  $$ |      $$$$$\\     \\$$$$  / $$$$$\\             $$ |   $$ |  $$ |      $$$$$$$  | \\$$$$  /  
$$  __$$ |$$ |  $$ | \\$$\\$$  / $$  __$$ |$$ \\$$$$ |$$ |      $$  __|   $$ |  $$ |      $$  __|    $$  $$<  $$  __|            $$ |   $$ |  $$ |      $$  ____/   \\$$  /   
$$ |  $$ |$$ |  $$ |  \\$$$  /  $$ |  $$ |$$ |\\$$$ |$$ |  $$\\ $$ |      $$ |  $$ |      $$ |      $$  /\\$$\\ $$ |               $$ |   $$ |  $$ |      $$ |         $$ |    
$$ |  $$ |$$$$$$$  |   \\$  /   $$ |  $$ |$$ | \\$$ |\\$$$$$$  |$$$$$$$$\\ $$$$$$$  |      $$$$$$$$\\ $$ /  $$ |$$$$$$$$\\          $$ |    $$$$$$  |      $$ |         $$ |    
\\__|  \\__|\\_______/     \\_/    \\__|  \\__|\\__|  \\__| \\______/ \\________|\\_______/       \\________|\\__|  \\__|\\________|         \\__|    \\______/       \\__|         \\__|    
"""

# Use static colors for the banner
banner = Colorate.Vertical(Colors.StaticRGB(173, 216, 230), Center.XCenter(banner))

class Riptide:
    def __init__(self, path: str):
        stage("Démarrage de l'extraction...")
        if isdir('extracted'):
            rmtree('extracted')
        stage("Renouvellement du répertoire 'extracted'...")
        mkdir('extracted')
        chdir('extracted')
        npath = path.split('\\')[-1]
        copy(path, npath)
        self.path = npath
        stage("Extraction des fichiers .EXE avec pyinstxtractor...")
        if not self.EXE_to_PYC():
            self.extracted = False
            chdir('..')
            rmtree('extracted')
        else:
            stage("Obtention du fichier .PYC avec le bytecode compilé du programme...")
            stage("Correction de l'en-tête du fichier .PYC...")
            self.PYCFIXER()
            stage("Décompilation du fichier .PYC avec pycdc...")
            self.PYC_to_PY()
            self.extracted = True

    def EXE_to_PYC(self):
        self.pyc = extract(self.path)
        if not self.pyc:
            return False
        pycpath = f'{self.path}_extracted/{self.pyc}'
        copy(pycpath, self.pyc)
        return True

    def PYCFIXER(self):
        header = self.GET_HEADER()
        with open(self.pyc, mode='rb') as f:
            content = f.read()[16:]
        with open(self.pyc, mode='wb') as f:
            f.write(header + content)

    def PYC_to_PY(self):
        check_output(f'start ..\\etc\\pycdc.exe -o "{self.pyc[:-1]}" "{self.pyc}"', shell=True)

    def GET_HEADER(self):
        with open('header.py', mode='w') as f:
            f.write('...')
        compile('header.py')
        pycache = '__pycache__'
        compiled = listdir(pycache)[0]
        with open(f'{pycache}/{compiled}', mode='rb') as f:
            header = f.read(16)
        rmtree(pycache)
        remove('header.py')
        return header

blue = Col.light_blue
lblue = Colors.StaticRGB(173, 216, 230)

def stage(text: str, symbol: str = '...'):
    if symbol == '...':
        print(f"{lblue}{symbol} {text}{Col.reset}")
    else:
        print(f"{blue}{symbol} {text}{Col.reset}")

def tui():
    System.Clear()
    System.Title("Exe-to-py")
    System.Size(160, 40)
    Cursor.HideCursor()
    print('\n')
    print(banner)
    print('\n' * 3)

def main():
    tui()
    path = input(stage(f"Drop le .exe que tu souhaite decompiler {lblue}-> ", '?')).replace('"', '').replace("'", "")
    print('\n')
    try:
        if not isfile(path):
            raise ValueError("Chemin de fichier invalide")
    except:
        input(f""" {blue} {Col.light_red}Fichier invalide!{Col.reset}""")
        exit()

    decompiled = Riptide(path)
    chdir('..')
    print('\n')
    if decompiled.extracted:
        path = f'extracted/{decompiled.pyc[:-1]}'
        if isfile(path):
            input(stage(f"Decompiler dans '{lblue}{path}{blue}'!", '!'))
        else:
            input(stage(f"Decompiler dans '{lblue}{path[:-1]}{blue}'!", '!'))
    else:
        input(f""" {blue} {Col.light_red}Impossible de décompiler le fichier ! Ce n'est peut-être pas une archive pyinstaller ?{Col.reset}""")

main()
