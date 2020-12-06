def play_again():
    print("\nApakah kamu mau bermain lagi? (y atau t)")
    
    jawaban = input(">").lower()
    
    if "y" in jawaban:
        mulai()
    else:
        exit()

def kalah(alasan):
    print("\n" + alasan)
    print("kalah")
    
    play_again()

def ruangan_permata():
    print("\Sekarang kamu ada di ruangan yang penuh permata")
    print("Dan disana ada pintu")
    print("Apa yang harus kamu lakukan? (1 atau 2)")
    print("1). Ambil beberapa permata dan pergi ke pintu")
    print("2). hanya pergi ke pintu")
    
    jawaban = input(">")
    
    if jawaban == "1":
        kalah("Itu adalah permata jebakan, dan bangunan itu akan runtuh dan kamu akan mati")
    elif  jawaban == "2":
        print("\nBagus, kamu adalah orang yang baik! Selamat kamu menang permainan, Itu sebenarnya adalah permata jebakan")
        play_again()
    else:
        kalah("Belajar angka dulu sana.")

def ruangan_monster():
    print("\nSekarang kamu ada di ruangan yang ada monster")
    print("Monsternya sedang tidur.\nDibelakang monster ada pintu, apa yang harus kamu lakukan? (1 atau 2)")
    print("1). Pergi ke pintu diam-diam")
    print("2). Membunuh Monster itu dan tunjukkan keberaniamu!")
    
    jawaban = input(">")
    
    if  jawaban == "1":
        ruangan_permata()
    elif jawaban == "2":
        kalah("Monster itu sedang kelaparan, dan dia akan memakanmu.")
    else:
        kalah("Belajar angka dulu sana.")

def ruangan_beruang():
    print("\nDisana ada beruang")
    print("Dibelakang pintu yang lain.")
    print("Beruang itu sedang makan madu!")
    print("apa yang akan kamu lakukan? (1 atau 2)")
    print("1). Ambil madunya.")
    print("2). Ejek beruang tersebut")
    
    jawaban = input(">")
    
    if jawaban == "1":
        kalah("Beruang itu akan membunuhmu.")
    elif jawaban == "2":
        print("\nKamu dalam waktu yang tepat,beruang itu pergi ddari pintu. sekarang kamu bisa pergi kesana!")
        ruangan_permata()
    else:
        kalah("Kamu gak tau cara ngetik angka?")

def mulai():
    print("\nKamu sekarang berada di ruangan yang gelap")
    print("Disana ada pintu di sebelaah kanan dan kirimu, mana yang akan kamu pilih? (ka atau ki)")
    
    jawaban = input(">").lower()
    
    if  "ka" in jawaban:
        ruangan_beruang()
    elif "ki" in jawaban:
        ruangan_monster()
    else:
        kalah("kamu gak tau cara ngetik sesuai perintah?")
        
mulai()