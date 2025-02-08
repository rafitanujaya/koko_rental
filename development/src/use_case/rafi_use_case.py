# TEMPAT DEVELOPMENT

# I.S :
# F.S :

MAKSBARIS   = 10

# IMPORT STANDAR LIBRARY
import os

# PROSEDURE

def DEBUG_DUMMY_DATA(plat_nomor, model, brand, harga_sewa, supir, nomor_supir):
    brand[:] = ['1Toyota', '2Honda', '3Suzuki', '4Daihatsu', '5Nissan', '6Mitsubishi', '7Mazda', '8Kia', '9Hyundai', '10Ford']
    model[:] = ['Avanza', 'Civic', 'Ertiga', 'Xenia', 'Livina', 'Pajero', 'CX-5', 'Seltos', 'Elantra', 'Focus']
    harga_sewa[:] = [200000000, 300000000, 150000000, 180000000, 250000000, 400000000, 350000000, 220000000, 270000000, 320000000]
    plat_nomor[:] = ['B 1234 AB', 'B 5678 CD', 'B 9101 EF', 'B 1213 GH', 'B 1415 IJ', 'B 1617 KL', 'B 1819 MN', 'B 2021 OP', 'B 2223 QR', 'B 2425 ST']
    supir[:] = ['John Doe', 'Jane Smith', 'Alice Johnson', 'Bob Brown', 'Charlie Davis', 'Eve White', 'Frank Black', 'Grace Green', 'Hank Blue', 'Ivy Yellow']
    nomor_supir[:] = [81234567890, 82345678901, 83456789012, 84567890123, 85678901234, 86789012345, 87890123456, 88901234567, 89012345678, 90123456789]
    print(f'dummy success = {brand}-{model}-{harga_sewa}-{plat_nomor}-{supir}-{nomor_supir}')
    return 10

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
        
def prosedur_penambahan_data_rental(plat_nomor, model, brand, harga_sewa, supir, nomor_supir, banyak_data):
    if (banyak_data < MAKSBARIS):
        banyak_data += 1
        plat_nomor[banyak_data-1]  = input(f'nomor plat ke-{banyak_data}        : ')
        model[banyak_data-1]       = input(f'nomor model ke-{banyak_data}       : ')
        brand[banyak_data-1]       = input(f'nomor brand ke-{banyak_data}       : ')
        harga_sewa[banyak_data-1]  = int(input(f'nomor harga sewa ke-{banyak_data}  : '))
        supir[banyak_data-1]       = input(f'nomor supir ke-{banyak_data}       : ')
        nomor_supir[banyak_data-1] = int(input(f'nomor nomor supir ke-{banyak_data} : '))
        return banyak_data
    else:
        print('data rental sudah pernuh')
        return banyak_data
    
def prosedur_penyisipan_data_rental(plat_nomor, model, brand, harga_sewa, supir, nomor_supir, banyak_data, posisi_penyisipan):
    posisi_penyisipan -= 1
    if(banyak_data < MAKSBARIS):
        if(posisi_penyisipan < banyak_data) and (posisi_penyisipan >= 0):
            for i in range(banyak_data, 0, -1):
                plat_nomor[i+1]  = plat_nomor[i]
                model[i+1]       = model[i] 
                brand[i+1]       = brand[i]
                harga_sewa[i+1]  = harga_sewa[i]
                supir[i+1]       = supir[i] 
                nomor_supir[i+1] = nomor_supir[i]
            
            plat_nomor[posisi_penyisipan]  = input(f'nomor plat ke-{posisi_penyisipan + 1}        : ')
            model[posisi_penyisipan]       = input(f'nomor model ke-{posisi_penyisipan + 1}       : ')
            brand[posisi_penyisipan]       = input(f'nomor brand ke-{posisi_penyisipan + 1}       : ')
            harga_sewa[posisi_penyisipan]  = int(input(f'nomor harga sewa ke-{posisi_penyisipan + 1}  : '))
            supir[posisi_penyisipan]       = input(f'nomor supir ke-{posisi_penyisipan + 1}       : ')
            nomor_supir[posisi_penyisipan] = int(input(f'nomor nomor supir ke-{posisi_penyisipan + 1} : '))
            return banyak_data + 1
        else:
            print('posisi tidak valid')
            return banyak_data
    else:
        print('data penuh')
        
def prosedur_penghapusan_data_rental(plat_nomor, model, brand, harga_sewa, supir, nomor_supir, banyak_data, posisi_hapus):
    posisi_hapus -= 1
    if(banyak_data > 0):
        if(posisi_hapus >= 0) and (posisi_hapus <= banyak_data):
            for i in range(posisi_hapus, banyak_data):
                plat_nomor[i]  = plat_nomor[i+1]
                model[i]       = model[i+1] 
                brand[i]       = brand[i+1]
                harga_sewa[i]  = harga_sewa[i+1]
                supir[i]       = supir[i+1] 
                nomor_supir[i] = nomor_supir[i+1]
                
            plat_nomor[banyak_data]  = ''
            model[banyak_data]       = ''
            brand[banyak_data]       = ''
            harga_sewa[banyak_data]  = 0
            supir[banyak_data]       = ''
            nomor_supir[banyak_data] = 0
            return banyak_data - 1
        else:
            print('posisi tidak valid')
            return banyak_data
    else:
        print('data kosong')
        return banyak_data

        
        
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
    
    while (menu_crud != 1) and (menu_crud != 2) and (menu_crud != 3) and (menu_crud != 4) and (menu_crud != 5) and (menu_crud != 6) and (menu_crud != 7) and (menu_crud != 0) and (menu_crud != 77):
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
                                        banyak_data = prosedur_penambahan_data_rental(plat_nomor, model, brand, harga_sewa, supir, nomor_supir, banyak_data)
                                    case 4:
                                        posisi_penyisipan = int(input('masukkan posisi data yang mau diisi : '))
                                        banyak_data = prosedur_penyisipan_data_rental(plat_nomor, model, brand, harga_sewa, supir, nomor_supir, banyak_data, posisi_penyisipan)
                                    case 5:
                                        posisi_hapus = int(input('masukkan posisi data yang mau dihapus : '))
                                        banyak_data = prosedur_penghapusan_data_rental(plat_nomor, model, brand, harga_sewa, supir, nomor_supir, banyak_data, posisi_hapus)
                                    case 6:
                                        print(" menu crud 1")
                                    case 7:
                                        print(" menu crud 1")
                                        print(f'{plat_nomor}')
                                    case 77:
                                        banyak_data = DEBUG_DUMMY_DATA(plat_nomor, model, brand, harga_sewa, supir, nomor_supir)
                                input('pp')
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

os.system('clear')
# print('                                 DATA RENTAL                                  ')
# print('                                                                              ')
# print('Pengurutan data bedasarkan = Brand                                            ')
# print('Format Pengurutan          = Menurun                                          ')
# print('                                                                              ')
# print('++====++============++========++=======++============++=====================++')
# print('|| No || Plat Nomor || Brand  || Model || Nama Supir || Nomor Telepon Supir ||')
# print('++====++============++========++=======++============++=====================++')
# print('|| 01 ||  D 1990 DY || Toyota || T-001 || Deriel Hoy ||     6281920202020   ||')
# print('++----++------------++--------++-------++------------++---------------------++')
# print('|| 01 ||  D 1990 DY || Toyota || T-001 || Deriel Hoy ||     6281920202020   ||')
# print('++----++------------++--------++-------++------------++---------------------++')
# print('|| 01 ||  D 1990 DY || Toyota || T-001 || Deriel Hoy ||     6281920202020   ||')
# print('++----++------------++--------++-------++------------++---------------------++')

print('                                 DATA RENTAL                                  ')
print('                                                                              ')
print('Pengurutan data bedasarkan = Brand                                            ')
print('Format Pengurutan          = Menurun                                          ')
print('                                                                              ')
print('╔══════════════════════════════════════════════════════════════════════════╗')
print('║                                                                          ║')
print('║                           DAFTAR RENTAL KENDARAAN                        ║')
print('║                           ───────────────────────                        ║')
print('║ Pengurutan    : Brand                                                    ║')
print('║ Format        : Menaik                                                   ║')
print('║ Total Product : 3                                                        ║')
print('╠════╦════════════╦════════╦════════╦══════════════╦═══════════════════════╣')
print('║ No ║ Plat Nomor ║ Brand  ║  Model ║  Nama Supir  ║  Nomor Telepon Supir  ║')
print('╠════╬════════════╬════════╬════════╬══════════════╬═══════════════════════╣')
print('║ 01 ║  D 1990 DY ║ Toyota ║ T-001  ║  Deriel Hoy  ║     6281920202020     ║')
print('╠════╬════════════╬════════╬════════╬══════════════╬═══════════════════════╣')
print('║ 01 ║  D 1990 DY ║ Toyota ║ T-001  ║  Deriel Hoy  ║     6281920202020     ║')
print('╠════╬════════════╬════════╬════════╬══════════════╬═══════════════════════╣')
print('║ 01 ║  D 1990 DY ║ Toyota ║ T-001  ║  Deriel Hoy  ║     6281920202020     ║')
print('╚════╩════════════╩════════╩════════╩══════════════╩═══════════════════════╝')

