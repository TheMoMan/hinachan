from app.services import imageService
from discord.ext import commands

class ImageHandler(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.service = imageService.ImageService()

    @commands.command()
    async def finger(self, ctx: commands.Context):
        img = self.service.getFinger()

        await ctx.channel.send(file=img)

    @commands.command()
    async def simon(self, ctx: commands.Context):
        img = self.service.getSimon()

        await ctx.channel.send(file=img)

    @commands.command()
    async def muppet(self, ctx: commands.Context):
        img = self.service.getMuppet()

        await ctx.channel.send(file=img)

    @commands.command(aliases=['+1', '👍'])
    async def thumbsup(self, ctx: commands.Context):
        img = self.service.getThumbsUp()

        await ctx.channel.send(file=img)

    @commands.command(aliases=['police'])
    async def fbi(self, ctx: commands.Context):
        img = self.service.getFbi()

        await ctx.channel.send(file=img)

    @commands.command(aliases=['ohno', 'anyway'])
    async def ohNo(self, ctx: commands.Context):
        img = self.service.getOhNo()

        await ctx.channel.send(file=img)

    @commands.command()
    async def what(self, ctx: commands.Context):
        img = self.service.what()

        await ctx.channel.send(file=img)

    @commands.command(aliases=['notwrong', 'nevermind'])
    async def speechless(self, ctx: commands.Context):
        img = self.service.speechless()

        await ctx.channel.send(file=img)

    @commands.command(aliases=['hmm', 'suspicious'])
    async def fry(self, ctx: commands.Context):
        img = self.service.fry()

        await ctx.channel.send(file=img)
