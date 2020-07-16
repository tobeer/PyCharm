magicians = ['alice', 'david', 'carolina', 'alice']
for magician in magicians: #for循环遍历列表
    print(magician)
for rg in range(1,6):
    print(rg)

num1 = list(range(1,6)) #range创建数值列表
print(num1)
num2 = list(range(2,11,2))
print(num2)

squares = []
for square in range(1,11): #遍历1-10的平方
    squares.append(square**2)
print(squares)
print(min(squares)) #列表中最小值
print(max(squares)) #列表中最大值
print(sum(squares)) #列表总和

cubes = [value**3 for value in range(1,11)] #列表解析
print(cubes)

print(cubes[0:3]) #切片，输出列表前三个元素
print(cubes[-2:]) #输出列表倒数两个元素

tempCubes = cubes[:] #复制列表副本，实为不同列表
print("tempCubes:", tempCubes)
cubes.append(0)
tempCubes.append(-1)
print("cubes:", cubes)
print("tempCubes:", tempCubes)
temp1Cubes = cubes #复制列表，实为同一列表
cubes.remove(0)
temp1Cubes.append(9999)
print("cubes:", cubes)
print("temp1Cubes:", temp1Cubes)
print("================================")

dimensions = (10,20) #元组，不可变的列表
print(dimensions[0])

print("Test Again")
print("Test Again1")
