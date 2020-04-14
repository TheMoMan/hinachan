import discord
from embeds import helpEmbed

class UtilService():
    def __init__(self, config):
        self.config = config

    async def sendHelp(self, ctx: discord.Message, category: str=None):
        print('help called')

        def switchHelp(category):
            return {
                'images': helpEmbed.getImages(),
                'responses': helpEmbed.getResponses(),
                'utilities': helpEmbed.getUtils(),
            }.get(category, helpEmbed.getMain())

        await ctx.channel.send(embed=switchHelp(category))

        return True

    async def sendNineOneOne(self, ctx: discord.Message):
        print('911 called')

        with open('lib/911.txt', 'r', encoding='utf-8') as f:
            await ctx.channel.send(f.read())

        return True