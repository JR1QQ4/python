print("Hello, world!\n")

# 一.变量和简单数据类型
print('\n*************** 一.变量和简单数据类型 ***************\n')

# 1.字符串
print("\n======= String =======\n")

name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "ada"
last_name= "lovelace"
full_name = first_name + " " + last_name
print("Hello, " + full_name.title() + "!")

print("Languages:\n\tPython\n\tC\n\tJavaScript")

favorite_language = ' python '
print(favorite_language.rstrip())
print(favorite_language.lstrip())
favorite_language = favorite_language.strip()
print(favorite_language)

# 2.数字
print("\n======= Number =======\n")

add_num = 2 + 3
sub_num = 3 - 2
mul_num = 2 * 3
div_num = 3 / 2
mod_num = 4 % 3
exp_num = 3 ** 2
float_num = 0.1 + 0.2
print(add_num, sub_num, mul_num, div_num, mod_num, exp_num, float_num)
age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)

# 二.列表
print('\n*************** 二.列表 ***************\n')

# 1.列表
print("\n======= List =======\n")

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0], bicycles[0].title(), bicycles[1], bicycles[-1])

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('honda')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')
print(motorcycles)

motorcycles = ['h', 'y', 's', 'd']
print(motorcycles)
too_expensive = 'd'
motorcycles.remove(too_expensive)
print(motorcycles)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted lost:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

cars.reverse()
print(cars)
print("The length of the list is " + str(len(cars)) + '.')

# 2.操作列表
print("\n======= 操作列表 =======\n")

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
print("Thank you, everyone. That was a great magic show!")

numbers = list(range(1, 6))
print(numbers)
even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)
print(squares)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits), max(digits), sum(digits))

squares = [value**2 for value in range(1, 11)]
print(squares)

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

# 3.元组
print('\n======= Tuple =======\n')

dimensions = (200, 50)
print(dimensions[0], dimensions[1])
# dimensions[0] = 250  # tuple object does not support item assignment

print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

# 三.if语句
print("\n*************** 三.if语句 ***************\n")

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)
age_1 = 22
print(age_0 >= 21 and age_1 >= 21)
age_0 = 18
print(age_0 >= 21 or age_1 >= 21)

requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)
print('pepperoni' not in requested_toppings)

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10
print("Your admission cost is $" + str(price) + ".")

# 四.字典
print("\n*************** 四.字典 ***************\n")

alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0['color'] = 'yellow'
print(alien_0)

del alien_0['points']
print(alien_0)

user_0 = {'username': 'efermi', 'first': 'enrico', 'last': 'fermi'}
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

print()
for key in user_0.keys():
    print(key.title())

print()
for key in sorted(user_0.keys()):
    print(key.title())

print()
for value in user_0.values():
    print(value.title())

print()
for value in set(user_0.values()):
    print(value.title())

print()
aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[:5]:
    print(alien)
print("...")
print("Total number of aliens: " + str(len(aliens)))

# 五.用户输入和while循环
print("\n*************** 五.input与while ***************\n")

print("\n======= input =======\n")
# message = input("Tell me something, and I will repeat it back to you:")
# print(message)

print("\n======= while =======\n")
current_number = 1
while current_number <= 5:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
print("\nThe following users have confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user)

# 六.函数
print("\n***************** 六.函数 ****************\n")
def greet_user(username):
    """显示简单的问候语"""
    print("Hello, " + username.title() + "!")
greet_user('jesse')

def describe_pet(pet_name, animal_type='dog'):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
# describe_pet("hamster", "harry")
# describe_pet("dog","willie")
describe_pet(pet_name='harry', animal_type="hamster")

def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

def make_pizza(size, *toppings):
    """打印顾客点的所有配料"""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print('- ' + topping)
make_pizza(16, 'popperoni')
make_pizza(12, "mushrooms", "greenpeppers", "extra cheese")

def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('albert', 'einstenin', location='princeton', field='physics')
print(user_profile)

# 模块
print('\n======= 模块 =======\n')
# import module_name
# from module_name import function_name
# from module_name import function_name as fn
# import module_name as mn
# from module_name impory *

# 七.类
print("\n*************** 七,类 ***************\n")

class Dog():
    """一次模拟小狗的简单尝试"""
    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age
    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")
    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")
my_dog = Dog('willine', 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())

# 八.文件和异常
print("\n*************** 八.文件和异常 ***************\n")

try:
    filename = 'pi_digits.txt'
    with open(filename) as file_object:
        lines = file_object.readlines()
        for line in lines:
            print(line.rstrip())
except:
    print("Read file error!")

filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I lobe programming.")
    file_object.write("I love creating new games.")









