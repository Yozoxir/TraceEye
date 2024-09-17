import requests
import time
import os
import threading
from pystyle import Colors, Colorate, Center

def clear():
    """Nettoyer l'écran."""
    os.system('cls' if os.name == 'nt' else 'clear')

def setTitle(title):
    """Définir le titre de la fenêtre du terminal."""
    print(f"\033]0;{title}\007")

def print_text_slowly(text, delay=0.1):
    """Affiche le texte lentement, ligne par ligne avec effet white_to_black."""
    lines = text.splitlines()
    for line in lines:
        print(Colorate.Horizontal(Colors.white_to_black, line))
        time.sleep(delay)
    print()

def webhspamtitle():
    """Afficher le titre ASCII art du spam."""
    ascii_art = """
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
"""
    print_text_slowly(ascii_art)

def main():
    print_text_slowly("Returning to main menu...")

def webhookspam():
    setTitle("© TraceEye-project discord.gg/traceeye")
    clear()
    webhspamtitle()
    
    print_text_slowly("Enter the WebHook you want to spam")
    webhook_prompt = Colorate.Horizontal(Colors.white_to_black, "WebHook Link -> ")
    webhook = input(webhook_prompt)
    
    try:
        requests.post(webhook, json={'content': ""})
    except:
        print_text_slowly("[!] Your WebHook is invalid!")
        time.sleep(2)
        clear()
        main()
    
    print_text_slowly("\nEnter the message to spam")
    message = input(Colorate.Horizontal(Colors.white_to_black, "Message -> "))
    
    print_text_slowly("\nAmount of messages to send")
    amount = int(input(Colorate.Horizontal(Colors.white_to_black, "Amount -> ")))
    
    def spam():
        try:
            requests.post(webhook, json={'content': message})
        except Exception as e:
            print_text_slowly(f"Error: {e}")

    for x in range(amount):
        threading.Thread(target=spam).start()
        time.sleep(0.1)  
    
    clear()
    webhspamtitle()
    print_text_slowly("[!] Webhook has been correctly spammed")
    input("\nPress ENTER to exit")
    main()

if __name__ == "__main__":
    webhookspam()
