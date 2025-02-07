#PLACEHOLDER LIST NAME. USE FOR DEBUG ONLY!
int_jumlah_maks = 30
array_brand =  ['/'] * int_jumlah_maks
array_model = ['/'] * int_jumlah_maks
array_harga = [0] * int_jumlah_maks
array_platnomor =  ['/'] * int_jumlah_maks
array_index =  [0] * int_jumlah_maks
array_supir = ['/'] * int_jumlah_maks
array_supir_nomor = [0] * int_jumlah_maks


import os
def fun_bersihkan_layar():
    #ini untuk bersihkan layar
    os.system('cls' if os.name == 'nt' else 'clear')

def seq_menu_utama(choice):
    while choice != 0:
        #placeholder untuk main menu
        fun_bersihkan_layar()
        print("Menu utama:")
        print("1. Tambah Kendaraan")
        print("2. Hapus Kendaraan")
        print("3. Urutkan Kendaraan")
        print("4. Cari Kendaraan")
        print("0. Keluar")

        choice = int(input("Pilihan: "))
        #pilih menu
        match choice:
            case '1':
                seq_tambah_kendaraan()
            case '2':
                seq_hapus_kendaraan()
            case '3':
                seq_urutkan_kendaraan()
            case '4':
                seq_cari_kendaraan()
            case '0':
                break
            case _:
                #validasi
                print("Pilihan tidak valid. Silakan coba lagi.")
                input("Press Enter to return to the main menu...")

#placeholder tambah kendaraan /CURRENT WORK
def seq_tambah_kendaraan(int_jumlah_maks=30,):
    fun_bersihkan_layar()
    print("Tambah Kendaraan")
    int_jumlah_input = int(input("Masukkan jumlah kendaraan: "))
    if int_jumlah_input > int_jumlah_maks:
        print("Jumlah melebihi batas maksimum, Harap masukkan ulang!")
    else:
        print("Kendaraan berhasil ditambahkan.")

    input("Press Enter to return to the main menu...")


#placeholder hapus kendaraan
def seq_hapus_kendaraan():
    fun_bersihkan_layar()
    print("Hapus Kendaraan")
    input("Press Enter to return to the main menu...")

#placeholder urutkan kendaraan
def seq_urutkan_kendaraan():
    fun_bersihkan_layar()
    print("Urutkan Kendaraan")
    input("Press Enter to return to the main menu...")

#placeholder cari kendaraan
def seq_cari_kendaraan():
    fun_bersihkan_layar()
    print("Cari Kendaraan")
    input("Press Enter to return to the main menu...")


#DEBUG PANGGIL FUNGSI
if __name__ == "__main__":
    seq_menu_utama(1)