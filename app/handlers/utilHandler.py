import discord
from app.services import utilService
from discord.ext import commands

class UtilHandler(commands.Cog):
    def __init__(self, client):
        self.service = utilService.UtilService()

    @commands.command()
    async def help(self, ctx: commands.Context):
        category = ctx.message.content[6:]


        helpEmbed = self.service.getHelp(category)

        await ctx.channel.send(embed=helpEmbed)

    @commands.command(name='911')
    async def nineOneOne(self, ctx: commands.Context):
        content = self.service.getNineOneOne()

        await ctx.channel.send(content)

    @commands.command()
    async def roll(self, ctx: commands.Context, max: str='100'):
        try:
            max = int(max)
            if max < 1 or max > 2147483647:
                max = 100

        except:
            max = 100
        
        num = self.service.getRandomInteger(max)

        await ctx.channel.send(':game_die: **{}** rolls **{}**'.format(ctx.author.display_name, num))

        if num == 69:
            await ctx.channel.send('nice')

    @commands.command()
    async def choose(self, ctx: commands.Context):
        print('')