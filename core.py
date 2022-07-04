import discord
import asyncio
import setting
from command import Command,Handler


client = discord.Client()
defalt = Handler()
TOKEN = setting.TOKEN

@client.event
async def on_ready():
    print("logined")

@client.event
async def on_message(message):
    if message.author.bot:
        return
    for hdl in Handler.INSTANCE:
        pass
    


@Command.recv(msg=(True,"message"))
async def normal(message):
    pass

defalt.attach(normal)


client.run(TOKEN)