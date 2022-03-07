# + - * / exit
command = ""

while command != "exit":
    command = input("Perintah : ")
    
    if command == "exit":
        break

    if command != "+" and command != "-" and command != "*" and command != "/": 
        print("Perintah tidak dikenali")
        continue
        
    a = int(input("Angka Pertama : "))
    b = int(input("Angka Kedua : "))
    
    if command == "+":
        result = a + b
    elif command == "-":
        result = a - b
    elif command == "*":
        result = a * b
    elif command == "/":
        result = a / b
    
    print(f"Hasil : {result}")
    
print("Terima Kasih sudah menggunakan aplikasi kami")