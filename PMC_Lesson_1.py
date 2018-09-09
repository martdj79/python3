#easy
# num = int(input('введите число: '))
# print (num + 2)
#
#
# age = int(input('Введите Ваш Возраст: '))
# if age >= 18:
#     print('Wellcome!')
# else:
#     print('Your entry is not allowed')

#normal
# num2 = int(input('Введите число: '))
# while num2 > 10 or num2 < 0:
#     num2 = int(input('Введите число от 0 до 10: '))
# else:
#     num3 = num2 ** 2
#     print('Вы ввели', num2, 'В квадрает это', num3)

#normal 2 (сам не догадался ;(, списано в интернете)

num1 = int(input('Введите число A: '))
num2 = int(input('Введите число B: '))
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2
print('Число А:', num1,)
print('Число B:', num2,)



#hard
name = input('Ваше имя?: ')
surname = input('Ваша Фамилия: ')
age = int(input('Ваш Возраст: '))
weight = int(input('Ваш вес: '))
if age < 30 and weight > 50 and weight < 120:
    print(name, surname,'Возраст:', age, 'Вес:', weight, 'Вы В хорошей форме')
elif age > 30 and age < 40 and weight < 50 or weight > 120:
     print(name, surname,'Возраст:', age, 'Вес:', weight, 'Вам необходимо начать вести здоровый образ жизни')
elif age > 40 and weight < 50 or weight > 120:
     print(name, surname,'Возраст:', age, 'Вес:', weight, 'Вам необходимо обратиться к врачу')
else:
    print(name, surname,'Возраст:', age, 'Вес:', weight, 'Похоже Вы мутант')