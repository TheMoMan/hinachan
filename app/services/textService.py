import discord

class TextService():
    def __init__(self, config):
        self.config = config

    async def sendIAgree(self, ctx: discord.Message):
        print('sendIAgree called')

        await ctx.channel.send('I agree!')

        return True