# Par yozoxir

#https://github.com/Yozoxir/Advanced-multitools



from random import choice, randint, shuffle
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from os.path import isfile, isdir
from py_compile import compile
from os import listdir, mkdir, remove, rmdir, rename, chdir, name
from shutil import move, copy, rmtree
from time import sleep
from binascii import hexlify


    
    
strings = "abcdefghijklmnopqrstuvwxyz0123456789"  # ne pas changer svp


class Kyrie():

    def encrypt(e: str):
        e = Kyrie._ekyrie(e)
        return Kyrie._encrypt(e)

    def decrypt(e: str):
        text = Kyrie._decrypt(e)
        return Kyrie._dkyrie(text)

    def _ekyrie(text: str):

        r = ""
        for a in text:
            if a in strings:
                a = strings[strings.index(a)-1]
            r += a
        return r

    def _dkyrie(text: str):
        r = ""
        for a in text:
            if a in strings:
                i = strings.index(a)+1
                if i >= len(strings):
                    i = 0
                a = strings[i]
            r += a
        return r

    def _encrypt(text: str, key: str = None):
        if type(key) == str:
            key = sum(ord(i) for i in key)
        t = [chr(ord(t)+key)if t != "\n" else "ζ" for t in text]
        return "".join(t)

    def _decrypt(text: str, key: str = None):
        if type(key) == str:
            key = sum(ord(i) for i in key)
        return "".join(chr(ord(t)-key) if t != "ζ" else "\n" for t in text)


class Key:

    def encrypt(e: str, key: str):
        e1 = Kyrie._ekyrie(e)
        return Kyrie._encrypt(e1, key=key)

    def decrypt(e: str, key: str):
        text = Kyrie._decrypt(e, key=key)
        return Kyrie._dkyrie(text)



def ran_int(min: int = 3, max: int = 1000000):
    return randint(min, max+1)


def kramer(content: str, key: int) -> str:

    _content_ = Key.encrypt(content, key=key)

    _lines_sep_ = '/'


    content = _lines_sep_.join(hexlify(x.encode()).decode() for x in _content_)

    _names_ = ["_eval", "_exec", "_byte", "_bytes", "_bit", "_bits", "_system", "_encode", "_decode", "_delete", "_exit", "_rasputin", "_kramer"]
    _names_ = ["self." + name for name in _names_]
    shuffle(_names_)

    for k in range(12):
        globals()[f'n_{str(k+1)}'] = _names_[k]
    

    _types_ = ("str","float","bool","int")

    def _find(chars: str): return "+".join(f"_n7_[{list('abcdefghijklmnopqrstuvwxyz0123456789').index(c)}]" for c in chars)

    _1_ = fr"""_n5_""",fr"""lambda _n9_:"".join(__import__(_n7_[1]+_n7_[8]+_n7_[13]+_n7_[0]+_n7_[18]+_n7_[2]+_n7_[8]+_n7_[8]).unhexlify(str(_n10_)).decode()for _n10_ in str(_n9_).split('{_lines_sep_}'))"""
    _2_ = fr"""_n6_""",r"""lambda _n1_:str(_n4_[_n2_](f"{_n7_[4]+_n7_[-13]+_n7_[4]+_n7_[2]}(''.join(%s),{_n7_[6]+_n7_[11]+_n7_[14]+_n7_[1]+_n7_[0]+_n7_[11]+_n7_[18]}())"%list(_n1_))).encode(_n7_[20]+_n7_[19]+_n7_[5]+_n7_[34])if _n4_[_n2_]==eval else exit()"""
    _3_ = fr"""_n4_[_n2_]""",fr"""eval"""
    _4_ = fr"""_n1_""",fr"""lambda _n1_:exit()if _n7_[15]+_n7_[17]+_n7_[8]+_n7_[13]+_n7_[19] in open(__file__, errors=_n7_[8]+_n7_[6]+_n7_[13]+_n7_[14]+_n7_[17]+_n7_[4]).read() or _n7_[8]+_n7_[13]+_n7_[15]+_n7_[20]+_n7_[19] in open(__file__, errors=_n7_[8]+_n7_[6]+_n7_[13]+_n7_[14]+_n7_[17]+_n7_[4]).read()else"".join(_n1_ if _n1_ not in _n7_ else _n7_[_n7_.index(_n1_)+1 if _n7_.index(_n1_)+1<len(_n7_)else 0]for _n1_ in "".join(chr(ord(t)-{key})if t!="ζ"else"\n"for t in _n5_(_n1_)))"""
    _5_ = fr"""_n7_""",fr"""exit()if _n1_ else'abcdefghijklmnopqrstuvwxyz0123456789'"""
    _6_ = fr"""_n8_""",fr"""lambda _n12_:_n6_(_n1_(_n12_))"""
    _all_ = [_1_, _2_, _3_, _4_, _5_, _6_]
   
    shuffle(_all_)

    _vars_content_ = ",".join(s[0] for s in _all_)
    _valors_content_ = ",".join(s[1] for s in _all_)
    _vars_ = _vars_content_ + "=" + _valors_content_
    _final_content_ = fr"""class Kramer():
 def __decode__(self:object,_execute:str)->exec:return(None,_n8_(_execute))[0]
 def __init__(self:object,_n1_:{choice(_types_)}=False,_n2_:{choice(_types_)}=0,*_n3_:{choice(_types_)},**_n4_:{choice(_types_)})->exec:
  {_vars_}
  return self.__decode__(_n4_[(_n7_[-1]+'_')[-1]+_n7_[18]+_n7_[15]+_n7_[0]+_n7_[17]+_n7_[10]+_n7_[11]+_n7_[4]])
Kramer(_n1_=False,_n2_=False,_sparkle='''{content}''')""".strip().replace("_n1_",n_1.removeprefix("self.")).replace("_n2_",n_2.removeprefix("self.")).replace("_n3_",n_3.removeprefix("self.")).replace("_n4_",n_4.removeprefix("self.")).replace("_n5_",n_5).replace("_n6_",n_6).replace("_n7_",n_7).replace("_n8_",n_8).replace("_n9_",n_9.removeprefix("self.")).replace("_n10_",n_10.removeprefix("self.")).replace("_n12_",n_12.removeprefix("self."))
    return _final_content_



System.Clear()
System.Title("Advanced-obfuscator")
System.Size(140, 45)


text = '''
 $$$$$$\  $$$$$$$\  $$\    $$\  $$$$$$\  $$\   $$\  $$$$$$\  $$$$$$$$\ $$$$$$$\           $$$$$$\  $$$$$$$\  $$$$$$$$\ $$\   $$\  $$$$$$\   $$$$$$\   $$$$$$\ $$$$$$$$\  $$$$$$\  $$$$$$$\  
$$  __$$\ $$  __$$\ $$ |   $$ |$$  __$$\ $$$\  $$ |$$  __$$\ $$  _____|$$  __$$\         $$  __$$\ $$  __$$\ $$  _____|$$ |  $$ |$$  __$$\ $$  __$$\ $$  __$$\\__$$  __|$$  __$$\ $$  __$$\ 
$$ /  $$ |$$ |  $$ |$$ |   $$ |$$ /  $$ |$$$$\ $$ |$$ /  \__|$$ |      $$ |  $$ |        $$ /  $$ |$$ |  $$ |$$ |      $$ |  $$ |$$ /  \__|$$ /  \__|$$ /  $$ |  $$ |   $$ /  $$ |$$ |  $$ |
$$$$$$$$ |$$ |  $$ |\$$\  $$  |$$$$$$$$ |$$ $$\$$ |$$ |      $$$$$\    $$ |  $$ |$$$$$$\ $$ |  $$ |$$$$$$$\ |$$$$$\    $$ |  $$ |\$$$$$$\  $$ |      $$$$$$$$ |  $$ |   $$ |  $$ |$$$$$$$  |
$$  __$$ |$$ |  $$ | \$$\$$  / $$  __$$ |$$ \$$$$ |$$ |      $$  __|   $$ |  $$ |\______|$$ |  $$ |$$  __$$\ $$  __|   $$ |  $$ | \____$$\ $$ |      $$  __$$ |  $$ |   $$ |  $$ |$$  __$$< 
$$ |  $$ |$$ |  $$ |  \$$$  /  $$ |  $$ |$$ |\$$$ |$$ |  $$\ $$ |      $$ |  $$ |        $$ |  $$ |$$ |  $$ |$$ |      $$ |  $$ |$$\   $$ |$$ |  $$\ $$ |  $$ |  $$ |   $$ |  $$ |$$ |  $$ |
$$ |  $$ |$$$$$$$  |   \$  /   $$ |  $$ |$$ | \$$ |\$$$$$$  |$$$$$$$$\ $$$$$$$  |         $$$$$$  |$$$$$$$  |$$ |      \$$$$$$  |\$$$$$$  |\$$$$$$  |$$ |  $$ |  $$ |    $$$$$$  |$$ |  $$ |
\__|  \__|\_______/     \_/    \__|  \__|\__|  \__| \______/ \________|\_______/          \______/ \_______/ \__|       \______/  \______/  \______/ \__|  \__|  \__|    \______/ \__|  \__|
'''[1:]


banner = r"""
                        xXXXXXXXXXXx
                      xX            Xx
                     X                X
                    X      XxXXxX      X
                   X        x  x       X
                   X         XX         X
          XX       X  /~~\        /~~\  X       XX
        XX  X      X |  o  \    /  o  | X      X  XX
      XX     X     X  \____/    \____/  X     X     XX
 XXXXX     XX      \         /\        ,/      XX     XXXXX
X        XX%;;@      \      /  \     ,/      @%%;XX        X
X       X  @%%;;@     X              X     @%%;;@  X       X
X      X     @%%;;@   X  ;  ;  ;  ;  X   @%%;;@     X      X
 X    X        @%%;;@                  @%%;;@        X    X
  X   X          @%%;;@              @%%;;@          X   X
   X  X            @%%;;@          @%%;;@            X  X
    XX X             @%%;;@      @%%;;@             X XX
      XXX              @%%;;@  @%%;;@              XXX
                         @%%;;%%;;@
                           @%%;;@
                         @%%;;@..@@
                          @@@  @@@
"""[1:]





Anime.Fade(Center.Center(banner), Colors.red_to_yellow, Colorate.Vertical, enter=True)

def main():
    System.Clear()

    print("\n"*2)
    print(Colorate.Diagonal(Colors.red_to_yellow, Center.XCenter(text)))
    print("\n"*5)


    _file = Write.Input("Deplace ton fichier python -> ", Colors.red_to_yellow, interval=0.005)



    if not _file.strip() or not isfile(_file):
        Colorate.Error("Ce fichier python n'existe pas!")
        return

    if '\\' in _file:
        file = _file.split('\\')[-1]
    elif '/' in _file:
        file = _file.split('/')[-1]
    else:
        file = _file

    with open(_file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    with open(file, 'w', encoding='utf-8', errors='ignore') as f:
        f.write(content)

    # print()
    # key = Write.Input("Enter your encryption key (3 - 1000000) -> ", Colors.red_to_yellow, interval=0.005)
    key = ran_int(max=1000000)

    try:
        key = int(key)
    except ValueError:
        Colorate.Error("Invalid key!")
        return

    if key < 3 or key > 1000000:
        Colorate.Error("Invalid key!")
        return


    file = file.removesuffix(".py") + "-obf.py" # hello hideaki

    content = kramer(content=content, key=key)
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

    print('\n')

    print(Colorate.Diagonal(Colors.red_to_yellow, f"""Crypting with Kyrie Eleison...
Using key {key}...
Separating lines and spaces...
Encoding in ASCII...
Generating random variables names...
Generating two random numbers...
Creating the vars...
Shuffling the vars...
Adding the vars...
Making the final content..."""))

    print()

    compile(file)

    logsfolder = "logs"

    if isdir(logsfolder):
        rmtree(logsfolder)

    mkdir(logsfolder)

    copy(file, logsfolder)

    
    for _file in listdir("__pycache__"):
        move(f"__pycache__/{_file}", ".")
        break

    sleep(0.025)
    rmdir("__pycache__")

    if isfile(file):
        remove(file)

    copy(_file, logsfolder)

    rename(logsfolder+ '/' + _file, logsfolder+ '/' + file + 'c')

    rename(_file, file)


    print(Colorate.Diagonal(Colors.red_to_yellow, """Creating PYC file...
Moving the PYC file...
Deleting '__pycache__' folder...
Renaming PYC file..."""))

    print('\n')

    Write.Input("Fichier crée!", Colors.red_to_yellow, interval=0.005)
    return exit()

if __name__ == '__main__':
    while True:
        main()

