import os
import random
import discord
from discord.ext import commands

def pickRandomFile(directory: str):
    dir = 'lib/{}/'.format(directory)

    files = ([name for name in os.listdir(dir)])
    return dir + random.choice(files)

def getFlags(ctx: commands.Context):
    arguments = ctx.message.content.split(' ')
    flags = {}

    for i in range(len(arguments)):
        if arguments[i][0] == '-':
            flagArg = ''

            if i == len(arguments) - 1 or arguments[i+1][0] == '-':
                flags[arguments[i]] = True
                continue

            flags[arguments[i]] = arguments[i+1]
            i += 1

    return flags
