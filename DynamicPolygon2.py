import math
import numpy as np


class DynamicPolygon(object):
    def __init__(self, number_of_tops, rad=None, coordinates=None):
        self.number_of_tops = number_of_tops
        self.coords = []
        print("Багатокутник створено")
        if coordinates is not None and rad is None:
            self.__init_with_coords_(coordinates)

        elif rad is not None:
            self.__init_with_rad__(rad)

    def __init_with_coords_(self, coordinates):
        if len(coordinates) % 2 == 0:
            self.coords = coordinates
        else:
            print('Задана невірна кількість координатів.')

    def __init_with_rad__(self, rad):
        self.coords = []
        for i in range(1, self.number_of_tops + 1):
            angle = (360 / self.number_of_tops) * i
            self.coords.extend([round(rad * math.cos(angle * math.pi / 180), 2),
                                round(rad * math.sin(angle * math.pi / 180), 2)])
        print('Координати створеного багатокутника: ', self.coords)

    def read_coordinates(self, coords):
        if len(coords) % 2 == 0:
            self.coords.extend(coords)
            print('Координати успішно додано.')
        else:
            print('Задана невірна кількість координатів.')

    def polygon_area(self):
        x = []
        y = []
        for i in range(len(self.coords)):
            if i % 2 != 0:
                x.append(int(self.coords[i]))
            else:
                y.append(int(self.coords[i]))
        print(0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1))))

    def __del__(self):
        print('Багатокутник видалено.')

    @staticmethod
    def entering_tops():
        while 1:
            try:
                n = int(input('Введіть кількість вершин і натисніть Enter: '))
                if n > 2:
                    return n
                else:
                    print('Введіть число більше за 2!')
            except ValueError:
                print('Введіть число!')

    @staticmethod
    def entering_coords(n):
        while 1:
            coords = input('Введіть координати через кому, наприклад 1, 3, 2, 4 (де перше число Х,'
                           ' а друге Y, і так далі...)').replace(' ', '').split(',')
            if len(coords) % 2 != 0 or len(coords) / 2 != n:
                print('Введена неправильна кількість аргументів!')
                continue
            for i in coords:
                try:
                    int(i)
                except ValueError:
                    print('Введіть цифри!')
                    continue
            return coords
