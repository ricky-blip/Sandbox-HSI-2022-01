numbers = [5,6,7,8,1]

total = sum(numbers) # menjumlahkan angka list
print(total)

max_number = max(numbers) # angka terbesar
print(max_number)

numbers.sort() # angka terbesar
max_number = numbers[-1]
print(max_number)

max_num = numbers[0]
for number in numbers:
    if number > max_num:
        max_num = number
        
print(max_num)

