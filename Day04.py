#https://adventofcode.com/2023/day/4
from AoC import inputData
import re

dataInput = inputData('data/day04.txt')
#dataInput = inputData('data/test04.txt')


def main():

    ans1 = 0
    cardsTotal = {}
    for i in dataInput:
        result = re.split(r'[:,|]', i)
        card = int(re.findall(r'\b\d+\b', result[0])[0])
        win = re.findall(r'\b\d+\b', result[1])
        numChoice = re.findall(r'\b\d+\b', result[2])
        matchingNumbers = list(set(win).intersection(set(numChoice)))
        if len(matchingNumbers) > 0:
            if card in cardsTotal:
                numberOfCards = cardsTotal[card]
            else:
                numberOfCards = 0
            cardsTotal[card] = cardsTotal.setdefault(card, 0) + 1
            for cards in range(card + 1, card + len(matchingNumbers) + 1):
                cardsTotal[cards] = cardsTotal.setdefault(cards, 0) + 1 + numberOfCards
            ans1 += 1 * 2 ** (len(matchingNumbers) - 1)
        else:
            cardsTotal[card] = cardsTotal.setdefault(card, 0) + 1
    ans2 = sum(cardsTotal.values())

    return ans1, ans2


data = main()
print("Answer 1")
#26426
print(data[0])
print("Answer 2")
#6227972
print(data[1])