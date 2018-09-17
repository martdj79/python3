# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

# ------решение---------
# import random
# result = []
# result2 = []
# count = int(input('Введите количество ячеек в списке: '))
# rand_from = int(input('Введите нижнюю границу рандома: '))
# rand_to = int(input('Введите верхнюю границу рандома: '))
# result = [random.randint(rand_from,rand_to) for _ in range(count)]
# for index in result:
#     index2 = index ** 2
#     result2.append(index2)
# print(f'Исходный рандомный список {result}')
# print(f'Cписок квадратов исходного рандомного списка {result2}')
# print(f'Количество ячеек в списке {count}')


# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

# # ------решение_1---------
# fruits = ['яблоко','арбуз','апельсин','мардарин','киви']
# fruits2 = ['яблоко','арбуз','апельсин','мардарин','киви','помело','грейпфрут']
# fruits3 = [] #Список совпадающих фруктов
# fruits4 = [] #Список не совпадающих фруктов
# for item in fruits:
#     if item in fruits2:
#         fruits3.append(item)
#     else:
#         fruits4.append(item)
# for item in fruits2: # импровизвция(в задании этого нет) создаю список не совпадающих фруктов
#     if item not in fruits:
#         fruits4.append(item)
# print(f' Список совпадающих фруктов {fruits3}')
# print(f' Список не совпадающих фруктов {fruits4}')
#
# # ------решение_2--------
# fruits = ['яблоко','арбуз','апельсин','мардарин','киви']
# fruits2 = ['яблоко','арбуз','апельсин','мардарин','киви','помело','грейпфрут']
# fruits3 = list(set(fruits) & set(fruits2))
# print(f' Список совпадающих фруктов (решение2) {fruits3}')


# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
import random
list1 = []
list2 = []
list1 = [random.randint(-300,300) for _ in range(300)]
print(f' Исходный рандомный список {list1}')
for item in list1:
    if item > 0 and item % 3 == False and item % 4 == True:
        list2.append(item)
print(f' Полученный список чисел больше нуля, кратных 3 и не кратных 4 {list2}')



