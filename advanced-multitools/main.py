#advanced-tools
import os
import subprocess
import colorama
from pystyle import Colorate, Colors
# Définir cls en fonction du système d'exploitation
if os.name == 'nt':
    cls = 'cls'
else:
    cls = 'clear'

colorama.init()

color =  "\033[0;34m"

interface = f"""           /$$$$$$  /$$$$$$$  /$$    /$$  /$$$$$$  /$$   /$$  /$$$$$$  /$$$$$$$$ /$$$$$$$ 
          /$$__  $$| $$__  $$| $$   | $$ /$$__  $$| $$$ | $$ /$$__  $$| $$_____/| $$__  $$
         | $$  \\ $$| $$  \\ $$| $$   | $$| $$  \\ $$| $$$$| $$| $$  \\__/| $$      | $$  \\ $$
         | $$$$$$$$| $$  | $$|  $$ / $$/| $$$$$$$$| $$ $$ $$| $$      | $$$$$   | $$  | $$
         | $$__  $$| $$  | $$ \\  $$ $$/ | $$__  $$| $$  $$$$| $$      | $$__/   | $$  | $$
         | $$  | $$| $$  | $$  \\  $$$/  | $$  | $$| $$\\  $$$| $$    $$| $$      | $$  | $$
         | $$  | $$| $$$$$$$/   \\  $/   | $$  | $$| $$ \\  $$|  $$$$$$/| $$$$$$$$| $$$$$$$/
         |__/  |__/|_______/     \\_/    |__/  |__/|__/  \\__/ \\______/ |________/|_______/  

         [ 1  > Server Lookup     ]       [ 2  > Token Mass DM    ]       [ 3 > Token Raid       ]
         [ 4  > Token Info        ]       [ 5  > Account disabler ]       [ 6 > Anti-grabber     ]
         [ 7  > IP Lookup         ]       [ 8  > Phone lookup     ]       [ 9 > Webhook Info     ]
         [ 10 > Webhook Spammer   ]       [ 11 > Group Spammer    ]

"""
choice = f"{color}Enter your choice >>> \033[39m"

colored_ascii_art = Colorate.Horizontal(Colors.blue_to_red, interface)


def options():
    # other code
    commandes = [str(i) for i in range(1, 20)]
    # more code
    
while True:
    os.system(cls)
    gg = input(colored_ascii_art + "\n\n" + choice)
    if gg =='1':
        subprocess.run(['python', 'plugins\\Serveurlookup.py'])

    if gg =='2':
        subprocess.run(['python', 'plugins\\massdm.py'])
        
    if gg =='3':
        subprocess.run(['python', 'plugins\\Tokenraid.py'])
    
    if gg =='4':
        subprocess.run(['python', 'plugins\\Tokeninfo.py'])

    if gg =='5':
        subprocess.run(['python', 'plugins\\Account-disabler.py'])
    
    if gg =='6':
        subprocess.run(['python', 'plugins\\Anti-grabber.py'])

    if gg =='7':
        subprocess.run(['python', 'plugins\\pinger.py'])

    if gg =='8':
        subprocess.run(['python', 'plugins\\lookup.py'])

    if gg =='9':
        subprocess.run(['python', 'plugins\\Webhook-info.py'])

    if gg =='10':
        subprocess.run(['python', 'plugins\\Webhook-spammer.py'])

    if gg =='11':
        subprocess.run(['python', 'plugins\\Group-spammer.py'])