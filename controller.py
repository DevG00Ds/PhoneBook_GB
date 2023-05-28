import model, view
import os


def start():
    view.hello()
    while True:
        view.menu()
        sw = input(' Сделайте выш выбор ')
        os.system('cls')
        print()
        if sw == '1':
            data = model.all_cantacts()
            view.show_cantacts(data)
        elif sw == '2':
            cantacts = input('Введите абонента: ')
            data_number = model.all_cantacts(cantacts)
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
            cantacts = input('Введите данные абонента: ')
            new_data = model.new_cantacts(cantacts)
        elif sw == '4':
            model.edits_data()
        elif sw == '5':
            model.delete_cantakts()
        elif sw == '0':
            os.system('cls')
            print('Всего хорошего!')
            break
        else:
            view.error_func()
