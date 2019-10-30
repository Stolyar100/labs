import readchar
from DynamicPolygon2 import DynamicPolygon

if __name__ == '__main__':
    print('/---------------------------------------------------\\\n'
          'Об\'єктно орієнтована модель динамічного багатокутника\n'
          '|---------------------------------------------------|\n'
          '|--------------------Інструкції---------------------|\n'
          '|1 - Створити новий багатокутник                    |\n'
          '|2 - Обрахувати площу створеного багатокутника      |\n'
          '|3 - Додати координати для свореного багатокутника  |\n'
          '|4 - Видалити створений багатокутник                |\n'
          '|5 - Переглянути координати створеного багатокутника|\n'
          '|___________________________________________________|\n')

    while 1:
        command = repr(readchar.readchar()).replace('\'', '')
        if command == 'e' or command == 'у':
            break

        elif command == '1':
            try:
                polygon.number_of_tops
                print('Ви впевнені що хочете видалити старий многокутник і створити новий? (так - y, ні - n)')
                while 1:
                    sure = repr(readchar.readchar()).replace('\'', '')
                    if sure == 'n':
                        print('Створення багатокутника скасовано')
                        stop = 1
                        break

                    elif sure in ['y', 'у']:
                        stop = 0
                        break
                    else:
                        print('так - y, ні - n')
                if stop:
                    continue
            except NameError:
                pass

            while 1:
                print('Як ви хочете створити багатокутник?\n'
                      '1. З кількістю вершин без їх координат.\n'
                      '2. З кількістю вершин та їх координатами.\n'
                      '3. З кількістю вершин та радіусом описаного навколо багатокутника кола\n'
                      '4. Скасувати\n')
                second_command = repr(readchar.readchar()).replace('\'', '')
                if second_command == '1':
                    n = DynamicPolygon.entering_tops()
                    polygon = DynamicPolygon(n)
                    break
                elif second_command == '2':
                    n = DynamicPolygon.entering_tops()
                    coords = DynamicPolygon.entering_coords(n)
                    polygon = DynamicPolygon(n, coordinates=coords)
                    break
                elif second_command == '3':
                    n = DynamicPolygon.entering_tops()
                    while 1:
                        try:
                            r = int(input('Введіть радіус: '))
                        except ValueError:
                            print('Введіть число!')
                            continue
                        if r < 0:
                            print('Введіть додатнє значення!')
                            continue
                        break
                    polygon = DynamicPolygon(n, rad=r)
                    break
                elif second_command == '4':
                    print('Дію скасовано.')
                    break
                else:
                    print('Виберіть один з заданих вище варіантів!\n\n')

        elif command == '2':
            try:
                if polygon.coords:
                    polygon.polygon_area()
                else:
                    print('Створений багатокутник немає координат!')
            except NameError:
                print('Для початку створіть багатокутник!')

        elif command == '3':
            try:
                if not polygon.coords:
                    polygon.read_coordinates(DynamicPolygon.entering_coords(polygon.number_of_tops))
                else:
                    print('У багатокутника вже є координати, щоб створити новий натисніть 1.')
            except NameError:
                print('Для початку створіть багатокутник!')

        elif command == '4':
            try:
                del polygon
            except NameError:
                print('Нема що видаляти!')

        elif command == '5':
            try:
                if polygon.coords:
                    print('Координати створеного багатокутника:')
                    print(polygon.coords)
                else:
                    print('Ви не заповнювали координати!')
            except NameError:
                print('Немає створеного багатокутника!')

