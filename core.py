import discord
import asyncio
import setting


client = discord.Client()
TOKEN = setting.TOKEN

@client.event
async def on_ready():
    print("logined")

@client.event
async def on_message(message):
    if message.guild.id == 824527491614900224:
        await message.channel.send(message.content)


client.run(TOKEN)