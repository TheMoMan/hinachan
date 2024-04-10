import discord
import os
from app.handlers import *
from discord.ext import commands

prefix = os.environ['PREFIX']

client = commands.Bot(command_prefix=prefix, help_command=None, intents=discord.Intents.all())

response = responseHandler.ResponseHandler(client)

@client.event
async def on_message(message: discord.Message):
    if message.author == client.user or message.author.bot:
        return
    
    if await response.handle(message):
        return

    await client.process_commands(message)

    await response.handleLast(message)

@client.event
async def on_ready():
    print('User: {}'.format(client.user.name))
    print('Client ID: {}'.format(client.user.id))
    print('------')

    await client.add_cog(imageHandler.ImageHandler(client))
    await client.add_cog(gameUtilHandler.GameUtilHandler(client))
    await client.add_cog(masterHandler.MasterHandler(client))
    await client.add_cog(utilHandler.UtilHandler(client))

    loopHandler.LoopHandler(client).startLoops()

with open(os.environ['SECRET'], 'r') as f:
    client.run(f.readline())
