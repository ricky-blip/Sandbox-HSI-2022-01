names = ["Ricky", 77, False, 99]

print(names[0])
print(f"range = {names[2:4]}")
print(f"range = {names[-1]}")
print(90 * "-")

for name in names:
    print(f"Item : {type(name)} {name}")