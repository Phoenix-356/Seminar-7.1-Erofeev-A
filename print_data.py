def print_data(data, search = False):
    if len(data) > 0:
        print("id".center(5), "Фамилия".center(20), "Имя".center(10), "Номер".center(6), "Статус".center(6))
        print("-"*120)
        if not search:
            del data[0]
        for item in data:
            print(item[0].center(5), item[1].center(20), item[2].center(10), item[3].center(6), item[4].center(6))
    else:
        print("\n")
        print("*"*100 + "\nСправочник пуст!\n" + "*"*100)
        print("\n")