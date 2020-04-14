import discord
from app.embeds import helpEmbed

class UtilService():
    async def sendHelp(self, ctx: discord.Message, category: str=None):
        print('sendHelp called')

        if not category:
            embed = helpEmbed.getMain()

        elif category.lower() == 'images':
            embed = helpEmbed.getImages()
        
        elif category.lower() == 'responses':
            embed = helpEmbed.getResponses()

        elif category.lower() == 'utilities':
            embed = helpEmbed.getUtils()

        await ctx.channel.send(embed=embed)

        return True

    async def sendNineOneOne(self, ctx: discord.Message):
        print('sendNineOneOne called')

        with open('lib/911.txt', 'r', encoding='utf-8') as f:
            await ctx.channel.send(f.read())

        return True