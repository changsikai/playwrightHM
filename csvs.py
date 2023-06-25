import csv

with open("shuju.csv") as file_name:
    file_read = csv.reader(file_name)
    array = list(file_read)

print(array)