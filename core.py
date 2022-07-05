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
    atach = {
        "msg":message
    }
    for hdl in Handler.INSTANCE:
        handler = Handler.INSTANCE[hdl]
        for cmd in handler.getCommands():
            await cmd.run(atach)
    


@Command.recv(msg=(True,"message"))
async def normal(message:discord.Message):
    await message.channel.send(message.content)

defalt.attach(normal)


client.run(TOKEN)