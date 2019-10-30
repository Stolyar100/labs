import math


class Iron(object):
    def __init__(self):   # конструктор ініціалізації
        self.power = False
        self.mode = 1
        self.filling = 0
        self.temperature = 10

    # def __init__(self, power=False, mode=1, filling=0, temperature=10):  # конструктор за замовчуванням
    #     self.power = power
    #     self.mode = mode
    #     self.filling = filling
    #     self.temperature = temperature

    def power_on(self):
        if self.power:
            print('Праска уже ввімкнена!')
            return
        self.power = True
        self.__need_time__()
        self.temperature = self.__need_temperature__()
        print(f'Праску ввімкнено і розігріто до {self.temperature} градусів.')

    def power_off(self):
        if not self.power:
            print('Праска ітак вимкнена!')
            return
        self.power = False
        self.temperature = 20
        print(f'Праску вимкнено (температура 10 градусів)')

    def fill_water(self):
        if not self.power:
            if self.filling < 200:
                self.filling = 200
                print('Праску успішно наповнено.')
            else:
                print('Праска повна!')
        else:
            print('Не можна наповнювати ввімкнену праску!')

    def change_mode(self, mode):
        self.mode = mode
        print(f'Режим праски змінено на {mode}')
        if self.power:
            self.__need_time__()

    def water_blow(self):
        if self.power:
            if self.mode == 1 and self.filling >= 5:
                self.filling -= 5
                print(f'Зроблено паровий удар, у прасці залишилось {self.filling} грам води.')
            elif self.mode == 2 and self.filling >= 7.5:
                self.filling -= 7.5
                print(f'Зроблено паровий удар, у прасці залишилось {self.filling} грам води.')
            elif self.mode == 3 and self.filling >= 10:
                self.filling -= 10
                print(f'Зроблено паровий удар, у прасці залишилось {self.filling} грам води.')
            else:
                print('У прасці недостатньо води, наповніть її для здійснення парового удару!')
        else:
            print('Паровий удар можливий тільки при ввімкненій прасці!')

    def __need_temperature__(self):
        if self.mode == 1:
            return 100
        elif self.mode == 2:
            return 150
        else:
            return 200

    def __need_time__(self):
        time = math.fabs(self.__need_temperature__() - self.temperature) / 2
        print(f'Час нагріву від {self.temperature} до {self.__need_temperature__()} градусів: {int(time)} c.')
