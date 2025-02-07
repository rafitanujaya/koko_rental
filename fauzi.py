# fauzi
import os

#subrutin validasi login
def function_validasi_login(password) :
    #variabel constant untuk login dan counter
    PASSWORD = 'admin123'
    counter = 0
    login = False
    while (password != PASSWORD) and counter < 2:
        print('Password atau Username salah!')
        os.system('pause')
        os.system('cls')
        counter += 1
        password = input('Password: ')
    if password == PASSWORD:
        login = True
        return login

#subrutin validasi jumlah mobil yang diinginkan
def function_maks_array(maks_array) :
    while maks_array < 0 :
        print('Maks Mobil Tidak Boleh Negatif')
        maks_array = int(input('Masukkan Jumlah Mobil : '))
    return maks_array

#subrutin validasi jumlah supir
def function_maks_supir(maks_supir) :
    while maks_supir < 0 :
        print('Maks Supir Tidak Boleh Negatif')
        maks_supir = int(input('Masukkan Jumlah Supir : '))
    return maks_supir

#subrutin tambah seluruh array mobil
def procedure_tambah_mobil(maks_array, array_plat_mobil, array_brand_mobil, array_model_mobil, array_harga_mobil) :
    for i in range(maks_array) :
        array_brand_mobil[i] = str(input('Masukkan brand Mobil : '))
        array_model_mobil[i] = str(input('Masukkan model Mobil : '))
        array_harga_mobil[i] = int(input('Masukkan harga Mobil : '))
        array_plat_mobil[i] = str(input('Masukkan Plat Mobil : '))

#subrutin tambah seluruh array supir
def procedure_tambah_supir(maks_array, array_nama_supir, array_nomor_supir) :
    for i in range(maks_array) :
        array_nama_supir[i] = str(input('Masukkan Nama Supir : '))
        array_nomor_supir[i] = str(input('Masukkan Nomor Supir : '))

#subrutin validasi pengurutan array
def function_validasi_menu_pengurutan(pilihan_menu_pengurutan) :
    while pilihan_menu_pengurutan != 1 and pilihan_menu_pengurutan != 2 :
        pilihan_menu_pengurutan = int(input('Masukkan Pilihan Urutan : '))
    return pilihan_menu_pengurutan

#subrutin validasi menu pilihan pengurutan ascending
def function_validasi_menu_ascending(pilihan_menu_ascending) :
    while pilihan_menu_ascending > 6 or pilihan_menu_ascending < 1:
        print('Menu ascending tidak tersedia, pilih ulang')
        pilihan_menu_ascending = int(input('Masukkan Pilihan Menu Sorting : '))
    return pilihan_menu_ascending

#subrutin bubble sort secara ascending tergantung brand
def procedure_pengurutan_brand_asceding(maks_array, array_plat_mobil, array_brand_mobil, array_model_mobil, array_harga_mobil, array_nomor_supir, array_nama_supir) :
    for i in range(maks_array - 1) :
        j = maks_array
        while j >= i + 1 :
            if array_brand_mobil[j] < array_brand_mobil[j-1] :
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
                print(f'{array_brand_mobil}')
                print(f'{array_model_mobil}')
                print(f'{array_plat_mobil}')
                print(f'{array_harga_mobil}')
                print(f'{array_nama_supir}')
                print(f'{array_nomor_supir}')

#subrutin bubble sort secara ascending tergantung model
def procedure_pengurutan_model_ascending(maks_array, array_plat_mobil, array_brand_mobil, array_model_mobil, array_harga_mobil, array_nomor_supir, array_nama_supir) :
    for i in range(maks_array - 1) :
        j = maks_array
        while j >= i + 1 :
            if array_model_mobil[j] < array_model_mobil[j-1] :
                #model
                temp = array_model_mobil[j]
                array_model_mobil[j] = array_model_mobil[j-1]
                array_model_mobil[j-1] = temp
                #brand
                temp = array_brand_mobil[j]
                array_brand_mobil[j] = array_brand_mobil[j-1]
                array_brand_mobil[j-1] = temp
                #harga
                temp = array_harga_mobil[j]
                array_harga_mobil[j] = array_harga_mobil[j-1]
                array_harga_mobil[j-1] = temp
                #plat
                temp = array_plat_mobil[j]
                array_plat_mobil[j] = array_plat_mobil[j-1]
                array_plat_mobil[j-1] = temp
                #nomor supir
                temp = array_nomor_supir[j]
                array_nomor_supir[j] = array_nomor_supir[j-1]
                array_nomor_supir[j-1] = temp
                #nama supir
                temp = array_nama_supir[j]
                array_nama_supir[j] = array_nama_supir[j-1]
                array_nama_supir[j-1] = temp
                print(f'{array_brand_mobil}')
                print(f'{array_model_mobil}')
                print(f'{array_plat_mobil}')
                print(f'{array_harga_mobil}')
                print(f'{array_nama_supir}')
                print(f'{array_nomor_supir}')

#subrutin bubble sort secara ascending tergantung plat
def procedure_pengurutan_plat_ascending(maks_array, array_plat_mobil, array_brand_mobil, array_model_mobil, array_harga_mobil, array_nomor_supir, array_nama_supir) :
    for i in range(maks_array - 1) :
        j = maks_array
        while j >= i + 1 :
            if array_plat_mobil[j] < array_plat_mobil[j-1] :
                #model
                temp = array_model_mobil[j]
                array_model_mobil[j] = array_model_mobil[j-1]
                array_model_mobil[j-1] = temp
                #brand
                temp = array_brand_mobil[j]
                array_brand_mobil[j] = array_brand_mobil[j-1]
                array_brand_mobil[j-1] = temp
                #harga
                temp = array_harga_mobil[j]
                array_harga_mobil[j] = array_harga_mobil[j-1]
                array_harga_mobil[j-1] = temp
                #plat
                temp = array_plat_mobil[j]
                array_plat_mobil[j] = array_plat_mobil[j-1]
                array_plat_mobil[j-1] = temp
                #nomor supir
                temp = array_nomor_supir[j]
                array_nomor_supir[j] = array_nomor_supir[j-1]
                array_nomor_supir[j-1] = temp
                #nama supir
                temp = array_nama_supir[j]
                array_nama_supir[j] = array_nama_supir[j-1]
                array_nama_supir[j-1] = temp
                print(f'{array_brand_mobil}')
                print(f'{array_model_mobil}')
                print(f'{array_plat_mobil}')
                print(f'{array_harga_mobil}')
                print(f'{array_nama_supir}')
                print(f'{array_nomor_supir}')

#subrutin bubble sort secara ascending tergantung harga
def procedure_pengurutan_harga_ascending(maks_array, array_plat_mobil, array_brand_mobil, array_model_mobil, array_harga_mobil, array_nomor_supir, array_nama_supir) :
    for i in range(maks_array - 1) :
        j = maks_array
        while j >= i + 1 :
            if array_harga_mobil[j] < array_harga_mobil[j-1] :
                #model
                temp = array_model_mobil[j]
                array_model_mobil[j] = array_model_mobil[j-1]
                array_model_mobil[j-1] = temp
                #brand
                temp = array_brand_mobil[j]
                array_brand_mobil[j] = array_brand_mobil[j-1]
                array_brand_mobil[j-1] = temp
                #harga
                temp = array_harga_mobil[j]
                array_harga_mobil[j] = array_harga_mobil[j-1]
                array_harga_mobil[j-1] = temp
                #plat
                temp = array_plat_mobil[j]
                array_plat_mobil[j] = array_plat_mobil[j-1]
                array_plat_mobil[j-1] = temp
                #nomor supir
                temp = array_nomor_supir[j]
                array_nomor_supir[j] = array_nomor_supir[j-1]
                array_nomor_supir[j-1] = temp
                #nama supir
                temp = array_nama_supir[j]
                array_nama_supir[j] = array_nama_supir[j-1]
                array_nama_supir[j-1] = temp
                print(f'{array_brand_mobil}')
                print(f'{array_model_mobil}')
                print(f'{array_plat_mobil}')
                print(f'{array_harga_mobil}')
                print(f'{array_nama_supir}')
                print(f'{array_nomor_supir}')

#subrutin bubble sort secara ascending tergantung nama supir
def procedure_pengurutan_nama_supir_ascending(maks_array, array_plat_mobil, array_brand_mobil, array_model_mobil, array_harga_mobil, array_nomor_supir, array_nama_supir) :
    for i in range(maks_array - 1) :
        j = maks_array
        while j >= i + 1 :
            if array_nama_supir[j] < array_nama_supir[j-1] :
                #model
                temp = array_model_mobil[j]
                array_model_mobil[j] = array_model_mobil[j-1]
                array_model_mobil[j-1] = temp
                #brand
                temp = array_brand_mobil[j]
                array_brand_mobil[j] = array_brand_mobil[j-1]
                array_brand_mobil[j-1] = temp
                #harga
                temp = array_harga_mobil[j]
                array_harga_mobil[j] = array_harga_mobil[j-1]
                array_harga_mobil[j-1] = temp
                #plat
                temp = array_plat_mobil[j]
                array_plat_mobil[j] = array_plat_mobil[j-1]
                array_plat_mobil[j-1] = temp
                #nomor supir
                temp = array_nomor_supir[j]
                array_nomor_supir[j] = array_nomor_supir[j-1]
                array_nomor_supir[j-1] = temp
                #nama supir
                temp = array_nama_supir[j]
                array_nama_supir[j] = array_nama_supir[j-1]
                array_nama_supir[j-1] = temp
                print(f'{array_brand_mobil}')
                print(f'{array_model_mobil}')
                print(f'{array_plat_mobil}')
                print(f'{array_harga_mobil}')
                print(f'{array_nama_supir}')
                print(f'{array_nomor_supir}')

#subrutin bubble sort secara ascending tergantung nomor supir
def procedure_pengurutan_nomor_supir_ascending(maks_array, array_plat_mobil, array_brand_mobil, array_model_mobil, array_harga_mobil, array_nomor_supir, array_nama_supir) :
    for i in range(maks_array - 1) :
        j = maks_array
        while j >= i + 1 :
            if array_nomor_supir[j] < array_nomor_supir[j-1] :
                #model
                temp = array_model_mobil[j]
                array_model_mobil[j] = array_model_mobil[j-1]
                array_model_mobil[j-1] = temp
                #brand
                temp = array_brand_mobil[j]
                array_brand_mobil[j] = array_brand_mobil[j-1]
                array_brand_mobil[j-1] = temp
                #harga
                temp = array_harga_mobil[j]
                array_harga_mobil[j] = array_harga_mobil[j-1]
                array_harga_mobil[j-1] = temp
                #plat
                temp = array_plat_mobil[j]
                array_plat_mobil[j] = array_plat_mobil[j-1]
                array_plat_mobil[j-1] = temp
                #nomor supir
                temp = array_nomor_supir[j]
                array_nomor_supir[j] = array_nomor_supir[j-1]
                array_nomor_supir[j-1] = temp
                #nama supir
                temp = array_nama_supir[j]
                array_nama_supir[j] = array_nama_supir[j-1]
                array_nama_supir[j-1] = temp
                print(f'{array_brand_mobil}')
                print(f'{array_model_mobil}')
                print(f'{array_plat_mobil}')
                print(f'{array_harga_mobil}')
                print(f'{array_nama_supir}')
                print(f'{array_nomor_supir}')
#program utama
os.system('cls')
password = str(input('Password: '))
login = function_validasi_login(password)
if login:
    maks_array = int(input('Masukkan Jumlah Mobil : '))
    maks_array_mobil = function_maks_array(maks_array)
    array_plat_mobil = ['/'] * maks_array_mobil
    array_brand_mobil = ['/'] * maks_array_mobil
    array_model_mobil = ['/'] * maks_array_mobil
    array_harga_mobil = [0] * maks_array_mobil
    array_nama_supir = ['/'] * maks_array_mobil
    array_nomor_supir = ['/'] * maks_array_mobil
    print('Menu pilihan')
    print('1. Tambah Array')
    print('2. Hapus Elemen Array')
    print('3. Pengurutan Array')
    print('4. Pencarian Array')
    print('5. Penghancuran Array')
    print('0. Keluar Program')
    menu_pilihan = int(input('Masukkan Menu Pilihan : '))
    while menu_pilihan != 0:
        match(menu_pilihan) :
            case 1 :
                print('Menu Tambah Array')
                os.system('pause')
                os.system('cls')
                print('Silahkan Tambahkan Data Mobil Terbaru')
                procedure_tambah_mobil(maks_array, array_plat_mobil, array_brand_mobil, array_model_mobil, array_harga_mobil)
                procedure_tambah_supir(maks_array, array_nama_supir, array_nomor_supir)
            case 2 :
                print('Hapus Elemen Array')
                os.system('pause')
                os.system('cls')
            case 3 :
                print('Pengurutan Array')
                print('1. Pengurutan secara ascending')
                print('2. Pengurutan secara descending')
                pilihan_menu_pengurutan = int(input('Masukkan Pilihan Urutan : '))
                pilihan_menu_pengurutan = function_validasi_menu_pengurutan(pilihan_menu_pengurutan)
                match(pilihan_menu_pengurutan) :
                    case 1 :
                        print('Pengurutan bubble secara ascending')
                        print('1. Pengurutan sesuai brand mobil')
                        print('2. Pengurutan sesuai model mobil')
                        print('3. Pengurutan sesuai harga mobil')
                        print('4. Pengurutan sesuai plat mobil')
                        print('5. Pengurutan sesuai nama supir')
                        print('6. Pengurutan sesuai nomor supir')
                        pilihan_menu_ascending = int(input('Masukkan Pilihan Menu Sorting : '))
                        pilihan_menu_ascending = function_validasi_menu_ascending(pilihan_menu_ascending)
                        match (pilihan_menu_ascending) :
                            case 1 :
                                print('Pengurutan sesuai brand mobil')
                                procedure_pengurutan_brand_asceding(maks_array, array_plat_mobil, array_brand_mobil, array_model_mobil, array_harga_mobil, array_nomor_supir, array_nama_supir)
                            case 2 :
                                print('Pengurutan sesuai model mobil')
                                procedure_pengurutan_model_ascending(maks_array, array_plat_mobil, array_brand_mobil, array_model_mobil, array_harga_mobil, array_nomor_supir, array_nama_supir)
                            case 3 :
                                print('Pengurutan sesuai harga mobil')
                                procedure_pengurutan_harga_ascending(maks_array, array_plat_mobil, array_brand_mobil, array_model_mobil, array_harga_mobil, array_nomor_supir, array_nama_supir)
                            case 4 :
                                print('Pengurutan sesuai plat mobil')
                                procedure_pengurutan_plat_ascending(maks_array, array_plat_mobil, array_brand_mobil, array_model_mobil, array_harga_mobil, array_nomor_supir, array_nama_supir)
                            case 5 :
                                print('Pengurutan sesuai nama supir')
                                procedure_pengurutan_nama_supir_ascending(maks_array, array_plat_mobil, array_brand_mobil, array_model_mobil, array_harga_mobil, array_nomor_supir, array_nama_supir)
                            case 6 :
                                print('Pengurutan sesuai nomor supir')
                                procedure_pengurutan_nomor_supir_ascending(maks_array, array_plat_mobil, array_brand_mobil, array_model_mobil, array_harga_mobil, array_nomor_supir, array_nama_supir)
        print('Menu pilihan')
        print('1. Tambah Array')
        print('2. Hapus Elemen Array')
        print('3. Pengurutan Array')
        print('4. Pencarian Array')
        print('5. Penghancuran Array')
        print('0. Keluar Program')
        menu_pilihan = int(input('Masukkan Menu Pilihan : '))
else :
    print('Maaf, Login anda gagal')