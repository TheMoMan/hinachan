import re
import discord
from random import randint
from typing import TypedDict
from operator import itemgetter

dicePattern = re.compile(r'^(?:\s*)(?:(?:\d+)?d\d+|\d+)(?:\s*[+\-]\s*(?:(?:\d+)?d\d+|\d+))*\s*$', re.IGNORECASE)
singleDicePattern = re.compile(r'(\-?)(\d*)d(\d+)', re.IGNORECASE)

class DiceResults(TypedDict):
    roll: str
    results: list[int]
    sum: int
    numberOfDice: int

def getRandomInteger(max: int=100):
    # print('getRandomInteger called')

    print(f'rolling: {max}')

    return randint(1, max)

def getRandomIntegerFromStr(max: str='100'):
    try:
        max = int(max)
        if max < 1 or max > 2147483647:
            max = 100

    except:
        max = 100

    return getRandomInteger(max)

def rollSingleDice(roll: str) -> DiceResults:
    if not singleDicePattern.fullmatch(roll):
        raise ValueError('Not a dice format')

    iterations, dice = roll.lower().split('d')

    negative = False

    if iterations and iterations[0] == '-':
        negative = True
        iterations = iterations.replace('-', '')

    iterations = int(iterations or 1)
    dice = int(dice)

    if dice > 10000:
        raise ValueError('Dice too large')

    if iterations > 100:
        raise ValueError(f'Too many d{dice}s')

    results = []

    for _ in range(iterations):
        results.append(getRandomInteger(dice))

    totalSum = sum(results)
    if negative:
        totalSum = totalSum * -1

    return {
        'roll': roll,
        'results': results,
        'sum': totalSum,
        'numberOfDice': iterations
    }

def isDiceFormat(roll: str):
    try:
        int(roll)
        return False

    except:
        sanitisedRoll = roll.replace(' ', '')

        if dicePattern.fullmatch(sanitisedRoll):
            return True

    return False

def evaluateDiceFormat(roll: str):
    rolls = roll.strip().replace('-', '+-').split('+')

    if len(rolls) > 20:
        raise ValueError('Too many rolls')

    total = 0
    diceResults = []
    values = []
    numberOfDice = 0

    for diceRoll in rolls:
        diceRoll = diceRoll.strip()

        try:
            total += int(diceRoll)
            values.append(int(diceRoll))

        except:
            rollResult = rollSingleDice(diceRoll)
            total += rollResult['sum']
            diceResults.append(rollResult)
            values.append(rollResult['sum'])
            numberOfDice += rollResult['numberOfDice']

        if numberOfDice > 100:
            raise ValueError('Too many dice')

    return formatDiceResults(roll, total, values, diceResults, numberOfDice)

def formatDiceResults(roll: str, total: int, values: list[int], diceResults: list[DiceResults], numberOfDice: int):
    rollEmbed = discord.Embed(colour=0xFA8681)
    rollEmbed.title = '🎲 Rolled dice'
    rollEmbed.description = roll

    rolls = []

    for result in diceResults:
        roll, results, sum = itemgetter('roll', 'results', 'sum')(result)

        formattedResult = ' + '.join(str(r) for r in results)

        if len(results) > 1:
            rolls.append(f'- **{roll}**: {formattedResult} = {sum}')
            continue

        rolls.append(f'- **{roll}**: {formattedResult}')

    if numberOfDice > 1:
        rollEmbed.add_field(name='Rolls', value='\n'.join(rolls), inline=False)

    if len(values) > 1:
        formattedValues = ' + '.join(str(v) for v in values) + f' = {total}'
        rollEmbed.add_field(name='Sum', value=formattedValues, inline=False)

    rollEmbed.add_field(name='Result', value=f'**{total}**', inline=False)

    return rollEmbed
