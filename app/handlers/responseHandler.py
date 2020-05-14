import discord
import re
from app.services import imageService, textService, gameUtilService
from discord.ext import commands

class ResponseHandler():
    def __init__(self, client):
        self.client = client
        self.imageService = imageService.ImageService()
        self.textService = textService.TextService()
        self.gameUtilService = gameUtilService.GameUtilService()

    async def handle(self, ctx: commands.Context):
        content = ctx.content

        timestamps = re.findall('\d{2}:\d{2}:\d{3}(?: \((?:\d|\d,)+\))?', content)
        
        if content in ['!^', '^']:
            msg = self.textService.getIAgree()

            await ctx.channel.send(msg)

            return True

        elif content == '👍':
            img = self.imageService.getThumbsUp()

            await ctx.channel.send(file=img)

            return True

        elif content == '🖕':
            img = self.imageService.getFinger()

            await ctx.channel.send(file=img)

            return True
        
        elif len(timestamps) > 0:
            embed = self.gameUtilService.createOsuEditorLink(timestamps)

            await ctx.channel.send(embed=embed)

            return True

        return False