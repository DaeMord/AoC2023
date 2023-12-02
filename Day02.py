#https://adventofcode.com/2023/day/2
from AoC import inputData
from numpy import prod

dataInput = inputData('data/day02.txt')
#dataInput = inputData('data/test02.txt')

cubesInBag = [[12, "red"], [13, "green"], [14, "blue"]]
def main():
    finalSum = 0
    answer2 = 0
    dataExtract = {}
    finalData = {}
    for i in dataInput:
        game = i.split(": ")[0]
        data = i.split(": ")[1].split("; ")
        dataExtract[game] = []
        for i in data:
            loopdata = i.split(", ")
            for i in loopdata:
                datacheck = i.split(" ")
                dataExtract[game].append(datacheck)
    for i in dataExtract:
        finalData[i] = {}
        for x in dataExtract[i]:
            colourtoCompare = x[1]
            valuetoCompare = x[0]
            if colourtoCompare in finalData[i]:
                if int(finalData[i][colourtoCompare]) < int(valuetoCompare):
                    finalData[i][colourtoCompare] = valuetoCompare
            else:
                finalData[i][colourtoCompare] = valuetoCompare
    for i in finalData:
        answer2 += (prod(list(int(n) for n in list(finalData[i].values()))))
        if possibleBag(cubesInBag, finalData[i]):
            finalSum += int(i.split(" ")[1])
    return finalSum, answer2

def possibleBag(cubes, bag):
    #print(bag)
    for i in cubes:
        if int(bag[i[1]]) > int(i[0]):
            return False
    return True

data = main()
print("Answer 1")
print(data[0])
print("Answer 2")
print(data[1])