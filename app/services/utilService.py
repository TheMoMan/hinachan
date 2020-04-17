import discord
from app.embeds import helpEmbed
from random import randint

class UtilService():
    def getHelp(self, category: str=None):
        print('getHelp called')

        if not category:
            return helpEmbed.getMain()

        elif category.lower() == 'images':
            return helpEmbed.getImages()
        
        elif category.lower() == 'responses':
            return helpEmbed.getResponses()

        elif category.lower() in ['game utilities', 'game_utilities']:
            return helpEmbed.getGameUtils()

        elif category.lower() == 'utilities':
            return helpEmbed.getUtils()

        return helpEmbed.getMain()


    def getNineOneOne(self):
        print('getNineOneOne called')

        with open('lib/911.txt', 'r', encoding='utf-8') as f:
            content = f.read()

        return content

    def getRandomInteger(self, max: int=100):
        print('getRandomInteger called')

        return randint(1, max)

    def chooseOptionFromString(self, options: str):
        optionsArr = options.split('|')
        optionsLen = len(optionsArr)

        if optionsLen <= 1:
            raise ValueError('Not enough options.')

        index = randint(0, optionsLen-1)

        return optionsArr[index].strip(' ')
