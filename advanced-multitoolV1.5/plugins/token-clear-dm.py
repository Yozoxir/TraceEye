import os
import os.path
import discord
from discord.ext import commands
from colorama import Fore

def clear():
    pass

def cleardmtitle():
    pass

def setTitle(title):
    pass

def main():
    pass

setTitle("Clear DM")
clear()
cleardmtitle()

ascii_banner = f"""{Fore.RED}
 $$$$$$\  $$\       $$$$$$$$\ $$$$$$$$\  $$$$$$\  $$$$$$$\        $$$$$$$\  $$\      $$\ 
$$  __$$\ $$ |      $$  _____|$$  _____|$$  __$$\ $$  __$$\       $$  __$$\ $$$\    $$$ |
$$ /  \__|$$ |      $$ |      $$ |      $$ /  $$ |$$ |  $$ |      $$ |  $$ |$$$$\  $$$$ |
$$ |      $$ |      $$$$$\    $$$$$\    $$$$$$$$ |$$$$$$$  |      $$ |  $$ |$$\$$\$$ $$ |
$$ |      $$ |      $$  __|   $$  __|   $$  __$$ |$$  __$$<       $$ |  $$ |$$ \$$$  $$ |
$$ |  $$\ $$ |      $$ |      $$ |      $$ |  $$ |$$ |  $$ |      $$ |  $$ |$$ |\$  /$$ |
\$$$$$$  |$$$$$$$$\ $$$$$$$$\ $$$$$$$$\ $$ |  $$ |$$ |  $$ |      $$$$$$$  |$$ | \_/ $$ |
 \______/ \________|\________|\________|\__|  \__|\__|  \__|      \_______/ \__|     \__| 
"""

print(ascii_banner)

print(f"{Fore.YELLOW}Entré votre token")
token = input(f"{Fore.YELLOW}Token: ")
print(f"{Fore.YELLOW}Ecrit \"!clear\" dans un de tes messages privé pour supprimer tout les messages que tu as ecris")

global bot
bot = commands.Bot(command_prefix="!", self_bot=True)
bot.remove_command("help")

@bot.command()
async def clear(ctx, limit: int=None):
    passed = 0
    failed = 0
    async for msg in ctx.message.channel.history(limit=limit):
        if msg.author.id == bot.user.id:
            try:
                await msg.delete()
                passed += 1
            except:
                failed += 1
    print(f"\n{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}]{Fore.WHITE} Message supprimé {passed} avec {failed} d'erreurs")
    input(f"""\n{Fore.YELLOW}[{Fore.BLUE}#{Fore.YELLOW}]{Fore.WHITE} Press ENTER to exit""")
    main()

bot.run(token, bot=False)
