import os
from marshal import dumps
from binascii import hexlify
from random import randint, shuffle
from pystyle import Col, Center, Colorate, System, Cursor, Add

os.system("cls")

banner1 = r'''
 $$$$$$\  $$$$$$$\  $$\    $$\  $$$$$$\  $$\   $$\  $$$$$$\  $$$$$$$$\ $$$$$$$\         $$$$$$\  $$$$$$$\  $$$$$$$$\ $$\   $$\  $$$$$$\   $$$$$$\   $$$$$$\ $$$$$$$$\  $$$$$$\  $$$$$$$\        $$\    $$\  $$$$$$\  
$$  __$$\ $$  __$$\ $$ |   $$ |$$  __$$\ $$$\  $$ |$$  __$$\ $$  _____|$$  __$$\       $$  __$$\ $$  __$$\ $$  _____|$$ |  $$ |$$  __$$\ $$  __$$\ $$  __$$\\__$$  __|$$  __$$\ $$  __$$\       $$ |   $$ |$$  __$$\ 
$$ /  $$ |$$ |  $$ |$$ |   $$ |$$ /  $$ |$$$$\ $$ |$$ /  \__|$$ |      $$ |  $$ |      $$ /  $$ |$$ |  $$ |$$ |      $$ |  $$ |$$ /  \__|$$ /  \__|$$ /  $$ |  $$ |   $$ /  $$ |$$ |  $$ |      $$ |   $$ |\__/  $$ |
$$$$$$$$ |$$ |  $$ |\$$\  $$  |$$$$$$$$ |$$ $$\$$ |$$ |      $$$$$\    $$ |  $$ |      $$ |  $$ |$$$$$$$\ |$$$$$\    $$ |  $$ |\$$$$$$\  $$ |      $$$$$$$$ |  $$ |   $$ |  $$ |$$$$$$$  |      \$$\  $$  | $$$$$$  |
$$  __$$ |$$ |  $$ | \$$\$$  / $$  __$$ |$$ \$$$$ |$$ |      $$  __|   $$ |  $$ |      $$ |  $$ |$$  __$$\ $$  __|   $$ |  $$ | \____$$\ $$ |      $$  __$$ |  $$ |   $$ |  $$ |$$  __$$<        \$$\$$  / $$  ____/ 
$$ |  $$ |$$ |  $$ |  \$$$  /  $$ |  $$ |$$ |\$$$ |$$ |  $$\ $$ |      $$ |  $$ |      $$ |  $$ |$$ |  $$ |$$ |      $$ |  $$ |$$\   $$ |$$ |  $$\ $$ |  $$ |  $$ |   $$ |  $$ |$$ |  $$ |        \$$$  /  $$ |      
$$ |  $$ |$$$$$$$  |   \$  /   $$ |  $$ |$$ | \$$ |\$$$$$$  |$$$$$$$$\ $$$$$$$  |       $$$$$$  |$$$$$$$  |$$ |      \$$$$$$  |\$$$$$$  |\$$$$$$  |$$ |  $$ |  $$ |    $$$$$$  |$$ |  $$ |         \$  /   $$$$$$$$\ 
\__|  \__|\_______/     \_/    \__|  \__|\__|  \__| \______/ \________|\_______/        \______/ \_______/ \__|       \______/  \______/  \______/ \__|  \__|  \__|    \______/ \__|  \__|          \_/    \________|'''[1:]

banner2 = r"""
                            ,-.                               
       ___,---.__          /'|`\          __,---,___        
    ,-'    \`    `-.____,-'  |  `-.____,-'    //    `-.     
  ,'        |           ~'\     /`~           |        `.    
 /      ___//              `. ,'          ,  , \___      \  
|    ,-'   `-.__   _         |        ,    __,-'   `-.    |  
|   /          /\_  `   .    |    ,      _/\          \   | 
\  |           \ \`-.___ \   |   / ___,-'/ /           |  /
 \  \           | `._   `\\  |  //'   _,' |           /  /    
  `-.\         /'  _ `---'' , . ``---' _  `\         /,-'   
     ``       /     \    ,='/ \`=.    /     \       ''        
             |__   /|\_,--.,-.--,--._/|\   __|                
             /  `./  \\`\ |  |  | /,//' \,'  \                
            /   /     ||--+--|--+-/-|     \   \               
           |   |     /'\_\_\ | /_/_/`\     |   |              
            \   \__, \_     `~'     _/ .__/   /            
             `-._,-'   `-._______,-'   `-._,-'"""[1:]

banner = Add.Add(banner1, banner2, center=True)

r = 128  # Red component
g = 0    # Green component
b = 128  # Blue component

purple = Col.StaticRGB(r, g, b)

def stage(text: str, symbol: str = '...') -> str:
    ppurple = purple if symbol == '...' else Col.light_blue
    return f""" {symbol} {ppurple}{text}{Col.reset}"""

class Specter:

    vars = []

    @staticmethod
    def specterize(script: str) -> str:
        print(stage("Démarrer la spectérisation!"))
        script = Specter.anti_skid(script=script)
        print(stage("Ajout du calque 1!"))
        script = Specter.layer_1(script=script)
        print(stage("Ajout du calque 2!"))
        script = Specter.layer_2(script=script)
        print(stage("Ajout du calque 3!"))
        script = Specter.layer_3(script=script)
        return script

    @staticmethod
    def hex(text: str) -> str:
        return "b'" + "".join(fr"\x{hexlify(t.encode('utf-8')).decode()}" for t in text) + "'"

    @staticmethod
    def encrypt(text: str, key: int) -> str:
        return "\x00".join(str(ord(x)+key) for x in text)

    @staticmethod
    def randvar() -> str:
        var = randint(1000, 9999)
        while var in Specter.vars:
            var = randint(1000, 9999)
        Specter.vars.append(var)
        return f"__{var}__"
    
    @staticmethod
    def get_key_by_value(vars, key) -> str:
        return list(vars.keys())[list(vars.values()).index(key)]

    @staticmethod
    def anti_skid(script: str) -> str:
        return r"""
try:
    if (
        __author__ != "Yozoxir" or
        __github__ != "https://github.com/Yozoxir/Advanced-multitools" or
        __discord__ != "https://discord.gg/ZDb4DYdtXS" or
        __license__ != "EPL-2.0" or
        __code__ != "Allez star les rhey!" or
        "Specter" not in globals() or
        "Func" not in globals()
    ):
        int('skid')
except:
    input("Vous venez d'exécuter un fichier obscurci avec Advanced Multi-Tools!\n\nAuthor: Yozoxir\nGitHub: https://github.com/Yozoxir/Advanced-multitools\nDiscord: https://discord.gg/ZDb4DYdtXS")
    __import__('sys').exit()    


"""[1:] + script

    @staticmethod
    def layer_1(script: str) -> str:
        ten_split = []
        key = randint(3, 33)
        splitting = randint(3, 9)
        while True:
            if len(script) >= splitting:
                ten_split.append(Specter.hex(Specter.encrypt(script[:splitting], key)))
                script = script[splitting:]
            else:
                ten_split.append(Specter.hex(Specter.encrypt(script, key)))
                break
        lexec = Specter.hex(Specter.encrypt("exec", key))
        lkey = Specter.hex(str(key))
        ten_split.append(lexec)
        ten_split.append(lkey)
        ten_split.append("globals")
        correct = [x for x in ten_split]
        shuffle(ten_split)
        vars = {Specter.randvar(): x for x in ten_split}
        script = ",".join(vars.keys()) + '=' + ",".join(vars.values()) + '\n'
        all_correct = []
        for x in correct:
            if x not in (lexec, lkey, "globals"):
                all_correct.append(Specter.get_key_by_value(vars, x))
        l1, l2, l3 = Specter.randvar(), Specter.randvar(), Specter.randvar()
        glob = f"{Specter.get_key_by_value(vars, 'globals')}()[{l1}({l2}={Specter.get_key_by_value(vars, lexec)})]"
        print(stage("Creating random vars..."))
        lambdas = [fr"{l1}=lambda {l2}:''.join(chr(int({l3})-int({lkey}))for {l3} in {l2}.decode().split('\x00'))",
                   f"(lambda {l3}:{glob}(''.join({l1}({l2}={l2})for {l2} in {l3}),{Specter.get_key_by_value(vars, 'globals')}()))([{','.join(all_correct)}])",]
        script = "from builtins import *\n" + script + '\n'.join(lambdas)
        return script

    @staticmethod
    def layer_2(script: str) -> str:
        print(stage("Compilation et dumping du code avec Marshal..."))
        return dumps(compile(script, 'Specter', 'exec'))

    @staticmethod
    def layer_3(script: str) -> str:
        split = []
        splitting = 2000
        while True:
            if len(script) >= splitting:
                split.append(script[:splitting])
                script = script[splitting:]
            else:
                split.append(script)
                break
        vars = {Specter.randvar(): x for x in split}
        codevars = "\n".join(f"{a} = Func.calculate({randint(1,9)}){' ' * 500},Func.define('{a}', {b})" for a, b in vars.items())
        print(stage("Camouflage du code obfusqué..."))
        script = fr"""

__author__ = "Yozoxir"
__github__ = "https://github.com/yozoxir/Advanced-multitools"
__discord__ = "https://discord.gg/ZDb4DYdtXS"
__license__ = "EPL-2.0"
__code__ = "Allez regarder le tool !"

Any = (...,)

class Specter:
    def __init__(self, code: str) -> None:
        self.code = code
        self.execute(...)
        return None
    def execute(self, code: str = ...) -> None:
        return exec(str(code))
    
class Func:
    def calculate(num: int) -> int:
        return num*2
    def define(key, value: Any) -> Any:
        globals()[key] = value
        return globals()[key]

{codevars}

if __name__ == '__main__':
    Specter(__code__){' ' * 500},exec(__import__('marshal').loads({"+".join(var + "[1]" for var in vars)}),globals())"""[1:]
        return script

def main():
    System.Size(150, 40)
    System.Title("Advanced-obfv2")
    Cursor.HideCursor()
    print()
    print(Colorate.Diagonal(Col.StaticRGB(128, 0, 128), Center.XCenter(banner + '\n\n')))

    file = input(stage(f"Faites glisser le fichier que vous souhaitez obfusquer {Col.blue}-> {Col.reset}", "?")).replace('"','').replace("'","")
    print('\n')

    try:
        with open(file, mode='r', encoding='utf-8') as f:
            script = f.read()
        filename = file.split('\\')[-1]
    except:
        input(f"""{stage("Fichier invalide!", '!')}""")
        exit()

    script = Specter.specterize(script=script)

    with open(f'obf-{filename}', mode='w', encoding='utf-8') as f:
        f.write(script)
    
    print('\n')
    input(stage("Fait!", '!'))

main()
