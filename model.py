path = "book.txt"
contacts = []
currentContact = []

def read_file():
    global contacts
    with open (path, 'r') as data:
        contacts = [i.strip().split(';') for i in data.readlines()]
    return contacts

def get_contacts():
    global contacts
    return contacts

def save_file():
    global contacts
    try:
        with open(path, 'w', encoding='utf_8') as f:
            for contact in contacts:
                f.write(';'.join(contact) + "\n")
    except:
        return False            
    return True
        
def add_contact():
    global contacts
    contact = [input('Введите Имя: '),\
        input('Введите Телефон: '),\
        input('Введите Комментарий: ')]
    contacts.append(contact)
    return contact

def find_contact_name(name: str):
    global contacts
    for i in range(len(contacts)):
        if contacts[i][0] == name:
            return contacts[i]
    return None

def change_contact_name(name: str):
    global contacts
    global currentContact
    for i in range(len(contacts)):
        if contacts[i][0] == name:
            currentContact = contacts[i]
            select = "1 - изменить ИМЯ\
            \n2 - изменить ТЕЛЕФОН\
            \n3 - изменить КОММЕНТАРИЙёё\
            \n: "  
            command = input(select)
            match command:
                case '1':
                    currentContact[0] = input('Введите новое ИМЯ: ')
                case '2':
                    currentContact[1] = input('Введите номер ТЕЛЕФОНА: ')
                case '3':
                    currentContact[2] = input('Введите новый КОММЕНТАРИЙ: ')
    return currentContact

def delete_contact(name: str):
    global contacts
    for i in range(len(contacts)):
        if contacts[i][0] == name:
            contacts.pop(i)
    return True