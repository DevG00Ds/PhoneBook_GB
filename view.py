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


def show_contacts(data):
    for num in data.keys():
        print(f'№ {num}. Владелец -', data[num])


def error_func():
    print(' Вы ввели не верные данные.')


def add_new_contacts(new_data):
    print('Новый контакт добавлен')
    print(new_data)


def error_add_new_contacts(new_data):
    print('Новый контакт не добавлен')


if __name__ == "__main__":
    hello()
    menu()
    error_func()
