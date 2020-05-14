import discord

class GameUtilService():
    def findWordsWithCombination(self, letters: str):
        print('findWordsWithCombination called')

        with open('lib/words.txt', 'r') as f:
            words = set(f.read().split())
            
            validWords = [word for word in words if letters.lower() in word]
            validWords.sort(key=len)

            return validWords

    def categoriseWordsWithCombination(self, letters: str):
        print('categoriseWordsWithCombination called')

        validWords = self.findWordsWithCombination(letters)

        if len(validWords) == 0:
            return []

        longest = len(validWords[-1])

        categories = []

        for i in range(longest):
            category = [word for word in validWords if len(word) == i]

            if len(category) > 0:
                categories.append(category)

        return categories

    def createOsuEditorLink(self, timestamps: list):
        print('createOsuEditorLink called')

        formatted = ['<osu://edit/{}>'.format(timestamp, timestamp).replace(' ', '_') for timestamp in timestamps]

        embed = discord.Embed(colour=0xFA8681)

        embed.title = ':thought_balloon: Timestamps'
        embed.description = '\n'.join(formatted)

        return embed
