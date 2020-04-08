import yaml
import discord
import os
import random
from discord.ext import commands

DEV_MODE = True

with open('configs/dev.yml' if DEV_MODE else 'configs/prod.yml', 'r') as f:
    config = yaml.safe_load(f)

# PREFIX = config['prefix']

client = commands.Bot(command_prefix = config['prefix'])


# Functionality

# Owner commands
@client.command()
async def setnick(ctx: discord.Message, nickname: str = None):
    print('setnick called')

    if ctx.author.id == config['ownerId']:
        print('Attempt to set my nickname to {}'.format(nickname))
        await ctx.guild.get_member(config['userId']).edit(nick=nickname)

# Public commands
@client.command(name='911')
async def nineoneone(ctx: discord.Message):
    print('911 called')

    with open('lib/911.txt', 'r', encoding='utf-8') as f:
        # print(f.read())
        await ctx.channel.send(f.read())

@client.command()
async def finger(ctx: discord.Message):
    print('finger called')

    files = ([name for name in os.listdir('lib/finger')])
    file = 'lib/finger/{}'.format(random.choice(files))

    await ctx.channel.send(file=discord.File(file))

# Text events
@client.event
async def on_message(message: discord.Message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content == '!^' or message.content == '^':
        print('!^ called')

        await message.channel.send('I agree!')

    # if message.content == '!resetName':
    #     print('Attempting to reset my name...')
    #     await message.guild.get_member(config['userId']).edit(nick=None)

    await client.process_commands(message)


# Initialisation

@client.event
async def on_ready():
    print('User: {}'.format(client.user.name))
    print('Client ID: {}'.format(client.user.id))
    print('------')

client.run(config['secret'])
