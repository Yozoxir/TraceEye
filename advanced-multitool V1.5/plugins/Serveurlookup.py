import requests
from colorama import Fore
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def setTitle(title):
    print(f"Setting title to: {title}")

def serverlookuptitle():
    print("""
 $$$$$$\  $$$$$$$\  $$\    $$\  $$$$$$\  $$\   $$\  $$$$$$\  $$$$$$$$\ $$$$$$$\         $$$$$$\  $$$$$$$$\ $$$$$$$\  $$\    $$\ $$$$$$$$\ $$$$$$$\        $$$$$$\ $$\   $$\ $$$$$$$$\  $$$$$$\  
$$  __$$\ $$  __$$\ $$ |   $$ |$$  __$$\ $$$\  $$ |$$  __$$\ $$  _____|$$  __$$\       $$  __$$\ $$  _____|$$  __$$\ $$ |   $$ |$$  _____|$$  __$$\       \_$$  _|$$$\  $$ |$$  _____|$$  __$$\ 
$$ /  $$ |$$ |  $$ |$$ |   $$ |$$ /  $$ |$$$$\ $$ |$$ /  \__|$$ |      $$ |  $$ |      $$ /  \__|$$ |      $$ |  $$ |$$ |   $$ |$$ |      $$ |  $$ |        $$ |  $$$$\ $$ |$$ |      $$ /  $$ |
$$$$$$$$ |$$ |  $$ |\$$\  $$  |$$$$$$$$ |$$ $$\$$ |$$ |      $$$$$\    $$ |  $$ |      \$$$$$$\  $$$$$\    $$$$$$$  |\$$\  $$  |$$$$$\    $$$$$$$  |        $$ |  $$ $$\$$ |$$$$$\    $$ |  $$ |
$$  __$$ |$$ |  $$ | \$$\$$  / $$  __$$ |$$ \$$$$ |$$ |      $$  __|   $$ |  $$ |       \____$$\ $$  __|   $$  __$$<  \$$\$$  / $$  __|   $$  __$$<         $$ |  $$ \$$$$ |$$  __|   $$ |  $$ |
$$ |  $$ |$$ |  $$ |  \$$$  /  $$ |  $$ |$$ |\$$$ |$$ |  $$\ $$ |      $$ |  $$ |      $$\   $$ |$$ |      $$ |  $$ |  \$$$  /  $$ |      $$ |  $$ |        $$ |  $$ |\$$$ |$$ |      $$ |  $$ |
$$ |  $$ |$$$$$$$  |   \$  /   $$ |  $$ |$$ | \$$ |\$$$$$$  |$$$$$$$$\ $$$$$$$  |      \$$$$$$  |$$$$$$$$\ $$ |  $$ |   \$  /   $$$$$$$$\ $$ |  $$ |      $$$$$$\ $$ | \$$ |$$ |       $$$$$$  |
\__|  \__|\_______/     \_/    \__|  \__|\__|  \__| \______/ \________|\_______/        \______/ \________|\__|  \__|    \_/    \________|\__|  \__|      \______|\__|  \__|\__|       \______/ 
""")

def main():
    print("Main function")

def serverlookup():
    setTitle("Server Lookup")
    clear()
    serverlookuptitle()
    print(f"""{Fore.LIGHTBLUE_EX}#{Fore.LIGHTYELLOW_EX} Tu peux trouver: \n\n""")
    print(f"""          {Fore.LIGHTYELLOW_EX}>{Fore.LIGHTBLUE_EX} Lien d'invitation       {Fore.LIGHTYELLOW_EX}>{Fore.LIGHTBLUE_EX} nom de l'Inviteur   {Fore.LIGHTYELLOW_EX}>{Fore.LIGHTBLUE_EX} Banniere du serveur        {Fore.LIGHTYELLOW_EX}>{Fore.LIGHTBLUE_EX} Serveur Splash\n""")
    print(f"""          {Fore.LIGHTYELLOW_EX}>{Fore.LIGHTBLUE_EX} Nom du Channel          {Fore.LIGHTYELLOW_EX}>{Fore.LIGHTBLUE_EX} ID de l'inviteur    {Fore.LIGHTYELLOW_EX}>{Fore.LIGHTBLUE_EX} Description du serveur     {Fore.LIGHTYELLOW_EX}>{Fore.LIGHTBLUE_EX} Serveur Features\n""")
    print(f"""          {Fore.LIGHTYELLOW_EX}>{Fore.LIGHTBLUE_EX} ID du Channel           {Fore.LIGHTYELLOW_EX}>{Fore.LIGHTBLUE_EX} Nom du serveur      {Fore.LIGHTYELLOW_EX}>{Fore.LIGHTBLUE_EX} Lien d'invitation personnalisé\n""")
    print(f"""          {Fore.LIGHTYELLOW_EX}>{Fore.LIGHTBLUE_EX} Date d'expiration       {Fore.LIGHTYELLOW_EX}>{Fore.LIGHTBLUE_EX} ID du serveur       {Fore.LIGHTYELLOW_EX}>{Fore.LIGHTBLUE_EX} Niveau de vérification\n\n\n\n""")
    print(f"{Fore.LIGHTBLUE_EX}~{Fore.LIGHTYELLOW_EX} Insérer la derniere parti du lien d'invitation: ")
    invitelink = input(f"{Fore.LIGHTYELLOW_EX}~{Fore.LIGHTBLUE_EX} Lien d'invitation: ")
    clear()
    try:
        if "discord.gg" in invitelink:
            code = invitelink.split('/')[-1]
        else:
            code = invitelink
        res = requests.get(f"https://discord.com/api/v9/invites/{code}")
        if res.status_code == 200:
            res_json = res.json()

            print(f"""\n{Fore.LIGHTBLUE_EX}#{Fore.LIGHTYELLOW_EX} Information de l'invitation:""")
            print(f"""          {Fore.LIGHTYELLOW_EX}>{Fore.LIGHTBLUE_EX} Lien d'invitation: {f'https://discord.gg/{res_json["code"]}'}""")
            print(f"""          {Fore.LIGHTYELLOW_EX}>{Fore.LIGHTBLUE_EX} Channel: {res_json["channel"]["name"]} ({res_json["channel"]["id"]})""")
            print(f"""                    {Fore.LIGHTYELLOW_EX}+{Fore.LIGHTBLUE_EX} Date d'expiration: {res_json["expires_at"]}\n""")

            print(f"""{Fore.LIGHTBLUE_EX}#{Fore.LIGHTYELLOW_EX} Information de l'inviteur:""")
            print(f"""          {Fore.LIGHTYELLOW_EX}>{Fore.LIGHTBLUE_EX} Nom de  l'inviteur: {f'{res_json["inviter"]["username"]}#{res_json["inviter"]["discriminator"]}'}""")
            print(f"""          {Fore.LIGHTYELLOW_EX}>{Fore.LIGHTBLUE_EX} ID de l'inviteur: {res_json["inviter"]["id"]}\n""")

            print(f"""{Fore.LIGHTBLUE_EX}#{Fore.LIGHTYELLOW_EX} Serveur Information:""")
            print(f"""          {Fore.LIGHTYELLOW_EX}>{Fore.LIGHTBLUE_EX} Nom du serveur: {res_json["guild"]["name"]}""")
            print(f"""          {Fore.LIGHTYELLOW_EX}>{Fore.LIGHTBLUE_EX} Serveur ID: {res_json["guild"]["id"]}""")
            print(f"""          {Fore.LIGHTYELLOW_EX}>{Fore.LIGHTBLUE_EX} Banniere: {res_json["guild"]["banner"]}""")
            print(f"""          {Fore.LIGHTYELLOW_EX}>{Fore.LIGHTBLUE_EX} Description: {res_json["guild"]["description"]}""")
            print(f"""          {Fore.LIGHTYELLOW_EX}>{Fore.LIGHTBLUE_EX} lien d'invitation personnalisé: {res_json["guild"]["vanity_url_code"]}""")
            print(f"""          {Fore.LIGHTYELLOW_EX}>{Fore.LIGHTBLUE_EX} Niveau de vérification: {res_json["guild"]["verification_level"]}""")
            print(f"""          {Fore.LIGHTYELLOW_EX}>{Fore.LIGHTBLUE_EX} Splash: {res_json["guild"]["splash"]}""")
            print(f"""          {Fore.LIGHTYELLOW_EX}>{Fore.LIGHTBLUE_EX} Features: {res_json["guild"]["features"]}""")
        else:
            input(f"""          {Fore.LIGHTYELLOW_EX}~{Fore.LIGHTBLUE_EX} Une erreur s'est produite lors de l'envoi de la demande""")
            main()
    except Exception as e:
        print(f"Error: {e}")
        input(f"Press ENTER to exit...")
        main()
    
    main()
    input(f"\nPress ENTER to exit...")

setTitle("Server Lookup")
serverlookup()
