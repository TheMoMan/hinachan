import discord
from app.services import imageService, textService

class ResponseHandler():
    def __init__(self, client):
        self.client = client
        self.imageService = imageService.ImageService()
        self.textService = textService.TextService()

    async def handle(self, ctx: discord.Message):
        if ctx.author == self.client.user:
            return True

        content = ctx.content
        
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

        return False