numbers = [5,6,7,8,1]
print(numbers)

numbers.append(99) #add value list
print(f"Append : {numbers}")

numbers.insert(2,100) # indeks, insert value list
print(f"Insert : {numbers}")

numbers.pop(5) #delete indeks 
print(f"Pop    : {numbers}")

numbers.remove(6) # remove value list
print(f"Remove : {numbers}")

numbers.sort() # Sorting value list
print(f"Sorting List : {numbers}")