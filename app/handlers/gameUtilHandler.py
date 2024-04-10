import app.utils as utils
from app.services import gameUtilService
from discord.ext import commands

class GameUtilHandler(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.service = gameUtilService.GameUtilService()

    @commands.command()
    async def defuse(self, ctx: commands.Context, letters: str=''):
        flags = utils.getFlags(ctx)

        if len(letters) < 2:
            await ctx.channel.send('Need a combination of at least 2 letters!')
            return

        if '-v' in flags or '--verbose' in flags:
            async with ctx.channel.typing():
                display = 30

                wordCategories = self.service.categoriseWordsWithCombination(letters)

                if len(wordCategories) == 0:
                    await ctx.channel.send('No words with combination {} found!'.format(letters.upper()))
                    return

                msg = ''

                for category in wordCategories:
                    line = '**{} - {} letters:**\n`'.format(letters.upper(), len(category[0]))  + '` `'.join(category[0:display]) + '`'

                    if len(category) > display:
                        line += ' and {} more'.format(len(category) - display)

                    if len(msg) + len(line) > 1996:
                        await ctx.channel.send(msg)
                        msg = line + '\n\n'

                    else:
                        msg += (line + '\n\n')

                await ctx.channel.send(msg)

                return

        display = 15
        
        words = self.service.findWordsWithCombination(letters)

        if len(words) == 0:
            await ctx.channel.send('No words with combination {} found!'.format(letters.upper()))

        else:
            msg = '**{}** : `'.format(letters.upper()) + '` `'.join(words[0:display]) + '`'

            if len(words) > display:
                msg += ' and {} more'.format(len(words) - display)

            await ctx.channel.send(msg)
