import discord
from app.services import gameUtilService
from discord.ext import commands

class GameUtilHandler(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.service = gameUtilService.GameUtilService()

    @commands.command()
    async def defuse(self, ctx: commands.Context, letters: str=''):
        if len(letters) < 2:
            await ctx.channel.send('Need a combination of at least 2 letters!')

        display = 15
        
        words = self.service.findWordsWithCombination(letters)

        if len(words) == 0:
            await ctx.channel.send('No words with combination {} found!'.format(letters.upper()))

        else:
            msg = '{} : `'.format(letters.upper()) + '` `'.join(words[0:display]) + '`'

            if len(words) > display:
                msg += ' and {} more'.format(len(words) - display)

            await ctx.channel.send(msg)
