import discord

class GameUtilService():
    async def findWordWithCombination(self, ctx: discord.Message, letters: str):
        print('findWordWithCombination called')
        
        if len(letters) < 2:
            await ctx.channel.send('Need a combination of at least 2 letters!')
            return True
        
        # validWords = []

        with open('lib/words.txt', 'r') as f:
            words = set(f.read().split())

            # i = 0
            # for word in words:
            #     print('checking {}'.format(i))
            #     i += 1
            #     if letters in word:
            #         validWords.append(word)
            
            validWords = [word for word in words if letters.lower() in word]
            validWords.sort(key=len)

            if len(validWords) == 0:
                await ctx.channel.send('No words with combination {} found!'.format(letters))

            else:
                display = 15

                msg = '`' + '` `'.join(validWords[0:display]) + '`'

                if len(validWords) > display:
                    msg += ' and {} more'.format(len(validWords) - display)

                await ctx.channel.send(msg)

            return True
