#advanced-tools
#Merci de garder ce code simplement pour vous et de ne pas le vendre ou le partager sans le github 
#Nous ne somme en aucun cas responsable de vos probleme
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

color =  "\033[93m"

interface = f"""            /$$$$$$  /$$$$$$$  /$$    /$$  /$$$$$$  /$$   /$$  /$$$$$$  /$$$$$$$$ /$$$$$$$ 
           /$$__  $$| $$__  $$| $$   | $$ /$$__  $$| $$$ | $$ /$$__  $$| $$_____/| $$__  $$
    ▒    ▒| $$  \\ $$| $$  \\ $$| $$   | $$| $$  \\ $$| $$$$| $$| $$  \\__/| $$      | $$  \\ $$   ▒
      ▒ ▒ | $$$$$$$$| $$  | $$|  $$ / $$/| $$$$$$$$| $$ $$ $$| $$      | $$$$$   | $$  | $$     ▒
          | $$__  $$| $$  | $$ \\  $$ $$/ | $$__  $$| $$  $$$$| $$      | $$__/   | $$  | $$    ▒
    ▒   ▒ | $$  | $$| $$  | $$  \\  $$$/  | $$  | $$| $$\\  $$$| $$    $$| $$      | $$  | $$  ▒
      ▒   | $$  | $$| $$$$$$$/   \\  $/   | $$  | $$| $$ \\  $$|  $$$$$$/| $$$$$$$$| $$$$$$$/ ▒
       ▒  |__/  |__/|_______/     \\_/    |__/  |__/|__/  \\__/ \\______/ |________/|_______/  
       
       ╔═════════════════════════════════════════════════════════════════════════════════════════╗                                                                           
       ║ 1  > Server Lookup      ]       [ 2  > Token Mass DM      ]       [ 3  > Token Raid     ║
       ║ 4  > Token Info         ]       [ 5  > Account disabler   ]       [ 6  > Anti-grabber   ║ 
       ║ 7  > IP Lookup          ]       [ 8  > Phone lookup       ]       [ 9  > Webhook Info   ║
       ║ 10 > Webhook Spammer    ]       [ 11 > Group Spammer      ]       [ 12 > Roblox id      ║ 
       ║ 13 > Nitro generateur   ]       [ 14 > token clear dm     ]       [ 15 > site- scanner  ║
       ║ 16 > Token grabber      ]       [ 17 > Advanced-obf       ]       [ 18 > Anti-grabv2    ║
       ║ 19 > Compréssé un .py   ]       [ 20 > Obfuscatorv2       ]       [ 21 > Image to ascii ║
       ║ 22 > RAT(virus)         ]       [ 23 > Text to image      ]       [ 24 > Youtube dl     ║
       ║ 25 > exe to py          ]       [ 26 > Protect you script ]       [ 27 >                ║
       ╚═════════════════════════════════════════════════════════════════════════════════════════╝

       
         ┌──(user@advanced)-[~/Home]
         │                      
         └─$> 
"""

colored_ascii_art = Colorate.Horizontal(Colors.red_to_yellow, interface)


def options():
    # other code
    commandes = [str(i) for i in range(1, 20)]
    # more code
    
while True:
    os.system(cls)
    gg = input(colored_ascii_art)
    if gg.isdigit():
        gg = int(gg)
    

    if gg == 1:
        subprocess.run(['python', 'plugins\\Serveurlookup.py'])
    elif gg == 2:
        subprocess.run(['python', 'plugins\\massdm.py']) 
    elif gg == 3:
        subprocess.run(['python', 'plugins\\Tokenraid.py'])
    elif gg == 4:
        subprocess.run(['python', 'plugins\\Tokeninfo.py'])
    elif gg == 5:
        subprocess.run(['python', 'plugins\\Account-disabler.py'])
    elif gg == 6:
        subprocess.run(['python', 'plugins\\Anti-grabber.py'])
    elif gg == 7:
        subprocess.run(['python', 'plugins\\pinger.py'])
    elif gg == 8:
        subprocess.run(['python', 'plugins\\lookup.py'])
    elif gg == 9:
        subprocess.run(['python', 'plugins\\Webhook-info.py'])
    elif gg == 10:
        subprocess.run(['python', 'plugins\\Webhook-spammer.py'])
    elif gg == 11:
        subprocess.run(['python', 'plugins\\Group-spammer.py'])
    elif gg == 12:
        subprocess.run(['python', 'plugins\\robloxidinfo.py'])
    elif gg == 13:
        subprocess.run(['python', 'plugins\\nitro-gen.py'])
    elif gg == 14:
        subprocess.run(['python', 'plugins\\token-clear-dm.py'])
    elif gg == 15:
        subprocess.run(['python', 'plugins\\site-scanner.py'])
    elif gg == 16:
        subprocess.run(['python', 'plugins\\token-grabber\\builder.py'])
    elif gg == 17:
        subprocess.run(['python', 'plugins\\obfuscator\\adv-obf.py'])
    elif gg == 18:
        subprocess.run(['python', 'plugins\\anti-grabberv2\\anti-grabberv2.pyw'])
    elif gg == 19:
        subprocess.run(['python', 'plugins\\adv-para\\advanced-para.py'])
    elif gg == 20:
        subprocess.run(['python', 'plugins\\Advanced-obfuscatorV2\\Advanced-obfv2.py'])
    elif gg == 21:
        subprocess.run(['python', 'plugins\\Pandore\\pandore.py'])
    elif gg == 22:
        subprocess.run(['python', 'plugins\\Advanced-rat\\advanced-rat.py'])
    elif gg == 23:
        subprocess.run(['python', 'plugins\\advanced-ia\\Advanced-ia.py'])
    elif gg == 24:
        subprocess.run(['python', 'plugins\\advanced-youtube\\advanced-youtube.py'])
    elif gg == 25:
        subprocess.run(['python', 'plugins\\exe-back-to-py\\exe-back-to-.py'])
    elif gg == 26:
        subprocess.run(['python', 'plugins\\Protect-script\\advanced-protect.py'])
    else:
        print("\033[39mMerci de choisir un nombre entre 1 et 27.")
        input("\033[0;38mAppuyez sur Entrée pour continuer...")