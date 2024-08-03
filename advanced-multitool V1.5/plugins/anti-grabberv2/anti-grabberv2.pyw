# -*- coding: utf-8 -*-

# Par yozoxir

# https://github.com/Yozoxir/Advanced-multitools


# REQUIREMENTS

from os import name, getenv, startfile, remove
from os.path import exists
from webbrowser import open as wbopen




username = getenv("username")

startup_path = "C:/Users/%s/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/" % username
downloads_path = "C:/Users/%s/Downloads/" % username





# GUI SETUP


import tkinter as tk
import tkinter.ttk as ttk





"""
       |
       |
-------|------- width - x
       |
       |
   height - y

"""



width = x = 380
height = y = 240

gui = tk.Tk()
gui.title("Anti-grabberv2")
gui.geometry("{}x{}".format(width, height))
gui.resizable(width=False, height=False)
gui.config(background='#000000')


style = ttk.Style(gui)

style.theme_use("default")





def center(arg1:int, arg2:int):
    return (arg2 - arg1) / 2

def xcenter(x:int, width:int=width):
    return center(x, arg2=width)

def ycenter(y:int, height:int=height):
    return center(y, arg2=height)



start_bool = tk.BooleanVar()

def start_func():
    if start_bool.get():
        start_bool.set(False)
        start_button.configure(fg="black", bg="white")
    else:
        start_bool.set(True)
        start_button.configure(fg="white", bg="blue")



author_label = ttk.Label(gui, text = "by yozoxir", foreground="white", background="black")
author_label.place(x=xcenter(100), y=20, width=100, height=20)

start_button = tk.Button(gui, text = "Exécuter après l'installation", command = start_func)
start_button.place(x=xcenter(170), y=65, width = 170, height=20)


def boom(sup:bool=False):


    if uninstall_button.winfo_ismapped():
        uninstall_button.place_forget()

    start = start_bool.get()
    webhook = webhook_entry.get()

    start_button.place_forget()
    install_button.place_forget()
    webhook_button.place_forget()
    webhook_entry.place_forget()



    if name != 'nt':
        tk.Label(gui, text="Erreur. Aftermath fonctionne uniquement sur Windows.", fg="white", bg="black").place(x=xcenter(300), y=100, width=300, height=20)

    elif not exists(startup_path):
        tk.Label(gui, text="Erreur. Le chemin d'accés du démarrage n'est pas valide.",
                 fg="white", bg="black").place(x=xcenter(320), y=100, width=320, height=20)

    elif not exists(downloads_path):
        tk.Label(gui, text="Erreur. Le chemin d'accés des téléchargements n'est pas valide.",
                 fg="white", bg="black").place(x=xcenter(340), y=100, width=340, height=20)

    else:

        place_credits()
        if not sup:
            build(start=start, webhook=webhook)
            ttk.Label(gui, text="Aftermath à été installé avec succés!", foreground="white", background="black").place(x=xcenter(200), y=150, width=200, height=20)
        else:
            remove(startup_path + "aftermath.pyw")
            ttk.Label(gui, text="Aftermath à été désinstallé avec succés!", foreground="white", background="black").place(x=xcenter(220), y=150, width=220, height=20)
    tk.Button(gui, text="Quitter", command=exit, fg="white", bg="black").place(x=xcenter(100), y=60, width=100, height=30)


def sup():
    return boom(True)

def open_credits():
    wbopen("https://github.com/Yozoxir/Advanced-multitools")

def place_credits():
    tk.Button(gui, text="Github", command=open_credits, fg="white", bg="black").place(x=xcenter(100), y=190, width=100, height=30)


uninstall_button = tk.Button(gui, text="Désinstaller", command=sup, bg="black", fg="white")
install_button = tk.Button(gui, text="Installer",command=boom, bg="black", fg="white")

if exists(startup_path + "aftermath.pyw"):

    install_button.place(x=70, y=180, width = 120, height=40)
    uninstall_button.place(x=190, y=180, width=120, height=40)
else:
    install_button = tk.Button(gui, text="Installer", command=boom, bg="black", fg="white")
    install_button.place(x=xcenter(120), y=180, width=120, height=40)

webhook_bool = False

def webhook_choose():
    global webhook_bool
    if webhook_bool:
        webhook_bool = False
        webhook_button.configure(fg="black", bg="white")
        webhook_entry.place_forget()
        webhook_entry.delete(0, len(webhook_entry.get()))
    else:
        webhook_bool = True
        webhook_button.configure(fg="white", bg="blue")
        webhook_entry.place(x=xcenter(180), y=130, width=180, height=25)

webhook_button = tk.Button(gui, text = "Choisir un Webhook pour les logs", fg="black", bg="white", command=webhook_choose)
webhook_button.place(x=xcenter(200), y=90, width = 200, height=22)


webhook_variable = tk.StringVar()
webhook_entry = ttk.Entry(gui, textvariable=webhook_variable)






def build(start:bool, webhook:str):

    if webhook == "":
        webhook = "https://test.com"

    content = r"""# -*- coding: utf-8 -*-

# by yozoxir

# https://github.com/Yozoxir/Advanced-multitools

# Eclipse Public License 2.0

# <3


from os import getenv, listdir, mkdir
from os.path import exists, isdir
from re import findall
from requests import get, post, delete





username = getenv("username")

downloads_path = "C:/Users/%s/Downloads/" % username 



pattern = "[http|https]+://[canary.discord.com|discord.com|discordapp.com]+/api/webhooks/[\w\S/]+"


webhook = '""" + webhook + r"""'
already_checked = []


valid = ['py', 'pyw', 'js']
maxilen = 10000000


def isvalid(file:str):
    return any(file.endswith(char) for char in valid)

def rlistdir(path:str):
    return [path+file for file in listdir(path) if path+file not in already_checked and isvalid(file)]


def websearch(content:str, filename:str):

    found = 0
    for webhook in findall(pattern, content):
        webhook = webhook.replace("'", "").replace('"', '')
        if (
            "token" in content
            and "discord" in webhook 
            and "api/webhooks" in webhook
            and get(webhook).status_code == 200
        ):
            found += 1
            send("Webhook **{}** trouvé!".format(webhook))
            fuck(webhook)
            send("Webhook supprimé :)")


    
    return found
        



def fuck(webhook:str):
    send("Petit coucou de la part de https://github.com/Yozoxir/Advanced-multitools :)", webhook)
    delete(webhook).status_code

def send(content:str, webhook:str=webhook):
    return post(webhook, json={"content":content, "username":"Aftermath", "avatar_url":"https://repository-images.githubusercontent.com/399563822/47933843-fd9b-4490-94ae-cf102d653de0"})




def check(file:str):
    try:
        with open(file, 'r', encoding="cp850") as f:
            content = f.read()
            if len(content) <= maxilen:
                found = websearch(content, file)

    except OSError:
        pass
    already_checked.append(file)


def run():
    rlist = rlistdir(downloads_path)
    print(len(rlist))
    for file in rlist:
        print(f"{rlist.index(file)+1}/{len(rlist)} : {file}")
        check(file)



def main():
    send("Aftermath à été démarré avec succés!", webhook)
    while True:
        run()

if __name__ == '__main__':
    main()

"""

    with open(startup_path + "aftermath.pyw", 'w', encoding='utf-8') as f:
        f.write(content)
    if start:
        startfile(startup_path+"aftermath.pyw")


gui.mainloop()
