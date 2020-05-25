import discord
import os
import random
from datetime import datetime, timedelta

class TextService():
    def getIAgree(self):
        print('getIAgree called')

        return 'I agree!'
    
    async def getRandomMessage(self, channel: discord.TextChannel):
        print('getRandomMessage called')

        oldest = await channel.history(oldest_first=True, limit=1).flatten()
        channelAge = (datetime.now() - oldest[0].created_at).days

        randomDay = random.randint(0, channelAge)
        randomMinute = random.randint(-720, 720)
        randomDate = datetime.now() - timedelta(days=randomDay, minutes=randomMinute)

        messages = await channel.history(limit=101, around=randomDate).filter(lambda msg: msg.author.bot == False).flatten()

        print('{} messages to choose from'.format(len(messages)))
        return random.choice(messages).content
