import discord
from app.services import gameUtilService
from discord.ext import commands

class GameUtilHandler(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.service = gameUtilService.GameUtilService()

    @commands.command()
    async def defuse(self, ctx: discord.Message, letters: str=''):
        await self.service.findWordWithCombination(ctx, letters)
