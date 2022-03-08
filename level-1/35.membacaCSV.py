import csv

users = open("./level-1/35.file.csv", "r")

file_csv = csv.reader(users, delimiter=",")

#print(file_csv)

for baris in file_csv:
    #print(baris)
    print(f"Name : {baris[0]}, Username : {baris[1]}, Role : {baris[2]}")

users.close()