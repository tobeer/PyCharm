alien_0 = {'color': 'green', 'points': 5}  # 字典 键值对
print(alien_0['color'])
print(alien_0['points'])
alien_0['x_position'] = 0  # 字典 增加键值对
alien_0['y_position'] = 1
print(alien_0)


def move(alien):
    if alien['speed'] == 'slow':
        alien['x_position'] += 10
        alien['y_position'] += 10
    elif alien['speed'] == 'medium':
        alien['x_position'] += 20
        alien['y_position'] += 20
    elif alien['speed'] == 'fast':
        alien['x_position'] += 30
        alien['y_position'] += 30


alien_0['speed'] = 'medium'
move(alien_0)
print('中速' + str(alien_0))

alien_0['speed'] = 'slow'
move(alien_0)
print('低速' + str(alien_0))

del alien_0['color']  # 删除键值对
print(alien_0)
print(str(alien_0['speed']) +
      str(alien_0['x_position']) +
      str(alien_0['y_position']))

for key, value in alien_0.items():  # 遍历键值对
    print("\nkey:\t" + key)
    print("value:\t" + str(value))

favorite_language = {
    '张三': 'Python',
    '李四': 'C++',
    '王五': 'Java',
    '和二': 'Python'
}
friends = ['李四']
for name in favorite_language.keys():
    print(name)
    if name in friends:
        print('Hi ' + name + ', I see your favorite language is ' + favorite_language[name])

if '老六' not in favorite_language.keys():
    print('老六不在')

for language in favorite_language.values():
    print('排序前的语音' + language)
for language in sorted(favorite_language.values()):  # 排序后遍历
    print('排序后的语音' + language)
print("===================")

for language in set(favorite_language.values()):  # 使用set去重
    print('去重' + language)

aliens = []  # 在列表中存储字典
for i in range(3):
    aliens.append(alien_0)
print(aliens)

pizza = {  # 在字典中存储列表
    'crust': 'thick',
    'toppings': ['mushroom', 'extra cheese']
}
print("You ordered a " + pizza['crust'] + '-crusted pizza ' + 'with the following toppings:')
for topping in pizza['toppings']:
    print('\t' + topping)

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princetion'
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
    }
}
for username, user_info in users.items():
    print('\nUser name:\t' + username)
    full_name = user_info['first'] + ' ' + user_info['last']
    location = user_info['location']
    print('\tFull name:\t' + full_name)
    print('\tLocation:\t' + location)
