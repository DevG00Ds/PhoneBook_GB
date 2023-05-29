def hello():
    print(' \nВы используете учебный телефонный справочник.'
          '\nДля работы со справочником выберите следуещие действия:\n')


def menu():
    print('\n- Просмотреть  справочник   - введите "1"'
          '\n- Поиск абонента            - введите "2"'
          '\n- Ввести  нового  абонента  - введите "3"'
          '\n- Изменить данные абонента  - введите "4"'
          '\n- Удалить данные абонента   - введите "5"'
          '\n- Закончить работу со справочником - введите "0"\n'
          )


def show_cantacts(data):
    return None


def error_func():
    print(' Вы ввели не верные данные.')


def add_new_cantacts(new_data):
    return None


def error_add_new_cantacts(new_data):
    return None


if __name__ == "__main__":
    hello()
    menu()
