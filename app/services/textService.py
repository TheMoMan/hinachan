import discord
import random
import json
import os
from datetime import datetime, timedelta, timezone
from discord.ext import commands

class TextService():
    def getIAgree(self):
        print('getIAgree called')

        return 'I agree!'

    def getHappyBirthday(self):
        print('getHappyBirthday called')

        return 'Happy Birthday!'

    def getRockAndStone(self):
        print('getRockAndStoneCalled')

        rockAndStone = [
            'Rock and Stone!',
            'Did I hear a Rock and Stone?',
            'For Rock and Stone!',
            'For Karl!',
            'Rock and Stone to the Bone!',
            'Rock and Rolling Stone!',
            'If you don\'t Rock and Stone, you ain\'t coming home!',
            'We fight for Rock and Stone!',
            'Rock and Stone in the Heart!',
            'Rock and Stone forever!',
            'We\'re rich!',
        ]

        return random.choice(rockAndStone)

    def wysi(self):
        print ('wysi called')

        return 'wysi'
    
    def getSteamMaintenanceAlert(self):
        print('getSteamMaintenanceAlert called')

        return "**:warning: It's Tuesday :warning: Steam Maintenance Starting Soon :warning:** https://steamstat.us/"

    async def getRandomMessage(self, channel: discord.TextChannel):
        print('getRandomMessage called')

        oldest: list[discord.Message] = [message async for message in channel.history(oldest_first=True, limit=1)]
        channelAge = (datetime.now(timezone.utc) - oldest[0].created_at).days

        randomDay = random.randint(0, channelAge)
        randomMinute = random.randint(-720, 720)
        randomDate = datetime.now() - timedelta(days=randomDay, minutes=randomMinute)

        messages = [message async for message in channel.history(limit=99, around=randomDate) if message.author.bot == False]

        print('{} messages to choose from'.format(len(messages)))
        return random.choice(messages).content
    
    async def messageRepeater(self, ctx: commands.Context, lastMessagesCache):
        try:
            oldMessage = lastMessagesCache[ctx.channel.id]

        except:
            oldMessage = { 'message': '', 'author': '' }

        messageText = oldMessage['message']
        
        if bool(messageText) and messageText == ctx.content and oldMessage['author'] != ctx.author.id and not ctx.author.bot:
            await ctx.channel.send(ctx.content)
            lastMessagesCache[ctx.channel.id] = { 'message': '', 'author': '' }

            return

        badWords = json.loads(os.environ['BAD_WORDS'])
        for word in badWords:
            if word in messageText.lower:
                return

        lastMessagesCache[ctx.channel.id] = { 'message': ctx.content, 'author': ctx.author.id }
