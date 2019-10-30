import math


class Equation(object):
    def __init__(self):
        self.number_of_roots = 0
        self.solutions = []

    def read_roots(self, a, b, c=None):
        equation_type = 'Linear' if c is None else 'Quad'
        if equation_type == 'Linear':
            return f'({a}x) + ({b}) = 0\nx = {self.solutions[0]}'
        elif equation_type == 'Quad':
            print(f'({a}x^2) + ({b}x) + ({c}) = 0')
            if type(self.solutions[0]) is str:
                return 'Рівняння немає коренів.'
            else:
                for n, i in enumerate(self.solutions):
                    return f'X{n + 1} = {i}'


class LinearEquation(Equation):
    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b

    def roots(self):  # ax + b = 0
        if self.a == 0 and self.b == 0:
            self.solutions.append(0)
        elif self.a == 0 and self.b != 0:
            self.solutions = 'Рівняння немає коренів!'
        else:
            self.solutions.append((self.b * -1) / self.a)
        return self.read_roots(self.a, self.b)


class QuadEquation(Equation):
    def __init__(self, a, b, c):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c
        self.d = self.calculate_discriminator()

    def calculate_discriminator(self):
        return self.b ** 2 - 4 * self.a * self.c

    def roots(self):
        if self.a == 0:
            if self.b == 0 or self.c == 0:
                self.solutions.append(0)
            elif self.b == 0 and self.c != 0:
                self.solutions = 'Рівняння немає коренів!'
            else:
                self.solutions.append((self.c * -1) / self.b)
        elif self.d == 0:
            self.solutions.append((-self.b * -1 + math.sqrt(self.d)) / (2 * self.a))

        elif self.d < 0:
            self.solutions = 'Рівняння немає коренів!'

        else:
            self.solutions.extend([(-self.b + math.sqrt(self.d)) / (2 * self.a),
                                 (-self.b - math.sqrt(self.d)) / (2 * self.a)])
        return self.read_roots(self.a, self.b, self.c)
