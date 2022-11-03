from read_data import read_data


def init():
    if not (len(read_data()) > 0):
        
        with open("phone.csv", 'a+') as file:
            file.write("id;surname;name;class;status\n")

        