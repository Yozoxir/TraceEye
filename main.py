import os
import json
import colorama
from pystyle import Colorate, Colors
import subprocess
import webbrowser
import sys

def open_discord_invite():
    invite_url = "https://discord.gg/UKBKWMwR7u"
    webbrowser.open(invite_url)

if __name__ == "__main__":
    open_discord_invite()

def check_requirements():
    utils_folder = './utils'
    config_file = os.path.join(utils_folder, 'config.json')

    if not os.path.isdir(utils_folder):
        raise FileNotFoundError(f"Dossier requis '{utils_folder}' est manquant.")

    if not os.path.isfile(config_file):
        raise FileNotFoundError(f"Fichier de configuration '{config_file}' est manquant.")

    with open(config_file, 'r') as f:
        try:
            config = json.load(f)
            if (config.get('github') != "Github Yozoxir/TraceEye" or
                config.get('discord') != "discord.gg/traceye"):
                raise ValueError("Le fichier de configuration ne contient pas les valeurs attendues.")
        except json.JSONDecodeError:
            raise ValueError("Erreur de décodage du fichier de configuration.")

    print("Configuration valide.")

def main():
    # Affiche l'interface ASCII art
    print(colored_ascii_art)

if __name__ == "__main__":
    try:
        check_requirements()
    except (FileNotFoundError, ValueError) as e:
        print(f"Erreur: {e}")
        exit(1)
    
    # Initialise colorama
    colorama.init()

    # Définit la couleur
    color =  "\033[93m"

    # Définit l'interface ASCII art
    interface = f"""
░▒▓████████▓▒░▒▓███████▓▒░ ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓████████▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░ 
   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
   ░▒▓█▓▒░   ░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒░      ░▒▓██████▓▒░ ░▒▓██████▓▒░  ░▒▓██████▓▒░░▒▓██████▓▒░   
   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░         ░▒▓█▓▒░   ░▒▓█▓▒░        
   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓████████▓▒░▒▓████████▓▒░  ░▒▓█▓▒░   ░▒▓████████▓▒░

                                ┏━━━━━━━━━━━━━━━━━━━━━┓
                                ┃Github :  Yozoxir    ┃
                                ┃Discord: .gg/TraceEye┃
                                ┗━━━━━━━━━━━━━━━━━━━━━┛

┏━━━━    Discord Tools    ━━━━┓   ┏━━━━    Osint Tools    ━━━━┓
┃   (01) Token   Information  ┃   ┃   (11)                    ┃
┃   (02) Token   Checker      ┃   ┃   (12)                    ┃
    (03) Token   Dmall                (13)
    (04) Token   Raid                 (14)  
    (05) Token   Name                 (15)
    (06) Token   Hypesquad            (16)
    (07) Token   Bio                  (17)                     
    (08) Webhook Info                 (18)                    
┃   (09) Webhook Spammer      ┃   ┃   (19)                    ┃
┃   (10) Tool info            ┃   ┃   (20)                    ┃
┗━━━━                     ━━━━┛   ┗━━━━                   ━━━━┛
"""

    colored_ascii_art = Colorate.Horizontal(Colors.white_to_black, interface)
    main()

while True:
    os.system('cls')  # Utiliser 'clear' pour Linux/Mac
    print(colored_ascii_art)
    
    gg = input("""
┌──(user@advanced)-[~/Home]
│                      
└─$> """)
    
    if gg.isdigit():
        gg = int(gg)
    
        if gg == 1:
            subprocess.run(['python', 'plugins\\Discord\\Tokeninfo.py'])
        elif gg == 2:
            subprocess.run(['python', 'plugins\\Discord\\Tokenchecker.py'])
        elif gg == 3:
            subprocess.run(['python', 'plugins\\Discord\\Tokendmall.py'])
        elif gg == 4:
            subprocess.run(['python', 'plugins\\Discord\\Tokenraid.py'])
        elif gg == 5:
            subprocess.run(['python', 'plugins\\Discord\\Tokenname.py'])
        elif gg == 6:
            subprocess.run(['python', 'plugins\\Discord\\Tokenhypesquad.py'])
        elif gg == 7:
            subprocess.run(['python', 'plugins\\Discord\\Tokenbio.py'])
        elif gg == 8:
            subprocess.run(['python', 'plugins\\Discord\\Webhookinfo.py'])
        elif gg == 9:
            subprocess.run(['python', 'plugins\\Discord\\Webhookspammer.py'])
        elif gg == 10:
            subprocess.run(['python', 'plugins\\Discord\\info.py'])
        else:
            print("\033[39mVeuillez entrer un numéro valide.")
            input("\033[0;38mAppuyez sur Entrée pour continuer...")
