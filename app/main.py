import discord

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content == '!^' or message.content == '^':
        # msg = 'Hello {0.author.mention}'.format(message)
        await message.channel.send('I agree!')

    if message.content == '!resetName':
        print('Attempting to reset my name...')
        await message.guild.get_member(292810126967046154).edit(nick=None)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

# Get token and start bot
with open('lib/secret.txt', 'r') as f:
    secret = f.readline()

client.run(secret)
