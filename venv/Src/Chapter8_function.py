def greet_user0():  # 无参函数
    print("Hello!")


greet_user0()


def greet_user1(username):  # 有参函数
    print("Hello! " + username + "!")


greet_user1('Jerry')
greet_user1(username='Arf')  # 关键字实参，避免因参数位置引起的混淆


def pet(pet_name, pet_type="dog"):  # 默认值
    print("\nI have a " + pet_type + "!")
    print("My " + pet_type + "'s name is " + pet_name + "!")


pet("Iron")
pet("Nancy", "cat")


def name(first_name, last_name, middle_name=""):  # 返回值return
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()


print(name("jack", "l"))
print(name("jack", "l", "k"))


def build_person(first_name, last_name, age=''):  # 返回字典
    person = {'firstName': first_name, 'lastName': last_name}
    if age:
        person['age'] = age
    return person


person1 = build_person("P1", "L1")
person2 = build_person("P2", "L2", "20")
print(person1, person2)


def greet_users(names):  # 传递列表
    for nam in names:
        print("Hello! " + nam)


usernames = ['张三', '李四', '王五']
greet_users(usernames)


def print_models(unprinted_models, completed_models):  # 在函数中修改列表
    while unprinted_models:
        print_model = unprinted_models.pop()
        completed_models.append(print_model)
        print("print_model " + print_model)
    print("completed_models " + str(completed_models))


unprintedModels = ["L1", "L2", "L3"]
completedModels = []
print_models(unprintedModels, completedModels)
print(unprintedModels)

unprintedModels = ["L1", "L2", "L3"]
completedModels = []
print_models(unprintedModels[:], completedModels)  # 禁止函数修改列表
print(unprintedModels)


def make_pizza1(*toppings):  # 传递任意数量的参数
    print(toppings)


make_pizza1("pepperoni")
make_pizza1("mushroom", "green peppers", "extra cheese")


def make_pizza2(size, *toppings):  # 结合使用位置实参和任意数量的实参
    print("Making a " + str(size) + "-inch pizza with following toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza2(8, "pepperoni")
make_pizza2(10, "green peppers", "extra cheese")


def build_profile(first, last, **user_info):  # 使用任意数量的关键字实参，**代表创建空字典，将所有输入的键值对传入其中
    profile = {"firstName": first, "lastName": last}
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile("albert", "einstein", location="princeton", field="physics")
print(user_profile)
