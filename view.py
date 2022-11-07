def show_menu():
    menu = "Введите номер команды:\
    \n0. Открыть файл с контактами\
    \n1. Показать все контакты\
    \n2. Записать файл с контактами\
    \n3. Добавить контакт\
    \n4. Изменить контакт\
    \n5. Удалить контакт\
    \n6. Поиск по контактам\
    \n7. Pавершить работу.\
    \n: "
    command = input(menu)
    return command

def open_file(contacts: list):
    if len(contacts) == 0:
        print('Список контактов пуст')
    else:
        [print(contact) for contact in contacts]
    print()
    
def show_contacts(contacts: list):
    if len(contacts) == 0:
        print('Список контактов пуст')
    else:
        [print(contact) for contact in contacts]
    print()
    
def show_contact(contact: list):
    if (contact == None):
        print('Нет контакта для отображения\n')
    else:
        print(f'{contact}\n')
        return contact
    
def show_read_result(contacts: list):
    if len(contacts) == 0:
        print('Файл прочитан, записей контактов не содержит\n')
    else:
        print('Файл прочитан. Для отображения контактнов выберите соответствующий пункт в меню.')
    
def add_contact(contact: list):
    print("Новый контакт добавлен.")
    print(f'{contact}\n')
    
def write_file(result: bool):
    if result:
        print('Контакты успешно сохранены в файл\n')
    else:
        print('Ошибка сохрания\n')

def find_contact():
    name = input('Введите имя контакта для поиска: ')
    return name
    
def change_contact():
    name = input('Введите имя контакта для изменения: ')
    return name 

# def change_contact_name():
#     name = input('Введите новое имя: ')
#     return name 

def get_contact_del():
    name = input('Введите имя контакта для удаления: ')
    return name 

def del_contact(result: bool):
    if result:
        print('Контакт удален.')
    else:
        print('Выберите контакт для удаления. /n')
    