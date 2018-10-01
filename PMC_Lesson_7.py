import random
# def card_gen():
#     rand_index = random.sample(range(0,10), 4) #генератор рандомного индекса
#     rand_index2 = random.sample(range(0,10), 4)
#     rand_index3 = random.sample(range(0,10), 4)
#     list1 = random.sample(range(1,90), 15) #генератор чисел от 1 до 90
#     line1 = sorted(list1[0:5])
#     line2 = sorted(list1[5:10])
#     line3 = sorted(list1[10:15])
#     space = ' '
#     for a in rand_index:
#          line1.insert(a,space)
#     for a in rand_index2:
#          line2.insert(a,space)
#     for a in rand_index3:
#          line3.insert(a,space)
#     line1 = str(line1)
#     print('----------------------------------------')
#     print(line1)
#     print(line2)
#     print(line3)
#     print('----------------------------------------')
answer = ''
while answer != 'n':
    answer = input('Играем в лото? (y/n) \n'
                   'y -Да! \n'
                    'n - Выход \n'
                   'Ваш ответ: ')
    if answer == 'y':
        print('Ваша карточка')
        rand_index = random.sample(range(0,10), 4) #генератор рандомного индекса
        rand_index2 = random.sample(range(0,10), 4)
        rand_index3 = random.sample(range(0,10), 4)
        list1 = random.sample(range(1,90), 15) #генератор чисел от 1 до 90
        line1 = sorted(list1[0:5])
        line2 = sorted(list1[5:10])
        line3 = sorted(list1[10:15])
        space = ' '
        for a in rand_index:
            line1.insert(a,space)
        for a in rand_index2:
            line2.insert(a,space)
        for a in rand_index3:
            line3.insert(a,space)
        print('----------------------------------------')
        print(line1)
        print(line2)
        print(line3)
        print('----------------------------------------')
        print('Карточка компьютера')
        rand_index1_1 = random.sample(range(0, 10), 4)  # генератор рандомного индекса
        rand_index2_1 = random.sample(range(0, 10), 4)
        rand_index3_1 = random.sample(range(0, 10), 4)
        list1_1 = random.sample(range(1, 90), 15)  # генератор чисел от 1 до 90
        line1_1 = sorted(list1_1[0:5])
        line2_1 = sorted(list1_1[5:10])
        line3_1 = sorted(list1_1[10:15])
        space = ' '
        for a in rand_index:
            line1_1.insert(a, space)
        for a in rand_index2:
            line2_1.insert(a, space)
        for a in rand_index3:
            line3_1.insert(a, space)
        print('----------------------------------------')
        print(line1_1)
        print(line2_1)
        print(line3_1)
        print('----------------------------------------')
        bocho_hod = random.sample(range(0, 90), 90)
        print(f' Бочонок номер: {bocho_hod[0]}')
        for x in list1:
            z = 0
            if bocho_hod[z] == x:
                answer2 = input('Да - \n'
                      'Нет q \n'
                      'Зачеркнуть число?: ')
                if answer2 == '-':
                    list1.remove(x)
                z = z + 1
                print(list1)
            else:
                continue



