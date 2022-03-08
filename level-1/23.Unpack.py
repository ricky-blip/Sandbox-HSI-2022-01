# unpack mencetak value dari index
angka = (4,5,6)

x = angka[0]
y = angka[1]
z = angka[2]
print(x , y , z)

a,b,c = angka
print(c,b,a)

# angka yang lain akan masuk ke variable k
j, *k = angka
print(j, k)