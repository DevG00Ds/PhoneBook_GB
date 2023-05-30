import model, view


def start():
    view.hello()
    while True:
        view.menu()
        sw = input(' Сделайте выш выбор :  ')
        if sw == '1':
            view.show_contacts(model.all_contacts())
        elif sw == '2':
            data_number = model.all_contacts()
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
            num = int(input('Введите номер телефона: '))
            ls.append(input('Введите фамилию: '))
            ls.append(input('Введите имя: '))
            ls.append(input('Введите отчество: '))
            new_data = model.new_contacts(num, ls)
            if new_data:
                view.add_new_contacts(new_data)
            else:
                view.error_add_new_contacts(new_data)
        elif sw == '4':
            numdell = input('Введите номер контакта для редактирования: ')
            ls = []
            num = int(input('Введите новый номер: '))
            ls.append(input('Введите фамилию: '))
            ls.append(input('Введите имя: '))
            ls.append(input('Введите отчество: '))
            model.edits_data(num, ls, numdell)
        elif sw == '5':
            num = input('Введите номер контакта для удаления: ')
            model.delete_contakts(num)
        elif sw == '0':
            print('Всего хорошего!')
            break
        else:
            view.error_func()
            break
