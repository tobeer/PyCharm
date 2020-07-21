prompt = "If you tell us who you are, we can personalize the message you see."
prompt += "\nWhat is your first name? "
name = input(prompt)  # 获取输入信息
print("\nHello, " + name + "!")

age = input("How old are you? ")
print(age)
# age > 10 wrong compare, age is string type
if int(age) > 18:
    print("已成年")
else:
    print("未成年")

print(5 / 3)
print(5 % 2)  # 判断奇偶数用模2
