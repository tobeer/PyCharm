class Dog:
    def __init__(self, name, age):
        # 初始化属性name和age
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " rolled over.")


dog1 = Dog("teddy", 6)
print("My dog name is " + dog1.name.title())
print("My dog is " + str(dog1.age) + " years old")
dog1.sit()
dog1.roll_over()
dog1.sex = 'male'  # 动态性
print(dog1.sex)


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = 0  # 给属性指定默认值

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def show_mileage(self):
        print("This car has " + str(self.mileage) + " miles on it.")

    def update_mileage(self, mileage):
        if mileage > self.mileage:
            self.mileage = mileage
        else:
            print("You cannot roll back an odometer!")

    def increase_mileage(self, mileage):
        self.mileage += mileage

    def fill_gas_tank(self):
        print("正在加油！")


class Battery:
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kwh battery")

    def get_range(self):
        if self.battery_size == 70:
            rang = 240
        elif self.battery_size == 85:
            rang = 270
        else:
            rang = 0
        message = "This car can go approximately " + str(rang)
        message += " miles on a full charge."
        print(message)


class ElectircCar(Car):  # 继承
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70
        self.battery = Battery()  # 将实例用作属性

    def fill_gas_tank(self):  # 重写父类方法
        print("This car doesn't need a gas tank!")


car1 = Car('German', 'x', 3)
print(car1.get_descriptive_name())
car1.show_mileage()
car1.mileage = 20  # 直接修改属性值
car1.show_mileage()
car1.update_mileage(30)  # 通过方法修改属性值
car1.show_mileage()
car1.update_mileage(10)
car1.increase_mileage(10)  # 通过方法对属性的值进行增加
car1.show_mileage()

electricCar1 = ElectircCar('tesla', 's', 2)
my_tesla = electricCar1.get_descriptive_name()
print(my_tesla)
electricCar1.battery.describe_battery()
electricCar1.fill_gas_tank()
electricCar1.battery.get_range()
