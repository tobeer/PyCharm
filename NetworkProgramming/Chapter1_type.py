# Python有六种基本类型, number, string, tuple, list, dictionary, set

# number
a, b, c, d = 1, 1.0, True, 1 + 2j
print(type(a), type(b), type(c), type(d))

# string
str0 = '可用单引号'
str1 = "可用双引号"
str2 = """三引号可输出双引号"""""
print(str0, str1, str2)
# "\"转义字符
str3 = 'he say:\"hello world\"'
print(str3)

# List
list0 = ['abc', 123, 2.22, 'def', 53.6, 'ves']
print(list0)
print(list0[0])
print(list0[2:])
print(list0[0] + list0[-1])

# Tuple元组，内容不能修改
tuple0 = (23, 'we', 42, 'gw')
try:
    tuple0[0] = 32
except TypeError:
    print("元组不能修改")

# Dictionary无序的，列表（List,Tuple）是有序的
dictionary0 = {'name': 'Jc', 'age': 16}
print(dictionary0, dictionary0.keys(), dictionary0.values())

# Set集合(无序的不重复元素序列)
basket = {'apple', 'orange', 'apple', 'pear', 'orange'}
print(basket)

# 数据类型转换
b = int(2.3)
print(type(b), b)
