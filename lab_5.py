import readchar
from Equation5 import LinearEquation, QuadEquation

if __name__ == '__main__':
    print('/-------------------------------------------\\\n'
          '|Калькулятор лінійних та квадратних ріванянь|\n'
          '|-------------------------------------------|\n'
          '|                  Функції                  |\n'
          '|1. Розв\'язати рівняння типу ax±b=0         |\n'
          '|2. Розв\'язати рівняння типу a^х2±bx±c=0    |\n'
          '|e - Закрити програму                       |\n'
          '|___________________________________________|')
    while 1:
        command = repr(readchar.readchar()).replace('\'', '')
        if command == 'e':
            break
        elif command == '1':
            print('Вводіть значення a, b натискаючи Enter')
            while 1:
                try:
                    a = int(input())
                    break
                except ValueError:
                    print('Введіть число!')
            while 1:
                try:
                    b = int(input())
                    break
                except ValueError:
                    print('Введіть число!')

            equation = LinearEquation(a, b)
            print(equation.roots())

        elif command == '2':
            print('Вводіть значення a, b, c натискаючи Enter')
            while 1:
                try:
                    a = int(input())
                    break
                except ValueError:
                    print('Введіть число!')
            while 1:
                try:
                    b = int(input())
                    break
                except ValueError:
                    print('Введіть число!')
            while 1:
                try:
                    c = int(input())
                    break
                except ValueError:
                    print('Введіть число!')

            equation = QuadEquation(a, b, c)
            print(equation.roots())

