from write_data import count_data

def input_data():
    dct = dict()
    Id = count_data("phone.csv") 
    dct["id"] = Id     
    dct["surname"] = input('Введите Фамилию: ')
    dct["name"] = input('Введите Имя: ')
    dct["number"] = input('Введите Номер Телефона: ')
    dct["status"] = input('Введите Статус: ')
    return dct