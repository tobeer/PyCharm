import Chapter8_function  # 引入文件中全部函数

Chapter8_function.greet_user0()

from Chapter8_function import greet_user0, greet_users  # 引入文件中特定函数

greet_user0()
greet_users(['张三', '李四', '王五'])

import Chapter8_function as C8  # 使用as给模块指定别名

C8.greet_user0()

from Chapter8_function import greet_user0 as greet  # 使用as给函数指定别名

greet()

from Chapter8_function import *  # 导入模块中所有函数, 不建议使用容易出现同名函数覆盖, 尽量使用文件名+'.'或导入特定函数

make_pizza1("pepperoni")
