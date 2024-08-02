import requests
import time
from colorama import Fore
import threading

def clear():
    print("\033c", end="")

def setTitle(title):
    print(f"\033]0;{title}\007")

def webhspamtitle():
    print(f"""{Fore.RED}
 __     __     ______     ______     __  __     ______     ______     __  __        ______     ______   ______     __    __    
/\ \  _ \ \   /\  ___\   /\  == \   /\ \_\ \   /\  __ \   /\  __ \   /\ \/ /       /\  ___\   /\  == \ /\  __ \   /\ "-./  \   
\ \ \/ ".\ \  \ \  __\   \ \  __<   \ \  __ \  \ \ \/\ \  \ \ \/\ \  \ \  _"-.     \ \___  \  \ \  _-/ \ \  __ \  \ \ \-./\ \  
 \ \__/".~\_\  \ \_____\  \ \_____\  \ \_\ \_\  \ \_____\  \ \_____\  \ \_\ \_\     \/\_____\  \ \_\    \ \_\ \_\  \ \_\ \ \_\ 
  \/_/   \/_/   \/_____/   \/_____/   \/_/\/_/   \/_____/   \/_____/   \/_/\/_/      \/_____/   \/_/     \/_/\/_/   \/_/  \/_/
{Fore.RESET}""")

def main():
    print("Retour sur la fonction principale...")

def webhookspam():
    setTitle("WebHook Spammer")
    clear()
    webhspamtitle()
    print(f"Entrer le lien du webhook concerner ")
    webhook = input(f"Webhook Link: ")
    try:
        requests.post(webhook, json={'content': ""})
    except:
        print(f"      [!]{Fore.LIGHTRED_EX} Ton webhook est invalide !{Fore.RESET}")
        time.sleep(2)
        clear()
        main()
    print(f"\nEntrer le message a spam ")
    message = input(f"Message: ")
    print(f"\nNombre de méssage a envoyer ")
    amount = int(input(f"Nombre: "))
    
    def spam():
        try:
            requests.post(webhook, json={'content': message})
        except Exception as e:
            print(f"Error: {e}")

    for x in range(amount):
        threading.Thread(target=spam).start()
        time.sleep(0.1)  
    
    clear()
    webhspamtitle()
    print(f"[{Fore.LIGHTGREEN_EX}!{Fore.RESET}] Le webhook a bien envoyé les méssages")
    input(f"\nPress ENTER to exit...")
    main()

webhookspam()
