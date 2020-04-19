import discord

class GameUtilService():
    def findWordsWithCombination(self, letters: str):
        print('findWordsWithCombination called')

        with open('lib/words.txt', 'r') as f:
            words = set(f.read().split())
            
            validWords = [word for word in words if letters.lower() in word]
            validWords.sort(key=len)

            return validWords
