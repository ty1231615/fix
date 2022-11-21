import discord
import asyncio
import setting
import re
import json
from discord.ext import commands
from discord_buttons_plugin import *

client = commands.Bot(command_prefix="!")
buttons = ButtonsClient(client)

def extension_reload():
    load_list = json.loads(open("extension.json","r",encoding="UTF-8").read())
    for path in load_list:
        client.reload_extension(path)

def extension_load():
    load_list = json.loads(open("extension.json","r",encoding="UTF-8").read())
    for path in load_list:
        client.load_extension(path)

class Defalt(commands.Cog):
    def __init__(self,bot:commands.Bot) -> None:
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        extension_load()
    @commands.Cog.listener()
    async def on_message(self,ctx):
        print(ctx.content)
    @commands.command()
    async def reload(self,ctx):
        try:
            extension_reload()
        except Exception as e:
            await ctx.send(e)
        await ctx.send(self.bot.cogs)

client.add_cog(Defalt(client))


print("Startup system")
client.run(setting.TOKEN)