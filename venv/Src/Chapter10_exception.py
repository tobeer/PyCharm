import json

try:  # 使用try-except处理异常
    print(5 / 0)
except ZeroDivisionError:
    print("You can't divide by zero!")

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)

file_name = "NotExistFile.txt"
try:
    with open(file_name) as notExistFile:
        notExistFile.read()
except FileNotFoundError:
    print("Sorry, the file " + file_name + " does not exist.")

file_name1 = "IdentifiedFiles/AliceInWonderland.txt"
try:
    with open(file_name1) as alice:
        content = alice.read()
except FileNotFoundError:
    print("Sorry, the file " + file_name1 + " does not exist.")
else:
    words = content.split()  # 分析文本有多少字
    number = len(words)
    print("The file " + file_name1 + " has about " + str(number) + " words.")

try:
    print(5 / 0)
except ZeroDivisionError:
    pass  # 捕获到异常后什么都不做

numbers = [1, 2, 3, 4, 5, 6]
with open("IdentifiedFiles/writeFile.txt", 'w') as f_obj:
    json.dump(numbers, f_obj)

with open("IdentifiedFiles/writeFile.txt") as f_obj1:
    numbers = json.load(f_obj1)
print(numbers)
print(type(numbers))
