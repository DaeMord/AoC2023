#https://adventofcode.com/2023/day/3
from AoC import inputData, flatten
import re

dataInput = inputData('data/day03.txt')
#dataInput = inputData('data/test03.txt')

# print(dataInput)

SYMBOLS =('[*#+$/@=&%-]')
def main():
    finalNum = 0
    finalOutput = 1
    finalFinalOutput = 0
    starData = {}
    regex = re.compile('\d+')
    maxRow = len(dataInput) - 1
    for row, i in enumerate(dataInput):
        maxCol = (len(i) - 1)
        numbers = regex.findall(i.strip())
        for num in numbers:
            startrow = max((row - 1), 0)
            startcol = max((i.find(num) - 1), 0)
            endrow = min((row + 1), maxRow)
            endcol = min((i.find(num) + len(str(num)) + 1), maxCol)
            section = [row[startcol:+endcol] for row in dataInput[startrow:endrow + 1]]
            i = i[:i.find(num)] + '.' * len(str(num)) + i[i.find(num) + len(str(num)):]
            if re.search(SYMBOLS, ''.join(flatten(section))):
                if re.search('[*]', ''.join(flatten(section))):
                    for index, entry in enumerate(section):
                        if '*' in entry:
                            starLoc = startrow + index
                            starLocCol = startcol + entry.find("*")
                            star = str(starLoc) + "-" + str(starLocCol)
                            starData.setdefault(star, []).append(num)
                            break
                    else:
                        print("No entry in the array contains a star.")
                finalNum += int(num)

    for key in starData:
        if len(starData[key]) == 2:
            for num in starData[key]:
                finalOutput *= int(num)
            finalFinalOutput += finalOutput
            finalOutput = 1

    return finalNum, finalFinalOutput


data = main()
print("Answer 1")
#522726
print(data[0])
print("Answer 2")
#29348398
#80799715
#81721933
#too low
print(data[1])