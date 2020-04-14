import discord
import os

class MasterService():
    def __init__(self):
        self.userId = int(os.environ['USER_ID'])
        self.ownerId = int(os.environ['OWNER_ID'])

    async def setGuildNick(self, ctx: discord.Message, nickname: str=None):
        print('setGuildNick called')

        if ctx.author.id == self.ownerId:
            print('Attempt to set my nickname to {}'.format(nickname))

            try:
                await ctx.guild.get_member(self.userId).edit(nick=nickname)
                newNick = ctx.guild.get_member(self.userId).display_name
                await ctx.channel.send('My nickname is now {}!'.format(newNick))
            except:
                await ctx.channel.send('I don\'t have permission to do that :(')

        return True
