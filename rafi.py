# TEMPAT DEVELOPMENT

# I.S :
# F.S :

# IMPORT STANDAR LIBRARY
import os

# PROSEDURE

# FUNCTION

# subrutin fungsi untuk menampilkan menu utama
# mengembalikan data integer menu_utama
def fungsi_tampil_menu_utama(menu_utama):
    print('++===================================++')
    print('||             KOKO RENTAL           ||')
    print('++===================================++')
    print('|| Waktu DD-MM-YYY                   ||')
    print('||                                   ||')
    print('|| Selamat datang di KOKO RENTAL!    ||')
    print('||                                   ||')
    print('++-------------- MENU ---------------++')
    print('||  1. Admin                         ||')
    print('||  2. User                          ||')
    print('||  0. Keluar                        ||')
    print('++===================================++')
    menu_utama = int(input('Masukkan pilihan Anda : '))
    
    while (menu_utama != 1) and (menu_utama != 2):
        os.system('clear')
        print('++===================================++')
        print('||             KOKO RENTAL           ||')
        print('++===================================++')
        print('|| Waktu DD-MM-YYY                   ||')
        print('||                                   ||')
        print('|| Selamat datang di KOKO RENTAL!    ||')
        print('||                                   ||')
        print('++-------------- MENU ---------------++')
        print('||  1. Admin                         ||')
        print('||  2. User                          ||')
        print('||  0. Keluar                        ||')
        print('++===================================++')
        menu_utama = int(input('Masukkan pilihan Anda : '))
    return menu_utama

# subrutin fungsi login

def fungsi_login():
    print('++===========================================++')
    print('||                ADMIN LOGIN                ||')
    print('++===========================================++')
    password = input(' Masukkan Password : ')
    
    salah = 0
    if (password == "admin"):
        return True
    else:
        salah += 1
        
    while salah < 3 :
        os.system('clear')
        print('Password Anda salah ulangiii!!!')
        print(f'Sisa percobaan {3 - salah} lagi')
        input()
        os.system('clear')
        print('++===========================================++')
        print('||                ADMIN LOGIN                ||')
        print('++===========================================++')
        password = input('Masukkan Password : ')
        if (password == "admin"):
            return True
        else:
            salah += 1

    return False


def main():
    # DEKLARASI VARIABEL
    menu_utama = 0
    login = False
    
    
    
    menu_utama = fungsi_tampil_menu_utama(menu_utama)
    while(menu_utama != 0):
        os.system('clear')
        match menu_utama:
            case 1 :
               login = fungsi_login()
               if login:
                   print('success')
               else:
                   menu_utama = 0
# Algoritma Utama
main()
print("Keluar aplikasi, selamat tinggall!!")