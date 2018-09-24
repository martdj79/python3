# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        self.go = self.speed > 0
    def stop(self):
        self.go = self.speed = 0
    def turn(self, direction):
        if direction == 'left':
            print('Turned Left')
        if direction == 'right':
            print('Turned Right')
Towncar = Car(60,'white','Renault',False)
SportCar = Car(180,'red','Ferrarri',False)
WorkCar = Car(50,'Grey','Man',False)
PoliceCar = Car(160, 'Blue','BMW',True)
print(Towncar.speed)
print(PoliceCar.color)
print(WorkCar.color)
print(SportCar.name)
Towncar.stop()
Towncar.turn('right')
print(Towncar.speed)
print(Towncar.turn)

class HybridCar(Car):
    def __init__(self, speed, color, name, is_police, battery_capacity):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.batterry_capacity = batterry_capacity
    def go(self):
        self.go = self.speed > 0
    def stop(self):
        self.go = self.speed = 0
    def turn(self, direction):
        if direction == 'left':
            print('Turned Left')
        if direction == 'right':
            print('Turned Right')
    def batterry_charge(self):
        self.batterry_charge = self.batterry_capacity > 0
hybrid1 = HybridCar(90,'red','Chevrolet_Volt',False, 100)


