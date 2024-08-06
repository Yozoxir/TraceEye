from colorama import Fore, Back, Style, init
from termcolor import colored
from requests import get
from os import system, mkdir, name
from os.path import isdir
from base64 import b64decode as bd

init(autoreset=True)  # Initialize Colorama

def clear():
    system("cls" if name == 'nt' else "clear")

clear()

if name == 'nt':
    system("title Pantheon")
    system("mode 160, 50")

pantheon = """
 $$$$$$\  $$$$$$$\  $$\    $$\  $$$$$$\  $$\   $$\  $$$$$$\  $$$$$$$$\ $$$$$$$\       $$\     $$\                     $$\               $$\                 
$$  __$$\ $$  __$$\ $$ |   $$ |$$  __$$\ $$$\  $$ |$$  __$$\ $$  _____|$$  __$$\      \$$\   $$  |                    $$ |              $$ |                
$$ /  $$ |$$ |  $$ |$$ |   $$ |$$ /  $$ |$$$$\ $$ |$$ /  \__|$$ |      $$ |  $$ |      \$$\ $$  /$$$$$$\  $$\   $$\ $$$$$$\   $$\   $$\ $$$$$$$\   $$$$$$\  
$$$$$$$$ |$$ |  $$ |\$$\  $$  |$$$$$$$$ |$$ $$\$$ |$$ |      $$$$$\    $$ |  $$ |$$$$$$\\$$$$  /$$  __$$\ $$ |  $$ |\_$$  _|  $$ |  $$ |$$  __$$\ $$  __$$\ 
$$  __$$ |$$ |  $$ | \$$\$$  / $$  __$$ |$$ \$$$$ |$$ |      $$  __|   $$ |  $$ |\______|\$$  / $$ /  $$ |$$ |  $$ |  $$ |    $$ |  $$ |$$ |  $$ |$$$$$$$$ |
$$ |  $$ |$$ |  $$ |  \$$$  /  $$ |  $$ |$$ |\$$$ |$$ |  $$\ $$ |      $$ |  $$ |         $$ |  $$ |  $$ |$$ |  $$ |  $$ |$$\ $$ |  $$ |$$ |  $$ |$$   ____|
$$ |  $$ |$$$$$$$  |   \$  /   $$ |  $$ |$$ | \$$ |\$$$$$$  |$$$$$$$$\ $$$$$$$  |         $$ |  \$$$$$$  |\$$$$$$  |  \$$$$  |\$$$$$$  |$$$$$$$  |\$$$$$$$\ 
\__|  \__|\_______/     \_/    \__|  \__|\__|  \__| \______/ \________|\_______/          \__|   \______/  \______/    \____/  \______/ \_______/  \_______|
"""

author = "   - - - {Yozoxir} - - -".format(bd("YmlsbHl0aGVnb2F0MzU2").decode('utf-8'))

# Simulate color transitions with a simple approach
print(Fore.RED + pantheon)
print(Fore.YELLOW + author)

print()

print(Fore.YELLOW + "Le meilleur et le plus rapide youtube dowloander." + Style.RESET_ALL)

print("\n\n")

video_url = input(Fore.YELLOW + "Video url > " + Style.RESET_ALL)
video_id = video_url.split("watch?v=")[-1]
video_id = video_id.split("&")[0]

print()

def get_title(id) -> str:
    verify_url = "https://www.youtube.com/oembed?format=json&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D" + id
    response = get(verify_url)
    if response.status_code == 400:
        return False
    json = response.json()
    return json["title"]

video_title = get_title(video_id)

if not video_title:
    input(Fore.RED + "URL invalide!" + Style.RESET_ALL)
    exit()
else:
    print(Fore.YELLOW + "Titre de la vidéo: " + Style.RESET_ALL + video_title)

print()

mode = input(Fore.YELLOW + "1: MP3 - 2: MP4 > " + Style.RESET_ALL)

print()

if mode == '1':
    download_url = "https://www.yt-download.org/api/button/mp3/"
elif mode == '2':
    download_url = "https://www.yt-download.org/api/button/videos/"
else:
    input(Fore.RED + "Mode invalide!" + Style.RESET_ALL)
    exit()

download_url += video_id

print(Fore.YELLOW + "Entrain de chercher le lien pour le telechargement...\n" + Style.RESET_ALL)

response = get(download_url).text
response = response.split('"')
textures = list(reversed([link for link in response if video_id in link]))

if mode == '1':
    quality = input(Fore.YELLOW + "1: 128kbps - 2: 192kbps - 3: 256kbps - 4: 320kbps > " + Style.RESET_ALL)
elif mode == '2':
    if len(textures) == 1:
        quality = input(Fore.YELLOW + "1: 360p > " + Style.RESET_ALL)
    else:
        quality = input(Fore.YELLOW + "1: 360p - 2: 720p > " + Style.RESET_ALL)

print()

try:
    quality = int(quality)
except ValueError:
    input(Fore.RED + "Veuillez saisir un nombre entier!" + Style.RESET_ALL)
    exit()

if quality > len(textures):
    input(Fore.RED + "Choix invalide!" + Style.RESET_ALL)
    exit()

download_url = textures[quality-1]

print(Fore.YELLOW + "Telechargement en cours...\n\n" + Style.RESET_ALL)

content = get(download_url).content

if not isdir("Downloads"):
    mkdir("Downloads")

if mode == '1':
    file = ".mp3"
elif mode == '2':
    file = ".mp4"

for char in ('\\', '/', ':', '*', '?', '"', '<', '>', '|'):
    video_title = video_title.replace(char, '')

path = "Downloads/" + video_title + file

with open(path, 'wb') as f:
    f.write(content)

input(Fore.GREEN + "Telechargé!" + Style.RESET_ALL)
