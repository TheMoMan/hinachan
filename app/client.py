import discord
import os
import random
import app.utils
from app.handlers import *
from app.embeds import helpEmbed
from discord.ext import commands

prefix = os.environ['PREFIX']

client = commands.Bot(command_prefix=prefix, help_command=None)

response = responseHandler.ResponseHandler(client)

@client.event
async def on_message(message: discord.Message):
    if(await response.handle(message)):
        return

    await client.process_commands(message)

@client.event
async def on_ready():
    print('User: {}'.format(client.user.name))
    print('Client ID: {}'.format(client.user.id))
    print('------')


client.add_cog(imageHandler.ImageHandler(client))
client.add_cog(masterHandler.MasterHandler(client))
client.add_cog(utilHandler.UtilHandler(client))

with open(os.environ['SECRET'], 'r') as f:
    client.run(f.readline())
