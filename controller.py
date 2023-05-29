import model, view


def start():
    view.hello()
    while True:
        view.menu()
        sw = input(' Сделайте выш выбор :  ')
        if sw == '1':
            data = model.all_cantacts()
            view.show_cantacts(data)
        elif sw == '2':
            data_number = model.all_cantacts()
            while True:
                print(' \nНайти абонента по номеру - Введите "1"'
                      '\nНайти абонента по Ф.И.О - Введите "2"'
                      '\nПрекратить поиск - Введите "3"')
                number = int(input(" Введите число : "))
                if number == 1:
                    model.search_number(data_number)
                elif number == 2:
                    model.search_name(data_number)
                elif number == 3:
                    print(" Поиск завершен")
                    break
                else:
                    print(" Неккоректный ввод")
        elif sw == '3':
            ls = []
            num = int(input('Введите номер: '))
            ls.append(input('Введите фамилию: '))
            ls.append(input('Введите имя: '))
            ls.append(input('Введите отчество: '))
            new_data = model.new_cantacts(num, ls)
            if new_data:
                view.add_new_cantacts(new_data)
            else:
                view.error_add_new_cantacts(new_data)
        elif sw == '4':
            model.edits_data()
        elif sw == '5':
            model.delete_cantakts()
        elif sw == '0':
            print('Всего хорошего!')
            break
        else:
            view.error_func()
            break
