import os

# kamus
# int
int_jumlah_input = 0
int_jumlah_maks = 30
# array
array_index = [0] * int_jumlah_maks
array_brand = ['/'] * int_jumlah_maks
array_model = ['/'] * int_jumlah_maks
array_harga = [0] * int_jumlah_maks
array_platnomor = ['/'] * int_jumlah_maks
array_supir = ['/'] * int_jumlah_maks
array_supir_nomor = [0] * int_jumlah_maks


# FUNGSI
def fun_bersihkan_layar():
    # ini untuk bersihkan layar
    os.system('cls' if os.name == 'nt' else 'clear')


def fun_tambah_array(indeks, teks, array_nama):
    if teks == 'indeks':
        temp = array_nama[indeks] = indeks
    else:
        massukkan_pengguna = str(input('Masukkan ' + teks + ' : '))
        temp = array_nama[indeks] = massukkan_pengguna
    return temp


def fun_tampil_kendaraan(int_jumlah_input):
    print(int_jumlah_input)
    fun_bersihkan_layar()
    print('Tampilan data kendaraan:')
    print('------------------------')
    for i in range(int_jumlah_input):
        print(f'Index: {array_index[i]}')
        print(f'Brand: {array_brand[i]}')
        print(f'Model: {array_model[i]}')
        print(f'Harga: {array_harga[i]}')
        print(f'Plat Nomor: {array_platnomor[i]}')
        print(f'Supir: {array_supir[i]}')
        print(f'Supir Nomor: {array_supir_nomor[i]}')
        print('------------------------')

    input('Tekan Enter untuk Melanjutkan')


# PROSEDURE
def seq_menu_utama(choice, int_jumlah_input):
    while choice != 0:
        # placeholder untuk main menu
        fun_bersihkan_layar()
        print('Menu utama:')
        print('1. Tambah Kendaraan')
        print('2. Hapus Kendaraan')
        print('3. Urutkan Kendaraan')
        print('4. Cari Kendaraan')
        print('5. Tampil Kendaraan')
        print('0. Keluar')
        choice = int(input('Pilihan: '))
        # pilih menu
        match choice:
            case 1:
                int_jumlah_input = seq_tambah_kendaraan(int_jumlah_maks)
            case 2:
                seq_hapus_kendaraan()
            case 3:
                seq_urutkan_kendaraan()
            case 4:
                seq_cari_kendaraan()
            case 5:
                fun_tampil_kendaraan(int_jumlah_input)
            case 0:
                break
            case _:
                # validasi
                print('Pilihan tidak valid. Silakan coba lagi.')
                input('Tekan Enter untuk Melanjutkan')


# sequential tambah kendaraan pada array
def seq_tambah_kendaraan(int_jumlah_maks):
    fun_bersihkan_layar()
    print('Tambah Kendaraan')

    # Loop validasi
    int_jumlah_input = int(input('Masukkan jumlah kendaraan: '))

    while not (0 < int_jumlah_input <= int_jumlah_maks):
        if int_jumlah_input <= 0:
            print('Jumlah kendaraan harus lebih dari 0. Harap masukkan ulang!')
        else:
            print('Jumlah melebihi batas maksimum. Harap masukkan ulang!')
        int_jumlah_input = int(input('Masukkan jumlah kendaraan: '))

    for i in range(int_jumlah_input):
        fun_bersihkan_layar()
        print(f'masukkan data kendaraan ke-{i + 1}')
        print('------------------------')
        fun_tambah_array(i, 'indeks', array_index)
        fun_tambah_array(i, 'brand', array_brand)
        fun_tambah_array(i, 'model', array_model)
        fun_tambah_array(i, 'harga', array_harga)
        fun_tambah_array(i, 'platnomor', array_platnomor)
        fun_tambah_array(i, 'supir', array_supir)
        fun_tambah_array(i, 'supir_nomor', array_supir_nomor)
    return int_jumlah_input


# placeholder hapus kendaraan
def seq_hapus_kendaraan():
    fun_bersihkan_layar()
    print('Hapus Kendaraan')
    input('Tekan Enter untuk Melanjutkan')


# placeholder urutkan kendaraan
def seq_urutkan_kendaraan():
    fun_bersihkan_layar()
    print('Urutkan Kendaraan')
    input('Tekan Enter untuk Melanjutkan')


# placeholder cari kendaraan
def seq_cari_kendaraan():
    fun_bersihkan_layar()
    print('Cari Kendaraan')
    input('Tekan Enter untuk Melanjutkan')


# DEBUG PANGGIL FUNGSI
if __name__ == '__main__':
    seq_menu_utama(1, int_jumlah_input)