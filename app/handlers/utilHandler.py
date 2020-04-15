import discord
from app.services import utilService
from discord.ext import commands

class UtilHandler(commands.Cog):
    def __init__(self, client):
        self.service = utilService.UtilService()

    @commands.command()
    async def help(self, ctx: discord.Message, category: str=None):
        await self.service.sendHelp(ctx, category)

    @commands.command(name='911')
    async def nineoneone(self, ctx: discord.Message):
        await self.service.sendNineOneOne(ctx)

    @commands.command()
    async def roll(self, ctx: discord.Message, max: str='100'):
        try:
            max = int(max)
            if max < 1 or max > 2147483647:
                max = 100

        except:
            max = 100
        
        await self.service.randomInteger(ctx, max)