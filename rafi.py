# TEMPAT DEVELOPMENT

# I.S :
# F.S :

MAKSBARIS   = 10

# IMPORT STANDAR LIBRARY
import os

# PROSEDURE

def prosedur_isi_data_rental(plat_nomor, model, brand, harga_sewa, supir, nomor_supir, banyak_data):
    for i in range(banyak_data):
        tumbal = input(f'nomor plat ke-{i+1}        : ')
        plat_duplikat = prosedur_sequential_search_sentinel(plat_nomor, tumbal)
        while plat_duplikat:
            print(f'plat nomor sudah ada, ulangiii')
            input()
            os.system('clear')
            tumbal = input(f'nomor plat ke-{i+1}        : ')
            plat_duplikat = prosedur_sequential_search_sentinel(plat_nomor, tumbal)
        plat_nomor[i]  = tumbal
        model[i]       = input(f'nomor model ke-{i+1}       : ')
        brand[i]       = input(f'nomor brand ke-{i+1}       : ')
        harga_sewa[i]  = int(input(f'nomor harga sewa ke-{i+1}  : '))
        supir[i]       = input(f'nomor supir ke-{i+1}       : ')
        nomor_supir[i] = int(input(f'nomor nomor supir ke-{i+1} : '))
    
def prosedur_sequential_search_sentinel(array, dicari):
    # print(array)
    array[MAKSBARIS] = dicari
    i = 0
    while (array[i] != dicari):
        i += 1
    if(i < MAKSBARIS):
        print(f'{dicari} ditemukan pada indeks ke-{i+1}')
        return True
    else:
        print(f'{dicari} tidak ditemukan')
        return False
    
def prosedur_tampil_data_rental(plat_nomor, model, brand, harga_sewa, supir, nomor_supir, banyak_data):
    for i in range(banyak_data):
        print(f'Data ke-{i+1} : {plat_nomor[i]}')
        print(f'Data ke-{i+1} : {model[i]}')
        print(f'Data ke-{i+1} : {brand[i]}')
        print(f'Data ke-{i+1} : {harga_sewa[i]}')
        print(f'Data ke-{i+1} : {supir[i]}')
        print(f'Data ke-{i+1} : {nomor_supir[i]}')
        
        
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
    
    while (menu_utama != 1) and (menu_utama != 2) and (menu_utama != 0):
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

def fungsi_login(password):
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

# subrutin fungsi untuk menampilkan menu admin
# mengembalikan data integer menu admin
def fungsi_tampil_menu_admin(menu_admin):
    print('++===================================++')
    print('||             KOKO RENTAL           ||')
    print('++===================================++')
    print('|| Waktu DD-MM-YYY                   ||')
    print('||                                   ||')
    print('|| Selamat datang Admin              ||')
    print('||                                   ||')
    print('++-------------- MENU ---------------++')
    print('||  1. CRUD                          ||')
    print('||  2. Sorting                       ||')
    print('||  3. Searching                     ||')
    print('||  0. Keluar                        ||')
    print('++===================================++')
    menu_admin = int(input('Masukkan pilihan Anda : '))
    
    while (menu_admin != 1) and (menu_admin != 2) and (menu_admin != 3) and (menu_admin != 0):
        os.system('clear')
        print('++===================================++')
        print('||             KOKO RENTAL           ||')
        print('++===================================++')
        print('|| Waktu DD-MM-YYY                   ||')
        print('||                                   ||')
        print('|| Selamat datang Admin              ||')
        print('||                                   ||')
        print('++-------------- MENU ---------------++')
        print('||  1. CRUD                          ||')
        print('||  2. Sorting                       ||')
        print('||  3. Searching                     ||')
        print('||  0. Keluar                        ||')
        print('++===================================++')
        menu_admin = int(input('Masukkan pilihan Anda : '))
    return menu_admin

# subrutin fungsi untuk menampilkan menu CRUD admin
# mengembalikan data integer CRUD admin
def fungsi_tampil_menu_crud_admin(menu_crud):
    print('++===========================================++')
    print('||                 KOKO RENTAL               ||')
    print('++===========================================++')
    print('||                                           ||')
    print('++------------------- MENU ------------------++')
    print('||  1. Pengisian Data Rental                 ||')
    print('||  2. Penyajian Data Rental                 ||')
    print('||  3. Penambahan Data Rental                ||')
    print('||  4. Penyisipan Data Rental                ||')
    print('||  5. Penghapusan Data Rental               ||')
    print('||  6. Penghapusan Data Rental               ||')
    print('||  7. Penghitungan Rata-Rata Biaya Rental   ||')
    print('||  7. Mencari min-max Biaya Rental          ||')
    print('||  0. Kembali ke menu admin                 ||')
    print('++===========================================++')
    menu_crud = int(input('Masukkan pilihan Anda : '))
    
    while (menu_crud != 1) and (menu_crud != 2) and (menu_crud != 3) and (menu_crud != 4) and (menu_crud != 5) and (menu_crud != 6) and (menu_crud != 7) and (menu_crud != 0):
        os.system('clear')
        print('++===========================================++')
        print('||                 KOKO RENTAL               ||')
        print('++===========================================++')
        print('||                                           ||')
        print('++------------------- MENU ------------------++')
        print('||  1. Pengisian Data Rental                 ||')
        print('||  2. Penyajian Data Rental                 ||')
        print('||  3. Penambahan Data Rental                ||')
        print('||  4. Penyisipan Data Rental                ||')
        print('||  5. Penghapusan Data Rental               ||')
        print('||  6. Penghapusan Data Rental               ||')
        print('||  7. Penghitungan Rata-Rata Biaya Rental   ||')
        print('||  7. Mencari min-max Biaya Rental          ||')
        print('||  0. Kembali ke menu admin                 ||')
        print('++===========================================++')
        menu_crud = int(input('Masukkan pilihan Anda : '))
    return menu_crud


def main():
    # DEKLARASI VARIABEL
    
    # var menu
    menu_utama = 0
    menu_admin = 0
    menu_crud  = 0
    password = ""
    login = False
    
    
    
    
    # ARRAY
    plat_nomor  = [""] * (MAKSBARIS + 1)
    model       = [""] * MAKSBARIS
    brand       = [""] * MAKSBARIS
    harga_sewa  = [0] * MAKSBARIS
    supir       = [""] * MAKSBARIS
    nomor_supir = [0] * MAKSBARIS
    

    
    
    menu_utama = fungsi_tampil_menu_utama(menu_utama)
    while(menu_utama != 0):
        os.system('clear')
        match menu_utama:
            case 1 :
                login = fungsi_login(password)
                if login:
                    os.system('clear')
                    menu_admin = fungsi_tampil_menu_admin(menu_admin)
                    match menu_admin:
                        case 1:
                            menu_crud = fungsi_tampil_menu_crud_admin(menu_crud)
                            while(menu_crud != 0):
                                match menu_crud:
                                    case 1:
                                        banyak_data = int(input('Banyak Data yang mau dimasukkan : '))
                                        prosedur_isi_data_rental(plat_nomor, model, brand, harga_sewa, supir, nomor_supir, banyak_data)
                                    case 2:
                                        if (banyak_data > MAKSBARIS):
                                            prosedur_tampil_data_rental(plat_nomor,model,brand,harga_sewa,supir,nomor_supir, MAKSBARIS)
                                        else:
                                            prosedur_tampil_data_rental(plat_nomor,model,brand,harga_sewa,supir,nomor_supir, banyak_data)
                                    case 3:
                                        print(" menu crud 1")
                                    case 4:
                                        print(" menu crud 1")
                                    case 5:
                                        print(" menu crud 1")
                                    case 6:
                                        print(" menu crud 1")
                                    case 7:
                                        print(" menu crud 1")
                                menu_crud = fungsi_tampil_menu_crud_admin(menu_crud)
                        case 2:
                            print('menu admin 1')
                        case 0:
                            menu_utama = 0
                    input('bro')
                else:
                    menu_utama = 0
# Algoritma Utama
main()
print("Keluar aplikasi, selamat tinggall!!")