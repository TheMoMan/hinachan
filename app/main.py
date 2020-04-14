import yaml
import discord
import os
import random
import utils
from handlers import *
from embeds import helpEmbed
from discord.ext import commands

DEV_MODE = True

with open('configs/dev.yml' if DEV_MODE else 'configs/prod.yml', 'r') as f:
    config = yaml.safe_load(f)

client = commands.Bot(command_prefix=config['prefix'], help_command=None)


# Text events
@client.event
async def on_message(message: discord.Message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content == '!^' or message.content == '^':
        print('!^ called')

        await message.channel.send('I agree!')

        return

    if message.content == '👍':
        print('👍 called')

        await thumbsup(message)

        return

    if message.content == '🖕':
        print('🖕 called')

        await finger(message)

        return

    await client.process_commands(message)


# Initialisation

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
