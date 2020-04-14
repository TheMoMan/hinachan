import discord
from services import utilService
from discord.ext import commands

class UtilHandler(commands.Cog):
    def __init__(self, client, config):
        self.client = client
        self.service = utilService.UtilService(config)

    @commands.command()
    async def help(self, ctx: discord.Message, category: str=None):
        await self.service.sendHelp(ctx, category)

    @commands.command(name='911')
    async def nineoneone(self, ctx: discord.Message):
        await self.service.sendNineOneOne(ctx)