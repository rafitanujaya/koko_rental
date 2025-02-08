# fauzi
import os
# subrutin validasi login
def function_validasi_login(password):
    # variabel constant untuk login dan counter
    PASSWORD = 'admin123'
    percobaan = 0
    login = False
    while (password != PASSWORD) and percobaan < 2:
        print('Password atau Username salah!')
        os.system('pause')
        os.system('cls')
        percobaan += 1
        password = input('Password: ')
    if password == PASSWORD:
        login = True
        return login

# subrutin validasi jumlah unit mobil dan supir yang diinginkan
def function_maks_array(maks_array):
    while maks_array < 0:
        print('Maks Unit Tidak Boleh Negatif')
        maks_array = int(input('Masukkan Jumlah Unit : '))
    return maks_array


# subrutin validasi jumlah supir
def function_maks_supir(maks_supir):
    while maks_supir < 0:
        print('Maks Supir Tidak Boleh Negatif')
        maks_supir = int(input('Masukkan Jumlah Supir : '))
    return maks_supir


# subrutin validasi banyak data yang ingin ditraversal
def function_validasi_banyak_data(banyak_data, maks_array):
    while banyak_data < 0 or banyak_data > maks_array:
        print('Banyak Tidak Boleh Negatif atau Tidak Boleh Melebihi Maks Array')
        banyak_data = int(input('Masukkan Banyak Data Yang Ingin Diinput : '))
    return banyak_data


# subrutin traversal tambah seluruh array mobil
def procedure_traversal_mobil_supir(banyak_data, array_plat_mobil, array_brand_mobil, array_model_mobil, array_harga_mobil, array_nama_supir, array_nomor_supir):
    for i in range(banyak_data):
        array_brand_mobil[i] = str(input('Masukkan brand Mobil : '))
        array_model_mobil[i] = str(input('Masukkan model Mobil : '))
        array_plat_mobil[i] = str(input('Masukkan Plat Mobil : '))
        array_harga_mobil[i] = int(input('Masukkan harga Mobil : '))
        array_nama_supir[i] = str(input('Masukkan Nama Supir : '))
        array_nomor_supir[i] = str(input('Masukkan Nomor Supir : '))


# subrutin validasi pengurutan array
def function_validasi_menu_pengurutan(pilihan_menu_pengurutan):
    while pilihan_menu_pengurutan != 1 and pilihan_menu_pengurutan != 2:
        pilihan_menu_pengurutan = int(input('Masukkan Pilihan Urutan : '))
    return pilihan_menu_pengurutan


# subrutin validasi menu pilihan pengurutan ascending
def function_validasi_menu_bubble_sort(pilihan_menu_ascending):
    while pilihan_menu_ascending > 7 or pilihan_menu_ascending < 1:
        print('Menu ascending tidak tersedia, pilih ulang')
        pilihan_menu_ascending = int(input('Masukkan Pilihan Menu Sorting : '))
    return pilihan_menu_ascending

# subrutin bubble sort secara ascending tergantung brand
def procedure_pengurutan_bubble_asceding(temp_array_sorting, maks_array, array_plat_mobil, array_brand_mobil, array_model_mobil, array_harga_mobil, array_nomor_supir, array_nama_supir):
    for i in range((maks_array - 1) - 1):
        j = maks_array - 1
        while j >= i + 1:
            if temp_array_sorting[j] < temp_array_sorting[j - 1]:
                # model
                temp = array_model_mobil[j]
                array_model_mobil[j] = array_model_mobil[j - 1]
                array_model_mobil[j - 1] = temp
                # brand
                temp = array_brand_mobil[j]
                array_brand_mobil[j] = array_brand_mobil[j - 1]
                array_brand_mobil[j - 1] = temp
                # harga
                temp = array_harga_mobil[j]
                array_harga_mobil[j] = array_harga_mobil[j - 1]
                array_harga_mobil[j - 1] = temp
                # plat
                temp = array_plat_mobil[j]
                array_plat_mobil[j] = array_plat_mobil[j - 1]
                array_plat_mobil[j - 1] = temp
                # nomor supir
                temp = array_nomor_supir[j]
                array_nomor_supir[j] = array_nomor_supir[j - 1]
                array_nomor_supir[j - 1] = temp
                # nama supir
                temp = array_nama_supir[j]
                array_nama_supir[j] = array_nama_supir[j - 1]
                array_nama_supir[j - 1] = temp
            j -= 1

# subrutin bubble sort secara descending tergantung brand
def procedure_pengurutan_bubble_descending(temp_array_sorting, maks_array, array_plat_mobil, array_brand_mobil, array_model_mobil, array_harga_mobil, array_nomor_supir, array_nama_supir):
    for i in range((maks_array) - 1):
        for j in range((maks_array) - (i + 1)):
            if temp_array_sorting[j] < temp_array_sorting[j + 1]:
                # brand
                temp = array_brand_mobil[j]
                array_brand_mobil[j] = array_brand_mobil[j + 1]
                array_brand_mobil[j + 1] = temp
                # model
                temp = array_model_mobil[j]
                array_model_mobil[j] = array_model_mobil[j + 1]
                array_model_mobil[j + 1] = temp
                # plat
                temp = array_plat_mobil[j]
                array_plat_mobil[j] = array_plat_mobil[j + 1]
                array_plat_mobil[j + 1] = temp
                # harga
                temp = array_harga_mobil[j]
                array_harga_mobil[j] = array_harga_mobil[j + 1]
                array_harga_mobil[j + 1] = temp
                # nama supir
                temp = array_nama_supir[j]
                array_nama_supir[j] = array_nama_supir[j + 1]
                array_nama_supir[j + 1] = temp
                # nomor supir
                temp = array_nomor_supir[j]
                array_nomor_supir[j] = array_nomor_supir[j + 1]
                array_nomor_supir[j + 1] = temp


# subrutin penghapusan unit dalam array bergantung indeks dari plat nomor
def procedure_penghapusan_elemen(banyak_data, indeks_dihapus, array_plat_mobil, array_brand_mobil, array_model_mobil, array_harga_mobil, array_nama_supir, array_nomor_supir):
    if banyak_data > 0:
        if indeks_dihapus >= 0 and indeks_dihapus <= banyak_data:
            for i in range(indeks_dihapus, banyak_data - 1):
                array_brand_mobil[i - 1] = array_brand_mobil[i]
                array_model_mobil[i - 1] = array_model_mobil[i]
                array_plat_mobil[i - 1] = array_plat_mobil[i]
                array_harga_mobil[i - 1] = array_harga_mobil[i]
                array_nama_supir[i - 1] = array_nama_supir[i]
                array_nomor_supir[i - 1] = array_nomor_supir[i]
            array_brand_mobil[banyak_data - 1] = 0
            array_model_mobil[banyak_data - 1] = 0
            array_plat_mobil[banyak_data - 1] = 0
            array_harga_mobil[banyak_data - 1] = 0
            array_nama_supir[banyak_data - 1] = 0
            array_nomor_supir[banyak_data - 1] = 0
        else:
            print('Posisi tidak valid')
    else:
        print('Data Kosong')


# subrutin untuk tampilan tabel menggunakan traversal
def procedure_traversal_tampilan(banyak_data, array_plat_mobil, array_brand_mobil, array_model_mobil, array_harga_mobil, array_nama_supir, array_nomor_supir):
    print(
        '------------------------------------------------------------------------------------------------------------')
    print(
        '| No | Brand Mobil |   Model   |   Harga Mobil   | Plat Nomor |      Nama Supir      | Nomor Telepon Supir |')
    print(
        '------------------------------------------------------------------------------------------------------------')
    for i in range(banyak_data):
        print(
            f'| {i + 1:>2} | {array_brand_mobil[i]:11} | {array_model_mobil[i]:9} | Rp {array_harga_mobil[i]:12} | {array_plat_mobil[i]:10} | {array_nama_supir[i]:20} |     {array_nomor_supir[i]:15} |')
    print(
        '------------------------------------------------------------------------------------------------------------')


# subrutin validasi menu pilihan yang dicari
def function_validasi_sequential(hal_dicari):
    while hal_dicari < 1 or hal_dicari > 4:
        print('Pilihan tidak valid')
        os.system('pause')
        os.system('cls')
        print('Silahkan Pilih Ulang!')
        print('1. Brand mobil')
        print('2. Model mobil')
        print('3. Harga mobil')
        print('4. Nama supir')
        hal_dicari = int('Mau cari apa? [1-4] : ')
    return hal_dicari


# subrutin sequential search tanpa sentinel dan boolean
def procedure_sequential_tanpa_sentinel(data_dicari, banyak_data, temp_array, array_plat_mobil, array_brand_mobil, array_model_mobil, array_harga_mobil, array_nama_supir, array_nomor_supir):
    i = 0
    while temp_array[i] != data_dicari and i < banyak_data - 1:
        i += 1
    if temp_array[i] == data_dicari and i < banyak_data - 1:
        print('Data Ditemukan!')
        print(f'Nama Brand    : {array_brand_mobil[i]}')
        print(f'Nama Model    : {array_model_mobil[i]}')
        print(f'Plat Nomor    : {array_plat_mobil[i]}')
        print(f'Harga         : {array_harga_mobil[i]}')
        print(f'Nama Supir    : {array_nama_supir[i]}')
        print(f'Nomor Telepon : {array_nomor_supir[i]}')
    else:
        print('Maaf Data Tidak Ditemukan')


# subrutin pencarian sequential dengan boolean
def procedure_sequential_boolean(data_dicari, banyak_data, temp_array, array_plat_mobil, array_brand_mobil, array_model_mobil, array_harga_mobil, array_nama_supir, array_nomor_supir):
    i = 0
    ketemu = False
    while not ketemu and i <= banyak_data - 1:
        if temp_array[i] == data_dicari:
            ketemu = True
        else:
            i += 1
    if ketemu:
        print('Data Ditemukan!')
        print(f'Nama Brand    : {array_brand_mobil[i]}')
        print(f'Nama Model    : {array_model_mobil[i]}')
        print(f'Plat Nomor    : {array_plat_mobil[i]}')
        print(f'Harga         : {array_harga_mobil[i]}')
        print(f'Nama Supir    : {array_nama_supir[i]}')
        print(f'Nomor Telepon : {array_nomor_supir[i]}')
    else:
        print('Maaf Data Tidak Ditemukan')


# subrutin pencarian binary
def procedure_binary(data_dicari, banyak_data, temp_array, array_plat_mobil, array_brand_mobil, array_model_mobil, array_harga_mobil, array_nama_supir, array_nomor_supir):
    ia = 0
    ib = banyak_data - 1
    ketemu = False
    while not ketemu and ia <= ib:
        k = (ia + ib) // 2
        if temp_array[k] == data_dicari:
            ketemu = True
        else:
            if temp_array[k] < data_dicari:
                ia = k + 1
            else:
                ib = k - 1
    if ketemu:
        print('Data Ditemukan!')
        print(f'Nama Brand    : {array_brand_mobil[k]}')
        print(f'Nama Model    : {array_model_mobil[k]}')
        print(f'Plat Nomor    : {array_plat_mobil[k]}')
        print(f'Harga         : {array_harga_mobil[k]}')
        print(f'Nama Supir    : {array_nama_supir[k]}')
        print(f'Nomor Telepon : {array_nomor_supir[k]}')
    else:
        print('Maaf Data Tidak Ditemukan')

#subrutin tambah array
def function_tambah_array(maks_array, banyak_data, array_plat_mobil, array_brand_mobil, array_model_mobil, array_harga_mobil, array_nama_supir, array_nomor_supir) :
    if banyak_data >= maks_array:
        print('Array sudah penuh!')
        return banyak_data
    else :
        array_brand_mobil[banyak_data] = str(input('Masukkan brand Mobil : '))
        array_model_mobil[banyak_data] = str(input('Masukkan model Mobil : '))
        array_plat_mobil[banyak_data] = str(input('Masukkan Plat Mobil : '))
        array_harga_mobil[banyak_data] = int(input('Masukkan harga Mobil : '))
        array_nama_supir[banyak_data] = str(input('Masukkan Nama Supir : '))
        array_nomor_supir[banyak_data] = str(input('Masukkan Nomor Supir : '))
        return banyak_data + 1

# program utama
os.system('cls')
password = str(input('Password: '))
login = function_validasi_login(password)
if login:
    print('Menu pilihan')
    print('1. Traversal tambah Array')
    print('2. Hapus Elemen Array')
    print('3. Tambah Array')
    print('4. Pengurutan Array')
    print('5. Pencarian Array')
    print('6. Penghancuran Array')
    print('7. Penciptaan Array')
    print('8. Tampilkan Array')
    print('0. Keluar Program')
    menu_pilihan = int(input('Masukkan Menu Pilihan : '))
    while menu_pilihan != 0:
        if menu_pilihan != 7:
            print('Silahkan pilih menu no. 7 dulu')
        match (menu_pilihan):
            case 1:
                print('Menu Traversal Array')
                banyak_data = int(input('Masukkan Banyak Data Yang Ingin Diinput : '))
                banyak_data = function_validasi_banyak_data(banyak_data, maks_array)
                os.system('pause')
                os.system('cls')
                print('Silahkan Tambahkan Data Mobil Terbaru')
                procedure_traversal_mobil_supir(banyak_data, array_plat_mobil, array_brand_mobil, array_model_mobil, array_harga_mobil, array_nama_supir, array_nomor_supir)
            case 2:
                print('Hapus Elemen Array')
                os.system('pause')
                os.system('cls')
                indeks_dihapus = int(input('Masukkan Indeks Yang Dihapus : '))
                procedure_penghapusan_elemen(banyak_data, indeks_dihapus, array_plat_mobil, array_brand_mobil, array_model_mobil, array_harga_mobil, array_nama_supir, array_nomor_supir)
            case 3:
                print('Tambah Array')
                print('Menambahkan array di elemen paling akhir')
                banyak_data = function_tambah_array(maks_array, banyak_data, array_plat_mobil, array_brand_mobil, array_model_mobil, array_harga_mobil, array_nama_supir, array_nomor_supir)
            case 4:
                print('Pengurutan Array')
                print('1. Pengurutan secara ascending')
                print('2. Pengurutan secara descending')
                pilihan_menu_pengurutan = int(input('Masukkan Pilihan Urutan : '))
                pilihan_menu_pengurutan = function_validasi_menu_pengurutan(pilihan_menu_pengurutan)
                match (pilihan_menu_pengurutan):
                    case 1:
                        print('Pengurutan bubble secara ascending')
                        print('1. Pengurutan sesuai brand mobil')
                        print('2. Pengurutan sesuai model mobil')
                        print('3. Pengurutan sesuai harga mobil')
                        print('4. Pengurutan sesuai plat mobil')
                        print('5. Pengurutan sesuai nama supir')
                        print('6. Pengurutan sesuai nomor supir')
                        pilihan_menu_bubble_sort = int(input('Masukkan Pilihan Menu Sorting : '))
                        pilihan_menu_bubble_sort = function_validasi_menu_bubble_sort(pilihan_menu_bubble_sort)
                        match (pilihan_menu_bubble_sort):
                            case 1:
                                print('Pengurutan sesuai brand mobil')
                                temp_array_sorting = array_brand_mobil
                                procedure_pengurutan_bubble_asceding(temp_array_sorting, maks_array, array_plat_mobil, array_brand_mobil, array_model_mobil, array_harga_mobil, array_nomor_supir, array_nama_supir)
                            case 2:
                                print('Pengurutan sesuai model mobil')
                                temp_array_sorting = array_model_mobil
                                procedure_pengurutan_bubble_asceding(temp_array_sorting, maks_array, array_plat_mobil, array_brand_mobil, array_model_mobil, array_harga_mobil, array_nomor_supir, array_nama_supir)
                            case 3:
                                print('Pengurutan sesuai harga mobil')
                                temp_array_sorting = array_harga_mobil
                                procedure_pengurutan_bubble_asceding(temp_array_sorting, maks_array, array_plat_mobil, array_brand_mobil, array_model_mobil, array_harga_mobil, array_nomor_supir, array_nama_supir)
                            case 4:
                                print('Pengurutan sesuai plat mobil')
                                temp_array_sorting = array_plat_mobil
                                procedure_pengurutan_bubble_asceding(temp_array_sorting, maks_array, array_plat_mobil, array_brand_mobil, array_model_mobil, array_harga_mobil, array_nomor_supir, array_nama_supir)
                            case 5:
                                print('Pengurutan sesuai nama supir')
                                temp_array_sorting = array_nama_supir
                                procedure_pengurutan_bubble_asceding(temp_array_sorting, maks_array, array_plat_mobil, array_brand_mobil, array_model_mobil, array_harga_mobil, array_nomor_supir, array_nama_supir)
                            case 6:
                                print('Pengurutan sesuai nomor supir')
                                temp_array_sorting = array_nomor_supir
                                procedure_pengurutan_bubble_asceding(temp_array_sorting, maks_array, array_plat_mobil, array_brand_mobil, array_model_mobil, array_harga_mobil, array_nomor_supir, array_nama_supir)
                    case 2:
                        print('Pengurutan bubble secara descending')
                        print('1. Pengurutan sesuai brand mobil')
                        print('2. Pengurutan sesuai model mobil')
                        print('3. Pengurutan sesuai harga mobil')
                        print('4. Pengurutan sesuai plat mobil')
                        print('5. Pengurutan sesuai nama supir')
                        print('6. Pengurutan sesuai nomor supir')
                        pilihan_menu_bubble_sort = int(input('Masukkan Pilihan Menu Sorting : '))
                        pilihan_menu_bubble_sort = function_validasi_menu_bubble_sort(pilihan_menu_bubble_sort)
                        match (pilihan_menu_bubble_sort):
                            case 1:
                                print('Pengurutan sesuai brand mobil')
                                temp_array_sorting = array_brand_mobil
                                procedure_pengurutan_bubble_descending(temp_array_sorting, maks_array, array_plat_mobil,array_brand_mobil, array_model_mobil,array_harga_mobil, array_nomor_supir,array_nama_supir)
                            case 2:
                                print('Pengurutan sesuai model mobil')
                                temp_array_sorting = array_model_mobil
                                procedure_pengurutan_bubble_descending(temp_array_sorting, maks_array, array_plat_mobil, array_brand_mobil, array_model_mobil, array_harga_mobil, array_nomor_supir, array_nama_supir)
                            case 3:
                                print('Pengurutan sesuai harga mobil')
                                temp_array_sorting = array_harga_mobil
                                procedure_pengurutan_bubble_descending(temp_array_sorting, maks_array, array_plat_mobil, array_brand_mobil, array_model_mobil, array_harga_mobil, array_nomor_supir, array_nama_supir)
                            case 4:
                                print('Pengurutan sesuai plat mobil')
                                temp_array_sorting = array_plat_mobil
                                procedure_pengurutan_bubble_descending(temp_array_sorting, maks_array, array_plat_mobil, array_brand_mobil, array_model_mobil, array_harga_mobil, array_nomor_supir, array_nama_supir)
                            case 5:
                                print('Pengurutan sesuai nama supir')
                                temp_array_sorting = array_nama_supir
                                procedure_pengurutan_bubble_descending(temp_array_sorting, maks_array, array_plat_mobil,array_brand_mobil, array_model_mobil, array_harga_mobil, array_nomor_supir, array_nama_supir)
                            case 6:
                                print('Pengurutan sesuai nomor supir')
                                temp_array_sorting = array_nomor_supir
                                procedure_pengurutan_bubble_descending(temp_array_sorting, maks_array, array_plat_mobil, array_brand_mobil, array_model_mobil, array_harga_mobil, array_nomor_supir, array_nama_supir)
            case 5 :
                print('Pencarian Array')
                print('1. Metode Pencarian Sequential')
                print('2. Metode Pencarian Binary')
                metode_pencarian = int(input('Masukkan Metode Pencarian : '))
                match (metode_pencarian):
                    case 1:
                        # procedure_traversal_tampilan(banyak_data, array_plat_mobil, array_brand_mobil, array_model_mobil, array_harga_mobil, array_nama_supir, array_nomor_supir)
                        print('Metode Pencarian')
                        print('1. Pencarian Sequential tanpa sentinel dan boolean')
                        print('2. Pencarian Sequential dengan boolean')
                        pencarian_sequential = int(input('Masukkan Metode Pencarian : '))
                        match (pencarian_sequential):
                            case 1:
                                print('Pencarian Sequential tanpa sentinel dan boolean')
                                print('1. Brand mobil')
                                print('2. Model mobil')
                                print('3. Harga mobil')
                                print('4. Nama supir')
                                hal_dicari = int('Mau cari apa? [1-4] : ')
                                hal_dicari = function_validasi_sequential(hal_dicari)
                                match (hal_dicari):
                                    case 1:
                                        data_dicari = str(input('Masukkan brand mobil yang dicari : '))
                                        temp_array = array_brand_mobil
                                        pencarian = procedure_sequential_tanpa_sentinel(data_dicari, banyak_data, temp_array, array_plat_mobil, array_brand_mobil, array_model_mobil, array_harga_mobil, array_nama_supir, array_nomor_supir)
                                    case 2:
                                        data_dicari = str(input('Masukkan model mobil yang dicari : '))
                                        temp_array = array_model_mobil
                                        pencarian = procedure_sequential_tanpa_sentinel(data_dicari, banyak_data,temp_array, array_plat_mobil, array_brand_mobil, array_model_mobil, array_harga_mobil, array_nama_supir, array_nomor_supir)
                                    case 3:
                                        data_dicari = int(input('Masukkan harga mobil yang dicari : '))
                                        temp_array = array_harga_mobil
                                        pencarian = procedure_sequential_tanpa_sentinel(data_dicari, banyak_data, temp_array, array_plat_mobil, array_brand_mobil, array_model_mobil, array_harga_mobil, array_nama_supir, array_nomor_supir)
                                    case 4:
                                        data_dicari = str(input('Masukkan nama supir yang dicari : '))
                                        temp_array = array_nama_supir
                                        pencarian = procedure_sequential_tanpa_sentinel(data_dicari, banyak_data, temp_array, array_plat_mobil, array_brand_mobil, array_model_mobil, array_harga_mobil, array_nama_supir, array_nomor_supir)
                            case 2:
                                print('Pencarian Sequential dengan boolean')
                                print('1. Brand mobil')
                                print('2. Model mobil')
                                print('3. Harga mobil')
                                print('4. Nama supir')
                                hal_dicari = int('Mau cari apa? [1-4] : ')
                                hal_dicari = function_validasi_sequential(hal_dicari)
                                match (hal_dicari):
                                    case 1:
                                        data_dicari = str(input('Masukkan brand mobil yang dicari : '))
                                        temp_array = array_brand_mobil
                                        procedure_sequential_boolean(data_dicari, banyak_data, temp_array, array_plat_mobil, array_brand_mobil, array_model_mobil, array_harga_mobil, array_nama_supir, array_nomor_supir)
                                    case 2:
                                        data_dicari = str(input('Masukkan model mobil yang dicari : '))
                                        temp_array = array_model_mobil
                                        procedure_sequential_boolean(data_dicari, banyak_data, temp_array, array_plat_mobil, array_brand_mobil, array_model_mobil, array_harga_mobil, array_nama_supir, array_nomor_supir)
                                    case 3:
                                        data_dicari = int(input('Masukkan harga mobil yang dicari : '))
                                        temp_array = array_harga_mobil
                                        procedure_sequential_boolean(data_dicari, banyak_data, temp_array, array_plat_mobil, array_brand_mobil, array_model_mobil, array_harga_mobil, array_nama_supir, array_nomor_supir)
                                    case 4:
                                        data_dicari = str(input('Masukkan nama supir yang dicari : '))
                                        temp_array = array_nama_supir
                                        procedure_sequential_boolean(data_dicari, banyak_data, temp_array, array_plat_mobil, array_brand_mobil, array_model_mobil, array_harga_mobil, array_nama_supir, array_nomor_supir)
                    case 2:
                        print('Metode Pencarian Binary')
                        print('1. Plat Nomor Mobil')
                        print('2. Nomor Telepon Supir')
                        pencarian_binary = int(input('Mau cari apa? [1-2] : '))
                        match (pencarian_binary):
                            case 1 :
                                data_dicari = str(input('Masukkan plat nomor mobil yang dicari : '))
                                temp_array = array_plat_mobil
                                procedure_binary(data_dicari, banyak_data, temp_array, array_plat_mobil, array_brand_mobil, array_model_mobil, array_harga_mobil, array_nama_supir, array_nomor_supir)
                            case 2 :
                                data_dicari = str(input('Masukkan nomor telepon supir yang dicari : '))
                                temp_array = array_nomor_supir
                                procedure_binary(data_dicari, banyak_data, temp_array, array_plat_mobil, array_brand_mobil, array_model_mobil, array_harga_mobil, array_nama_supir, array_nomor_supir)
            case 6 :
                print('Penghancuran Array')
                persetujuan = str('Yakin Mau Reset Array? [y/n] : ').lower()
                if persetujuan == 'y':
                    array_brand_mobil *= 0
                    array_model_mobil *= 0
                    array_plat_mobil *= 0
                    array_harga_mobil *= 0
                    array_nama_supir *= 0
                    array_nomor_supir *= 0
                else :
                    print('ok')
            case 7 :
                maks_array = int(input('Masukkan Jumlah Elemen Kosong : '))
                maks_array_mobil = function_maks_array(maks_array)
                array_plat_mobil = ['/'] * maks_array_mobil
                array_brand_mobil = ['/'] * maks_array_mobil
                array_model_mobil = ['/'] * maks_array_mobil
                array_harga_mobil = [0] * maks_array_mobil
                array_nama_supir = ['/'] * maks_array_mobil
                array_nomor_supir = ['/'] * maks_array_mobil
            case 8 :
                print(f'{array_brand_mobil}')
                print(f'{array_model_mobil}')
                print(f'{array_plat_mobil}')
                print(f'{array_harga_mobil}')
                print(f'{array_nama_supir}')
                print(f'{array_nomor_supir}')
                os.system('pause')
                os.system('cls')

        print('Menu pilihan')
        print('1. Traversal Array')
        print('2. Hapus Elemen Array')
        print('3. Tambah Array')
        print('4. Pengurutan Array')
        print('5. Pencarian Array')
        print('6. Penghancuran Array')
        print('7. Penciptaan Array')
        print('8. Tampilkan Array')
        print('0. Keluar Program')
        menu_pilihan = int(input('Masukkan Menu Pilihan : '))
else:
    print('Maaf, Login anda gagal')