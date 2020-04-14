import discord
from services import imageService, textService

class ResponseHandler():
    def __init__(self, client, config):
        self.client = client
        self.imageService = imageService.ImageService(config)
        self.textService = textService.TextService(config)

    async def handle(self, ctx: discord.Message):
        if ctx.author == self.client.user:
            return True

        content = ctx.content
        
        if content in ['!^', '^']:
            return await self.textService.sendIAgree(ctx)

        if content == '👍':
            return await self.imageService.sendThumbsUp(ctx)

        if content == '🖕':
            return await self.imageService.sendFinger(ctx)

        return False