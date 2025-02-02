#    Copyright (C) Midhun KM 2020
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.


from fridaybot import ALIVE_NAME
from fridaybot.modules import currentversion

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://telegra.ph/file/9de90ce6fb5093f92db7c.jpg"
pm_caption = "➻ **ASSISTANT IS:** `ONLINE`\n\n"
pm_caption += "➻ **SYSTEMS STATS**\n"
pm_caption += "➻ **Telethon Version:** `1.15.0` \n"
pm_caption += "➻ **Python:** `3.7.4` \n"
pm_caption += "➻ **Database Status:**  `Functional`\n"
pm_caption += "➻ **Current Branch** : `master`\n"
pm_caption += f"➻ **Version** : `{currentversion}`\n"
pm_caption += f"➻ **My Boss** : {DEFAULTUSER} \n"
pm_caption += "➻ **Heroku Database** : `AWS - Working Properly`\n\n"
pm_caption += "➻ **License** : [GNU General Public License v3.0](github.com/StarkGang/FridayUserbot/blob/master/LICENSE)\n"
pm_caption += "➻ **Copyright** : By [Bruce Wayne](https://t.me/BruceSL)\n"
pm_caption += "[Assistant By Bruce Wayne](https://t.me/BruceSL)"

# only Owner Can Use it
@assistant_cmd("alive", is_args=False)
@peru_only
async def friday(event):
    await tgbot.send_file(event.chat_id, PM_IMG, caption=pm_caption)
