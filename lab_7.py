import readchar
from Iron7 import Iron, OnIronException

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
        if command == '\'e\'':
            break
        elif command == '\'1\'':
            tefal == True
        elif command == '\'2\'':
            tefal == False
        elif command == '\'3\'':
            try:
                if not tefal.is_full():
                    while 1:
                        try:
                            second_command = int(input('Скільки води ви хочете залити у паровик? '
                                                       '(Введіть число і натисніть Enter)\n'))
                            if second_command < 0:
                                print('Введіть число більше за 0!')
                            else:
                                break
                        except TypeError:
                            print('Введіть число!')
                    tefal += second_command
                else:
                    print('Праска повна!')
            except OnIronException as ex:  # Перехоплення помилки про ввімкнену праску
                print(ex.text)

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

            tefal << mode
        elif command == '\'5\'':
            tefal -= 1
