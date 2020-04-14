import discord
import utils

class ImageService():
    def __init__(self, config):
        self.config = config

    async def sendFinger(self, ctx: discord.Message):
        print('finger called')

        file = utils.pickRandomFile('finger')

        await ctx.channel.send(
            file=discord.File(file)
        )

        return True

    async def sendSimon(self, ctx: discord.Message):
        print('simon called')

        if(ctx.guild.get_member(109626488076111872) != None):
            file = utils.pickRandomFile('simon')

            await ctx.channel.send(
                file=discord.File(file)
            )

        return True

    async def sendMuppet(self, ctx: discord.Message):
        print('muppet called')

        file = 'lib/muppet.jpg'

        await ctx.channel.send(
            file=discord.File(file)
        )

        return True

    async def sendThumbsUp(self, ctx: discord.Message):
        print('thumbsup called')

        file = 'lib/thumbsup.jpg'

        await ctx.channel.send(
            file=discord.File(file)
        )

        return True