import os

# kamus
# int
int_jumlah_masuk = 0
int_jumlah_maks = 10
# array
array_indeks = [0] * int_jumlah_maks
array_brand = ['/'] * int_jumlah_maks
array_model = ['/'] * int_jumlah_maks
array_harga = [0] * int_jumlah_maks
array_platnomor = ['/'] * int_jumlah_maks
array_supir = ['/'] * int_jumlah_maks
array_supir_nomor = [0] * int_jumlah_maks

#FOR DEBUGGING PURPOSE
def DEBUG_DUMMY_DATA():
    global array_indeks, array_brand, array_model, array_harga, array_platnomor, array_supir, array_supir_nomor

    array_indeks = list(range(1, 11))  # Indeks dari 1 sampai 10
    array_brand = ['1Toyota', '2Honda', '3Suzuki', '4Daihatsu', '5Nissan', '6Mitsubishi', '7Mazda', '8Kia', '9Hyundai', '10Ford']
    array_model = ['Avanza', 'Civic', 'Ertiga', 'Xenia', 'Livina', 'Pajero', 'CX-5', 'Seltos', 'Elantra', 'Focus']
    array_harga = [200000000, 300000000, 150000000, 180000000, 250000000, 400000000, 350000000, 220000000, 270000000, 320000000]
    array_platnomor = ['B 1234 AB', 'B 5678 CD', 'B 9101 EF', 'B 1213 GH', 'B 1415 IJ', 'B 1617 KL', 'B 1819 MN', 'B 2021 OP', 'B 2223 QR', 'B 2425 ST']
    array_supir = ['John Doe', 'Jane Smith', 'Alice Johnson', 'Bob Brown', 'Charlie Davis', 'Eve White', 'Frank Black', 'Grace Green', 'Hank Blue', 'Ivy Yellow']
    array_supir_nomor = ['081234567890', '082345678901', '083456789012', '084567890123', '085678901234', '086789012345', '087890123456', '088901234567', '089012345678', '090123456789']
    return 10
# FUNGSI
def fun_bersihkan_layar():
    # ini untuk bersihkan layar
    os.system('cls' if os.name == 'nt' else 'clear')


def fun_tambah_array(indeks, teks, array_nama):
    if teks == 'indeks':
        array_nama[indeks] = indeks + 1  # Menyimpan indeks yang benar (indeks + 1)
    else:
        massukkan_pengguna = str(input('Masukkan ' + teks + ' : '))
        array_nama[indeks] = massukkan_pengguna



def fun_tampil_kendaraan(int_jumlah_masuk, array_indeks, array_brand, array_model, array_harga, array_platnomor, array_supir, array_supir_nomor):
    fun_bersihkan_layar()
    print('Tampilan data kendaraan:')
    print('------------------------')

    if int_jumlah_masuk == 0:
        print('Tidak ada kendaraan yang ditambahkan.')
    else:
        for i in range(int_jumlah_masuk):  # Mulai dari 0
            print(f'indeks: {array_indeks[i]}')
            print(f'Brand: {array_brand[i]}')
            print(f'Model: {array_model[i]}')
            print(f'Harga: {array_harga[i]}')
            print(f'Plat Nomor: {array_platnomor[i]}')
            print(f'Supir: {array_supir[i]}')
            print(f'Supir Nomor: {array_supir_nomor[i]}')
            print('------------------------')

    input('Tekan Enter untuk Melanjutkan')

# PROSEDURE

def seq_menu_utama(choice, int_jumlah_masuk):
    while choice != 0:
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
                int_jumlah_masuk = seq_tambah_kendaraan(int_jumlah_maks, int_jumlah_masuk)  # Update indeks terakhir
            case 2:
                seq_hapus_kendaraan()
            case 3:
                seq_urutkan_kendaraan()
            case 4:
                seq_cari_kendaraan()
            case 5:
                fun_tampil_kendaraan(int_jumlah_masuk, array_indeks, array_brand, array_model, array_harga, array_platnomor, array_supir, array_supir_nomor)
            case 99:
                int_jumlah_masuk = DEBUG_DUMMY_DATA()  # THIS IS DEBUG!
            case 0:
                break
            case _:
                print('Pilihan tidak valid. Silakan coba lagi.')
                input('Tekan Enter untuk Melanjutkan')

# sequential tambah kendaraan pada array
def seq_tambah_kendaraan(int_jumlah_maks, int_jumlah_masuk):
    fun_bersihkan_layar()
    print('Tambah Kendaraan')

    # Loop validasi
    jumlah_kendaraan = int(input('Masukkan jumlah kendaraan: '))

    while not (0 < jumlah_kendaraan <= int_jumlah_maks - int_jumlah_masuk):
        if jumlah_kendaraan <= 0:
            print('Jumlah kendaraan harus lebih dari 0. Harap masukkan ulang!')
        else:
            print('Jumlah melebihi batas maksimum. Harap masukkan ulang!')
        jumlah_kendaraan = int(input('Masukkan jumlah kendaraan: '))

    for i in range(jumlah_kendaraan):  # Mulai dari 0
        fun_bersihkan_layar()
        print(f'Masukkan data kendaraan ke-{i+1}')  # Menampilkan nomor urut yang benar
        print('------------------------')
        fun_tambah_array(int_jumlah_masuk + i, 'indeks', array_indeks)
        fun_tambah_array(int_jumlah_masuk + i, 'brand', array_brand)
        fun_tambah_array(int_jumlah_masuk + i, 'model', array_model)
        fun_tambah_array(int_jumlah_masuk + i, 'harga', array_harga)
        fun_tambah_array(int_jumlah_masuk + i, 'platnomor', array_platnomor)
        fun_tambah_array(int_jumlah_masuk + i, 'supir', array_supir)
        fun_tambah_array(int_jumlah_masuk + i, 'supir_nomor', array_supir_nomor)

    return int_jumlah_masuk + jumlah_kendaraan

# sequential hapus kendaraan
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
    seq_menu_utama(1, int_jumlah_masuk)