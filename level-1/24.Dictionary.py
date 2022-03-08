user = {
    "nama": "Ricky Rinaldy",
    "umur": 25,
    "is_admin": True 
} 

print(user)

user["umur"] = 20

temp = user["umur"]
temp1 = user.get("username")
temp2 = user.get("username", "Ricky!!!!")


print(temp1)
print(temp2)
print(temp)

