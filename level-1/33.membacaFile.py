users = open("./level-1/33.file.txt", "r")

list = users.readlines()
# print(users.read()) #Semua
# print(users.readline()) #Per Baris
# print(users.readlines()) #List

index = 1
for pengguna in list:
    print(f"{index}.{pengguna}")
    index += 1

users.close()