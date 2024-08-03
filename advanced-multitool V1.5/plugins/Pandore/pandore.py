#Developpé par yozoxir
#https://github.com/Yozoxir/Advanced-multitools

from os import name, chdir
from os.path import isfile
from PIL import Image
from pystyle import Anime, Colorate, Colors, Center, System, Write




class build:
  def __init__(self, imagepath: str, scale: int) -> None:
    self.path = imagepath
    self.scale = scale

    return self.run()

  def run(self) -> None:
    img = self.mkimage(path=self.path)
    pixels = self.mkpixels(img=img)
    ascii = self.mkascii(pixels=pixels)

    with open(self.npath, mode="w", encoding='utf-8') as f:
      f.write(ascii)
    
    return None

  def mkimage(self, path: str) -> object:
    img = Image.open(path)
    width, height = img.size

    self.nwidth = round(width / self.scale)

    img = img.resize((self.nwidth, round(height / (self.scale * 2))))

    return img.convert('L')

  def mkpixels(self, img: object) -> str:
    pixels = img.getdata()

    pixels = [self.chars[pixel//25] for pixel in pixels]
    return ''.join(pixels).replace('.',' ')

  def mkascii(self, pixels: str) -> str:
    ascii = [pixels[index:index + self.nwidth] for index in range(0, len(pixels), self.nwidth)]
    nascii = []
    for line in ascii:
      if line.strip():
        nascii.append(line)
    return "\n".join(nascii)

  @property
  def npath(self) -> str:
    return ".".join(self.path.split(".")[:-1]) + ".txt"

  @property
  def chars(self) -> str:
    return ["§","/","#","&","@","$","%","*","!",":","."]



ascii = """
 $$$$$$\  $$$$$$$\  $$\    $$\  $$$$$$\  $$\   $$\  $$$$$$\  $$$$$$$$\ $$$$$$$\          $$$$$$$\   $$$$$$\  $$\   $$\ $$$$$$$\   $$$$$$\  $$$$$$$\  $$$$$$$$\ 
$$  __$$\ $$  __$$\ $$ |   $$ |$$  __$$\ $$$\  $$ |$$  __$$\ $$  _____|$$  __$$\         $$  __$$\ $$  __$$\ $$$\  $$ |$$  __$$\ $$  __$$\ $$  __$$\ $$  _____|
$$ /  $$ |$$ |  $$ |$$ |   $$ |$$ /  $$ |$$$$\ $$ |$$ /  \__|$$ |      $$ |  $$ |        $$ |  $$ |$$ /  $$ |$$$$\ $$ |$$ |  $$ |$$ /  $$ |$$ |  $$ |$$ |      
$$$$$$$$ |$$ |  $$ |\$$\  $$  |$$$$$$$$ |$$ $$\$$ |$$ |      $$$$$\    $$ |  $$ |$$$$$$\ $$$$$$$  |$$$$$$$$ |$$ $$\$$ |$$ |  $$ |$$ |  $$ |$$$$$$$  |$$$$$\    
$$  __$$ |$$ |  $$ | \$$\$$  / $$  __$$ |$$ \$$$$ |$$ |      $$  __|   $$ |  $$ |\______|$$  ____/ $$  __$$ |$$ \$$$$ |$$ |  $$ |$$ |  $$ |$$  __$$< $$  __|   
$$ |  $$ |$$ |  $$ |  \$$$  /  $$ |  $$ |$$ |\$$$ |$$ |  $$\ $$ |      $$ |  $$ |        $$ |      $$ |  $$ |$$ |\$$$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |      
$$ |  $$ |$$$$$$$  |   \$  /   $$ |  $$ |$$ | \$$ |\$$$$$$  |$$$$$$$$\ $$$$$$$  |        $$ |      $$ |  $$ |$$ | \$$ |$$$$$$$  | $$$$$$  |$$ |  $$ |$$$$$$$$\ 
\__|  \__|\_______/     \_/    \__|  \__|\__|  \__| \______/ \________|\_______/         \__|      \__|  \__|\__|  \__|\_______/  \______/ \__|  \__|\________|
"""[1:]


flower = '''
                ..ooo.
             .888888888.
           .888"P""T"T888 8o
         o8o 8.8"8 88o."8o 8o
        88 . o88o8 8 88."8 88P"o
       88 o8 88 oo.8 888 8 888 88
       88 88 88o888" 88"  o888 88
       88."8o."T88P.88". 88888 88
       888."888."88P".o8 8888 888
       "888o"8888oo8888 o888 o8P"
        "8888.""888P"P.888".88P
         "88888ooo  888P".o888
           ""8P"".oooooo8888P
  .oo888ooo.    888PANDORE88
o88888"888"88o.  "8888"".88   .oo888oo..
 8888" "88 88888.       88".o88888888"888.
 "8888o.""o 88"88o.    o8".888"888"88 "88P
  T888C.oo. "8."8"8   o8"o888 o88" ".=888"
   88YOZO8o "8 8 8  .8 .8"88 8"".o888o8P
    "8888C.o8o  8 8  8" 8 o" ...o"""8888
      "88888888 " 8 .8  8   8THEGOAT8"
        "8888888o  .8o=" o8o..o(8oo88"
            "888" 88"    888888888""
                o8P       "888"""
          ...oo88
 "8oo...oo888""
'''[1:]




System.Size(140, 40)
System.Title("Pandore by yozo")
System.Clear()
Anime.Fade(Center.Center(flower), Colors.red_to_green, Colorate.Vertical, interval=0.025, enter=True)



def main():
  System.Clear()
  print("\n"*2)
  print(Colorate.Diagonal(Colors.red_to_green, Center.XCenter(ascii)))
  print("\n"*5)
  
  file = Write.Input("Drop ton image a convertir -> ", Colors.green_to_yellow, interval=0.005)
  
  if not isfile(file):
      print()
      print(Colorate.Error("Erreur! Cette image n'existe pas!"))
      return

  scale = Write.Input("Entrée l'echelle voulu (recommandé: 8) -> ", Colors.green_to_yellow, interval=0.005)
  
  try:
    scale = int(scale)
  except:
    print()
    print(Colorate.Error("Erreur! L'échelle doit être un nombre entier"))
    return

  build(imagepath=file, scale=scale)
  
  print()
  Write.Input("Fini!", Colors.green_to_yellow, interval=0.005)
  return exit()
        

if __name__ == '__main__':
    while True:
        main()
