import random
import re
import time

import requests
from cowpy import cow
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName

from userbot.cmdhelp import CmdHelp
from mafiabot.utils import admin_cmd, sudo_cmd, edit_or_reply



@bot.on(admin_cmd(pattern=f"repo", outgoing=True))
@bot.on(sudo_cmd(pattern=f"repo", allow_sudo=True))
async def source(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await edit_or_reply(e, "[Click here]() to open this\n🔥**Lit AF!!**🔥__ALONEhttps://github.com/T3AM-ALONE-FIGHTER/ALONE-FIGHTER-BOT__ repo.\nJoin [support](https://t.me/ALONE_FIGHTER_USERBOT) group)")
