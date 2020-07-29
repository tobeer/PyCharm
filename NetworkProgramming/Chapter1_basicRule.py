# Python字母区分大小写

# 变量赋值，变量在内存中创建，都包含变量的标识、名称、数据等信息
x = 1
print(id(x))  # x的标识符
x = 2
print(id(x))

a = (1, 2, 3)
(x, y, z) = a
print(x, y, z)  # 通过序列的定义与拆分，实现同时对多个变量的赋值

_a = 1  # 全局变量，在函数外定义
_b = 2


def add():
    global _a  # 引用全局变量,可对_a进行修改
    _a = 3
    _b = 4
    return "_a + _b= ", _a + _b


print(add())
print(_a)
print(_b)


def fun():
    f = 1  # 局部变量，只能在函数体内使用
    print(f)


try:
    y = f + 1
except NameError:
    print("f 未定义")


# Python没有常量的保留字，但可以定义一个常量类来实现常量的功能
class _const:  # 定义常量类const
    class ConstError(TypeError): pass

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError("Can't rebind const(%s)" % name)
        self.__dict__[name] = value


import sys

sys.modules[__name__] = _const

n = _const()
n.magic = 20
try:
    n.magic = 30
except TypeError:
    print("Can't modify a const value")
