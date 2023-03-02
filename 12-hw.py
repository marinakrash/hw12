from collections import UserDict
from datetime import datetime
import pickle

class Field:
    def __init__(self, value):
        self.value = value

    def __setitem__(self, key, value):
        if key in AddressBook.data:
            print('We already have such contact in AB')
        else:
            AddressBook.data[key] = [value]

    def __getitem__(self, key):
        if key in AddressBook.data:
            result =AddressBook.data[key]
        return result


class Name(Field):
    def __init__(self, name):
        self.name = name


class Phone(Field):
    def __init__(self, phone):
        self.phone=[]
        self.phone.append(phone)

    def __setitem__(self, key, value):
        if key in AddressBook.data:
            if value.isdigit() and len(value) == 7:
                AddressBook.data[key].append(value)
            else:
                print('Incorrect value')
        else:
            AddressBook.data[key] = [value]


class Birthday(Field):
    def __init__(self, day, month, year):
        d =datetime(year, month, day)
        self.bdate=d.date()
        print(self.bdate)

    def __setitem__(self, key, value):
        if key in AddressBook.data:
            print('We have the birthdate already')
        else:
            if self.bdate.year<=2023 and self.bdate.month<=12 and self.bdate<=31:
                AddressBook.data[key].append(value)


class Record:
    def __init__(self,  name: Name, phone: Phone = None, bdate: Birthday = None):
        self.name=name
        self.phone=phone
        self.bdate=bdate

    def add_phone(self, phone):
        self.phone.append(phone)

    def days_to_birthday(self):
        now_d = datetime.now()
        self.current_datetime = now_d.date()
        if self.current_datetime <= self.bdate:
            pass
        else:
            print(self.bdate)
            plus_year=self.bdate.year
            plus_year.year=self.current_datetime.year+1
            print(plus_year)
        print(plus_year - self.current_datetime)
        return (plus_year - self.current_datetime)

    def delete_phone(self, phone):
        self.phone.remove(phone)

    def update_phone(self, phone):
        self.phone.clear()
        self.phone.append(phone)


class AddressBook(UserDict):

    def add_record(self, record, n=None):
        self.data[record.name.value] = record
        print(self.data)
        self.current_value = 0
        self.n = n

    def __iter__(self):
        return(self)

    def __next__(self):
        if self.n is not None and self.current_value < len(self.data):
            for i in self.n:
                contact = self.data[self.current_value]
                self.current_value += 1
                return contact
        raise StopIteration

    def save_to_file(self, filename):
        with open(filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            saved_data = pickle.load(file)
        return saved_data

    def __getstate__(self):
        attributes = self.__dict__.copy()
        return attributes

    def __setstate__(self, value):
        self.__dict__ = value

    def find_all(self):
        result=[]
        symbols_to_find = input("Введите символы для поиска:")
        print(self.data)
        for contact in self.data.values():
            print(contact)
            print(contact.values)
            contact_name=str(contact[Name])
            contact_phone = str(contact[Phone])
            if contact_name.find(symbols_to_find)>= 0 or contact_phone.find(symbols_to_find)>= 0:
                result.append(contact)
            if result == []:
                print("Простите, но такого контакта нет")
            else:
                print(result)
            return result











