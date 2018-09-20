# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.


# import os
# i = 1
# while i < 10:
#     mypath = (os.getcwd() + '/dir_'+ str(i))
#     os.mkdir(mypath)
#     i = i + 1


# И второй скрипт, удаляющий эти папки.


import os
i = 1
while i < 10:
    try:
        mypath = (os.getcwd() + '/dir_'+ str(i))
        os.rmdir(mypath)
        i = i + 1
    except FileNotFoundError:
        print('Несуществующий путь')
        break


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


# import os
# mypath = os.getcwd()
# print(os.listdir(mypath))

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

