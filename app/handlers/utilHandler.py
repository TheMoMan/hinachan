from app.services import utilService, diceService
from discord.ext import commands

class UtilHandler(commands.Cog):
    def __init__(self, client):
        self.service = utilService.UtilService()

    @commands.command()
    async def help(self, ctx: commands.Context):
        category = ctx.message.content[6:]

        helpEmbed = self.service.getHelp(category)

        await ctx.channel.send(embed=helpEmbed)

    @commands.command(name='911')
    async def nineOneOne(self, ctx: commands.Context):
        content = self.service.getNineOneOne()

        await ctx.channel.send(content)

    @commands.command(aliases=['dice', 'rand'])
    async def roll(self, ctx: commands.Context, roll: str='100'):
        if diceService.isDiceFormat(roll):
            try:
                value = diceService.evaluateDiceFormat(roll)
                await ctx.channel.send(embed=value)
                return

            except ValueError as error:
                await ctx.channel.send(str(error))
                return

        num = diceService.getRandomIntegerFromStr(roll)

        await ctx.channel.send(':game_die: **{}** rolls **{}**'.format(ctx.author.display_name, num))

        if num == 69:
            await ctx.channel.send('nice')

    @commands.command()
    async def choose(self, ctx: commands.Context):
        options = ctx.message.content[8:]

        try:
            option = self.service.chooseOptionFromString(options)

            await ctx.channel.send('{}!'.format(option))

        except ValueError:
            await ctx.channel.send('Use pipe `|` to separate options.')
