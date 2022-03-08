'''
menghindari dari lupa menuliskan close
mencegah file tidak close saat error
'''
import csv

#users = open("./level-1/35.file.csv", "r")

with open("./level-1/35.file.csv", "r") as users:
    file_csv = csv.reader(users, delimiter=",")

    for baris in file_csv:
        #print(baris)
        print(f"Name : {baris[0]}, Username : {baris[1]}, Role : {baris[2]}")

#users.close()