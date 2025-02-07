import os

# kamus
# int
int_jumlah_masuk = 0
int_jumlah_maks = 10
percobaan = 0
batas_percobaan = 3
# array
array_brand = ['/'] * int_jumlah_maks
array_model = ['/'] * int_jumlah_maks
array_price_rental = [0] * int_jumlah_maks
array_plat_nomor = ['/'] * int_jumlah_maks
array_supir = ['/'] * int_jumlah_maks
array_phone_supir = [0] * int_jumlah_maks

#FOR DEBUGGING PURPOSE
def DEBUG_DUMMY_DATA():
    global array_brand, array_model, array_price_rental, array_plat_nomor, array_supir, array_phone_supir
    array_brand = ['1Toyota', '2Honda', '3Suzuki', '4Daihatsu', '5Nissan', '6Mitsubishi', '7Mazda', '8Kia', '9Hyundai', '10Ford']
    array_model = ['Avanza', 'Civic', 'Ertiga', 'Xenia', 'Livina', 'Pajero', 'CX-5', 'Seltos', 'Elantra', 'Focus']
    array_price_rental = [200000000, 300000000, 150000000, 180000000, 250000000, 400000000, 350000000, 220000000, 270000000, 320000000]
    array_plat_nomor = ['B 1234 AB', 'B 5678 CD', 'B 9101 EF', 'B 1213 GH', 'B 1415 IJ', 'B 1617 KL', 'B 1819 MN', 'B 2021 OP', 'B 2223 QR', 'B 2425 ST']
    array_supir = ['John Doe', 'Jane Smith', 'Alice Johnson', 'Bob Brown', 'Charlie Davis', 'Eve White', 'Frank Black', 'Grace Green', 'Hank Blue', 'Ivy Yellow']
    array_phone_supir = ['081234567890', '082345678901', '083456789012', '084567890123', '085678901234', '086789012345', '087890123456', '088901234567', '089012345678', '090123456789']
    return 10








# FUNGSI
def fungsi_bersihkan_layar():
    # ini untuk bersihkan layar
    os.system('cls' if os.name == 'nt' else 'clear')

def fungsi_tambah_array(indeks, teks, array_nama):
    if teks == 'indeks':
        array_nama[indeks] = indeks + 1  # Menyimpan indeks yang benar (indeks + 1)
    else:
        massukkan_pengguna = str(input('Masukkan ' + teks + ' : '))
        array_nama[indeks] = massukkan_pengguna
    return array_nama[indeks]

def fungsi_tampil_kendaraan(int_jumlah_masuk, array_brand, array_model, array_price_rental, array_plat_nomor, array_supir, array_phone_supir):
    fungsi_bersihkan_layar()
    print('Tampilan data kendaraan:')
    print('------------------------')

    if int_jumlah_masuk == 0:
        print('Tidak ada kendaraan yang ditambahkan.')
    else:
        for i in range(int_jumlah_masuk):  # Mulai dari 0
            print(f'Brand: {array_brand[i]}')
            print(f'Model: {array_model[i]}')
            print(f'Harga: {array_price_rental[i]}')
            print(f'Plat Nomor: {array_plat_nomor[i]}')
            print(f'Supir: {array_supir[i]}')
            print(f'Supir Nomor: {array_phone_supir[i]}')
            print('------------------------')
    input('Tekan Enter untuk Melanjutkan')
    return int_jumlah_masuk


# PROSEDURE

def subrutin_menu_login(percobaan, batas_percobaan,int_jumlah_masuk):

    while percobaan < batas_percobaan:
        fungsi_bersihkan_layar()
        print('#--selamat datang di koko rental--#')
        print('|                                 |')
        print('| 1. Masuk sebagai Admin          |')
        print('| 2. Masuk sebagai User           |')
        print('| 0. Keluar                       |')
        print('|                                 |')
        print('#---------------------------------#')
        pilihan = input('Masukkan akun anda : ')

        if pilihan == '1':
            password_admin = 'admin123'
            password_input = input('Masukkan password  : ')
            if password_input == password_admin:
                subrutin_menu_utama(1, int_jumlah_masuk)
            else:
                percobaan += 1
                fungsi_bersihkan_layar()
                print('#-< AKSES DITOLAK >-------------------------------#')
                print('|                                         / \\    |')
                print('|  Password Salah                        /   \\   |')
                print('|  Harap masukkan ulang                 /  !  \\  |')
                print('|                                      /_______\\ |')
                print('#-------------------------------------------------#')
                input('tekan enter untuk melanjutkan')

        elif pilihan == '2':
            print('Login sebagai User berhasil!')
            #PLACEHOLDER
        elif pilihan == '0':
            exit(0)
        else:
            print('Pilihan tidak valid. Silakan coba lagi.')
    fungsi_bersihkan_layar()
    print('#-< AKSES DITOLAK >-------------------------------#')
    print('|                                         / \\    |')
    print('|  Anda telah melebihi batas percobaan   /   \\   |')
    print('|  Aplikasi akan keluar                 /  !  \\  |')
    print('|                                      /_______\\ |')
    print('#-------------------------------------------------#')
    exit(2)

def subrutin_menu_utama(menu_pilihan, int_jumlah_masuk):
    while menu_pilihan != 0:
        fungsi_bersihkan_layar()
        print('#--selamat datang di koko rental--#')
        print('|                                 |')
        print('| Menu Utama:                     |')
        print('| 1. Direksi kendaraan            |')
        print('| 2. Cari Kendaraan               |')
        print('| 3. Tampil Kendaraan             |')
        print('| 0. Keluar                       |')
        print('|                                 |')
        print('#---------------------------------#')
        menu_pilihan = int(input('Pilihan: '))
        # pilih menu
        match menu_pilihan:
            case 1:
                int_jumlah_masuk = subrutin_menu_direksi(menu_pilihan,int_jumlah_masuk)
            case 2:
                subrutin_cari_kendaraan()
            case 3:
                fungsi_tampil_kendaraan(int_jumlah_masuk, array_brand, array_model, array_price_rental, array_plat_nomor, array_supir, array_phone_supir)
            case 99:
                int_jumlah_masuk = DEBUG_DUMMY_DATA()  # THIS IS DEBUG!
            case 0:
                break
            case _:
                print('#-< PERHATIAN >------------------------#')
                print('|                               / \\    |')
                print('|  NOMOR MENU TIDAK ADA!       /   \\   |')
                print('|  HARAP ULANGIN KEMBALI      /  !  \\  |')
                print('|                            /_______\\ |')
                print('#--------------------------------------#')

def subrutin_menu_direksi(menu_pilihan,int_jumlah_masuk):
    while menu_pilihan != 0:
        fungsi_bersihkan_layar()
        print('#--selamat datang di koko rental--#')
        print('|                                 |')
        print('| Menu direksi kendaraan:         |')
        print('| 1. Tambah Kendaraan             |')
        print('| 2. Hapus Kendaraan              |')
        print('| 3. Urutkan Kendaraan            |')
        print('| 4. Cari Kendaraan               |')
        print('| 0. Kembali                      |')
        print('|                                 |')
        print('#---------------------------------#')
        menu_pilihan = int(input('Pilihan: '))
        # pilih menu
        match menu_pilihan:
            case 1:
                int_jumlah_masuk = subrutin_tambah_kendaraan(int_jumlah_maks, int_jumlah_masuk)  # Update indeks terakhir
            case 2:
                subrutin_hapus_kendaraan(array_brand, array_model, array_price_rental, array_plat_nomor, array_supir, array_phone_supir)
            case 3:
                subrutin_urutkan_kendaraan()
            case 4:
                subrutin_cari_kendaraan()
            case 99:
                int_jumlah_masuk = DEBUG_DUMMY_DATA()  # THIS IS DEBUG!
            case 0:
                return int_jumlah_masuk
            case _:
                print('#-< PERHATIAN >------------------------#')
                print('|                               / \\    |')
                print('|  NOMOR MENU TIDAK ADA!       /   \\   |')
                print('|  HARAP ULANGIN KEMBALI      /  !  \\  |')
                print('|                            /_______\\ |')
                print('#--------------------------------------#')


# subrutin tambah kendaraan pada array
def subrutin_tambah_kendaraan(int_jumlah_maks, int_jumlah_masuk):
    fungsi_bersihkan_layar()
    print('#------------------------------------------#')
    print('|      Masukkan data kendaraan baru        |')
    print('#------------------------------------------#')
    # Loop validasi
    jumlah_kendaraan = int(input('Masukkan jumlah kendaraan: '))

    while not (0 < jumlah_kendaraan <= int_jumlah_maks - int_jumlah_masuk):
        if jumlah_kendaraan <= 0:
            print('#-< PERHATIAN >-----------------------------------#')
            print('|                                         / \\    |')
            print('|  Jumlah kendaraan harus lebih dari 0   /   \\   |')
            print('|  Harap masukkan ulang                 /  !  \\  |')
            print('|                                      /_______\\ |')
            print('#-------------------------------------------------#')
        else:
            print('#-< PERHATIAN >-----------------------------------#')
            print('|                                         / \\    |')
            print('|  Jumlah melebihi batas maksimum!       /   \\   |')
            print('|  Harap masukkan ulang                 /  !  \\  |')
            print('|                                      /_______\\ |')
            print('#-------------------------------------------------#')
        jumlah_kendaraan = int(input('Masukkan jumlah kendaraan: '))

    for i in range(jumlah_kendaraan):
        fungsi_bersihkan_layar()
        print(f'#------------------------------------------#')
        print(f'|    Masukkan data kendaraan ke-{i+1}      |')
        print(f'#------------------------------------------#')
        fungsi_tambah_array(int_jumlah_masuk + i, 'brand', array_brand)
        fungsi_tambah_array(int_jumlah_masuk + i, 'model', array_model)
        fungsi_tambah_array(int_jumlah_masuk + i, 'harga', array_price_rental)
        fungsi_tambah_array(int_jumlah_masuk + i, 'platnomor', array_plat_nomor)
        fungsi_tambah_array(int_jumlah_masuk + i, 'supir', array_supir)
        fungsi_tambah_array(int_jumlah_masuk + i, 'supir_nomor', array_phone_supir)

    return int_jumlah_masuk + jumlah_kendaraan

# subrutin hapus kendaraan
def subrutin_hapus_kendaraan(array_brand, array_model, array_price_rental, array_plat_nomor, array_supir, array_phone_supir):
    indeks_dihapus = int(input('Masukkan indeks kendaraan yang ingin dihapus: '))-1
    if 0 <= indeks_dihapus < len(array_brand):
        print(f'Menghapus kendaraan dengan data:')
        print(f'Brand: {array_brand[indeks_dihapus]}')
        print(f'Model: {array_model[indeks_dihapus]}')
        print(f'Harga Rental: {array_price_rental[indeks_dihapus]}')
        print(f'Plat Nomor: {array_plat_nomor[indeks_dihapus]}')
        print(f'Supir: {array_supir[indeks_dihapus]}')
        print(f'Phone Supir: {array_phone_supir[indeks_dihapus]}')

        for i in range(indeks_dihapus, len(array_brand) - 1):
            array_brand[i] = array_brand[i + 1]
            array_model[i] = array_model[i + 1]
            array_price_rental[i] = array_price_rental[i + 1]
            array_plat_nomor[i] = array_plat_nomor[i + 1]
            array_supir[i] = array_supir[i + 1]
            array_phone_supir[i] = array_phone_supir[i + 1]

        array_brand[-1] = '/'
        array_model[-1] = '/'
        array_price_rental[-1] = 0
        array_plat_nomor[-1] = '/'
        array_supir[-1] = '/'
        array_phone_supir[-1] = 0

        print('Kendaraan berhasil dihapus.')
    else:
        print('Indeks tidak valid.')

# placeholder urutkan kendaraan
def subrutin_urutkan_kendaraan():
    fungsi_bersihkan_layar()
    print('Urutkan Kendaraan')
    input('Tekan Enter untuk Melanjutkan')

# placeholder cari kendaraan
def subrutin_cari_kendaraan():
    fungsi_bersihkan_layar()
    print('Cari Kendaraan')
    input('Tekan Enter untuk Melanjutkan')

# DEBUG PANGGIL FUNGSI
if __name__ == '__main__':
    subrutin_menu_login(percobaan,batas_percobaan,int_jumlah_masuk)
