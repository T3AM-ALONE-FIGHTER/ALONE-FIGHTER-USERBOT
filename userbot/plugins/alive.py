
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

# 🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔
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

pm_caption = "__                       **😎🔥 𝔸𝕃𝕆ℕ𝔼 𝔽𝕀𝔾ℍ𝕋𝔼ℝ 𝕌𝕊𝔼ℝ𝔹𝕆𝕋 😎🔥**  __\n\n"

pm_caption += f"               __↼🄼🄰🅂🅃🄴🅁⇀__\n**      『{DEFAULTUSER}』**\n\n"
pm_caption += "✘ ΔβØỮŦ Μ¥ Ş¥ŞŦ€Μ ✘\n\n"
pm_caption += "➾ 𝐓𝐄𝐋𝐄𝐓𝐇𝐎𝐍         ➣ 𝟏.𝟏𝟕.𝟓\n"
pm_caption += "➾ 𝐓𝐄𝐀𝐌 𝐆𝐑𝐎𝐔𝐏      ➣ [𝔸𝕃𝕆ℕ𝔼 𝐎𝐏](https://t.me/ALONE_FIGHTER_USERBOT_UPDATES)\n"
pm_caption += "➾ 𝐒𝐔𝐏𝐏𝐎𝐑𝐓 𝐂𝐇𝐍𝐍𝐋 ➣ [𝐉𝐎𝐈𝐍](https://t.me/ALONE_FIGHTER_USERBOT)\n"
pm_caption += " EMPTY
pm_caption += "➾ 𝐒𝐔𝐏𝐏𝐎𝐑𝐓 𝐆𝐑𝐎𝐔𝐏 ➣ [𝐉𝐎𝐈𝐍](https://t.me/ALONE_FIGHTER_USERBOT)\n"
pm_caption += "➾ 𝐎𝐖𝐍𝐄𝐑     ➣ [⚡�ℂ�ℝ𝔼𝔸𝕋𝔼ℝ 𝐁𝐎𝐘⚡](https://t.me/devil_darl_pro)\n\n" 
pm_caption += "[✨𝐃𝐄𝐏𝐋𝐎𝐘 𝔸𝕃𝕆ℕ𝔼 𝔽𝕀𝔾ℍ𝕋𝔼ℝ 𝐁𝐎𝐓✨](https://github.com/T3AM-ALONE-FIGHTER/ALONE-FIGHTER-BOT)"

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
