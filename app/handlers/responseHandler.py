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
        self.lastMessagesCache = {}
        # TODO: Replace with regex
        self.badWords = json.loads(os.environ['BAD_WORDS'])
        self.susWords = json.loads(os.environ['SUSPICIOUS_WORDS'])

    # I look at this now and I hate it. TODO: Stop with the elifs
    async def handle(self, ctx: commands.Context):
        content = ctx.content

        timestamps = re.findall('\d{2}:\d{2}:\d{3}(?: \((?:\d|\d,)+\))?', content)
        wysi = re.findall('(?<!<)7( +\D*|\D* +|\D?)2( +\D*|\D* +|\D?)7(?![\w\s]*[>])', content)
        happyBirthday = re.findall('\\bhappy birthday\\b', content, re.IGNORECASE)

        if content in ['!^', '^']:
            msg = self.textService.getIAgree()

            await ctx.channel.send(msg)

            return True

        if content == '👍':
            img = self.imageService.getThumbsUp()

            await ctx.channel.send(file=img)

            return True

        if content == '🖕':
            img = self.imageService.getFinger()

            await ctx.channel.send(file=img)

            return True

        if any(substring in content.lower() for substring in ['rock and stone', 'deep rock', 'mining', 'miner', 'dwarf']):
            msg = self.textService.getRockAndStone()

            await ctx.channel.send(msg)

            return True

        if len(timestamps) > 0:
            embed = self.gameUtilService.createOsuEditorLink(timestamps)

            await ctx.channel.send(embed=embed)

            return True

        if len(wysi) > 0:
            msg = self.textService.wysi()

            await ctx.channel.send(msg)

            return True

        if len(happyBirthday) > 0 and ctx.author.id == int(os.environ['OWNER_ID']):
            msg = self.textService.getHappyBirthday()

            await ctx.channel.send(msg)

            return True

        return False

    async def handleLast(self, ctx: commands.Context):
        content = ctx.content
        doNotRepeat = False

        if ('hina' in content.lower() or os.environ['USER_ID'] in content.lower()) and 'china' not in content.lower():
            tries = 0

            for word in self.susWords:
                if word in content.lower():
                    await ctx.channel.send('no')
                    return

            async with ctx.channel.typing():
                while tries < 5:
                    msg = await self.textService.getRandomMessage(ctx.channel)

                    for word in self.badWords:
                        if word in msg.lower():
                            msg = ''
                            break

                    if len(msg) > 0:
                        break

                    tries += 1

                # Don't ping people
                filteredMsg = re.sub('<@!*&*[0-9]+>', '', msg)

                if len(filteredMsg) == 0:
                    filteredMsg = '.'

                print(filteredMsg)

                await ctx.channel.send(filteredMsg)

        for word in self.badWords:
            if word in content.lower():
                doNotRepeat = True
                break

        if not doNotRepeat:
            await self.textService.messageRepeater(ctx, self.lastMessagesCache)
