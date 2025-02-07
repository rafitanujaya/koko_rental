# fauzi
import os

#subrutin validasi login
def function_validasi_login(username, password) :
    os.system('cls')
    #variabel constant untuk login dan counter
    USERNAME = 'admin123'
    PASSWORD = 'admin123'
    counter = 0
    is_login = False
    while (username != USERNAME or password != PASSWORD) and counter < 2:
        print('Password atau Username salah!')
        os.system('pause')
        os.system('cls')
        counter += 1
        username = input('Username: ')
        password = input('Password: ')
    if username == USERNAME and password == PASSWORD:
        is_login = True
        return is_login

#subrutin penciptaan array of list untuk plat mobil
def function_penciptaan_array_plat_mobil(maks_array_mobil) :
    array_plat_mobil = ['/'] * maks_array_mobil
    return array_plat_mobil

#subrutin penciptaan array of list untuk brand mobil
def function_penciptaan_array_brand_mobil(maks_array_mobil) :
    array_brand_mobil = ['/'] * maks_array_mobil
    return array_brand_mobil

#subrutin penciptaan array of list untuk model mobil
def function_penciptaan_array_model_mobil(maks_array_mobil) :
    array_model_mobil = ['/'] * maks_array_mobil
    return array_model_mobil

#subrutin penciptaan array of integer untuk harga mobil
def function_penciptaan_array_harga_mobil(maks_array_mobil) :
    array_harga_mobil = [0] * maks_array_mobil
    return array_harga_mobil

#subrutin validasi jumlah mobil yang diinginkan
def function_maks_array(maks_array) :
    while maks_array < 0 :
        print('Maks Mobil Tidak Boleh Negatif')
        maks_array = int(input('Masukkan Jumlah Mobil : '))
    return maks_array

#subrutin validasi tambah supir
# def function_validasi_supir(tambah_supir) :
#     while tambah_supir != 'yes' and tambah_supir != 'no' :
#         print('Jawab yes atau no saja')
#         tambah_supir = str(input('Tambah Supir? [yes/no] ')).lower()
#     if tambah_supir == 'yes' :
#         return True
#     else :
#         return False
    
#subrutin validasi jumlah supir
def function_maks_supir(maks_supir) :
    while maks_supir < 0 :
        print('Maks Supir Tidak Boleh Negatif')
        maks_supir = int(input('Masukkan Jumlah Supir : '))
    return maks_supir

#subrutin penciptaan array of list nama supir
def function_array_nama_supir(maks_supir) :
    array_nama_supir = ['/'] * maks_supir
    return array_nama_supir

#subrutin penciptaan array of list nomor telepon supir
def function_array_nomor_supir(maks_supir) :
    array_nomor_supir = ['/'] * maks_supir
    return array_nomor_supir

#subrutin tambah seluruh array mobil
def procedure_tambah_mobil(maks_array, array_plat_mobil, array_brand_mobil, array_model_mobil, array_harga_mobil) :
    for i in range(maks_array) :
        array_brand_mobil[i] = str(input('Masukkan brand Mobil : '))
        array_model_mobil[i] = str(input('Masukkan model Mobil : '))
        array_harga_mobil[i] = int(input('Masukkan harga Mobil : '))
        array_plat_mobil[i] = str(input('Masukkan Plat Mobil : '))

#subrutin tambah seluruh array supir
def procedure_tambah_supir(maks_supir, array_nama_supir, array_nomor_supir) :
    for i in range(maks_supir) :
        array_nama_supir[i] = str(input('Masukkan Nama Supir : '))
        array_nomor_supir[i] = str(input('Masukkan Nomor Supir : '))
#program utama
username = str(input('Username: '))
password = str(input('Password: '))
is_login = function_validasi_login(username, password)
if is_login:
    print('Menu pilihan')
    print('1. Tambah Array')
    print('2. Hapus Elemen Array')
    print('3. Pengurutan Array')
    print('4. Pencarian Array')
    print('5. Penghancuran Array')
    print('0. Keluar Program')
    menu_pilihan = int(input('Masukkan Menu Pilihan : '))
    match(menu_pilihan) :
        case 1 :
            print('Menu Tambah Array')
            os.system('pause')
            os.system('cls')
            print('Silahkan Ciptakan Array Terlebih Dahulu')
            maks_array = int(input('Masukkan Jumlah Mobil : '))
            maks_array_mobil = function_maks_array(maks_array)
            array_plat_mobil = function_penciptaan_array_plat_mobil(maks_array_mobil)
            array_brand_mobil = function_penciptaan_array_brand_mobil(maks_array_mobil)
            array_model_mobil = function_penciptaan_array_model_mobil(maks_array_mobil)
            array_harga_mobil = function_penciptaan_array_harga_mobil(maks_array_mobil)
            maks_supir = int(input('Masukkan Jumlah Supir : '))
            maks_supir = function_maks_supir(maks_supir)
            array_nama_supir = function_array_nama_supir(maks_supir)
            array_nomor_supir = function_array_nomor_supir(maks_supir)
            procedure_tambah_mobil(maks_array, array_plat_mobil, array_brand_mobil, array_model_mobil, array_harga_mobil)
            procedure_tambah_supir(maks_supir, array_nama_supir, array_nomor_supir)
        case 2 :
            print('Hapus Elemen Array')
else :
    print('Maaf, Login anda gagal')