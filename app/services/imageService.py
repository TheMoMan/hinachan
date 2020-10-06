import discord
import app.utils as utils

class ImageService():
    def getFinger(self):
        print('getFinger called')

        file = utils.pickRandomFile('finger')
        return discord.File(file)

    def getSimon(self):
        print('getSimon called')

        file = utils.pickRandomFile('simon')
        return discord.File(file)
    
    def getFbi(self):
        print('getFbi called')

        file = utils.pickRandomFile('fbi')
        return discord.File(file)

    def getMuppet(self):
        print('getMuppet called')

        return discord.File('lib/muppet.jpg')

    def getThumbsUp(self):
        print('getThumbsUp called')

        return discord.File('lib/thumbsup.jpg')

    def getOhNo(self):
        print('getOhNo called')

        return discord.File('lib/ohno.jpg')
