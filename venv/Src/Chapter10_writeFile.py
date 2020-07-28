with open('IdentifiedFiles/writeFile.txt', 'w') as file_object:  # 'w'写入模式，省略默认为只读模式
    file_object.write("First write to txt file.")  # python只能将字符串写入文本文件，写入其他类型需调用str进行转换
    file_object.write("One day you will leave this world.\n")
    file_object.write("So live a life you will remember.\n")

with open('IdentifiedFiles/writeFile.txt', 'a') as file_object1:  # 'a'附加模式，将内容写入文件末尾，不会覆盖原内容
    file_object1.write("My father told me when I was just a child\n")
