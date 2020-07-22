from Chapter9_class import Car, ElectircCar  # 从一个模块中导入多个类
from collections import OrderedDict

my_new_car = Car('audi', 'a8', 2020)
print(my_new_car.get_descriptive_name())
my_new_car.mileage = 20
my_new_car.show_mileage()

my_new_electricCar = ElectircCar('tesla', 'model s', 2020)
print(my_new_electricCar.get_descriptive_name())

favorite_language = OrderedDict()  # 记录键值对的添加顺序
favorite_language['jen'] = 'python'
favorite_language['sarah'] = 'c'
favorite_language['edward'] = 'ruby'
favorite_language['phil'] = 'python'

for name, language in favorite_language.items():
    print(name.title() + "'s favorite language is " + language.title())
