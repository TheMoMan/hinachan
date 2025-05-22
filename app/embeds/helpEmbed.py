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

    images = ['fbi', 'finger', 'muppet', 'ohno', 'simon', 'thumbsup']
    HELP_EMBED.add_field(name=':frame_photo: Images', value=formatCommandsForMain(images))

    gameUtils = ['defuse']
    HELP_EMBED.add_field(name=':game_die: Game Utilities', value=formatCommandsForMain(gameUtils))

    responses = ['^', '👍', '🖕']
    HELP_EMBED.add_field(name=':speech_left: Responses', value=formatCommandsForMain(responses))

    utils = ['911', 'choose', 'roll']
    HELP_EMBED.add_field(name=':wrench: Utilities', value=formatCommandsForMain(utils))

    return HELP_EMBED

def getImages():
    HELP_EMBED = getBase()
    HELP_EMBED.title = ':frame_photo: Hina-chan Image Commands'
    HELP_EMBED.description = 'Commands that return an image.'

    HELP_EMBED.add_field(name='!fbi', value='Open up!')
    HELP_EMBED.add_field(name='!finger', value='Flip the bird.')
    HELP_EMBED.add_field(name='!fry', value='Hmm...')
    HELP_EMBED.add_field(name='!muppet', value='You muppet!')
    HELP_EMBED.add_field(name='!ohno', value='Anyway...')
    HELP_EMBED.add_field(name='!thumbsup', value=':thumbsup:')
    HELP_EMBED.add_field(name='!simon', value='He whomst shall...')
    HELP_EMBED.add_field(name='!speechless', value='...')
    HELP_EMBED.add_field(name='!what', value='what.')

    return HELP_EMBED

def getGameUtils():
    HELP_EMBED = getBase()
    HELP_EMBED.title = ':game_die: Hina-chan Game Utilities'
    HELP_EMBED.description = 'Commands that return an image.'

    HELP_EMBED.add_field(name='!defuse <letters>', value='Solves a Bomb Party letter combination.\n`-v` Verbose mode.')

    return HELP_EMBED

def getResponses():
    HELP_EMBED = getBase()
    HELP_EMBED.title = ':speech_left: Hina-chan Responses'
    HELP_EMBED.description = 'Hina-chan responses to regular chat. Command prefix isn\'t required to trigger these.'

    HELP_EMBED.add_field(name='^', value='I agree!')
    HELP_EMBED.add_field(name='👍', value='ビッ')
    HELP_EMBED.add_field(name='🖕', value='Flip the bird.')

    return HELP_EMBED

def getUtils():
    HELP_EMBED = getBase()
    HELP_EMBED.title = ':wrench: Hina-chan Utilities'
    HELP_EMBED.description = 'Commands with a useful functionality.'

    HELP_EMBED.add_field(name='!911', value='For emergencies.')
    HELP_EMBED.add_field(name='!choose <option1> | <option2> ...', value='Picks a random option from a given list.')
    HELP_EMBED.add_field(name='!roll <max?>', value='Rolls a random number (default 1-100).')

    return HELP_EMBED
