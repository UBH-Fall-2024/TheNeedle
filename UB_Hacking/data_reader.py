import csv

def read_data():
    with open("UB_Hacking/CSV Files/D&R.csv", newline="") as csvfile:
        data = csv.reader(csvfile, delimiter=",")
        data_dict = {row[0].lower(): int(row[1]) for row in data}
        return data_dict
