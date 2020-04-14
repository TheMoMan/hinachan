import discord

class MasterService():
    def __init__(self, config):
        self.config = config

    async def setGuildNick(self, ctx: discord.Message, nickname: str=None):
        print('setNick called')

        if ctx.author.id == self.config['ownerId']:
            print('Attempt to set my nickname to {}'.format(nickname))

            try:
                await ctx.guild.get_member(self.config['userId']).edit(nick=nickname)
                newNick = ctx.guild.get_member(self.config['userId']).display_name
                await ctx.channel.send('My nickname is now {}!'.format(newNick))
            except:
                await ctx.channel.send('I don\'t have permission to do that :(')

        return True
