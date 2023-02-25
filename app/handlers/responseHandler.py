import discord
import re
import os
import json
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
        
        elif (substring in content.lower() for substring in ['rock and stone', 'drg', 'deep rock']):
            msg = self.textService.getRockAndStone()

            await ctx.channel.send(msg)

            return True
        
        elif len(timestamps) > 0:
            embed = self.gameUtilService.createOsuEditorLink(timestamps)

            await ctx.channel.send(embed=embed)

            return True
        
        elif 'Happy birthday' in content and ctx.author.id == int(os.environ['OWNER_ID']):
            msg = self.textService.getHappyBirthday()

            await ctx.channel.send(msg)

            return True

        return False

    async def handleLast(self, ctx: commands.Context):
        content = ctx.content
        badWords = json.loads(os.environ['BAD_WORDS'])

        if ('hina' in content.lower() or os.environ['USER_ID'] in content.lower()) and 'china' not in content.lower():
            tries = 0

            async with ctx.channel.typing():
                while tries < 5:
                    msg = await self.textService.getRandomMessage(ctx.channel)

                    for word in badWords:
                        if word in msg.lower():
                            msg = ''
                            break

                    if len(msg) > 0:
                        break

                    tries += 1
                
                if len(msg) == 0:
                    msg = 'I agree!'

                await ctx.channel.send(msg)
