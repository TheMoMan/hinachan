import yaml
import discord
import os
import random
import utils
from embeds import helpEmbed
from discord.ext import commands

DEV_MODE = True

with open('configs/dev.yml' if DEV_MODE else 'configs/prod.yml', 'r') as f:
    config = yaml.safe_load(f)

client = commands.Bot(command_prefix=config['prefix'], help_command=None)


# Functionality

# Owner commands
@client.command()
async def setnick(ctx: discord.Message, nickname: str=None):
    print('setnick called')

    if ctx.author.id == config['ownerId']:
        print('Attempt to set my nickname to {}'.format(nickname))
        await ctx.guild.get_member(config['userId']).edit(nick=nickname)

# Public commands
@client.command()
async def help(ctx:discord.Message, category: str=None):
    print('help called')

    def switchHelp(category):
        return {
            'images': helpEmbed.getImages(),
            'utilities': helpEmbed.getUtils(),
        }.get(category, helpEmbed.getMain())

    await ctx.channel.send(embed=switchHelp(category))

@client.command(name='911')
async def nineoneone(ctx: discord.Message):
    print('911 called')

    with open('lib/911.txt', 'r', encoding='utf-8') as f:
        # print(f.read())
        await ctx.channel.send(f.read())

@client.command()
async def finger(ctx: discord.Message):
    print('finger called')

    file = utils.pickRandomFile('finger')

    await ctx.channel.send(
        file=discord.File(file)
    )

@client.command()
async def simon(ctx: discord.Message):
    print('simon called')

    if(ctx.guild.get_member(109626488076111872) != None):
        file = utils.pickRandomFile('simon')

        await ctx.channel.send(
            file=discord.File(file)
        )

@client.command()
async def muppet(ctx: discord.Message):
    print('muppet called')

    file = 'lib/muppet.jpg'

    await ctx.channel.send(
        file=discord.File(file)
    )

@client.command(aliases=['+1', '👍'])
async def thumbsup(ctx: discord.Message):
    print('thumbsup called')

    file = 'lib/thumbsup.jpg'

    await ctx.channel.send(
        file=discord.File(file)
    )

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

client.run(config['secret'])
