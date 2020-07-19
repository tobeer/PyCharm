bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[-1])  # 访问最后一个元素可用'-1', '-2'访问倒数第二元素，以此类推

bicycles[0] = 'drop'  # 修改列表元素
print(bicycles)

bicycles.append('down')  # 在列表末尾添加元素
print(bicycles)

bicycles.insert(0, 'first')  # 在列表指定位置插入元素
print(bicycles)

del bicycles[0]  # 使用del删除元素
print(bicycles)

last = bicycles.pop(-2)  # 使用pop()删除元素
print(bicycles)
print(last)

bicycles.remove('drop')  # 根据值删除元素
print(bicycles)

bicycles.sort()  # 使用sort()对列表进行永久性排序
print(bicycles)
bicycles.sort(reverse=True)  # true首字母大写
print(bicycles)
temp = sorted(bicycles)  # 使用sorted()对列表进行临时排序
print(temp)
print(bicycles)
print('==================================')
print(bicycles)
bicycles.reverse()
print(bicycles)  # 倒着打印列表
print(len(bicycles))  # 确定列表长度
