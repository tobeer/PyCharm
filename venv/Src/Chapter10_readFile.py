with open('IdentifiedFiles/txtFile.txt') as file_object:  # 返回表示文件的对象
    contents = file_object.read()  # 将文件内容存储在contents中，with代码块之外仍可访问，with结束自动关闭文件
    print(contents)

print("\n=============================================================\n")

for line in contents:
    print(line)
    break

print("\n=============================================================\n")

with open('IdentifiedFiles/txtFile.txt') as file_object:
    contents1 = file_object.readline()  # 读取一行内容
    print(contents1)

print("\n=============================================================\n")

with open('IdentifiedFiles/txtFile.txt') as file_object:  # 读取整个文件
    contents2 = file_object.readlines()  # 读取整个文件，并按行返回到list中
    print(contents2)
for line1 in contents2:
    print(type(float(line1)))  # 字符转浮点
    print(line1)
    break
pi_string = ''
for line3 in contents2:
    pi_string += line3.rstrip()
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:  # birthday是否在pi_string里
    print("Your birthday appears in the pi!")
else:
    print("Your birthday does not appear in the pi!")

print("\n=============================================================\n")

with open('IdentifiedFiles/txtFile.txt') as file_object:  # 读取整个文件
    for line in file_object:  # 逐行读取
        print(line.rstrip())  # 去掉末尾空行

p1 = '3.1415926'
for i in p1:
    print(i)
