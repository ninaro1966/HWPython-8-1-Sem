import controller

phone_book = []
path = 'HelloPython/data/'

def get_phone_book():
    global phone_book
    return phone_book

def set_path(file):
    global path
    path += file

def open_file():
    global path
    global phone_book
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for item in data:
        contact = item.replace('\n', '').split(';')
        phone_book.append(contact)

def new_contact(contact):
    global phone_book
    phone_book.append(list(contact))

def change_contact(id, choise, value):
    global phone_book
    phone_book[int(id)][int(choise)] = value