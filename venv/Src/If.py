cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
x1 = cars[0] == 'audi'  # python 区分大小写
x2 = cars[0] == 'Audi'
x3 = cars[0].title() == 'Audi'
print(x1, x2, x3)
if 12 > 11 and 13 < 12:  # if 与/或关系用and/or
    print('wrong')
else:
    print('true')
if 12 > 11 or 13 < 12:
    print('wrong')
else:
    print('true')

if 'audi' in cars:  # 检查特定值是否包含在列表中
    print('audi在列表中')
else:
    print('audi不在列表总')

age = 67
if age < 7:
    print('小屁孩')
elif 7 <= age < 13:
    print('小孩')
elif 13 <= age < 17:
    print('少年')
else:
    print('成年人')

emptyList = []
if emptyList:  # list不为空返回true
    print('列表不为空')
else:
    print('列表为空')

requested_cars = ['audi', 'phaton']
for requested_car in requested_cars:
    if requested_car in cars:
        print('有', requested_car)
    else:
        print('没有' + requested_car)
print('谢谢惠顾')
