from input_data import input_data
from write_data import write_data


def push_data():
    dct = input_data()

    # id;surname;name;number;status   - phone.csv
    write_data([dct.get("id"), dct.get("surname"), dct.get("name"), dct.get("number"), dct.get("status")], "phone.csv")

    