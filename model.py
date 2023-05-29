def overwritingData():
    with open(path_file, 'w', encoding='UTF-8') as f:
        for key, value in data_number.items():
            f.write(str(key) + str(value).replace("[", " ").replace("]", "").replace(",", "").replace("'", "") + '\n')


def all_contacts():
    with open(path_file, 'r', encoding='UTF-8') as f:
        for line in f:
           data_number[line[:11]]=line[11:].strip()
    return data_number


def search_number(data_number):
    num = input('Введите номер абонента для поиска: ')
    print(f'\n№ {num}. Владелец - {data_number[num]}')
#    return None


def search_name(data_number):
    fam = input('Введите фамилию для поииска: ')
    for num in data_number:
        if fam in data_number[num]:
            print(data_number[num], f'имеет номер {num}')
            break
    else:
        print('Такой фамилии нет')        
#    print(f'\n№ {num}. Владелец - {data_number[num]}')
#    return None


def new_contacts(num, ls):
    if (not data_number):
        all_contacts()
    data_number[num] = ls
    print(num, f' ', data_number[num])
    overwritingData()
    return data_number[num]


def edits_data(num, ls):
    if (not data_number):
        all_contacts()
    numdell = input('Введите номер контакта для редактирования: ')
    print(f'\n№ {numdell}. Владелец - {data_number[numdell]}')
    data_number.pop(numdell)
    data_number[num] = ls
    print(f'\n№ {num}. Владелец -', *data_number[num])
    overwritingData()


def delete_contakts(num): # num = input('Введите номер контакта для удаления: ') (Добавь в controller)
    if (not data_number):
        all_contacts()
    keys = data_number.keys()
    if (num in keys):
        data_number.pop(num)
        overwritingData()
        return print("Запись успешно удалена")
    else:
        return print("Такого контакта нет")


global data_number
data_number = {}
path_file = r'D:\GB\2023.04.05-Python\PhoneBook\PhoneBook_GB\TelephoneBook.txt'