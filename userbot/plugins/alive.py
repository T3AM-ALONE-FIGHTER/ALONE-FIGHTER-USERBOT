
# Thanks to Sipak bro and Aryan.. 
# animation Idea by @NOOB_GUY_OP (Sipakisking) && @Hell boy_pikachu
# Made by @ROMANTIC_KILLER...and thanks to @Crackexy for the logos...
# Kang with credits else gay...
# Porting in Mafia Userbot by @H1M4N5HU0P

import asyncio
import random
from telethon import events
from userbot import ALIVE_NAME, mafiaversion
from mafiabot.utils import admin_cmd, sudo_cmd
from telethon.tl.types import ChannelParticipantsAdmins
from userbot.cmdhelp import CmdHelp

# ๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "ALONE FIGHTER BOT"

# Thanks to Sipak bro and Raganork.. 
# animation Idea by @NOOB_GUY_OP (Sipakisking)
# Made by @ROMANTIC_KILLER...and thanks to @Crackexy for the logos...
# Kang with credits else gay...


ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

mafia = bot.uid

edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/2603d71b3694d9a2684ab.jpg"
""" =======================CONSTANTS====================== """

pm_caption = "__                       **๐๐ฅ ๐ธ๐๐โ๐ผ ๐ฝ๐๐พโ๐๐ผโ ๐๐๐ผโ๐น๐๐ ๐๐ฅ**  __\n\n"

pm_caption += f"               __โผ๐ผ๐ฐ๐๐๐ด๐โ__\n**      ใ{DEFAULTUSER}ใ**\n\n"
pm_caption += "โ ฮฮฒรแปฎลฆ ฮยฅ ลยฅลลฆโฌฮ โ\n\n"
pm_caption += "โพ ๐๐๐๐๐๐๐๐         โฃ ๐.๐๐.๐\n"
pm_caption += "โพ ๐๐๐๐ ๐๐๐๐๐      โฃ [๐ธ๐๐โ๐ผ ๐๐](https://t.me/ALONE_FIGHTER_USERBOT_UPDATES)\n"
pm_caption += "โพ ๐๐๐๐๐๐๐ ๐๐๐๐๐ โฃ [๐๐๐๐](https://t.me/ALONE_FIGHTER_USERBOT)\n"
pm_caption += " EMPTY
pm_caption += "โพ ๐๐๐๐๐๐๐ ๐๐๐๐๐ โฃ [๐๐๐๐](https://t.me/ALONE_FIGHTER_USERBOT)\n"
pm_caption += "โพ ๐๐๐๐๐     โฃ [โก๏ฟฝโ๏ฟฝโ๐ผ๐ธ๐๐ผโ ๐๐๐โก](https://t.me/devil_darl_pro)\n\n" 
pm_caption += "[โจ๐๐๐๐๐๐ ๐ธ๐๐โ๐ผ ๐ฝ๐๐พโ๐๐ผโ ๐๐๐โจ](https://github.com/T3AM-ALONE-FIGHTER/ALONE-FIGHTER-BOT)"

# @command(outgoing=True, pattern="^.alive$")
@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    await alive.get_chat()   
    await alive.delete()
    on = await borg.send_file(alive.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(alive.chat_id, on, file=file2) 

    
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, caption=pm_caption)
    await alive.delete()
    
    
CmdHelp("alive").add_command(
  "alive", None, "To check am i alive"
).add_command(
  "savage", None, "To check am i alive with your favorite alive pic"
).add()
