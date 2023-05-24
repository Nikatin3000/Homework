import json

def phonebook():
    with open ('phonebook.json', 'r') as file:
        file_read = file.read()
        data = json.loads(file_read)
        print(data)
    user = input(""" Choose number what you want to do 
        1 - add new entries, 
        2 - search by first name, 
        3 - search by last name, 
        4 - search by full name, 
        5 - search by telephone number, 
        6 - search by city, 
        7 - delete a record for a given telephone number, 
        8 - exit:""")
    while True:
        if user == '1':
            add(data)
        if user == '2':
            func_search(data, 'name')
        if user == '3':
            func_search(data, 'last name')
        if user == '4':
            func_search(data, 'full name')
        if user == '5':
            func_search(data, 'telephone')
        if user == '6':
            func_search(data, 'city')
        if user == '7':
            delet_number(data)
        if user == '8':
            break
        user = input('Choose number what you want to do ')
    with open('phonebook.json', 'w') as file:
        json.dump(data, file)

def add(data):
    telephone = input("Add your telephone: ")
    name = input("Add your name: ")
    last_name = input("Add your last name: ")
    full_name = ' '.join((name,last_name))
    city = input("Add your city: ")
    data.append({'telephone':telephone,'name':name,'last name':last_name,'full name':full_name,'city':city})
    return data


def func_search(data, keys):
    user_answer = input('find your info: ')
    newList = []
    for i in data:
        if i[keys] == user_answer:
            newList.append(i)
    print(newList)


def delet_number(data):
    user_delete = input('delete your number')
    for i in range(len(data)):
        if data[i]['telephone'] == user_delete:
            data.pop(i)
    return data

phonebook()


