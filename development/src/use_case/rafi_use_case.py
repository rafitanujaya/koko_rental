# TEMPAT DEVELOPMENT

# I.S :
# F.S :

MAKSBARIS   = 10

# IMPORT STANDAR LIBRARY
import os

# PROSEDURE

def DEBUG_DUMMY_DATA(plat_nomor, model, brand, harga_sewa, supir, nomor_supir):
    datas = [
        ['1Toyota', '2Honda', '3Suzuki', '4Daihatsu', '5Nissan', '6Mitsubishi', '7Mazda', '8Kia', '9Hyundai', '10Ford'],
        ['Avanza', 'Civic', 'Ertiga', 'Xenia', 'Livina', 'Pajero', 'CX-5', 'Seltos', 'Elantra', 'Focus'],
        [200000000, 300000000, 150000000, 180000000, 250000000, 400000000, 350000000, 220000000, 270000000, 320000000],
        ['B 1234 AB', 'B 5678 CD', 'B 9101 EF', 'B 1213 GH', 'B 1415 IJ', 'B 1617 KL', 'B 1819 MN', 'B 2021 OP', 'B 2223 QR', 'B 2425 ST'],
        ['John Doe', 'Jane Smith', 'Alice Johnson', 'Bob Brown', 'Charlie Davis', 'Eve White', 'Frank Black', 'Grace Green', 'Hank Blue', 'Ivy Yellow'],
        [81234567891, 82345678902, 83456789013, 84567890124, 85678901235, 86789012346, 87890123457, 88901234568, 89012345679, 90123456789]
        ]
    
    for i in range(MAKSBARIS):
        brand[i] = datas[0][i]
        model[i] = datas[1][i]
        harga_sewa[i] = datas[2][i]
        plat_nomor[i] = datas[3][i]
        supir[i] = datas[4][i]
        nomor_supir[i] = datas[5][i]
    # brand[:] = ['1Toyota', '2Honda', '3Suzuki', '4Daihatsu', '5Nissan', '6Mitsubishi', '7Mazda', '8Kia', '9Hyundai', '10Ford']
    # model[:] = ['Avanza', 'Civic', 'Ertiga', 'Xenia', 'Livina', 'Pajero', 'CX-5', 'Seltos', 'Elantra', 'Focus']
    # harga_sewa[:] = [200000000, 300000000, 150000000, 180000000, 250000000, 400000000, 350000000, 220000000, 270000000, 320000000]
    # plat_nomor[:] = ['B 1234 AB', 'B 5678 CD', 'B 9101 EF', 'B 1213 GH', 'B 1415 IJ', 'B 1617 KL', 'B 1819 MN', 'B 2021 OP', 'B 2223 QR', 'B 2425 ST']
    # supir[:] = ['John Doe', 'Jane Smith', 'Alice Johnson', 'Bob Brown', 'Charlie Davis', 'Eve White', 'Frank Black', 'Grace Green', 'Hank Blue', 'Ivy Yellow']
    # nomor_supir[:] = [81234567891, 82345678902, 83456789013, 84567890124, 85678901235, 86789012346, 87890123457, 88901234568, 89012345679, 90123456789]
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
    if(banyak_data < MAKSBARIS):
        if(posisi_penyisipan < banyak_data) and (posisi_penyisipan >= 0):
            for i in range(banyak_data, 0, -1):
                print(i)
                plat_nomor[i]  = plat_nomor[i - 1]
                model[i]       = model[i - 1] 
                brand[i]       = brand[i - 1]
                harga_sewa[i]  = harga_sewa[i - 1]
                supir[i]       = supir[i - 1] 
                nomor_supir[i] = nomor_supir[i - 1]
            
            plat_nomor[posisi_penyisipan - 1]  = input(f'nomor plat ke-{posisi_penyisipan}        : ')
            model[posisi_penyisipan - 1]       = input(f'nomor model ke-{posisi_penyisipan}       : ')
            brand[posisi_penyisipan - 1]       = input(f'nomor brand ke-{posisi_penyisipan}       : ')
            harga_sewa[posisi_penyisipan - 1]  = int(input(f'nomor harga sewa ke-{posisi_penyisipan}  : '))
            supir[posisi_penyisipan - 1]       = input(f'nomor supir ke-{posisi_penyisipan}       : ')
            nomor_supir[posisi_penyisipan -1 ] = int(input(f'nomor nomor supir ke-{posisi_penyisipan} : '))
            return banyak_data + 1
        else:
            print('posisi tidak valid')
            return banyak_data
    else:
        print('data penuh')
        
def prosedur_penghapusan_data_rental(plat_nomor, model, brand, harga_sewa, supir, nomor_supir, banyak_data, posisi_hapus):
    if(banyak_data > 0):
        if(posisi_hapus >= 0) and (posisi_hapus <= banyak_data):
            for i in range(posisi_hapus, banyak_data):
                plat_nomor[i-1]  = plat_nomor[i]
                model[i-1]       = model[i] 
                brand[i-1]       = brand[i]
                harga_sewa[i-1]  = harga_sewa[i]
                supir[i-1]       = supir[i] 
                nomor_supir[i-1] = nomor_supir[i]
                
            plat_nomor[banyak_data - 1]  = ''
            model[banyak_data - 1]       = ''
            brand[banyak_data - 1 ]       = ''
            harga_sewa[banyak_data -1 ]  = 0
            supir[banyak_data- 1]       = ''
            nomor_supir[banyak_data - 1 ] = 0
            return banyak_data - 1
        else:
            print('posisi tidak valid')
            return banyak_data
    else:
        print('data kosong')
        return banyak_data

def prosedur_reset_data_rental(plat_nomor, model, brand, harga_sewa, supir, nomor_supir):
    for i in range(MAKSBARIS):
        plat_nomor[i] = ''
        model[i] = ''
        brand[i] = ''
        harga_sewa[i] = 0
        supir[i] = ''
        nomor_supir[i] = 0      
        
def prosedur_menghitung_rata_rata_data_rental(harga_sewa): 
    temp = 0
    pembagi = 0
    for i in range(MAKSBARIS):
        if(harga_sewa[i] != 0):
            temp += harga_sewa[i]
            pembagi += 1
    print(f'Rata-rata harga sewa = {temp / pembagi}')

def prosedur_min_max_data_rental(plat_nomor, harga_sewa,):
    min = harga_sewa[0]
    min_index = 0
    max = harga_sewa[0]
    max_index = 0
    for i in range(MAKSBARIS):
        if(harga_sewa[i] < min):
            min = harga_sewa[i]
            min_index = i
        if(harga_sewa[i] > max):
            max = harga_sewa[i]
            max_index = i
    print(f'Harga sewa termahal jatuh kepada = {harga_sewa[max_index]}-{plat_nomor[max_index]}')
    print(f'Harga sewa termurah jatuh kepada = {harga_sewa[min_index]}-{plat_nomor[min_index]}')
    
def prosedur_sorting_asc(plat_nomor, model, brand, harga_sewa, supir, nomor_supir, array_sorting):
    for i in range(MAKSBARIS):
        for j in range(MAKSBARIS -1, i, -1):
            if array_sorting[j] < array_sorting[j-1]:
                temp = plat_nomor[j-1]
                plat_nomor[j-1] = plat_nomor[j]
                plat_nomor[j] = temp
                
                temp = model[j-1]
                model[j-1] = model[j]
                model[j] = temp
                
                temp = brand[j-1]
                brand[j-1] = brand[j]
                brand[j] = temp
                
                temp = harga_sewa[j-1]
                harga_sewa[j-1] = harga_sewa[j]
                harga_sewa[j] = temp
                
                temp = supir[j-1]
                supir[j-1] = supir[j]
                supir[j] = temp
                
                temp = nomor_supir[j-1]
                nomor_supir[j-1] = nomor_supir[j]
                nomor_supir[j] = temp
    print('done')
    prosedur_tampil_data_rental(plat_nomor, model, brand, harga_sewa, supir, nomor_supir, MAKSBARIS)
      
def prosedur_sorting_desc(plat_nomor, model, brand, harga_sewa, supir, nomor_supir, array_sorting):
    for i in range(MAKSBARIS):
        max = i
        print(f'hallow {i}')
        for j in range(i, MAKSBARIS):
            print(f'hallow bro {j}')
            
            if(array_sorting[j] > array_sorting[max]):
                max = j
        
        temp = plat_nomor[i]
        plat_nomor[i] = plat_nomor[max]
        plat_nomor[max] = temp
        
        temp = model[i]
        model[i] = model[max]
        model[max] = temp
        
        temp = brand[i]
        brand[i] = brand[max]
        brand[max] = temp
        
        temp = harga_sewa[i]
        harga_sewa[i] = harga_sewa[max]
        harga_sewa[max] = temp
        
        temp = supir[i]
        supir[i] = supir[max]
        supir[max] = temp
        
        temp = nomor_supir[i]
        nomor_supir[i] = nomor_supir[max]
        nomor_supir[max] = temp
    print('done')
    prosedur_tampil_data_rental(plat_nomor, model, brand, harga_sewa, supir, nomor_supir, MAKSBARIS)
    
def prosedur_searching_seq(plat_nomor, model, brand, harga_sewa, supir, nomor_supir, searching_array, banyak_data):
        dicari = input('masukkan data yang ingin dicari : ')
        i = 0;
        while searching_array[i] != dicari and i < banyak_data - 1:
            i += 1;
            print(i)
        if searching_array[i] == dicari:
            print(f'data ditemukan {dicari}')
            print(f'Data : {plat_nomor[i]}')
            print(f'Data : {model[i]}')
            print(f'Data : {brand[i]}')
            print(f'Data : {harga_sewa[i]}')
            print(f'Data : {supir[i]}')
            print(f'Data : {nomor_supir[i]}')
            i += 1
            while(i < banyak_data):
                if(searching_array[i] == dicari):
                    print(f'data ditemukan {dicari}')
                    print(f'Data : {plat_nomor[i]}')
                    print(f'Data : {model[i]}')
                    print(f'Data : {brand[i]}')
                    print(f'Data : {harga_sewa[i]}')
                    print(f'Data : {supir[i]}')
                    print(f'Data : {nomor_supir[i]}')
                i += 1
        else:
            print(f'data tidak ditemukan')

def prosedur_searching_seq_int(plat_nomor, model, brand, harga_sewa, supir, nomor_supir, searching_array, banyak_data):
        dicari = int(input('masukkan data yang ingin dicari : '))
        i = 0;
        while searching_array[i] != dicari and i < banyak_data - 1:
            i += 1;
            print(i)
        if searching_array[i] == dicari:
            print(f'data ditemukan {dicari}')
            print(f'Data : {plat_nomor[i]}')
            print(f'Data : {model[i]}')
            print(f'Data : {brand[i]}')
            print(f'Data : {harga_sewa[i]}')
            print(f'Data : {supir[i]}')
            print(f'Data : {nomor_supir[i]}')
            i += 1
            while(i < banyak_data):
                if(searching_array[i] == dicari):
                    print(f'data ditemukan {dicari}')
                    print(f'Data : {plat_nomor[i]}')
                    print(f'Data : {model[i]}')
                    print(f'Data : {brand[i]}')
                    print(f'Data : {harga_sewa[i]}')
                    print(f'Data : {supir[i]}')
                    print(f'Data : {nomor_supir[i]}')
                i += 1
        else:
            print(f'data tidak ditemukan')    
            
def prosedur_search_binary(plat_nomor, model, brand, harga_sewa, supir, nomor_supir, searching_array, banyak_data):
    dicari = input('data yang dicari : ')
    la = 0
    lb = banyak_data - 1
    ketemu = False #dicari 7
    while not ketemu and la <= lb :
        k = (la + lb) // 2
        print(k)
        if (searching_array[k] == dicari):
            ketemu =  True
        else:
            if (searching_array[k] < dicari):
                la = k + 1
            else:
                lb = k - 1
    if ketemu :
        print(f'data dicari ketemu {dicari}')
        print(f'Data : {plat_nomor[k]}')
        print(f'Data : {model[k]}')
        print(f'Data : {brand[k]}')
        print(f'Data : {harga_sewa[k]}')
        print(f'Data : {supir[k]}')
        print(f'Data : {nomor_supir[k]}')
    else:
        print(f'tidak ketemu')
        
def prosedur_search_binary_int(plat_nomor, model, brand, harga_sewa, supir, nomor_supir, searching_array, banyak_data):
    dicari = input('data yang dicari : ')
    la = 0
    lb = banyak_data - 1
    ketemu = False #dicari 7
    while not ketemu and la <= lb :
        k = (la + lb) // 2
        if (searching_array[k] == dicari):
            ketemu =  True
        else:
            if (searching_array[k] < dicari):
                la = k + 1
            else:
                lb = k - 1
    if ketemu :
        print(f'data dicari ketemu {dicari}')
        print(f'Data : {plat_nomor[k]}')
        print(f'Data : {model[k]}')
        print(f'Data : {brand[k]}')
        print(f'Data : {harga_sewa[k]}')
        print(f'Data : {supir[k]}')
        print(f'Data : {nomor_supir[k]}')
    else:
        print(f'tidak ketemu')
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
    print('||  6. Reset Data Rental                     ||')
    print('||  7. Penghitungan Rata-Rata Biaya Rental   ||')
    print('||  8. Mencari min-max Biaya Rental          ||')
    print('||  0. Kembali ke menu admin                 ||')
    print('++===========================================++')
    menu_crud = int(input('Masukkan pilihan Anda : '))
    
    while (menu_crud != 1) and (menu_crud != 2) and (menu_crud != 3) and (menu_crud != 4) and (menu_crud != 5) and (menu_crud != 6) and (menu_crud != 7) and (menu_crud != 8) and (menu_crud != 0) and (menu_crud != 77):
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
        print('||  6. Reset Data Rental                     ||')
        print('||  7. Penghitungan Rata-Rata Biaya Rental   ||')
        print('||  8. Mencari min-max Biaya Rental          ||')
        print('||  0. Kembali ke menu admin                 ||')
        print('++===========================================++')
        menu_crud = int(input('Masukkan pilihan Anda : '))
    return menu_crud

def fungsi_tampil_menu_sorting_admin(menu_sorting):
    print('++===========================================++')
    print('||                 KOKO RENTAL               ||')
    print('++===========================================++')
    print('||                                           ||')
    print('++------------------- MENU ------------------++')
    print('||  1. Sorting Format ASC                    ||')
    print('||  2. Sorting Format DESC                   ||')
    print('||  0. Kembali ke menu admin                 ||')
    print('++===========================================++')
    menu_sorting = int(input('Masukkan pilihan Anda : '))
    
    
    while (menu_sorting != 1) and (menu_sorting != 2) and (menu_sorting != 0):
        os.system('clear')
        print('++===========================================++')
        print('||                 KOKO RENTAL               ||')
        print('++===========================================++')
        print('||                                           ||')
        print('++------------------- MENU ------------------++')
        print('||  1. Sorting Format ASC                    ||')
        print('||  2. Sorting Format DESC                   ||')
        print('||  0. Kembali ke menu admin                 ||')
        print('++===========================================++')
        menu_sorting = int(input('Masukkan pilihan Anda : '))
    return menu_sorting

def fungsi_tampil_menu_sorting_asc_admin(menu_sorting_asc):
    print('++===========================================++')
    print('||                 KOKO RENTAL               ||')
    print('++===========================================++')
    print('||                                           ||')
    print('++------------------- MENU ------------------++')
    print('||  1. Plat Nomor                            ||')
    print('||  2. Model                                 ||')
    print('||  3. Brand                                 ||')
    print('||  4. Harga Sewa                            ||')
    print('||  5. Supir                                 ||')
    print('||  6. Nomor Supir                           ||')
    print('||  0. Kembali ke menu admin                 ||')
    print('++===========================================++')
    menu_sorting_asc = int(input('Masukkan pilihan Anda : '))
    
    
    while (menu_sorting_asc != 1) and (menu_sorting_asc != 2) and (menu_sorting_asc != 3) and (menu_sorting_asc != 4) and (menu_sorting_asc != 5) and (menu_sorting_asc != 6) and (menu_sorting_asc != 0) and (menu_sorting_asc != 77):
        os.system('clear')
        print('++===========================================++')
        print('||                 KOKO RENTAL               ||')
        print('++===========================================++')
        print('||                                           ||')
        print('++------------------- MENU ------------------++')
        print('||  1. Plat Nomor                            ||')
        print('||  2. Model                                 ||')
        print('||  3. Brand                                 ||')
        print('||  4. Harga Sewa                            ||')
        print('||  5. Supir                                 ||')
        print('||  6. Nomor Supir                           ||')
        print('||  0. Kembali ke menu admin                 ||')
        print('++===========================================++')
        menu_sorting_asc = int(input('Masukkan pilihan Anda : '))
    return menu_sorting_asc

def fungsi_tampil_menu_sorting_desc_admin(menu_sorting_desc):
    print('++===========================================++')
    print('||                 KOKO RENTAL               ||')
    print('++===========================================++')
    print('||                                           ||')
    print('++------------------- MENU ------------------++')
    print('||  1. Plat Nomor                            ||')
    print('||  2. Model                                 ||')
    print('||  3. Brand                                 ||')
    print('||  4. Harga Sewa                            ||')
    print('||  5. Supir                                 ||')
    print('||  6. Nomor Supir                           ||')
    print('||  0. Kembali ke menu admin                 ||')
    print('++===========================================++')
    menu_sorting_desc = int(input('Masukkan pilihan Anda : '))
    
    
    while (menu_sorting_desc != 1) and (menu_sorting_desc != 2) and (menu_sorting_desc != 3) and (menu_sorting_desc != 4) and (menu_sorting_desc != 5) and (menu_sorting_desc != 6) and (menu_sorting_desc != 0) and (menu_sorting_desc != 77):
        os.system('clear')
        print('++===========================================++')
        print('||                 KOKO RENTAL               ||')
        print('++===========================================++')
        print('||                                           ||')
        print('++------------------- MENU ------------------++')
        print('||  1. Plat Nomor                            ||')
        print('||  2. Model                                 ||')
        print('||  3. Brand                                 ||')
        print('||  4. Harga Sewa                            ||')
        print('||  5. Supir                                 ||')
        print('||  6. Nomor Supir                           ||')
        print('||  0. Kembali ke menu admin                 ||')
        print('++===========================================++')
        menu_sorting_desc = int(input('Masukkan pilihan Anda : '))
    return menu_sorting_desc

def fungsi_tampil_menu_searching_admin(menu_searching):
    print('++===========================================++')
    print('||                 KOKO RENTAL               ||')
    print('++===========================================++')
    print('||                                           ||')
    print('++------------------- MENU ------------------++')
    print('||  1. Sequential Search                     ||')
    print('||  2. Binary Search                         ||')
    print('||  0. Kembali ke menu admin                 ||')
    print('++===========================================++')
    menu_searching = int(input('Masukkan pilihan Anda : '))
    
    
    while (menu_searching != 1) and (menu_searching != 2) and (menu_searching != 0) and (menu_searching != 77):
        os.system('clear')
        print('++===========================================++')
        print('||                 KOKO RENTAL               ||')
        print('++===========================================++')
        print('||                                           ||')
        print('++------------------- MENU ------------------++')
        print('||  1. Sequential Search                     ||')
        print('||  2. Binary Search                         ||')
        print('||  0. Kembali ke menu admin                 ||')
        print('++===========================================++')
        menu_searching = int(input('Masukkan pilihan Anda : '))
    return menu_searching

def fungsi_tampil_menu_searching_seq_admin(menu_searching_seq):
    print('++===========================================++')
    print('||                 KOKO RENTAL               ||')
    print('++===========================================++')
    print('||                                           ||')
    print('++------------------- MENU ------------------++')
    print('||  1. Model                                 ||')
    print('||  2. Brand                                 ||')
    print('||  3. Harga sewa                            ||')
    print('||  4. supir                                 ||')
    print('||  0. Kembali ke menu admin                 ||')
    print('++===========================================++')
    menu_searching_seq = int(input('Masukkan pilihan Anda : '))
    
    
    while (menu_searching_seq != 1) and (menu_searching_seq != 2)  and (menu_searching_seq != 3)  and (menu_searching_seq != 4) and (menu_searching_seq != 0):
        os.system('clear')
        print('++===========================================++')
        print('||                 KOKO RENTAL               ||')
        print('++===========================================++')
        print('||                                           ||')
        print('++------------------- MENU ------------------++')
        print('||  1. Model                                 ||')
        print('||  2. Brand                                 ||')
        print('||  3. Harga sewa                            ||')
        print('||  4. supir                                 ||')
        print('||  0. Kembali ke menu admin                 ||')
        print('++===========================================++')
        menu_searching_seq = int(input('Masukkan pilihan Anda : '))
    return menu_searching_seq

def fungsi_tampil_menu_searching_binary_admin(menu_searching_binary):
    print('++===========================================++')
    print('||                 KOKO RENTAL               ||')
    print('++===========================================++')
    print('||                                           ||')
    print('++------------------- MENU ------------------++')
    print('||  1. Plat Nomor                            ||')
    print('||  2. Nomor Telephone Supir                 ||')
    print('||  0. Kembali ke menu admin                 ||')
    print('++===========================================++')
    menu_searching_binary = int(input('Masukkan pilihan Anda : '))
    
    
    while (menu_searching_binary != 1) and (menu_searching_binary != 2) and (menu_searching_binary != 0):
        os.system('clear')
        print('++===========================================++')
        print('||                 KOKO RENTAL               ||')
        print('++===========================================++')
        print('||                                           ||')
        print('++------------------- MENU ------------------++')
        print('||  1. Sequential Search                     ||')
        print('||  2. Binary Search                         ||')
        print('||  0. Kembali ke menu admin                 ||')
        print('++===========================================++')
        menu_searching_binary = int(input('Masukkan pilihan Anda : '))
    return menu_searching_binary

def main():
    # DEKLARASI VARIABEL
    
    # var menu
    menu_utama = 0
    menu_admin = 0
    menu_crud  = 0
    menu_sorting = 0
    menu_sorting_asc = 0
    menu_sorting_desc = 0
    menu_searching = 0
    menu_searching_seq = 0
    menu_searching_binary = 0
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
                                        prosedur_reset_data_rental(plat_nomor, model, brand, harga_sewa, supir, nomor_supir)
                                        banyak_data = 0
                                    case 7:
                                        prosedur_menghitung_rata_rata_data_rental(harga_sewa)
                                    case 8:
                                        prosedur_min_max_data_rental(plat_nomor, harga_sewa)
                                    case 77:
                                        banyak_data = DEBUG_DUMMY_DATA(plat_nomor, model, brand, harga_sewa, supir, nomor_supir)
                                menu_crud = fungsi_tampil_menu_crud_admin(menu_crud)
                        case 2:
                            menu_sorting = fungsi_tampil_menu_sorting_admin(menu_sorting)
                            while(menu_sorting != 0):
                                match menu_sorting:
                                    case 1:
                                        menu_sorting_asc = fungsi_tampil_menu_sorting_asc_admin(menu_sorting_asc)
                                        while(menu_sorting_asc != 0):
                                            match menu_sorting_asc:
                                                case 1:
                                                    prosedur_sorting_asc(plat_nomor, model, brand, harga_sewa, supir, nomor_supir, plat_nomor)
                                                case 2:
                                                    prosedur_sorting_asc(plat_nomor, model, brand, harga_sewa, supir, nomor_supir, model)
                                                case 3:
                                                    prosedur_sorting_asc(plat_nomor, model, brand, harga_sewa, supir, nomor_supir, brand)
                                                case 4:
                                                    prosedur_sorting_asc(plat_nomor, model, brand, harga_sewa, supir, nomor_supir, harga_sewa)
                                                case 5:
                                                    prosedur_sorting_asc(plat_nomor, model, brand, harga_sewa, supir, nomor_supir, supir)
                                                case 6:
                                                    prosedur_sorting_asc(plat_nomor, model, brand, harga_sewa, supir, nomor_supir, nomor_supir)
                                                case 77:
                                                    banyak_data = DEBUG_DUMMY_DATA(plat_nomor, model, brand, harga_sewa, supir, nomor_supir)
                                            input('asc bos')
                                            menu_sorting_asc = fungsi_tampil_menu_sorting_asc_admin(menu_sorting_asc)
                                    case 2:
                                        menu_sorting_desc = fungsi_tampil_menu_sorting_desc_admin(menu_sorting_desc)
                                        while(menu_sorting_desc != 0):
                                            match menu_sorting_desc:
                                                case 1:
                                                    prosedur_sorting_desc(plat_nomor, model, brand, harga_sewa, supir, nomor_supir, plat_nomor)
                                                case 2:
                                                    prosedur_sorting_desc(plat_nomor, model, brand, harga_sewa, supir, nomor_supir, model)
                                                case 3:
                                                    prosedur_sorting_desc(plat_nomor, model, brand, harga_sewa, supir, nomor_supir, brand)
                                                case 4:
                                                    prosedur_sorting_desc(plat_nomor, model, brand, harga_sewa, supir, nomor_supir, harga_sewa)
                                                case 5:
                                                    prosedur_sorting_desc(plat_nomor, model, brand, harga_sewa, supir, nomor_supir, supir)
                                                case 6:
                                                    prosedur_sorting_desc(plat_nomor, model, brand, harga_sewa, supir, nomor_supir, nomor_supir)
                                                case 77:
                                                    banyak_data = DEBUG_DUMMY_DATA(plat_nomor, model, brand, harga_sewa, supir, nomor_supir)
                                            input('desc bos')
                                            menu_sorting_desc = fungsi_tampil_menu_sorting_desc_admin(menu_sorting_desc)
                                input('coba sort')
                                menu_sorting = fungsi_tampil_menu_sorting_admin(menu_sorting)
                        case 3:
                            menu_searching = fungsi_tampil_menu_searching_admin(menu_searching)
                            while menu_searching != 0:
                                match menu_searching:
                                    case 1:
                                        menu_searching_seq = fungsi_tampil_menu_searching_seq_admin(menu_searching_seq)
                                        while(menu_searching_seq != 0):
                                            match menu_searching_seq:
                                                case 1:
                                                    prosedur_searching_seq(plat_nomor, model, brand, harga_sewa, supir, nomor_supir, model, banyak_data)
                                                case 2:
                                                    prosedur_searching_seq(plat_nomor, model, brand, harga_sewa, supir, nomor_supir, brand, banyak_data)
                                                case 3:
                                                    prosedur_searching_seq_int(plat_nomor, model, brand, harga_sewa, supir, nomor_supir, harga_sewa, banyak_data)
                                                case 4:
                                                    prosedur_searching_seq(plat_nomor, model, brand, harga_sewa, supir, nomor_supir, supir, banyak_data)
                                            menu_searching_seq = fungsi_tampil_menu_searching_seq_admin(menu_searching_seq)
                                    case 2:
                                        menu_searching_binary = fungsi_tampil_menu_searching_binary_admin(menu_searching_binary)
                                        while(menu_searching_binary != 0):
                                            match menu_searching_binary:
                                                case 1:
                                                    prosedur_search_binary(plat_nomor, model, brand, harga_sewa, supir, nomor_supir, plat_nomor, banyak_data)
                                                case 2:
                                                    prosedur_search_binary_int(plat_nomor, model, brand, harga_sewa, supir, nomor_supir, nomor_supir, banyak_data)
                                            menu_searching_binary = fungsi_tampil_menu_searching_binary_admin(menu_searching_binary)
                                    case 77:
                                        banyak_data = DEBUG_DUMMY_DATA(plat_nomor, model, brand, harga_sewa, supir, nomor_supir)
                                menu_searching = fungsi_tampil_menu_searching_admin(menu_searching)
                        case 0:
                            menu_utama = 0
                    input('bro')
                else:
                    menu_utama = 0
# Algoritma Utama
main()
print("Keluar aplikasi, selamat tinggall!!")