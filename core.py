import discord
import asyncio
import setting
from command import Command,Handler


client = discord.Client()
TOKEN = setting.TOKEN

@client.event
async def on_ready():
    print("logined")

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.channel.id == 878106252478140456:
        await message.channel.send(message.content)


@Command.recv(msg=(True,"message"))
async def normal(message):
    pass



client.run(TOKEN)