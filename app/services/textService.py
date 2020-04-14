import discord
import os

class TextService():
    async def sendIAgree(self, ctx: discord.Message):
        print('sendIAgree called')

        await ctx.channel.send('I agree!')

        return True