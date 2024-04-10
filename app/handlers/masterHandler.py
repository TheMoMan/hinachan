import os
from app.services import masterService
from discord.ext import commands

class MasterHandler(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.service = masterService.MasterService()
        self.userId = int(os.environ['USER_ID'])
        self.ownerId = int(os.environ['OWNER_ID'])

    @commands.command()
    async def setNick(self, ctx: commands.Context, nickname: str=None):
        if ctx.author.id == self.ownerId:
            print('Attempt to set my nickname to {}'.format(nickname))

            try:
                await ctx.guild.get_member(self.userId).edit(nick=nickname)
                newNick = ctx.guild.get_member(self.userId).display_name
                await ctx.channel.send('My nickname is now {}!'.format(newNick))
            except:
                await ctx.channel.send('I don\'t have permission to do that :(')
