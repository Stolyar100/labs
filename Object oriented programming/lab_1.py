import readchar
from Iron import Iron

if __name__ == '__main__':
    print('______________________________________________\n'
          '|-----Об\'єктно орієнтована модель праски-----|\n'
          '|--------------------------------------------|\n'
          '|-----------Виберіть одну з опцій------------|\n'
          '|1. Ввімкнути праску                         |\n'
          '|2. Вимкнути праску                          |\n'
          '|3. Набір води в паровик                     |\n'
          '|4. Змінити режим роботи                     |\n'
          '|5. Зробити паровий удар                     |\n'
          '|e - закрити програму                        |\n'
          '|____________________________________________|')
    tefal = Iron()

    while 1:
        command = repr(readchar.readchar())
        # print(type(a))
        if command == '\'e\'':
            break
        elif command == '\'1\'':
            tefal.power_on()
        elif command == '\'2\'':
            tefal.power_off()
        elif command == '\'3\'':
            tefal.fill_water()
        elif command == '\'4\'':
            print('Доступні режими:\n'
                  '1 - температура 100 градусів\n'
                  '2 - температура 150 градусів\n'
                  '3 - температура 200 градусів\n')
            print('Виберіть режим:')
            while 1:
                try:
                    mode = int(repr(readchar.readchar()).replace('\'', ''))
                    if 1 <= mode <= 3:
                        break
                    else:
                        print('Вкажіть один з цих режимів роботи: 1, 2, 3!')

                except ValueError:
                    print('Введіть число!')

            tefal.change_mode(mode)
        elif command == '\'5\'':
            tefal.water_blow()
