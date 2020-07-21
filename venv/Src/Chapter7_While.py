current_number = 1
while current_number < 5:  # while loop
    print(current_number)
    current_number += 1

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)

active = True  # 使用标志, 将条件成立与否存储在标注中，简化使用elif
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

# 使用break退出循环
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        break
    else:
        print(message)

current_number = 1
while current_number < 10:  # while loop
    if current_number % 2 == 1:
        current_number += 1
        continue
    print(current_number)
    current_number += 1

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:  # 在列表之间移动元素
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
print("\nThe following users have been confirmed")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
print("unconfirmed_users" + str(unconfirmed_users))
print("confirmed_user" + str(confirmed_users))

responses = {}
polling_active = True
while polling_active:  # 使用用户输入来填充字典
    name = input("\nPlease input your name: ")
    montain = input("Which mountain would you like to climb someday? ")
    responses[name] = montain
    again = input("Would you like to let another person response?(yes/no)")
    if again in ['yes', 'y']:
        continue
    else:
        polling_active = False
for name, response in responses.items():
    print(name + "would like to clime mountain " + response)
