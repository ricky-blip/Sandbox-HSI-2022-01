users = open("./level-1/34.file.txt", "a") #w = write *mengganti isi dari file a=appen *menambah isi dari file

#print(users.readable()) #mengecek bisa di baca atau tidak
#print(users.writable()) #mengecek bisa di tulis atau tidak

users.write("---BARIS SAMA") # menambah di baris yang sama  menggunakan appen
users.write("\n---BARIS BARU") # menambah di baris yang selanjutnya  menggunakan appen

users.close()

