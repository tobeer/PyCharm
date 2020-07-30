def func0():  # 循环
    s = 1
    n = 1
    while n < 7:
        s *= n
        n += 1
    return s


print(func0())


def func1(n):  # 递归
    if n == 1:
        return 1
    return n * func1(n - 1)


print(func1(6))

# Lambda函数，不需要def就能定义的函数，即匿名函数
fun2 = lambda a, b: a * b
x = fun2(2, 3)
print(x)


# Generator函数(生成器)，在函数内使用yield
def func3(n):
    for i in range(n):
        yield i  # 返回多次，占用内存少


for f in func3(5):
    print(f)
m = func3(5)
print(m.__next__())
print(m.__next__())
print(m.__next__())
print(m.__next__())
print(m.__next__())

# 使用help()查看函数的参数说明
help(sorted)
