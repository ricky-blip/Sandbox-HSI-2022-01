from asyncore import loop
import random

nomor_soal = [0,1,2,3,4]
soal_soal  = [
    "Siapa nama pencipta bahasa pemrograman Python?",
    "Di kota mana bahasa pemrograman Python dibuat?",
    "Yang termasuk Python Framework adalah...",
    "Ekstensi dari bahasa pemrograman Python yaitu...",
    "Apa versi terakhir dari bahasa pemrograman Python?"
]
pilihan_a  = [
    "Brendan Eich",
    "Amsterdam",
    "FastAPI",
    ".python",
    "Python3"
]
pilihan_b  = [
    "Bill Gates",
    "Paris",
    "Flask",
    ".py",
    "Python2"
]
pilihan_c  = [
    "Guido van Rossum",
    "New York",
    "Django",
    ".exe",
    "Python7"
]
pilihan_d  = [
    "James Gosling",
    "London",
    "Semua Benar",
    ".script",
    "Python4"
]
kunci_jawaban    = ["C","A","D","B","A"]

jawaban                 = ''
hasil_jawaban           = ""
jumlah_soal             = 0
jumlah_soal_dikerjakan  = 0
ke_soal                 = 0 
total_skor              = 0
random_list             = [] # supaya random tidak berulang

for item in nomor_soal:
    jumlah_soal += 1
    
print(65 * "=")
print("     Kerjakan Quiz ini dijawab dengan memilih A/B/C/D     ")
print(65 * "=")
print(f"Jumlah Soal : {jumlah_soal}")

def soal(item, nomor):
    kumpulan_soal = soal_soal[item]
    
    print(f"{nomor+1}. {kumpulan_soal}")
    print(f"A. {pilihan_a[item]}")
    print(f"B. {pilihan_b[item]}")
    print(f"C. {pilihan_c[item]}")
    print(f"D. {pilihan_d[item]}")
    print(30 * "_")
    
command = ''
while command.upper() != 'Q':
    try:
        print("")
        command = input("Ingin mengerjakan berapa soal (0-5) / Ketik 'Q' untuk Exit ? : ")
        
        if command.upper() == "Q" or command == "0":
            break
        
        if (int(command) < 6 and int(command) > 0):
            jumlah_soal_dikerjakan = int(command)
            
            print("")
            print(f"Kamu harus kerjakan {jumlah_soal_dikerjakan} soal dari {jumlah_soal} soal yang tersedia")
            break
        else:
            print("TERJADI KESALAHAN : Masukkan Angka 0-5 / Ketik (Q) Exit")
            
    except:    
        print("TERJADI KESALAHAN : Masukkan Angka 0-5 / Ketik (Q) Exit")
        continue
    
while ke_soal < jumlah_soal_dikerjakan:
    
    loop = True
    while loop: # menghindari hasil random berulang
        index_random = random.choice(nomor_soal)
        if (index_random in random_list) == False:
            loop = False
    else:
        kunci       = kunci_jawaban[index_random]
        random_list.append(index_random)
        soal(index_random, ke_soal)
        skor = 0
        
        jawaban = ''
        while jawaban.upper() != "x":
            try:
                jawaban = input("Pilihan Jawabanmu ? : ")
                jawaban = jawaban.upper()
                
                if (jawaban == "A" or jawaban == "B" or jawaban == "C" or jawaban == "D"):
                    if (jawaban == kunci):
                        hasil_jawaban = "Benar"
                    else:
                        hasil_jawaban = "Salah"
                    break
                else:
                    print("Pilih ( A/B/C/D )")
                    continue
                
            except:
                print("Pilih ( A/B/C/D )")
                continue
            
        if (hasil_jawaban == "Benar"):
            total_skor = total_skor + 2
            skor = 2
            print(f"Yeay! Jawabanmu {hasil_jawaban}")
            print(f"Skor : {skor}")
        else:
            total_skor += 1
            skor = 1
            print(f"Waduh! Jawabanmu {hasil_jawaban} => Jawaban yang benar {kunci}")
            print(f"Skor : {skor}")
            
    ke_soal += 1
    print("")

else:
    print(30 * "=")
    print(f"Total Skor anda : {total_skor}")
    print("")
    print("__________TERIMA KASIH__________")           