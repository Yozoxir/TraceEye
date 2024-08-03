# Par yozoxir
#https://github.com/Yozoxir/Advanced-multitools



from os.path import isfile
from pystyle import Anime, Colorate, Colors, Center, System, Write
from zlib import compress


def Parasite(content):
    ncontent = compress(content)
    return f"eval(compile(__import__('zlib').decompress({ncontent}),filename='parasite',mode='exec'))"




banner = r'''
                                  _      ____ _                   
                             --'""             """"""---              
                   _   --""                               `-                
                 -'           :'::::;:::%: ::::::_;;:        `- 
              -'         ::::''"''   _   ---'"""":::+;_::       `        
            '        ::::'      _ -""               :::)::        ` 
                  ;:::'     _ -'                       f::'::    o  _
        /      :::%'      -"                         -   ::;;:    /" "x
       '  "":: ::'     -"     _ --'"""-            (   )  :: ::  |_ -' |
      '    ::;:'     '      -"  d@@b    \           `-'   ::%::   \_ _/     
     '    :,::'    /     _'    8@@@@8   j       -'       :::::      " o
    |    : %:'    j     (_)    `@@@P'   '    -"         :: ::       f
    |    ::::     (        -  ____   -'   -"           ::::'       /
    |    `:`::    `                   --'            ::'::        /
    j     `:::::    `- _____   ---""              ::%:::'        '   
     \      :: :%                               :,::::'        '
      \       `:::`:                      :::: ::::'        -'           
       \        ``:::%::`::       :::::%:: ::::''        -'
        `           ``::::::%:::: ::;;:::::'"'      _ -'           
          `-                ````''"''           _ -'                 
              ""--   ____        ______      --'                      
                         """"""""'''[1:]


ascii = '''
                                                                  < >
 $$$$$$\  $$$$$$$\  $$\    $$\  $$$$$$\  $$\   $$\  $$$$$$\  $$$$$$$$\ $$$$$$$\          $$$$$$$\   $$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\  $$$$$$\ $$$$$$$$\ $$$$$$$$\ 
$$  __$$\ $$  __$$\ $$ |   $$ |$$  __$$\ $$$\  $$ |$$  __$$\ $$  _____|$$  __$$\         $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ \_$$  _|\__$$  __|$$  _____|
$$ /  $$ |$$ |  $$ |$$ |   $$ |$$ /  $$ |$$$$\ $$ |$$ /  \__|$$ |      $$ |  $$ |        $$ |  $$ |$$ /  $$ |$$ |  $$ |$$ /  $$ |$$ /  \__|  $$ |     $$ |   $$ |      
$$$$$$$$ |$$ |  $$ |\$$\  $$  |$$$$$$$$ |$$ $$\$$ |$$ |      $$$$$\    $$ |  $$ |$$$$$$\ $$$$$$$  |$$$$$$$$ |$$$$$$$  |$$$$$$$$ |\$$$$$$\    $$ |     $$ |   $$$$$\    
$$  __$$ |$$ |  $$ | \$$\$$  / $$  __$$ |$$ \$$$$ |$$ |      $$  __|   $$ |  $$ |\______|$$  ____/ $$  __$$ |$$  __$$< $$  __$$ | \____$$\   $$ |     $$ |   $$  __|   
$$ |  $$ |$$ |  $$ |  \$$$  /  $$ |  $$ |$$ |\$$$ |$$ |  $$\ $$ |      $$ |  $$ |        $$ |      $$ |  $$ |$$ |  $$ |$$ |  $$ |$$\   $$ |  $$ |     $$ |   $$ |      
$$ |  $$ |$$$$$$$  |   \$  /   $$ |  $$ |$$ | \$$ |\$$$$$$  |$$$$$$$$\ $$$$$$$  |        $$ |      $$ |  $$ |$$ |  $$ |$$ |  $$ |\$$$$$$  |$$$$$$\    $$ |   $$$$$$$$\ 
\__|  \__|\_______/     \_/    \__|  \__|\__|  \__| \______/ \________|\_______/         \__|      \__|  \__|\__|  \__|\__|  \__| \______/ \______|   \__|   \________|
'''[1:]


def init():
  System.Title("Advanced-para")
  System.Size(180, 50)
  Anime.Fade(text=Center.Center(banner), color=Colors.green_to_yellow, mode=Colorate.Vertical, enter=True)


def main():
  System.Clear()
  print("\n"*2)
  print(Colorate.Diagonal(Colors.green_to_yellow, Center.XCenter(ascii)))
  print("\n"*5)

  file = Write.Input(" Drop ton fichier python -> ", Colors.green_to_yellow, interval=0.005)
  print()

  if not isfile(file):
      print(Colorate.Error(" Erreur! Ce fichier n'existe pas!"))
      return

  with open(file, mode='rb') as f:
    content = f.read()

  olen = len(content)
  content = Parasite(content)
  nlen = len(content)

  with open(file='new-' + (file.split('\\')[-1] if '\\' in file else file.split('/')[-1]), mode='w', encoding='utf-8') as f:
      f.write(content)

  print()

  Write.Input(f" Fini! Taille de l'ancien fichier e: [{olen} bytes] - Taille du nouveaux fichier: [{nlen} bytes]", Colors.green_to_yellow, interval=0.005)
  return exit()


if __name__ == '__main__':
  init()
  while True:
    main()