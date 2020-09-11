def initialise(inputNum):
    row = 0
    column = 0
    group = (len(inputNum) + 3 - 1) / 3
    generatedList = [['0' for _ in range(3)] for _ in range(int(group))]
    for i in inputNum:
        generatedList[row][column] = i
        column += 1
        if column == 3:
            row += 1
            column = 0
    return generatedList


def translate(item):
    switch1 = {
        "0": "",
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine",
        "10": "ten",
        "11": "eleven",
        "12": "twelve",
        "13": "thirteen",
        "14": "fourteen",
        "15": "fifteen",
        "16": "sixteen",
        "17": "seventeen",
        "18": "eighteen",
        "19": "nineteen"}
    switch2 = {
        "2": "twenty",
        "3": "thirty",
        "4": "forty",
        "5": "fifty",
        "6": "sixty",
        "7": "seventy",
        "8": "eighty",
        "9": "ninety"}
    resultItem = ''
    if item[2] != '0':
        resultItem = switch1.get(item[2]) + ' hundred'
    if item[1] != '0':
        if item[1] == '1':
            temp = item[1] + item[0]
            if item[2] != '0':
                resultItem += ' and ' + switch1.get(temp)
            else:
                resultItem += switch1.get(temp)
        else:
            if item[2] != '0':
                resultItem += ' and ' + switch2.get(item[1]) + ' ' + switch1.get(item[0])
            else:
                resultItem += switch2.get(item[1]) + ' ' + switch1.get(item[0])
    else:
        if item[2] != '0' and item[0] != '0':
            resultItem += ' and ' + switch1.get(item[0])
        else:
            resultItem += switch1.get(item[0])
    return resultItem


def merge(numList):
    translatedNum = ''
    unit = 0
    for i in numList:
        translatedNum = translate(i) + translatedNum
        unit += 1
        if len(numList) > 1 and unit == 1:
            translatedNum = ' thousand ' + translatedNum
        if len(numList) == 3 and unit == 2:
            translatedNum = ' million ' + translatedNum
    return translatedNum


while True:
    inputnum = input()
    if inputnum == 'q':
        break
    if str.isdigit(inputnum):
        if len(inputnum) > 9:
            print("Please input a number no longer than nine digits in length")
        else:
            if inputnum == '0':
                print('zero')
            else:
                num = inputnum[::-1]
                numlist = initialise(num)
                result = merge(numlist)
                print(result)
                print("Input Q to exit!")
    else:
        print("error")
