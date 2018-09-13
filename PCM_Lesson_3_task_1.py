# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"

name = input('Enter your name: ')
age = input('Enter your age: ')
city = input('Enter your city: ')

def id_card():
    print(f'{name.title()} возраст: {age} ,проживает в городе: {city.title()}')
id_card()

# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них

# x = input('Enter the 1st number: ')
# y = input('Enter the 2nd number: ')
# z = input('Enter the 3rd number: ')
#
# def compare_numbers():
#     if x > (y and z):
#         print(x)
#     elif y > (x and z):
#         print(y)
#     elif z > (x and y):
#         print(z)
#     else:
#         print('Вы вводите равные числа')
# compare_numbers()


# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов

# def length_count(*args):
#     maxlength = 0
#     for data in args:
#         if len(data) > maxlength:
#             maxlength = len(data)
#             longest_data = data
#     print(longest_data)
#     print(maxlength)
#
# length_count('dfvdr', 'sdfsrvgsr','sfwrfs')


