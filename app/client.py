import yaml
import discord
import os
import random
import app.utils
from app.handlers import *
from app.embeds import helpEmbed
from discord.ext import commands

DEV_MODE = True

with open('configs/dev.yml' if DEV_MODE else 'configs/prod.yml', 'r') as f:
    config = yaml.safe_load(f)

client = commands.Bot(command_prefix=config['prefix'], help_command=None)

response = responseHandler.ResponseHandler(client, config)

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


client.add_cog(imageHandler.ImageHandler(client, config))
client.add_cog(masterHandler.MasterHandler(client, config))
client.add_cog(utilHandler.UtilHandler(client, config))

with open(config['secret'], 'r') as f:
    client.run(f.readline())
