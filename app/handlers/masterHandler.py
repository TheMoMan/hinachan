import discord
from app.services import masterService
from discord.ext import commands

class MasterHandler(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.service = masterService.MasterService()

    @commands.command()
    async def setNick(self, ctx: discord.Message, nickname: str=None):
        await self.service.setGuildNick(ctx, nickname)