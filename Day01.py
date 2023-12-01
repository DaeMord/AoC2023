#https://adventofcode.com/2015/day/1
from AoC import inputData
from collections import OrderedDict
import re

dataInput = inputData('data/day01.txt')
#dataInput = inputData('data/test01.txt')
r = "(\d)"

data = {
    'one': 'o1e',
    'two': 't2o',
    'three': 't3e',
    'four': 'f4r',
    'five': 'f5e',
    'six': 's6x',
    'seven': 's7n',
    'eight': 'e8t',
    'nine': 'n9e'
}
def main():
    regex = re.compile(r)
    runningTotal1 = 0
    runningTotal2 = 0
    for word in dataInput:
        newWord = word
        for i in data:
            newWord = newWord.replace(i, data[i])
        numbers1 = regex.findall(word)
        numbers2 = regex.findall(newWord)
        fNumber1 = int(numbers1[0] + numbers1[-1])
        fNumber2 = int(numbers2[0] + numbers2[-1])
        runningTotal1 += fNumber1
        runningTotal2 += fNumber2
    return runningTotal1, runningTotal2

data = main()
#56397
print("Answer 1")
print(data[0])
#55701
print("Answer 2")
print(data[1])