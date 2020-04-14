import discord
from app.services import imageService
from discord.ext import commands

class ImageHandler(commands.Cog):
    def __init__(self, client, config):
        self.client = client
        self.service = imageService.ImageService(config)

    @commands.command()
    async def finger(self, ctx: discord.Message):
        await self.service.sendFinger(ctx)

    @commands.command()
    async def simon(self, ctx: discord.Message):
        await self.service.sendSimon(ctx)

    @commands.command()
    async def muppet(self, ctx: discord.Message):
        await self.service.sendMuppet(ctx)

    @commands.command(aliases=['+1', '👍'])
    async def thumbsup(self, ctx: discord.Message):
        await self.service.sendThumbsUp(ctx)
