print("Hello Python!")
p1 = "Hi！"
print(p1)
p1 = "Good Evening!"
print(p1)
p2 = "good morning!"
print(p2.title())  # 首字母大写
print(p2.upper())  # 全部大写
print(p2.lower())  # 全部小写
first_name = "anne"
last_name = "hathaway"
full_name = first_name + " " + last_name  # 字符串拼接
print(full_name.title())
print("python\tpython")  # 制表符(空格)
print("python\npython")  # 换行符
p3 = " delete_blank space "
print("!" + p3.rstrip() + "!")  # 删除末尾多余空白
print("!" + p3.lstrip() + "!")  # 删除开头多余空白
print("!" + p3.strip() + "!")  # 删除首末多余空白

age = 20
message = "Happy " + str(age) + " age"  # 非字符串转字符串
print(message)

import this  # Python之禅
