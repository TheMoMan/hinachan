import discord

def getBase():
    HELP_EMBED = discord.Embed(colour=0xFA8681)
    HELP_EMBED.set_thumbnail(url='https://cdn.discordapp.com/app-icons/292810126967046154/42bc50a3702dc9e73825de4dcd445544.png')

    return HELP_EMBED

def formatCommandsForMain(commands):
    return '`' + '` `'.join(commands) + '`'

def getMain():
    HELP_EMBED = getBase()
    HELP_EMBED.title = ':page_facing_up: Hina-chan Commands'
    HELP_EMBED.description = 'You can also do `!help <category>` for slightly more detailed help.\ne.g. `!help images`'
    
    images = ['finger', 'muppet', 'thumbsup', 'simon']
    HELP_EMBED.add_field(name=':frame_photo: Images', value=formatCommandsForMain(images))

    responses = ['^']
    HELP_EMBED.add_field(name=':speech_left: Responses', value=formatCommandsForMain(responses))

    utils = ['911']
    HELP_EMBED.add_field(name=':wrench: Utilities', value=formatCommandsForMain(utils))

    return HELP_EMBED

def getImages():
    HELP_EMBED = getBase()
    HELP_EMBED.title = ':frame_photo: Hina-chan Image Commands'
    HELP_EMBED.description = 'Commands that return an image.'
    
    HELP_EMBED.add_field(name='!finger', value='Flip the bird.')
    HELP_EMBED.add_field(name='!muppet', value='You muppet!')
    HELP_EMBED.add_field(name='!thumbsup', value=':thumbsup:')

    return HELP_EMBED

def getResponses():
    HELP_EMBED = getBase()
    HELP_EMBED.title = ':speech_left: Hina-chan Responses'
    HELP_EMBED.description = 'Hina-chan responses to regular chat. Command prefix isn\'t required to trigger these.'

    HELP_EMBED.add_field(name='^', value='I agree!')
    # HELP_EMBED.add_field(name='👍', value='ビッ')

def getUtils():
    HELP_EMBED = getBase()
    HELP_EMBED.title = ':wrench: Hina-chan Utility Commands'
    HELP_EMBED.description = 'Commands with a useful functionality.'

    HELP_EMBED.add_field(name='!911', value='For emergencies.')

    return HELP_EMBED