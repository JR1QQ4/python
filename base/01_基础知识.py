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
exp_num = 3 ** 2
float_num = 0.1 + 0.2
print(add_num, sub_num, mul_num, div_num, exp_num, float_num)
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






























































