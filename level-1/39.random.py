# mencetak angka random
import random

# print(random.random())

for i in range(5): # mencetak angka random antara 10 sampai 30 dengan range per 5 angka
    print(random.randint(10, 30))

print(50 * '-')
# cara 1
'''users = ['Ricky','Razor','Rush','Rich']

batas_bawah = 0
batas_atas  = 3

random_angka = random.randint(batas_bawah, batas_atas)

win = users[random_angka]

print(win)'''

#cara 2
users = ['Ricky','Razor','Rush','Rich']
win = random.choices(users)
print(win)


    