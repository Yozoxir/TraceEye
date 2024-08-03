from PIL import Image, ImageEnhance
from requests import get
from os import listdir, remove, mkdir, system
from os.path import isdir, isfile, join
from shutil import copy
from random import shuffle, randint
import os

# Define colors for printing (manual simulation)
class Colors:
    purple_to_red = '\033[35m'
    purple_to_blue = '\033[34m'
    blue_to_purple = '\033[35m'
    reset = '\033[0m'

def color_print(text, color):
    print(f"{color}{text}{Colors.reset}")

# ASCII Art and Banner
ascii_art = r"""
 $$$$$$\  $$$$$$$\  $$\    $$\  $$$$$$\  $$\   $$\  $$$$$$\  $$$$$$$$\ $$$$$$$\        $$$$$$\  $$$$$$\  
$$  __$$\ $$  __$$\ $$ |   $$ |$$  __$$\ $$$\  $$ |$$  __$$\ $$  _____|$$  __$$\       \_$$  _|$$  __$$\ 
$$ /  $$ |$$ |  $$ |$$ |   $$ |$$ /  $$ |$$$$\ $$ |$$ /  \__|$$ |      $$ |  $$ |        $$ |  $$ /  $$ |
$$$$$$$$ |$$ |  $$ |\$$\  $$  |$$$$$$$$ |$$ $$\$$ |$$ |      $$$$$\    $$ |  $$ |$$$$$$\ $$ |  $$$$$$$$ |
$$  __$$ |$$ |  $$ | \$$\$$  / $$  __$$ |$$ \$$$$ |$$ |      $$  __|   $$ |  $$ |\______|$$ |  $$  __$$ |
$$ |  $$ |$$ |  $$ |  \$$$  /  $$ |  $$ |$$ |\$$$ |$$ |  $$\ $$ |      $$ |  $$ |        $$ |  $$ |  $$ |
$$ |  $$ |$$$$$$$  |   \$  /   $$ |  $$ |$$ | \$$ |\$$$$$$  |$$$$$$$$\ $$$$$$$  |      $$$$$$\ $$ |  $$ |
\__|  \__|\_______/     \_/    \__|  \__|\__|  \__| \______/ \________|\_______/       \______|\__|  \__|
"""[1:]

banner = r'''
  ██                                                    
░░████░░                                                
▒▒  ▒▒████                                            ▒▒
  ██    ██████▒▒                                      ██
    ██████░░▒▒████████▓▓░░                          ▓▓▒▒
  ██  ▒▒████████████████████                ▒▒▓▓░░████▒▒
  ░░████  ██████████████████              ██████████████
      ████████████████████████          ██████████████  
    ▒▒░░  ████████████████████        ██████████████▒▒  
      ████████████████████████░░    ▒▒██████████████    
              ██████████████████    ██████████████      
              ░░██████████████████████████              
                ░░████████████████████████              
                  ██████████████████████████            
                    ▒▒████████████████████████          
                        ██████████████████████░░        
                          ████████████    ██▓▓▒▒        
                        ▒▒██████████        ████        
                        ██████████          ░░▒▒        
                    ▒▒████████    ▒▒                    
                    ██████████  ▓▓░░██░░▒▒              
                      ████████  ▒▒▒▒                    
                      ▒▒████▒▒                          
                      ░░██▓▓                            
                        ██'''[1:]

# Placeholder function to simulate image search
def search_images(query, num_results):
    # Replace with actual image search logic or API call
    return [
        "https://example.com/image1.jpg",
        "https://example.com/image2.jpg",
        "https://example.com/image3.jpg",
        "https://example.com/image4.jpg",
        "https://example.com/image5.jpg"
    ]

# Raven Class Definition
class Raven:

    def __init__(self, text: str) -> None:
        self.createdir()
        self.dir = 'Advanced-ia/' + text

        while isdir(self.dir):
            self.dir += str(randint(0, 9))

        mkdir(self.dir)
        color_print(f"Creating directory to store the files '{self.dir}'...", Colors.purple_to_blue)

        color_print("Searching for images...", Colors.purple_to_blue)
        links = self.search(text=text)

        color_print("Downloading the images...", Colors.purple_to_blue)
        self.files = self.download(links=links)

        color_print("Blending every image...", Colors.purple_to_blue)
        blended = self.blendall()

        if blended is None:
            color_print("No images were blended successfully.", Colors.purple_to_red)
            return

        color_print("Deleting the unnecessary images...", Colors.purple_to_blue)
        self.clean()

        color_print("Displaying the final image...", Colors.purple_to_blue)
        blended.show()
        return None

    def createdir(self) -> None:
        if not isdir('advanced-ia'):
            mkdir('advanced-ia')

    def clean(self) -> None:
        for file in self.files:
            if isfile(file):
                remove(file)
        return None

    def search(self, text: str) -> list:
        l = search_images(query=text, num_results=100)
        shuffle(l)
        if len(l) >= 5:
            l = l[:5]
        return l
    
    def download(self, links: list) -> list:
        downloaded_files = []
        for link in links:
            try:
                response = get(link)
                if response.status_code == 200:
                    c = response.content
                    name = links.index(link)
                    if name == 0:
                        name = 'font'
                    file_path = f"{self.dir}/{name}.jpg"
                    with open(file_path, 'wb') as f:
                        f.write(c)
                    downloaded_files.append(file_path)
                else:
                    color_print(f"Failed to download image from {link}. Status code: {response.status_code}", Colors.purple_to_red)
            except Exception as e:
                color_print(f"Error downloading image from {link}: {e}", Colors.purple_to_red)
        return downloaded_files

    def blendall(self) -> object:
        x = None
        for file in self.files:
            try:
                if isfile(file):
                    x = self.blend(img=file)
            except Exception as e:
                color_print(f"Error blending image {file}: {e}", Colors.purple_to_red)
        return x

    def blend(self, img:str) -> object:
        try:
            img1 = Image.open(join(self.dir, 'font.jpg'))
            img2 = Image.open(img)

            img1 = self.size(img1)
            img2 = self.size(img2)

            img1 = img1.convert("RGBA")
            img2 = img2.convert("RGBA")

            img = Image.blend(img1, img2, alpha=0.3)
            img = img.convert('RGB')

            bright = ImageEnhance.Brightness(img)
            contrast = ImageEnhance.Contrast(img)
            sharp = ImageEnhance.Sharpness(img)
            color = ImageEnhance.Color(img)

            img = bright.enhance(0.4)
            img = contrast.enhance(1.8)
            img = sharp.enhance(1.5)
            img = color.enhance(1.3)

            self.save(img)

            return img
        except Exception as e:
            color_print(f"Error processing image {img}: {e}", Colors.purple_to_red)
            return None

    def save(self, img: object) -> None:
        img.save(join(self.dir, 'font.jpg'))

    def size(self, img: object, maxw: int = 800, maxh: int = 500) -> object:
        return img.resize((int(maxw / img.size[0] * img.size[0]), int(maxh / img.size[1] * img.size[1])))

# Initialization Function
def init():
    system("cls" if os.name == "nt" else "clear")  # Clear the screen
    print("\033]0;Raven\007")  # Set terminal title
    color_print("Initializing...", Colors.purple_to_blue)

# Main Function
def main():
    print("\n"*2)
    print(color_print(ascii_art, Colors.purple_to_blue))
    print("\n"*5)

    text = input(f"{Colors.purple_to_blue}Imagine something... -> {Colors.reset}").strip()
    if not text:
        color_print("Please enter something to imagine...", Colors.purple_to_red)
        return

    color_print("Starting generation...", Colors.blue_to_purple)
    print()

    try:
        Raven(text=text)
    except Exception as e:
        print('\n')
        color_print(f"Oops! An error occurred: [{e}]", Colors.purple_to_red)
        return

    print('\n')
    input(f"{Colors.purple_to_blue}Here you go!{Colors.reset}")

# Entry Point
if __name__ == '__main__':
    init()
    while True:
        main()
