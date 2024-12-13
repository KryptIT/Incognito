from RBX.Execute import *
from RBX.Initalize import *
from UTILS.CustomPrints import *
from UTILS.Procces import *
import asyncio
import requests




stop = asyncio.Event()

ascciart = r"""

 ___  ________   ________  ________  ________  ________   ___  _________  ________     
|\  \|\   ___  \|\   ____\|\   __  \|\   ____\|\   ___  \|\  \|\___   ___\\   __  \    
\ \  \ \  \\ \  \ \  \___|\ \  \|\  \ \  \___|\ \  \\ \  \ \  \|___ \  \_\ \  \|\  \   
 \ \  \ \  \\ \  \ \  \    \ \  \\\  \ \  \  __\ \  \\ \  \ \  \   \ \  \ \ \  \\\  \  
  \ \  \ \  \\ \  \ \  \____\ \  \\\  \ \  \|\  \ \  \\ \  \ \  \   \ \  \ \ \  \\\  \ 
   \ \__\ \__\\ \__\ \_______\ \_______\ \_______\ \__\\ \__\ \__\   \ \__\ \ \_______\
    \|__|\|__| \|__|\|_______|\|_______|\|_______|\|__| \|__|\|__|    \|__|  \|_______|
                                                                                       
                                                                                       
                                                                                       

"""


import urllib.request

url = "https://raw.githubusercontent.com/rattedccsoftwares/Incognito/refs/heads/main/LUABIN/gui.IncognitoLUAME"
with urllib.request.urlopen(url) as response:
    raw = response.read().decode('utf-8')


async def main():
   startsupport()
   startup("Incognito.")
   print(ascciart)
   thread("Injecting Make Sure Youre IN A GAME")
   AttachGame()
   await asyncio.sleep(3)
   info("Injected.")
   offset("69X6969 COREGUI PATCHED AS COREPATCH 69X69X69 BIG BALLS")
   error("Restarting...")
   await asyncio.sleep(3)
   await refresh()

async def refresh():
       os.system("cls")
       startsupport()
       startup("Incognito.")
       print(ascciart)
       thread("Injecting Make Sure Youre IN A GAME")
       AttachGame()
       info("Injected.")
       offset("69X6969 COREGUI PATCHED AS COREPATCH 69X69X69 BIG BALLS")
       ExecuteSync(raw)
       await stop.wait()
   
