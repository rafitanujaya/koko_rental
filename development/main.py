# PROGRAM RENTAL KENDARAAN

# I.S : pengguna memilih salah satu nomor menu
# F.S : menampilkan hasil sesuai nomor menu yang dipilih

# IMPORT 
import os

# DEKLARASI VARIABEL

# KONSTANTA
PASSWORD = 'admin'
MAKSBARIS = 10
# VARIABEL
password = ''
banyak_data = 0
hapus = 'clear'
menu_utama = 0
menu_admin = 0
menu_admin_crud = 0
menu_admin_sorting = 0
menu_admin_sorting_asc = 0
menu_admin_sorting_desc = 0
menu_admin_searching = 0
menu_admin_searching_sequential = 0
menu_admin_searching_binary = 0
menu_user = 0

# PENCIPTAAN ARRAY platnomor, model, brand, harga_sewa, supir, nomor_supir
plat_nomor = [""] * (MAKSBARIS + 1)
model = [""] * MAKSBARIS
brand = [""] * MAKSBARIS
harga_sewa = [0] * MAKSBARIS
supir = [""] * MAKSBARIS
nomor_supir = [""] * (MAKSBARIS + 1)


# START SUB SUBRUTIN

# SUBRUTIN UNTUK MENGISI DATA RENRAL
def prosedur_isi_data_rental(plat_nomor, model, brand, harga_sewa, supir, nomor_supir, banyak_data):
    # I.S.: pengguna memasukkan data plat, brand, model, harga, nama supir, dan nomor telepon supir
    # F.S.: menambahkan data ke dalam array
    for i in range(banyak_data):
        print('╔══════════════════════════════════════════════════════════════════════════╗')
        print('║                M E M A S U K A N   D E T A I L   D A T A                 ║')
        print('║                         ───────────────────────                          ║')
        print(f'║  Jumlah data : {banyak_data:<2}                                                        ║')
        print('╚══════════════════════════════════════════════════════════════════════════╝')

        for j in range(i):
            if (j == 0):
                print(
                    '╔═══════════════════════════════════════════════════════════════════════════════════════════════════════╗')
                print(
                    '║ No ║  Plat Nomor  ║    Brand     ║     Model    ║  Harga Sewa  ║  Nama Supir  ║  Nomor Telepon Supir  ║')
                print(
                    '╠════╬══════════════╬══════════════╬══════════════╬══════════════╬══════════════╬═══════════════════════╣')
            print(
                f'║ {j + 1:<2} ║ {plat_nomor[j]:<10}   ║  {brand[j]:<10}  ║  {model[j]:<10}  ║  {harga_sewa[j]:<10}  ║  {supir[j]:<10}  ║    {nomor_supir[j]:<14}     ║')
            # print(f'{j} = {i}')
            if (j == i - 1):
                print(
                    '╚════╩══════════════╩══════════════╩══════════════╩══════════════╩══════════════╩═══════════════════════╝')
            else:
                print(
                    '╠════╬══════════════╬══════════════╬══════════════╬══════════════╬══════════════╬═══════════════════════╣')

        print(f'   Data kendaraan ke-{i + 1:<2}')
        temp = input(f'   · Plat nomor    : ')
        duplikat = fungsi_sequential_search_sentinel(plat_nomor, temp)
        while duplikat:
            print('╔══════════════════════════════════════════════════════════════════════════╗')
            print('║                                                                          ║')
            print('║        //\\              DATA YANG ANDA MASUKKAN SUDAH ADA !!             ║')
            print('║       // ║\\           ────────────────────────────────────────           ║')
            print('║      //  0 \\              SILAHKAN MASUKAN PERINTAH KEMBALI              ║')
            print('║     //______\\                 tekan enter untuk kembali <--              ║')
            print('║                                                                          ║')
            print('╚══════════════════════════════════════════════════════════════════════════╝')
            input('Tekan [ENTER] untuk melanjutkan.')
            os.system(hapus)

            print('╔══════════════════════════════════════════════════════════════════════════╗')
            print('║                M E M A S U K A N   D E T A I L   D A T A                 ║')
            print('║                         ───────────────────────                          ║')
            print(f'║  Jumlah data : {banyak_data:<2}                                                        ║')
            print('╚══════════════════════════════════════════════════════════════════════════╝')

            for j in range(i):
                if (j == 0):
                    print(
                        '╔═══════════════════════════════════════════════════════════════════════════════════════════════════════╗')
                    print(
                        '║ No ║  Plat Nomor  ║    Brand     ║     Model    ║  Harga Sewa  ║  Nama Supir  ║  Nomor Telepon Supir  ║')
                    print(
                        '╠════╬══════════════╬══════════════╬══════════════╬══════════════╬══════════════╬═══════════════════════╣')
                print(
                    f'║ {j + 1:<2} ║ {plat_nomor[j]:<10}   ║  {brand[j]:<10}  ║  {model[j]:<10}  ║  {harga_sewa[j]:<10}  ║  {supir[j]:<10}  ║    {nomor_supir[j]:<14}     ║')
                # print(f'{j} = {i}')
                if (j == i - 1):
                    print(
                        '╚════╩══════════════╩══════════════╩══════════════╩══════════════╩══════════════╩═══════════════════════╝')
                else:
                    print(
                        '╠════╬══════════════╬══════════════╬══════════════╬══════════════╬══════════════╬═══════════════════════╣')
            print(f'   Data kendaraan ke-{i + 1:<2}')
            temp = input(f'   · Plat nomor    : ')
            duplikat = fungsi_sequential_search_sentinel(plat_nomor, temp)
        plat_nomor[i] = temp
        model[i] = input('   · Model         : ')
        brand[i] = input('   · Brand         : ')
        harga_sewa[i] = int(input('   · Harga         : '))
        supir[i] = input('   · Nama Supir    : ')
        temp = input('   · Nomor telepon : ')
        duplikat = fungsi_sequential_search_sentinel(nomor_supir, temp)
        while duplikat:
            print('╔══════════════════════════════════════════════════════════════════════════╗')
            print('║                                                                          ║')
            print('║        //\\              DATA YANG ANDA MASUKKAN SUDAH ADA !!             ║')
            print('║       // ║\\           ────────────────────────────────────────           ║')
            print('║      //  0 \\              SILAHKAN MASUKAN PERINTAH KEMBALI              ║')
            print('║     //______\\                 tekan enter untuk kembali <--              ║')
            print('║                                                                          ║')
            print('╚══════════════════════════════════════════════════════════════════════════╝')
            input('Tekan [ENTER] untuk melanjutkan.')
            os.system(hapus)

            print('╔══════════════════════════════════════════════════════════════════════════╗')
            print('║                M E M A S U K A N   D E T A I L   D A T A                 ║')
            print('║                         ───────────────────────                          ║')
            print(f'║  Jumlah data : {banyak_data:<2}                                                        ║')
            print('╚══════════════════════════════════════════════════════════════════════════╝')
            for j in range(i):
                if (j == 0):
                    print(
                        '╔═══════════════════════════════════════════════════════════════════════════════════════════════════════╗')
                    print(
                        '║ No ║  Plat Nomor  ║    Brand     ║     Model    ║  Harga Sewa  ║  Nama Supir  ║  Nomor Telepon Supir  ║')
                    print(
                        '╠════╬══════════════╬══════════════╬══════════════╬══════════════╬══════════════╬═══════════════════════╣')
                print(
                    f'║ {j + 1:<2} ║ {plat_nomor[j]:<10}   ║  {brand[j]:<10}  ║  {model[j]:<10}  ║  {harga_sewa[j]:<10}  ║  {supir[j]:<10}  ║    {nomor_supir[j]:<14}     ║')
                # print(f'{j} = {i}')
                if (j == banyak_data - 1):
                    print(
                        '╚════╩══════════════╩══════════════╩══════════════╩══════════════╩══════════════╩═══════════════════════╝')
                else:
                    print(
                        '╠════╬══════════════╬══════════════╬══════════════╬══════════════╬══════════════╬═══════════════════════╣')
            print(f'   Data kendaraan ke-{i + 1:<2}')
            print(f'   · Plat nomor    : {plat_nomor[i]}')
            print(f'   · Model         : {model[i]}')
            print(f'   · Brand         : {brand[i]}')
            print(f'   · Harga         : {harga_sewa[i]}')
            print(f'   · Nama Supir    : {supir[i]}')
            temp = input(f'   · Nomor Supir    : ')
            duplikat = fungsi_sequential_search_sentinel(nomor_supir, temp)
        nomor_supir[i] = temp
        os.system(hapus)
        print('════════════════════════════════════════════════════════════════════════════')

# SUBRUTIN UNTUK MENAMBAH DATA RENTAL
def prosedur_tampil_data_rental(plat_nomor, model, brand, harga_sewa, supir, nomor_supir, banyak_data):
    # I.S.: plat, model, brand, harga, nama supir, nomor supir, dan banyak data sudah terdefinisi
    # F.S.: menampilkan tabel berisi array plat, brand, model, harga, nama supir, nomor telepon supir
    if (banyak_data == 0):
        print('data kosong')
    for j in range(banyak_data):
        if (j == 0):
            print(
                '╔═══════════════════════════════════════════════════════════════════════════════════════════════════════╗')
            print(
                '║ No ║  Plat Nomor  ║    Brand     ║     Model    ║  Harga Sewa  ║  Nama Supir  ║  Nomor Telepon Supir  ║')
            print(
                '╠════╬══════════════╬══════════════╬══════════════╬══════════════╬══════════════╬═══════════════════════╣')
        print(
            f'║ {j + 1:<2} ║ {plat_nomor[j]:<10}   ║  {brand[j]:<10}  ║  {model[j]:<10}  ║  {harga_sewa[j]:<10}  ║  {supir[j]:<10}  ║    {nomor_supir[j]:<14}     ║')
        # print(f'{j} = {i}')
        if (j == banyak_data - 1):
            print(
                '╚════╩══════════════╩══════════════╩══════════════╩══════════════╩══════════════╩═══════════════════════╝')
        else:
            print(
                '╠════╬══════════════╬══════════════╬══════════════╬══════════════╬══════════════╬═══════════════════════╣')

# SUBRUTIN UNTUK MENCARI DATA MIN DAN MAX
def prosedur_min_max_data_rental(plat_nomor, model, brand, harga_sewa, supir, nomor_supir):
    # I.S.: validasi apakah nilai di indeks harga_sewa tidak 0
    # F.S.: menampilkan data termurah dan termahal
    min = 0
    max = 0

    for i in range(MAKSBARIS):
        if (harga_sewa[i] != 0):
            if (harga_sewa[i] > harga_sewa[max]):
                max = i
            if (harga_sewa[i] < harga_sewa[min]):
                min = i

    print('╔══════════════════════════════════════════════════════════════════════════╗')
    print('║                     DATA MOBIL TERMURAH DAN TERMAHAL                     ║')
    print('║                ─────────────────────────────────────────                 ║')
    print('╚══════════════════════════════════════════════════════════════════════════╝')
    print('   Data Mobil Termurah ')
    print('════════════════════════════════════════════════════════════════════════════')
    print(f'   · Plat nomor    : {plat_nomor[min]}')
    print(f'   · Model         : {model[min]}')
    print(f'   · Brand         : {brand[min]}')
    print(f'   · Harga         : {harga_sewa[min]}')
    print(f'   · Nama Supir    : {supir[min]}')
    print(f'   · Nomor telepon : {nomor_supir[min]}')
    print('════════════════════════════════════════════════════════════════════════════')
    print('   Data Mobil Temahal ')
    print('════════════════════════════════════════════════════════════════════════════')
    print(f'   · Plat nomor    : {plat_nomor[max]}')
    print(f'   · Model         : {model[max]}')
    print(f'   · Brand         : {brand[max]}')
    print(f'   · Harga         : {harga_sewa[max]}')
    print(f'   · Nama Supir    : {supir[max]}')
    print(f'   · Nomor telepon : {nomor_supir[max]}')
    print('════════════════════════════════════════════════════════════════════════════')

# SUBRUTIN MENGHITUNG RATA-RATA HARGA RENTAL
def prosedur_menghitung_rata_rata_data_rental(harga_sewa):
    # I.S.: validasi harga nol atau tidak
    # F.S.: menampilkan rata-rata harga seluruh kendaraan
    temp = 0
    pembagi = 0
    for i in range(MAKSBARIS):
        if (harga_sewa[i] != 0):
            temp += harga_sewa[i]
            pembagi += 1
    print('╔══════════════════════════════════════════════════════════════════════════╗')
    print('║                      RATA-RATA HARGA SEWA MOBIL                          ║')
    print('║                ─────────────────────────────────────────                 ║')
    print('╚══════════════════════════════════════════════════════════════════════════╝')
    print(f'   Rata-Rata Harga Sewa Mobil di KOKO RENTAL : {(temp / pembagi):.2f}')
    print('════════════════════════════════════════════════════════════════════════════')

# SUBRUTIN UNTUK MERESET DATA RENTAL
def procedure_reset_data_rental(plat_nomor, model, brand, harga_sewa, supir, nomor_supir):
    # I.S.: harga MAKSBARIS sudah terdefinisi
    # F.S.: mengganti seluruh nilai data di array dengan nilai awal
    for i in range(MAKSBARIS):
        plat_nomor[i] = ''
        model[i] = ''
        brand[i] = ''
        harga_sewa[i] = 0
        supir[i] = ''
        nomor_supir[i] = ''

# SUBRUTIN UNTUK MENSORTING DATA, PLAT NOMOR, MODEL, BRAND, SUPIR, NOMOR SUPIR SECARA ASC MENGGUNAKAN BUBBLE SORT
def prosedur_sorting_asc(plat_nomor, model, brand, harga_sewa, supir, nomor_supir, array_sorting, banyak_data):
    # I.S.: array plat, model, brand, harga, supir, nomor supir sudah terdefinisi
    # F.S.: mengurutkan array plat, model, brand, harga, supir, nomor supir secara ascending
    prosedur_tampil_data_rental(plat_nomor, model, brand, harga_sewa, supir, nomor_supir, banyak_data)
    input('data sebelum di sorting, [Enter] untuk melanjutkan penyortingan')
    for i in range(banyak_data):
        for j in range(banyak_data - 1, i, -1):
            if array_sorting[j] < array_sorting[j - 1]:
                temp = plat_nomor[j - 1]
                plat_nomor[j - 1] = plat_nomor[j]
                plat_nomor[j] = temp

                temp = model[j - 1]
                model[j - 1] = model[j]
                model[j] = temp

                temp = brand[j - 1]
                brand[j - 1] = brand[j]
                brand[j] = temp

                temp = harga_sewa[j - 1]
                harga_sewa[j - 1] = harga_sewa[j]
                harga_sewa[j] = temp

                temp = supir[j - 1]
                supir[j - 1] = supir[j]
                supir[j] = temp

                temp = nomor_supir[j - 1]
                nomor_supir[j - 1] = nomor_supir[j]
                nomor_supir[j] = temp

    print('Proses Pengurutan Kelar')
    prosedur_tampil_data_rental(plat_nomor, model, brand, harga_sewa, supir, nomor_supir, banyak_data)

# SUBRUTIN UNTUK MENSORTING DATA, HARGA SEWA SECARA ASC MENGGUNAKAN BUBBLE SORT
def prosedur_sorting_asc_int(plat_nomor, model, brand, harga_sewa, supir, nomor_supir, array_sorting, banyak_data):
    # I.S.: array plat, model, brand, harga, supir, nomor supir sudah terdefinisi
    # F.S.: mengurutkan array plat, model, brand, harga, supir, nomor supir secara ascending
    prosedur_tampil_data_rental(plat_nomor, model, brand, harga_sewa, supir, nomor_supir, banyak_data)
    input('data sebelum di sorting, [Enter] untuk melanjutkan penyortingan')
    for i in range(banyak_data):
        for j in range(banyak_data - 1, i, -1):
            if array_sorting[j] < array_sorting[j - 1]:
                temp = plat_nomor[j - 1]
                plat_nomor[j - 1] = plat_nomor[j]
                plat_nomor[j] = temp

                temp = model[j - 1]
                model[j - 1] = model[j]
                model[j] = temp

                temp = brand[j - 1]
                brand[j - 1] = brand[j]
                brand[j] = temp

                temp = harga_sewa[j - 1]
                harga_sewa[j - 1] = harga_sewa[j]
                harga_sewa[j] = temp

                temp = supir[j - 1]
                supir[j - 1] = supir[j]
                supir[j] = temp

                temp = nomor_supir[j - 1]
                nomor_supir[j - 1] = nomor_supir[j]
                nomor_supir[j] = temp

    print('Proses Pengurutan Kelar')
    prosedur_tampil_data_rental(plat_nomor, model, brand, harga_sewa, supir, nomor_supir, banyak_data)

# SUBRUTIN UNTUK MENSORTING DATA, PLAT NOMOR, MODEL, BRAND, SUPIR, NOMOR SUPIR SECARA DESC MENGGUNAKAN SELECTION SORT MAX
def prosedur_sorting_desc(plat_nomor, model, brand, harga_sewa, supir, nomor_supir, array_sorting, banyak_data):
    # I.S.: array plat, model, brand, harga, supir, nomor supir sudah terdefinisi
    # F.S.: mengurutkan array plat, model, brand, harga, supir, nomor supir secara descending
    prosedur_tampil_data_rental(plat_nomor, model, brand, harga_sewa, supir, nomor_supir, banyak_data)
    print(f'data: {banyak_data}')
    input('data sebelum di sorting, [Enter] untuk melanjutkan penyortingan')
    for i in range(banyak_data):
        max = 0
        for j in range(banyak_data - i):
            if array_sorting[j] < array_sorting[max]:
                max = j
        temp = plat_nomor[j]
        plat_nomor[j] = plat_nomor[max]
        plat_nomor[max] = temp

        temp = model[j]
        model[j] = model[max]
        model[max] = temp

        temp = brand[j]
        brand[j] = brand[max]
        brand[max] = temp

        temp = harga_sewa[j]
        harga_sewa[j] = harga_sewa[max]
        harga_sewa[max] = temp

        temp = supir[j]
        supir[j] = supir[max]
        supir[max] = temp

        temp = nomor_supir[j]
        nomor_supir[j] = nomor_supir[max]
        nomor_supir[max] = temp

    print('Proses Pengurutan Kelar')
    prosedur_tampil_data_rental(plat_nomor, model, brand, harga_sewa, supir, nomor_supir, banyak_data)

# SUBRUTIN UNTUK MENSORTING DATA, HARGA SEWA SECARA DESC MENGGUNAKAN SELECTION SORT MAX
def prosedur_sorting_desc_int(plat_nomor, model, brand, harga_sewa, supir, nomor_supir, array_sorting, banyak_data):
    # I.S.: array plat, model, brand, harga, supir, nomor supir sudah terdefinisi
    # F.S.: mengurutkan array plat, model, brand, harga, supir, nomor supir secara descending
    prosedur_tampil_data_rental(plat_nomor, model, brand, harga_sewa, supir, nomor_supir, banyak_data)
    print(f'data: {banyak_data}')
    input('data sebelum di sorting, [Enter] untuk melanjutkan penyortingan')
    for i in range(banyak_data):
        max = 0
        for j in range(banyak_data - i):
            if array_sorting[j] < array_sorting[max]:
                max = j
        temp = plat_nomor[j]
        plat_nomor[j] = plat_nomor[max]
        plat_nomor[max] = temp

        temp = model[j]
        model[j] = model[max]
        model[max] = temp

        temp = brand[j]
        brand[j] = brand[max]
        brand[max] = temp

        temp = harga_sewa[j]
        harga_sewa[j] = harga_sewa[max]
        harga_sewa[max] = temp

        temp = supir[j]
        supir[j] = supir[max]
        supir[max] = temp

        temp = nomor_supir[j]
        nomor_supir[j] = nomor_supir[max]
        nomor_supir[max] = temp

    print('Proses Pengurutan Kelar')
    prosedur_tampil_data_rental(plat_nomor, model, brand, harga_sewa, supir, nomor_supir, banyak_data)

# SUBRUTIN UNTUK MELAKUKAN SEARCHING SECARA SEQUENTIAL STRING
def prosedur_searching_seq(plat_nomor, model, brand, harga_sewa, supir, nomor_supir, array_searching, banyak_data):
    # I.S.: pengguna memasukkan data yang ingin dicari
    # F.S.: menampilkan tabel data yang dicari jika ketemu
    dicari = input(' Masukkan data yang ingin dicari : ') 
    i = 0
    while array_searching[i] != dicari and i < banyak_data - 1:
        i += 1
    if array_searching[i] == dicari:
        print(
            '╔═══════════════════════════════════════════════════════════════════════════════════════════════════════╗')
        print(
            '║ No ║  Plat Nomor  ║    Brand     ║     Model    ║  Harga Sewa  ║  Nama Supir  ║  Nomor Telepon Supir  ║')
        print(
            '╠════╬══════════════╬══════════════╬══════════════╬══════════════╬══════════════╬═══════════════════════╣')
        print(
            f'║ {i + 1:<2} ║ {plat_nomor[i]:<10}   ║  {brand[i]:<10}  ║  {model[i]:<10}  ║  {harga_sewa[i]:<10}  ║  {supir[i]:<10}  ║    {nomor_supir[i]:<14}     ║')
        i += 1
        while i < banyak_data - 1:
            if (array_searching[i] == dicari):
                print(
                    f'║ {i + 1:<2} ║ {plat_nomor[i]:<10}   ║  {brand[i]:<10}  ║  {model[i]:<10}  ║  {harga_sewa[i]:<10}  ║  {supir[i]:<10}  ║    {nomor_supir[i]:<14}     ║')
            i += 1

        print(
            '╚════╩══════════════╩══════════════╩══════════════╩══════════════╩══════════════╩═══════════════════════╝')
    else:
        print('Data Tidak Ditemukan')

# SUBRUTIN UNTUK MELAKUKAN SEARCHING SECARA SEQUENTIAL INTEGER
def prosedur_searching_seq_int(plat_nomor, model, brand, harga_sewa, supir, nomor_supir, array_searching, banyak_data):
    # I.S.: pengguna memasukkan data yang ingin dicari
    # F.S.: menampilkan tabel data yang dicari jika ketemu
    dicari = int(input(' Masukkan data yang ingin dicari : '))
    i = 0
    while array_searching[i] != dicari and i < banyak_data - 1:
        i += 1
    if array_searching[i] == dicari:
        print(
            '╔═══════════════════════════════════════════════════════════════════════════════════════════════════════╗')
        print(
            '║ No ║  Plat Nomor  ║    Brand     ║     Model    ║  Harga Sewa  ║  Nama Supir  ║  Nomor Telepon Supir  ║')
        print(
            '╠════╬══════════════╬══════════════╬══════════════╬══════════════╬══════════════╬═══════════════════════╣')
        print(
            f'║ {i + 1:<2} ║ {plat_nomor[i]:<10}   ║  {brand[i]:<10}  ║  {model[i]:<10}  ║  {harga_sewa[i]:<10}  ║  {supir[i]:<10}  ║    {nomor_supir[i]:<14}     ║')
        i += 1
        while i < banyak_data - 1:
            if (array_searching[i] == dicari):
                print(
                    f'║ {i + 1:<2} ║ {plat_nomor[i]:<10}   ║  {brand[i]:<10}  ║  {model[i]:<10}  ║  {harga_sewa[i]:<10}  ║  {supir[i]:<10}  ║    {nomor_supir[i]:<14}     ║')
            i += 1

        print(
            '╚════╩══════════════╩══════════════╩══════════════╩══════════════╩══════════════╩═══════════════════════╝')
    else:
        print('Data Tidak Ditemukan')

# SUBRUTIN UNTUK MELAKUKAN SEARCHING USECARA BINARY DIMANA DATA WAJIB TERURUT
def prosedur_searching_binary(plat_nomor, model, brand, harga_sewa, supir, nomor_supir, array_searching, banyak_data):
    # I.S.: menampilkan pilihan dan pengguna memilih salah satu metode binary search
    # F.S.: menampilkan tabel data yang dicari jika ketemu
    print('╔════════════════════════════════════╗')
    print('║             BINARY MODE            ║')
    print('╠════════════════════════════════════╣')
    print('║   1. ASC        ║   2.DESC         ║')
    print('╚═════════════════╩══════════════════╝')
    print('>>> Masukkan pilihan Anda dan tekan [ENTER] untuk melanjutkan.')
    mode = int(input(' Masukkan pilihan Anda : '))

    while mode != 1 and mode != 2:
        print('pilihan tersedia hanya 1 dan 2 ulangii!!!')
        input('Tekan [ENTER] untuk melanjutkan.')
        mode = int(input(' Masukkan pilihan Anda : '))

    dicari = input(' Masukkan data yang ingin dicari : ')
    la = 0
    lb = banyak_data
    ketemu = False

    if (mode == 1):
        while not ketemu and la <= lb:
            k = (la + lb) // 2
            if (array_searching[k] == dicari):
                ketemu = True
            else:
                if (array_searching[k] < dicari):
                    la = k + 1
                else:
                    lb = k - 1
    if (mode == 2):
        while not ketemu and la <= lb:
            k = (la + lb) // 2
            if (array_searching[k] == dicari):
                ketemu = True
            else:
                if (array_searching[k] > dicari):
                    lb = k - 1
                else:
                    la = k + 1
    if ketemu:
        print(
            '╔═══════════════════════════════════════════════════════════════════════════════════════════════════════╗')
        print(
            '║ No ║  Plat Nomor  ║    Brand     ║     Model    ║  Harga Sewa  ║  Nama Supir  ║  Nomor Telepon Supir  ║')
        print(
            '╠════╬══════════════╬══════════════╬══════════════╬══════════════╬══════════════╬═══════════════════════╣')
        print(
            f'║ {0 + 1:<2} ║ {plat_nomor[k]:<10}   ║  {brand[k]:<10}  ║  {model[k]:<10}  ║  {harga_sewa[k]:<10}  ║  {supir[k]:<10}  ║    {nomor_supir[k]:<14}     ║')
        print(
            '╚════╩══════════════╩══════════════╩══════════════╩══════════════╩══════════════╩═══════════════════════╝')
    else:
        print('data tidak ketemu')

# SUBRUTIN UNTUK MENAMBAHKAN DATA RENTAL
def fungsi_penambahan_data_rental(plat_nomor, model, brand, harga_sewa, supir, nomor_supir, banyak_data) -> int:
    # I.S.: validasi apakah data sudah penuh atau belum
    # F.S.: menambahkan elemen baru di indeks terakhir array plat, model, brand, harga sewa, supir, nomor supir
    print(f'banyak data: {banyak_data}')
    if banyak_data < MAKSBARIS:
        print('╔══════════════════════════════════════════════════════════════════════════╗')
        print('║                M E N A M B A H K A N   D A T A   B A R U                 ║')
        print('║                ─────────────────────────────────────────                 ║')
        print('╚══════════════════════════════════════════════════════════════════════════╝')
        temp = input('   · Plat nomor    : ')
        duplikat = fungsi_sequential_search_sentinel(plat_nomor, temp)
        while duplikat:
            print('╔══════════════════════════════════════════════════════════════════════════╗')
            print('║                                                                          ║')
            print('║        //\\              DATA YANG ANDA MASUKKAN SUDAH ADA !!             ║')
            print('║       // ║\\           ────────────────────────────────────────           ║')
            print('║      //  0 \\              SILAHKAN MASUKAN PERINTAH KEMBALI              ║')
            print('║     //______\\                 tekan enter untuk kembali <--              ║')
            print('║                                                                          ║')
            print('╚══════════════════════════════════════════════════════════════════════════╝')
            input('Tekan [ENTER] untuk melanjutkan.')
            os.system(hapus)

            print('╔══════════════════════════════════════════════════════════════════════════╗')
            print('║                M E N A M B A H K A N   D A T A   B A R U                 ║')
            print('║                ─────────────────────────────────────────                 ║')
            print('╚══════════════════════════════════════════════════════════════════════════╝')
            temp = input('   · Plat nomor    : ')
            duplikat = fungsi_sequential_search_sentinel(plat_nomor, temp)

        plat_nomor[banyak_data] = temp
        model[banyak_data] = input('   · Model         : ')
        brand[banyak_data] = input('   · Brand         : ')
        harga_sewa[banyak_data] = int(input('   · Harga         : '))
        supir[banyak_data] = input('   · Nama Supir    : ')
        temp = input('   · Nomor telepon : ')
        duplikat = fungsi_sequential_search_sentinel(nomor_supir, temp)
        while duplikat:
            print('╔══════════════════════════════════════════════════════════════════════════╗')
            print('║                                                                          ║')
            print('║        //\\              DATA YANG ANDA MASUKKAN SUDAH ADA !!             ║')
            print('║       // ║\\           ────────────────────────────────────────           ║')
            print('║      //  0 \\              SILAHKAN MASUKAN PERINTAH KEMBALI              ║')
            print('║     //______\\                 tekan enter untuk kembali <--              ║')
            print('║                                                                          ║')
            print('╚══════════════════════════════════════════════════════════════════════════╝')
            input('Tekan [ENTER] untuk melanjutkan.')
            os.system(hapus)

            print('╔══════════════════════════════════════════════════════════════════════════╗')
            print('║                M E N A M B A H K A N   D A T A   B A R U                 ║')
            print('║                ─────────────────────────────────────────                 ║')
            print('╚══════════════════════════════════════════════════════════════════════════╝')
            print(f'   · Plat nomor    : {plat_nomor[banyak_data]}')
            print(f'   · Model         : {model[banyak_data]}')
            print(f'   · Brand         : {brand[banyak_data]}')
            print(f'   · Harga         : {harga_sewa[banyak_data]}')
            print(f'   · Nama Supir    : {supir[banyak_data]}')
            temp = input('   · Nomor telepon : ')
            duplikat = fungsi_sequential_search_sentinel(nomor_supir, temp)

        nomor_supir[banyak_data] = temp
        print('════════════════════════════════════════════════════════════════════════════')
        return banyak_data + 1
    else:
        print('data rental sudah pernuh')
        return banyak_data

# SUBRUTIN UNTUK MENYISIPKAN DATA RENTAL
def fungsi_penyisipan_data_rental(plat_nomor, model, brand, harga_sewa, supir, nomor_supir, banyak_data, posisi_penyisipan) :
    # I.S.: validasi apakah data sudah penuh atau belum
    # F.S.: menambahkan data di indeks yang ditentukan pengguna
    if banyak_data < MAKSBARIS:
        if posisi_penyisipan < banyak_data and posisi_penyisipan >= 0:
            for i in range(banyak_data, posisi_penyisipan - 1, - 1):
                plat_nomor[i] = plat_nomor[i - 1]
                model[i] = model[i - 1]
                brand[i] = brand[i - 1]
                harga_sewa[i] = harga_sewa[i - 1]
                supir[i] = supir[i - 1]
                nomor_supir[i] = nomor_supir[i - 1]

            print('╔══════════════════════════════════════════════════════════════════════════╗')
            print('║              M E N Y I S I P K A N   S E B U A H   D A T A               ║')
            print('║                ─────────────────────────────────────────                 ║')
            print('╚══════════════════════════════════════════════════════════════════════════╝')
            print(f'   Urutan data yang ingin disisip : {posisi_penyisipan}')
            print('════════════════════════════════════════════════════════════════════════════')
            temp = input('   · Plat nomor    : ')
            duplikat = fungsi_sequential_search_sentinel(plat_nomor, temp)
            while duplikat:
                print('╔══════════════════════════════════════════════════════════════════════════╗')
                print('║                                                                          ║')
                print('║        //\\              DATA YANG ANDA MASUKKAN SUDAH ADA !!             ║')
                print('║       // ║\\           ────────────────────────────────────────           ║')
                print('║      //  0 \\              SILAHKAN MASUKAN PERINTAH KEMBALI              ║')
                print('║     //______\\                 tekan enter untuk kembali <--              ║')
                print('║                                                                          ║')
                print('╚══════════════════════════════════════════════════════════════════════════╝')
                input('Tekan [ENTER] untuk melanjutkan.')
                os.system(hapus)
                print('╔══════════════════════════════════════════════════════════════════════════╗')
                print('║              M E N Y I S I P K A N   S E B U A H   D A T A               ║')
                print('║                ─────────────────────────────────────────                 ║')
                print('╚══════════════════════════════════════════════════════════════════════════╝')
                print(f'   Urutan data yang ingin disisip : {posisi_penyisipan}')
                print('════════════════════════════════════════════════════════════════════════════')
                temp = input('   · Plat nomor    : ')
                duplikat = fungsi_sequential_search_sentinel(plat_nomor, temp)
                

            plat_nomor[posisi_penyisipan - 1] = temp
            model[posisi_penyisipan - 1] = input('   · Model         : ')
            brand[posisi_penyisipan - 1] = input('   · Brand         : ')
            harga_sewa[posisi_penyisipan - 1] = int(input('   · Harga         : '))
            supir[posisi_penyisipan - 1] = input('   · Nama Supir    : ')
            temp = input('   · Nomor telepon : ')
            duplikat = fungsi_sequential_search_sentinel(nomor_supir, temp)
            while duplikat:
                print('╔══════════════════════════════════════════════════════════════════════════╗')
                print('║                                                                          ║')
                print('║        //\\              DATA YANG ANDA MASUKKAN SUDAH ADA !!             ║')
                print('║       // ║\\           ────────────────────────────────────────           ║')
                print('║      //  0 \\              SILAHKAN MASUKAN PERINTAH KEMBALI              ║')
                print('║     //______\\                 tekan enter untuk kembali <--              ║')
                print('║                                                                          ║')
                print('╚══════════════════════════════════════════════════════════════════════════╝')
                input('Tekan [ENTER] untuk melanjutkan.')
                os.system(hapus)

                print('╔══════════════════════════════════════════════════════════════════════════╗')
                print('║              M E N Y I S I P K A N   S E B U A H   D A T A               ║')
                print('║                ─────────────────────────────────────────                 ║')
                print('╚══════════════════════════════════════════════════════════════════════════╝')
                print(f'   Urutan data yang ingin disisip : {posisi_penyisipan}')
                print('════════════════════════════════════════════════════════════════════════════')
                print(f'   · Plat nomor    : {plat_nomor[posisi_penyisipan - 1]}')
                print(f'   · Model         : {model[posisi_penyisipan - 1]}')
                print(f'   · Brand         : {brand[posisi_penyisipan - 1]}')
                print(f'   · Harga         : {harga_sewa[posisi_penyisipan - 1]}')
                print(f'   · Nama Supir    : {supir[posisi_penyisipan - 1]}')
                temp = input('   · Nomor telepon : ')
                duplikat = fungsi_sequential_search_sentinel(nomor_supir, temp)
                

            nomor_supir[posisi_penyisipan - 1] = temp
            print('════════════════════════════════════════════════════════════════════════════')
            return banyak_data + 1
    else:
        print('Data sudah penuh')
        return banyak_data

# SUBRUTIN MENGHAPUS DATA RENTAL BEDASARKAN URUTAN
def fungsi_penghapusan_data_rental(plat_nomor, model, brand, harga_sewa, supir, nomor_supir, banyak_data, posisi_hapus) -> int:
    # I.S.: validasi apakah data kosong atau tidak
    # F.S.: menghapus data di indeks yang ditentukan user
    if banyak_data > 0:
        if posisi_hapus >= 0 and posisi_hapus <= banyak_data:
            for i in range(posisi_hapus, banyak_data):
                plat_nomor[i - 1] = plat_nomor[i]
                model[i - 1] = model[i]
                brand[i - 1] = brand[i]
                harga_sewa[i - 1] = harga_sewa[i]
                supir[i - 1] = supir[i]
                nomor_supir[i - 1] = nomor_supir[i]

            plat_nomor[banyak_data - 1] = ''
            model[banyak_data - 1] = ''
            brand[banyak_data - 1] = ''
            harga_sewa[banyak_data - 1] = 0
            supir[banyak_data - 1] = ''
            nomor_supir[banyak_data - 1] = ''
            print('Data Berhasil Dihapus')
            return banyak_data - 1
        else:
            print('Posisi Tidak Valid')
            return banyak_data
    else:
        print('Data Kosong')
        return banyak_data

# SABRUTIN SEARCHING SECARA SEQUENTIAL SEARCH UNTUK PENGECEKAN VALIDASI UNIQ
def fungsi_sequential_search_sentinel(array, dicari) -> bool:
    # I.S.: menambahkan data yang dicari pada indeks terakhir array
    # F.S.: menghasilkan tipe data boolean jika data ketemu atau tidak ketemu
    # print(array)
    array[MAKSBARIS] = dicari
    i = 0
    while (array[i] != dicari):
        i += 1
    if (i < MAKSBARIS):
        return True
    else:
        return False

# SABRUTIN MENAMPILKAN MENU UTAMA
def fungsi_menu_utama(menu_utama) -> int:
    # I.S.: menampilkan pilihan menu yang pengguna bisa pilih
    # F.S.: menghasilkan nilai sesuai pilihan pengguna
    print('╔════════════════════════════════════════════════════════════════════════════╗')
    print('║                            >> PILIH PERAN ANDA <<                          ║')
    print('╠════════════════════════════════════════════════════════════════════════════╣')
    print('║ [1] ADMIN / STAFF                                                          ║')
    print('║     Kelola unit kendaraan, pengguna, dan data operasional rental.          ║')
    print('╠────────────────────────────────────────────────────────────────────────────╣')
    print('║ [2] USER                                                                   ║')
    print('║     Pesan kendaraan favorit Anda dengan cepat dan mudah!                   ║')
    print('╠────────────────────────────────────────────────────────────────────────────╣')
    print('║ [0] KELUAR                                                                 ║')
    print('║     Selesaikan sesi ini dan kembali nanti.                                 ║')
    print('╚════════════════════════════════════════════════════════════════════════════╝')
    print('>>> Masukkan pilihan Anda dan tekan [ENTER] untuk melanjutkan.')
    menu_utama = int(input(' Masukkan pilihan Anda : '))

    while (menu_utama < 0) or (menu_utama > 2):
        print('╔══════════════════════════════════════════════════════════════════════════╗')
        print('║                                                                          ║')
        print('║        //\\            PERINTAH YANG ANDA MASUKAN TIDAK VALID!!           ║')
        print('║       // ║\\           ────────────────────────────────────────           ║')
        print('║      //  0 \\              SILAHKAN MASUKKAN PERINTAH KEMBALI             ║')
        print('║     //______\\                 tekan enter untuk kembali <--              ║')
        print('║                                                                          ║')
        print('╠══════════════════════════════════════════════════════════════════════════╣')
        print('║                       PILIHAN YANG TERSEDIA:                             ║')
        print('║                       [1] ADMIN / STAFF                                  ║')
        print('║                       [2] USER                                           ║')
        print('║                       [0] KELUAR                                         ║')
        print('╚══════════════════════════════════════════════════════════════════════════╝')
        input('Tekan [ENTER] untuk melanjutkan.')
        os.system(hapus)
        print('╔════════════════════════════════════════════════════════════════════════════╗')
        print('║                            >> PILIH PERAN ANDA <<                          ║')
        print('╠════════════════════════════════════════════════════════════════════════════╣')
        print('║ [1] ADMIN / STAFF                                                          ║')
        print('║     Kelola unit kendaraan, pengguna, dan data operasional rental.          ║')
        print('╠────────────────────────────────────────────────────────────────────────────╣')
        print('║ [2] USER                                                                   ║')
        print('║     Pesan kendaraan favorit Anda dengan cepat dan mudah!                   ║')
        print('╠────────────────────────────────────────────────────────────────────────────╣')
        print('║ [0] KELUAR                                                                 ║')
        print('║     Selesaikan sesi ini dan kembali nanti.                                 ║')
        print('╚════════════════════════════════════════════════════════════════════════════╝')
        print('>>> Masukkan pilihan Anda dan tekan [ENTER] untuk melanjutkan.')
        menu_utama = int(input(' Masukkan pilihan Anda : '))

    return menu_utama

# SUBRUTIN UNTUK MEMVALIDASI LOGIN ADMIN
def fungsi_validasi_admin(password) -> bool:
    # I.S.: pengguna memasukkan password khusus admin
    # F.S.: menghasilkan data boolean jika pengguna berhasil atau tidak berhasil
    print('╔══════════════════════════════════════════════════════════════════════════╗')
    print('║                                                                          ║')
    print('║                     ~ LOGIN ADMIN KOKO RENTAL ~                          ║')
    print('║                                                                          ║')
    print('╠══════════════════════════════════════════════════════════════════════════╣')
    print('║  Silakan masukkan password admin Anda untuk melanjutkan:                 ║')
    print('╚══════════════════════════════════════════════════════════════════════════╝')
    password = input('Masukkan password admin: ')

    percobaan = 0
    while password != PASSWORD and percobaan < 2:
        percobaan += 1
        print('╔══════════════════════════════════════════════════════════════════════════╗')
        print('║ ⚠️  PASSWORD SALAH!                                                       ║')
        print(f'║ ➡️  Anda masih memiliki {3 - percobaan} kesempatan lagi.                  ║')
        print('╚══════════════════════════════════════════════════════════════════════════╝')
        input('Tekan [ENTER] untuk melanjutkan.')

        os.system(hapus)
        print('╔══════════════════════════════════════════════════════════════════════════╗')
        print('║                                                                          ║')
        print('║                     ~ LOGIN ADMIN KOKO RENTAL ~                          ║')
        print('║                                                                          ║')
        print('╠══════════════════════════════════════════════════════════════════════════╣')
        print('║  Silakan masukkan password admin Anda untuk melanjutkan:                 ║')
        print('╚══════════════════════════════════════════════════════════════════════════╝')
        password = input('Masukkan password admin: ')
    if (password != PASSWORD):
        os.system(hapus)
        print('╔══════════════════════════════════════════════════════════════════════════╗')
        print('║  Anda telah kehabisan kesempatan! Silakan hubungi developer.             ║')
        print('╚══════════════════════════════════════════════════════════════════════════╝')
        input('Tekan [ENTER] untuk melanjutkan.')
        os.system(hapus)
        return False
    else:
        return True

# SUBRUTIN UNTUK MENAMPILKAN MENU ADMIN
def fungsi_menu_admin(menu_admin) -> int:
    # I.S.: pengguna memilih menu yang tersedia
    # F.S.: menghasilkan nilai sesuai pilihan pengguna
    print('╔══════════════════════════════════════════════════════════════════════════╗')
    print('║                    -  +  -  M E N U  A D M I N  -  +  -                  ║')
    print('╠══════════════════════════════════════════════════════════════════════════╣')
    print('║  1. MELAKUKAN C.R.U.D. ( CREATE, READ, UPDATE, DELETE ) DATA             ║')
    print('║  2. MELAKUKAN PENGURUTAN DATA                                            ║')
    print('║  3. MELAKUKAN PENCARIAN DATA                                             ║')
    print('╠══════════════════════════════════════════════════════════════════════════╣')
    print('║                               0. KEMBALI                                 ║')
    print('╚══════════════════════════════════════════════════════════════════════════╝')
    print('>>> Masukkan pilihan Anda dan tekan [ENTER] untuk melanjutkan.')
    menu_admin = int(input(' Masukkan pilihan anda : '))

    while (menu_admin < 0) or (menu_admin > 3):
        print('╔══════════════════════════════════════════════════════════════════════════╗')
        print('║                                                                          ║')
        print('║        //\\            PERINTAH YANG ANDA MASUKAN TIDAK VALID!!           ║')
        print('║       // ║\\           ────────────────────────────────────────           ║')
        print('║      //  0 \\              SILAHKAN MASUKKAN PERINTAH KEMBALI             ║')
        print('║     //______\\                 tekan enter untuk kembali <--              ║')
        print('║                                                                          ║')
        print('╠══════════════════════════════════════════════════════════════════════════╣')
        print('║                       PILIHAN YANG TERSEDIA:                             ║')
        print('║                       [1] MELAKUKAN C.R.U.D.                             ║')
        print('║                       [2] MELAKUKAN PENGURUTAN DATA                      ║')
        print('║                       [3] MELAKUKAN PENCARIAN DATA                       ║')
        print('║                       [0] KELUAR                                         ║')
        print('╚══════════════════════════════════════════════════════════════════════════╝')
        input('Tekan [ENTER] untuk melanjutkan.')
        os.system(hapus)

        print('╔══════════════════════════════════════════════════════════════════════════╗')
        print('║                    -  +  -  M E N U  A D M I N  -  +  -                  ║')
        print('╠══════════════════════════════════════════════════════════════════════════╣')
        print('║  1. MELAKUKAN C.R.U.D. ( CREATE, READ, UPDATE, DELETE ) DATA             ║')
        print('║  2. MELAKUKAN PENGURUTAN DATA                                            ║')
        print('║  3. MELAKUKAN PENCARIAN DATA                                             ║')
        print('╠══════════════════════════════════════════════════════════════════════════╣')
        print('║                               0. KEMBALI                                 ║')
        print('╚══════════════════════════════════════════════════════════════════════════╝')
        print('>>> Masukkan pilihan Anda dan tekan [ENTER] untuk melanjutkan.')
        menu_admin = int(input(' Masukkan pilihan anda : '))
    return menu_admin

# SUBRUTIN UNTUK MENAMPILKAN MENU ADMIN CRUD
def fungsi_menu_admin_crud(menu_admin_crud) -> int:
    # I.S.: pengguna memilih menu yang tersedia
    # F.S.: menghasilkan nilai sesuai pilihan pengguna
    print('╔══════════════════════════════════════════════════════════════════════════╗')
    print('║                 -  +  -  M E N U   C. R. U. D.  -  +  -                  ║')
    print('╠═══════════════════════════════════╦══════════════════════════════════════╣')
    print('║  1. MEMBUAT / MEMASUKAN DATA      ║  5. MENAMBAHKAN DATA BARU            ║')
    print('║  2. MENAMPILKAN DATA              ║  6. MENYISIPKAN SEBUAH DATA          ║')
    print('║  3. HARGA TERMAHAL DAN TERMURAH   ║  7. MENGHAPUS SEBUAH DATA            ║')
    print('║  4. RATA-RATA HARGA RENTAL        ║  8. HAPUS SEMUA DATA                 ║')
    print('╠═══════════════════════════════════╩══════════════════════════════════════╣')
    print('║                               0. KEMBALI                                 ║')
    print('╚══════════════════════════════════════════════════════════════════════════╝')
    print('>>> Masukkan pilihan Anda dan tekan [ENTER] untuk melanjutkan.')
    menu_admin_crud = int(input(' Masukan pilihan anda : '))

    while (menu_admin_crud < 0) or (menu_admin_crud > 9):
        print('╔══════════════════════════════════════════════════════════════════════════╗')
        print('║                                                                          ║')
        print('║        //\\            PERINTAH YANG ANDA MASUKAN TIDAK VALID!!           ║')
        print('║       // ║\\           ────────────────────────────────────────           ║')
        print('║      //  0 \\              SILAHKAN MASUKKAN PERINTAH KEMBALI             ║')
        print('║     //______\\                 tekan enter untuk kembali <--              ║')
        print('║                                                                          ║')
        print('╠══════════════════════════════════════════════════════════════════════════╣')
        print('║                       PILIHAN YANG TERSEDIA:                             ║')
        print('║═══════════════════════════════════╦══════════════════════════════════════║')
        print('║  1. MEMBUAT / MEMASUKAN DATA      ║  5. MENAMBAHKAN DATA BARU            ║')
        print('║  2. MENAMPILKAN DATA              ║  6. MENYISIPKAN SEBUAH DATA          ║')
        print('║  3. HARGA TERMAHAL DAN TERMURAH   ║  7. MENGHAPUS SEBUAH DATA            ║')
        print('║  4. RATA-RATA HARGA RENTAL        ║  8. HAPUS SEMUA DATA                 ║')
        print('╠═══════════════════════════════════╩══════════════════════════════════════╣')
        print('║                               0. KEMBALI                                 ║')
        print('╚══════════════════════════════════════════════════════════════════════════╝')
        input('Tekan [ENTER] untuk melanjutkan.')
        os.system(hapus)

        print('╔══════════════════════════════════════════════════════════════════════════╗')
        print('║                 -  +  -  M E N U   C. R. U. D.  -  +  -                  ║')
        print('╠═══════════════════════════════════╦══════════════════════════════════════╣')
        print('║  1. MEMBUAT / MEMASUKAN DATA      ║  5. MENAMBAHKAN DATA BARU            ║')
        print('║  2. MENAMPILKAN DATA              ║  6. MENYISIPKAN SEBUAH DATA          ║')
        print('║  3. HARGA TERMAHAL DAN TERMURAH   ║  7. MENGHAPUS SEBUAH DATA            ║')
        print('║  4. RATA-RATA HARGA RENTAL        ║  8. HAPUS SEMUA DATA                 ║')
        print('╠═══════════════════════════════════╩══════════════════════════════════════╣')
        print('║                               0. KEMBALI                                 ║')
        print('╚══════════════════════════════════════════════════════════════════════════╝')
        print('>>> Masukkan pilihan Anda dan tekan [ENTER] untuk melanjutkan.')
        menu_admin_crud = int(input(' Masukan pilihan anda : '))

    return menu_admin_crud

# SUBRUTIN UNTUK MENAMPILKAN MENU ADMIN SORTING
def fungsi_menu_admin_sorting(menu_admin_sorting) -> int:
    # I.S.: pengguna memilih menu yang tersedia
    # F.S.: menghasilkan nilai sesuai pilihan pengguna
    print('╔══════════════════════════════════════════════════════════════════════════╗')
    print('║              -  +  -  M E N U   P E N G U R U T A N  -  +  -             ║')
    print('╠═══════════════════════════════════╦══════════════════════════════════════╣')
    print('║  1. SECARA MENAIK ( ASCENDING )   ║  2. SECARA MENURUN ( DESCENDING )    ║')
    print('╠═══════════════════════════════════╩══════════════════════════════════════╣')
    print('║                               0. KEMBALI                                 ║')
    print('╚══════════════════════════════════════════════════════════════════════════╝')
    print('>>> Masukkan pilihan Anda dan tekan [ENTER] untuk melanjutkan.')
    menu_admin_sorting = int(input(' Masukan pilihan anda : '))

    while (menu_admin_sorting < 0) or (menu_admin_sorting > 2):
        print('╔══════════════════════════════════════════════════════════════════════════╗')
        print('║                                                                          ║')
        print('║        //\\            PERINTAH YANG ANDA MASUKAN TIDAK VALID!!           ║')
        print('║       // ║\\           ────────────────────────────────────────           ║')
        print('║      //  0 \\              SILAHKAN MASUKKAN PERINTAH KEMBALI             ║')
        print('║     //______\\                 tekan enter untuk kembali <--              ║')
        print('║                                                                          ║')
        print('╠══════════════════════════════════════════════════════════════════════════╣')
        print('║                       PILIHAN YANG TERSEDIA:                             ║')
        print('║                       [1] SECARA MENAIK ( ASCENDING )                    ║')
        print('║                       [2] SECARA MENURUN ( DESCENDING )                  ║')
        print('║                       [0] KELUAR                                         ║')
        print('╚══════════════════════════════════════════════════════════════════════════╝')
        input('Tekan [ENTER] untuk melanjutkan.')
        os.system(hapus)

        print('╔══════════════════════════════════════════════════════════════════════════╗')
        print('║              -  +  -  M E N U   P E N G U R U T A N  -  +  -             ║')
        print('╠═══════════════════════════════════╦══════════════════════════════════════╣')
        print('║  1. SECARA MENAIK ( ASCENDING )   ║  2. SECARA MENURUN ( DESCENDING )    ║')
        print('╠═══════════════════════════════════╩══════════════════════════════════════╣')
        print('║                               0. KEMBALI                                 ║')
        print('╚══════════════════════════════════════════════════════════════════════════╝')
        print('>>> Masukkan pilihan Anda dan tekan [ENTER] untuk melanjutkan.')
        menu_admin_sorting = int(input(' Masukan pilihan anda : '))

    return menu_admin_sorting

# SUBRUTIN UNTUK MENAMPILKAN MENU ADMIN SORTING SECARA ASC
def fungsi_menu_admin_sorting_asc(menu_admin_sorting_asc) -> int:
    # I.S.: pengguna memilih menu yang tersedia
    # F.S.: menghasilkan nilai sesuai pilihan pengguna
    print('╔══════════════════════════════════════════════════════════════════════════╗')
    print('║      -  +  -  M E N U   P E N G U R U T A N   M E N A I K  -  +  -       ║')
    print('╠═══════════════════════════════════╦══════════════════════════════════════╣')
    print('║  1. BERDASARKAN PLAT NOMOR        ║  5. BERDASARKAN NAMA SUPIR           ║')
    print('║  2. BERDASARKAN MODEL             ║  6. BERDASARKAN NOMOR TELEPON SUPIR  ║')
    print('║  3. BERDASARKAN BRAND             ║                                      ║')
    print('║  4. BERDASARKAN HARGA             ║                                      ║')
    print('╠═══════════════════════════════════╩══════════════════════════════════════╣')
    print('║                               0. KEMBALI                                 ║')
    print('╚══════════════════════════════════════════════════════════════════════════╝')
    print('>>> Masukkan pilihan Anda dan tekan [ENTER] untuk melanjutkan.')
    menu_admin_sorting_asc = int(input(' Masukan pilihan anda : '))

    while (menu_admin_sorting_asc < 0) or (menu_admin_sorting_asc > 6):
        print('╔══════════════════════════════════════════════════════════════════════════╗')
        print('║                                                                          ║')
        print('║        //\\            PERINTAH YANG ANDA MASUKAN TIDAK VALID!!           ║')
        print('║       // ║\\           ────────────────────────────────────────           ║')
        print('║      //  0 \\              SILAHKAN MASUKKAN PERINTAH KEMBALI             ║')
        print('║     //______\\                 tekan enter untuk kembali <--              ║')
        print('║                                                                          ║')
        print('╠══════════════════════════════════════════════════════════════════════════╣')
        print('║                       PILIHAN YANG TERSEDIA:                             ║')
        print('║═══════════════════════════════════╦══════════════════════════════════════║')
        print('║  1. BERDASARKAN PLAT NOMOR        ║  4. BERDASARKAN HARGA                ║')
        print('║  2. BERDASARKAN MODEL             ║  5. BERDASARKAN NAMA SUPIR           ║')
        print('║  3. BERDASARKAN BRAND             ║  6. BERDASARKAN NOMOR TELEPON SUPIR  ║')
        print('║  0. KEMBALI                       ║                                      ║')
        print('╚═══════════════════════════════════╩══════════════════════════════════════╝')
        input('Tekan [ENTER] untuk melanjutkan.')
        os.system(hapus)

        print('╔══════════════════════════════════════════════════════════════════════════╗')
        print('║      -  +  -  M E N U   P E N G U R U T A N   M E N A I K  -  +  -       ║')
        print('╠═══════════════════════════════════╦══════════════════════════════════════╣')
        print('║  1. BERDASARKAN PLAT NOMOR        ║  4. BERDASARKAN HARGA                ║')
        print('║  2. BERDASARKAN MODEL             ║  5. BERDASARKAN NAMA SUPIR           ║')
        print('║  3. BERDASARKAN BRAND             ║  6. BERDASARKAN NOMOR TELEPON SUPIR  ║')
        print('╠═══════════════════════════════════╩══════════════════════════════════════╣')
        print('║                               0. KEMBALI                                 ║')
        print('╚══════════════════════════════════════════════════════════════════════════╝')
        print('>>> Masukkan pilihan Anda dan tekan [ENTER] untuk melanjutkan.')
        menu_admin_sorting_asc = int(input(' Masukan pilihan anda : '))

    return menu_admin_sorting_asc

# SUBRUTIN UNTUK MENAMPILKAN MENU ADMIN SORTING SECARA DESC
def fungsi_menu_admin_sorting_desc(menu_admin_sorting_desc) -> int:
    # I.S.: pengguna memilih menu yang tersedia
    # F.S.: menghasilkan nilai sesuai pilihan pengguna
    print('╔══════════════════════════════════════════════════════════════════════════╗')
    print('║      -  +  -  M E N U   P E N G U R U T A N   M E N U R U N  -  +  -     ║')
    print('╠═══════════════════════════════════╦══════════════════════════════════════╣')
    print('║  1. BERDASARKAN PLAT NOMOR        ║  5. BERDASARKAN NAMA SUPIR           ║')
    print('║  2. BERDASARKAN MODEL             ║  6. BERDASARKAN NOMOR TELEPON SUPIR  ║')
    print('║  3. BERDASARKAN BRAND             ║                                      ║')
    print('║  4. BERDASARKAN HARGA             ║                                      ║')
    print('╠═══════════════════════════════════╩══════════════════════════════════════╣')
    print('║                               0. KEMBALI                                 ║')
    print('╚══════════════════════════════════════════════════════════════════════════╝')
    print('>>> Masukkan pilihan Anda dan tekan [ENTER] untuk melanjutkan.')
    menu_admin_sorting_desc = int(input(' Masukan pilihan anda : '))

    while (menu_admin_sorting_desc < 0) or (menu_admin_sorting_desc > 6):
        print('╔══════════════════════════════════════════════════════════════════════════╗')
        print('║                                                                          ║')
        print('║        //\\            PERINTAH YANG ANDA MASUKAN TIDAK VALID!!           ║')
        print('║       // ║\\           ────────────────────────────────────────           ║')
        print('║      //  0 \\              SILAHKAN MASUKKAN PERINTAH KEMBALI             ║')
        print('║     //______\\                 tekan enter untuk kembali <--              ║')
        print('║                                                                          ║')
        print('╠══════════════════════════════════════════════════════════════════════════╣')
        print('║                       PILIHAN YANG TERSEDIA:                             ║')
        print('║═══════════════════════════════════╦══════════════════════════════════════║')
        print('║  1. BERDASARKAN PLAT NOMOR        ║  4. BERDASARKAN HARGA                ║')
        print('║  2. BERDASARKAN MODEL             ║  5. BERDASARKAN NAMA SUPIR           ║')
        print('║  3. BERDASARKAN BRAND             ║  6. BERDASARKAN NOMOR TELEPON SUPIR  ║')
        print('║  0. KEMBALI                       ║                                      ║')
        print('╚═══════════════════════════════════╩══════════════════════════════════════╝')
        input('Tekan [ENTER] untuk melanjutkan.')
        os.system(hapus)

        print('╔══════════════════════════════════════════════════════════════════════════╗')
        print('║      -  +  -  M E N U   P E N G U R U T A N   M E N U R U N  -  +  -     ║')
        print('╠═══════════════════════════════════╦══════════════════════════════════════╣')
        print('║  1. BERDASARKAN PLAT NOMOR        ║  4. BERDASARKAN HARGA                ║')
        print('║  2. BERDASARKAN MODEL             ║  5. BERDASARKAN NAMA SUPIR           ║')
        print('║  3. BERDASARKAN BRAND             ║  6. BERDASARKAN NOMOR TELEPON SUPIR  ║')
        print('╠═══════════════════════════════════╩══════════════════════════════════════╣')
        print('║                               0. KEMBALI                                 ║')
        print('╚══════════════════════════════════════════════════════════════════════════╝')
        print('>>> Masukkan pilihan Anda dan tekan [ENTER] untuk melanjutkan.')
        menu_admin_sorting_desc = int(input(' Masukan pilihan anda : '))

    return menu_admin_sorting_desc

# SUBRUTIN UNTUK MENAMPILKAN MENU ADMIN SEARCHING DATA
def fungsi_menu_admin_searching(menu_admin_searching) -> int:
    # I.S.: pengguna memilih menu yang tersedia
    # F.S.: menghasilkan nilai sesuai pilihan pengguna
    print('╔══════════════════════════════════════════════════════════════════════════╗')
    print('║               -  +  -  M E N U   P E N C A R I A N  -  +  -              ║')
    print('╠═══════════════════════════════════╦══════════════════════════════════════╣')
    print('║  1. SECARA BERUNTUN ( SQUENTIAL ) ║  2. SECARA BINARY                    ║')
    print('╠═══════════════════════════════════╩══════════════════════════════════════╣')
    print('║                               0. KEMBALI                                 ║')
    print('╚══════════════════════════════════════════════════════════════════════════╝')
    print('>>> Masukkan pilihan Anda dan tekan [ENTER] untuk melanjutkan.')
    menu_admin_searching = int(input(' Masukan pilihan anda : '))

    while (menu_admin_searching < 0) and (menu_admin_searching > 2):
        print('╔══════════════════════════════════════════════════════════════════════════╗')
        print('║                                                                          ║')
        print('║        //\\            PERINTAH YANG ANDA MASUKAN TIDAK VALID!!           ║')
        print('║       // ║\\           ────────────────────────────────────────           ║')
        print('║      //  0 \\              SILAHKAN MASUKKAN PERINTAH KEMBALI             ║')
        print('║     //______\\                 tekan enter untuk kembali <--              ║')
        print('║                                                                          ║')
        print('╠══════════════════════════════════════════════════════════════════════════╣')
        print('║                       PILIHAN YANG TERSEDIA:                             ║')
        print('║                       [1] SECARA BERUNTUN (SEQUENTIAL)                   ║')
        print('║                       [2] SECARA BINARY                                  ║')
        print('║                       [0] KELUAR                                         ║')
        print('╚══════════════════════════════════════════════════════════════════════════╝')
        input('Tekan [ENTER] untuk melanjutkan.')

        os.system(hapus)
        print('╔══════════════════════════════════════════════════════════════════════════╗')
        print('║               -  +  -  M E N U   P E N C A R I A N  -  +  -              ║')
        print('╠═══════════════════════════════════╦══════════════════════════════════════╣')
        print('║  1. SECARA BERUNTUN (SEQUENTIAL)  ║  2. SECARA BINARY                    ║')
        print('╠═══════════════════════════════════╩══════════════════════════════════════╣')
        print('║                               0. KEMBALI                                 ║')
        print('╚══════════════════════════════════════════════════════════════════════════╝')
        print('>>> Masukkan pilihan Anda dan tekan [ENTER] untuk melanjutkan.')
        menu_admin_searching = int(input(' Masukan pilihan anda : '))
    return menu_admin_searching

# SUBRUTIN UNTUK MENAMPILKAN MENU ADMIN SEARCHING SECARA SEQUENTIAL
def fungsi_menu_admin_searching_sequential(menu_admin_searching_sequential) -> int:
    # I.S.: pengguna memilih menu yang tersedia
    # F.S.: menghasilkan nilai sesuai pilihan pengguna
    print('╔══════════════════════════════════════════════════════════════════════════╗')
    print('║     -  +  -  M E N U   P E N C A R I A N   B E R U N T U N  -  +  -      ║')
    print('╠═══════════════════════════════════╦══════════════════════════════════════╣')
    print('║  1. BERDASARKAN MODEL             ║  4. BERDASARKAN NAMA SUPIR           ║')
    print('║  2. BERDASARKAN BRAND             ║                                      ║')
    print('║  3. BERDASARKAN HARGA             ║                                      ║')
    print('╠═══════════════════════════════════╩══════════════════════════════════════╣')
    print('║                               0. KEMBALI                                 ║')
    print('╚══════════════════════════════════════════════════════════════════════════╝')
    print('>>> Masukkan pilihan Anda dan tekan [ENTER] untuk melanjutkan.')
    menu_admin_searching_sequential = int(input(' Masukan pilihan anda : '))

    while (menu_admin_searching_sequential < 0) and (menu_admin_searching_sequential > 4):
        print('╔══════════════════════════════════════════════════════════════════════════╗')
        print('║                                                                          ║')
        print('║        //\\            PERINTAH YANG ANDA MASUKAN TIDAK VALID!!           ║')
        print('║       // ║\\           ────────────────────────────────────────           ║')
        print('║      //  0 \\              SILAHKAN MASUKKAN PERINTAH KEMBALI             ║')
        print('║     //______\\                 tekan enter untuk kembali <--              ║')
        print('║                                                                          ║')
        print('╠══════════════════════════════════════════════════════════════════════════╣')
        print('║                       PILIHAN YANG TERSEDIA:                             ║')
        print('║═══════════════════════════════════╦══════════════════════════════════════║')
        print('║  1. BERDASARKAN MODEL             ║  3. BERDASARKAN HARGA                ║')
        print('║  2. BERDASARKAN BRAND             ║  4. BERDASARKAN NAMA SUPIR           ║')
        print('║  0. KELUAR                        ║                                      ║')
        print('╚═══════════════════════════════════╩══════════════════════════════════════╝')
        input('Tekan [ENTER] untuk melanjutkan.')
        os.system(hapus)
        print('╔══════════════════════════════════════════════════════════════════════════╗')
        print('║     -  +  -  M E N U   P E N C A R I A N   B E R U N T U N  -  +  -      ║')
        print('╠═══════════════════════════════════╦══════════════════════════════════════╣')
        print('║  1. BERDASARKAN MODEL             ║  4. BERDASARKAN NAMA SUPIR           ║')
        print('║  2. BERDASARKAN BRAND             ║                                      ║')
        print('║  3. BERDASARKAN HARGA             ║                                      ║')
        print('╠═══════════════════════════════════╩══════════════════════════════════════╣')
        print('║                               0. KEMBALI                                 ║')
        print('╚══════════════════════════════════════════════════════════════════════════╝')
        print('>>> Masukkan pilihan Anda dan tekan [ENTER] untuk melanjutkan.')
        menu_admin_searching_sequential = int(input(' Masukan pilihan anda : '))

    return menu_admin_searching_sequential

# SUBRUTIN UNTUK MENAMPILKAN MENU ADMIN SEARCHING SECARA BINARY
def fungsi_menu_admin_searching_binary(menu_admin_searching_binary) -> int:
    # I.S.: pengguna memilih menu yang tersedia
    # F.S.: menghasilkan nilai sesuai pilihan pengguna
    print('╔══════════════════════════════════════════════════════════════════════════╗')
    print('║       -  +  -  M E N U   P E N C A R I A N   B I N A R Y  -  +  -        ║')
    print('╠═══════════════════════════════════╦══════════════════════════════════════╣')
    print('║  1. BERDASARKAN PLAT NOMOR        ║  2. BERDASARKAN NOMOR TELEPON SUPIR  ║')
    print('║  0. KEMBALI                       ║                                      ║')
    print('╚═══════════════════════════════════╩══════════════════════════════════════╝')
    print('>>> Masukkan pilihan Anda dan tekan [ENTER] untuk melanjutkan.')
    menu_admin_searching_binary = int(input(' Masukan pilihan anda : '))

    while (menu_admin_searching_binary < 0) and (menu_admin_searching_binary > 2):
        print('╔══════════════════════════════════════════════════════════════════════════╗')
        print('║                                                                          ║')
        print('║        //\\            PERINTAH YANG ANDA MASUKAN TIDAK VALID!!           ║')
        print('║       // ║\\           ────────────────────────────────────────           ║')
        print('║      //  0 \\              SILAHKAN MASUKKAN PERINTAH KEMBALI             ║')
        print('║     //______\\                 tekan enter untuk kembali <--              ║')
        print('║                                                                          ║')
        print('╠══════════════════════════════════════════════════════════════════════════╣')
        print('║                       PILIHAN YANG TERSEDIA:                             ║')
        print('║═══════════════════════════════════╦══════════════════════════════════════║')
        print('║  1. BERDASARKAN PLAT NOMOR        ║  2. BERDASARKAN NOMOR TELEPON SUPIR  ║')
        print('║  0. KEMBALI                       ║                                      ║')
        print('╚═══════════════════════════════════╩══════════════════════════════════════╝')
        input('Tekan [ENTER] untuk melanjutkan.')
        os.system(hapus)

        print('╔══════════════════════════════════════════════════════════════════════════╗')
        print('║       -  +  -  M E N U   P E N C A R I A N   B I N A R Y  -  +  -        ║')
        print('╠═══════════════════════════════════╦══════════════════════════════════════╣')
        print('║  1. BERDASARKAN PLAT NOMOR        ║  2. BERDASARKAN NOMOR TELEPON SUPIR  ║')
        print('║  0. KEMBALI                       ║                                      ║')
        print('╚═══════════════════════════════════╩══════════════════════════════════════╝')
        print('>>> Masukkan pilihan Anda dan tekan [ENTER] untuk melanjutkan.')
        menu_admin_searching_binary = int(input(' Masukan pilihan anda : '))
    return menu_admin_searching_binary

# SUBRUTIN UNTUK MENAMPILKAN MENU USER
def fungsi_menu_user(menu_user):
    # I.S.: pengguna memilih menu yang tersedia
    # F.S.: menghasilkan nilai sesuai pilihan pengguna
    print('╔══════════════════════════════════════════════════════════════════════════╗')
    print('║             -  +  -  M E N U   P E L A N G G A N  -  +  -                ║')
    print('╠═══════════════════════════════════╦══════════════════════════════════════╣')
    print('║  1. MENAMPILKAN DATA KENDARAAN    ║  0. KEMBALI                          ║')
    print('╚═══════════════════════════════════╩══════════════════════════════════════╝')
    print('>>> Masukkan pilihan Anda dan tekan [ENTER] untuk melanjutkan.')
    menu_user = int(input(' Masukkan pilihan anda : '))

    while menu_user < 0 and menu_user > 1:
        print('╔══════════════════════════════════════════════════════════════════════════╗')
        print('║                                                                          ║')
        print('║        //\\            PERINTAH YANG ANDA MASUKAN TIDAK VALID!!           ║')
        print('║       // ║\\           ────────────────────────────────────────           ║')
        print('║      //  0 \\              SILAHKAN MASUKKAN PERINTAH KEMBALI             ║')
        print('║     //______\\                 tekan enter untuk kembali <--              ║')
        print('║                                                                          ║')
        print('╠══════════════════════════════════════════════════════════════════════════╣')
        print('║                       PILIHAN YANG TERSEDIA:                             ║')
        print('║                       [1] MENAMPILKAN DATA KENDARAAN                             ║')
        print('║                       [0] KELUAR                                         ║')
        print('╚══════════════════════════════════════════════════════════════════════════╝')
        input('Tekan [ENTER] untuk melanjutkan.')
        os.system(hapus)
        
        print('╔══════════════════════════════════════════════════════════════════════════╗')
        print('║             -  +  -  M E N U   P E L A N G G A N  -  +  -                ║')
        print('╠═══════════════════════════════════╦══════════════════════════════════════╣')
        print('║  1. MENAMPILKAN DATA KENDARAAN    ║  0. KEMBALI                          ║')
        print('╚═══════════════════════════════════╩══════════════════════════════════════╝')
        print('>>> Masukkan pilihan Anda dan tekan [ENTER] untuk melanjutkan.')
        menu_user = int(input(' Masukkan pilihan anda : '))
        
    return menu_user
        

# BADAN PROGRAM 

os.system(hapus)
menu_utama = fungsi_menu_utama(menu_utama)
while menu_utama != 0:
    os.system(hapus)
    match menu_utama:
        case 1:
            login = fungsi_validasi_admin(password)
            if (login):
                os.system(hapus)
                menu_admin = fungsi_menu_admin(menu_admin)
                while (menu_admin != 0):
                    match menu_admin:
                        case 1:
                            os.system(hapus)
                            menu_admin_crud = fungsi_menu_admin_crud(menu_admin_crud)
                            os.system(hapus)
                            while (menu_admin_crud != 0):
                                os.system(hapus)
                                match menu_admin_crud:
                                    case 1:
                                        banyak_data = int(input(' Banyak Data yang dimasukkan : '))
                                        prosedur_isi_data_rental(plat_nomor, model, brand, harga_sewa, supir,
                                                                 nomor_supir, banyak_data)
                                    case 2:
                                        if (banyak_data > MAKSBARIS):
                                            prosedur_tampil_data_rental(plat_nomor, model, brand, harga_sewa, supir,
                                                                        nomor_supir, MAKSBARIS)
                                        else:
                                            prosedur_tampil_data_rental(plat_nomor, model, brand, harga_sewa, supir,
                                                                        nomor_supir, banyak_data)
                                    case 3:
                                        prosedur_min_max_data_rental(plat_nomor, model, brand, harga_sewa, supir,
                                                                     nomor_supir)
                                    case 4:
                                        prosedur_menghitung_rata_rata_data_rental(harga_sewa)
                                    case 5:
                                        if (banyak_data > MAKSBARIS):
                                            prosedur_tampil_data_rental(plat_nomor, model, brand, harga_sewa, supir,
                                                                        nomor_supir, MAKSBARIS)
                                        else:
                                            prosedur_tampil_data_rental(plat_nomor, model, brand, harga_sewa, supir,
                                                                        nomor_supir, banyak_data)
                                        banyak_data = fungsi_penambahan_data_rental(plat_nomor, model, brand,
                                                                                      harga_sewa, supir, nomor_supir,
                                                                                      banyak_data)
                                    case 6:
                                        if (banyak_data > MAKSBARIS):
                                            prosedur_tampil_data_rental(plat_nomor, model, brand, harga_sewa, supir,
                                                                        nomor_supir, MAKSBARIS)
                                        else:
                                            prosedur_tampil_data_rental(plat_nomor, model, brand, harga_sewa, supir,
                                                                        nomor_supir, banyak_data)
                                        posisi_penyisipan = int(input('Nomor Penyisipan Data : '))
                                        banyak_data = fungsi_penyisipan_data_rental(plat_nomor, model, brand,
                                                                                      harga_sewa, supir, nomor_supir,
                                                                                      banyak_data, posisi_penyisipan)
                                    case 7:
                                        if (banyak_data > MAKSBARIS):
                                            prosedur_tampil_data_rental(plat_nomor, model, brand, harga_sewa, supir,
                                                                        nomor_supir, MAKSBARIS)
                                        else:
                                            prosedur_tampil_data_rental(plat_nomor, model, brand, harga_sewa, supir,
                                                                        nomor_supir, banyak_data)

                                        posisi_hapus = int(input('Nomor yang ingin dihapus : '))
                                        banyak_data = fungsi_penghapusan_data_rental(plat_nomor, model, brand,
                                                                                       harga_sewa, supir, nomor_supir,
                                                                                       banyak_data, posisi_hapus)
                                    case 8:
                                        konfirmasi = input('Apakah Anda yakin hapus semua data? Y/N : ').upper()
                                        while konfirmasi != 'Y' and konfirmasi != 'N':
                                            print('Masukkan tidak valid, harus Y atau N ulangiii!!')
                                            input('[ENTER] untuk melanjutkan...')
                                            os.system(hapus)
                                            konfirmasi = input('Apakah Anda yakin hapus semua data? Y/N : ').upper()

                                        if konfirmasi == 'Y':
                                            procedure_reset_data_rental(plat_nomor, model, brand, harga_sewa, supir,
                                                                       nomor_supir)
                                            banyak_data = 0
                                            print('data berhasil dihapus semua')
                                        else:
                                            print('Tidak ada penghapusan data')
                                input('[ENTER] untuk melanjutkan...')
                                os.system(hapus)
                                menu_admin_crud = fungsi_menu_admin_crud(menu_admin_crud)
                        case 2:
                            menu_admin_sorting = fungsi_menu_admin_sorting(menu_admin_sorting)
                            while (menu_admin_sorting != 0):
                                os.system(hapus)
                                match menu_admin_sorting:
                                    case 1:
                                        menu_admin_sorting_asc = fungsi_menu_admin_sorting_asc(menu_admin_sorting_asc)
                                        while (menu_admin_sorting_asc != 0):
                                            os.system(hapus)
                                            match menu_admin_sorting_asc:
                                                case 1:
                                                    prosedur_sorting_asc(plat_nomor, model, brand, harga_sewa, supir,
                                                                         nomor_supir, plat_nomor, banyak_data)
                                                case 2:
                                                    prosedur_sorting_asc(plat_nomor, model, brand, harga_sewa, supir,
                                                                         nomor_supir, model, banyak_data)

                                                case 3:
                                                    prosedur_sorting_asc(plat_nomor, model, brand, harga_sewa, supir,
                                                                         nomor_supir, brand, banyak_data)
                                                case 4:
                                                    prosedur_sorting_asc_int(plat_nomor, model, brand, harga_sewa, supir,
                                                                         nomor_supir, harga_sewa, banyak_data)

                                                case 5:
                                                    prosedur_sorting_asc(plat_nomor, model, brand, harga_sewa, supir,
                                                                         nomor_supir, supir, banyak_data)

                                                case 6:
                                                    prosedur_sorting_asc(plat_nomor, model, brand, harga_sewa, supir,
                                                                         nomor_supir, nomor_supir, banyak_data)
                                            input('[ENTER] untuk melanjutkan...')
                                            os.system(hapus)
                                            menu_admin_sorting_asc = fungsi_menu_admin_sorting_asc(
                                                menu_admin_sorting_asc)
                                    case 2:
                                        menu_admin_sorting_desc = fungsi_menu_admin_sorting_desc(
                                            menu_admin_sorting_desc)
                                        while (menu_admin_sorting_desc != 0):
                                            os.system(hapus)
                                            match menu_admin_sorting_desc:
                                                case 1:
                                                    prosedur_sorting_desc(plat_nomor, model, brand, harga_sewa, supir,
                                                                          nomor_supir, plat_nomor, banyak_data)
                                                case 2:
                                                    prosedur_sorting_desc(plat_nomor, model, brand, harga_sewa, supir,
                                                                          nomor_supir, model, banyak_data)
                                                case 3:
                                                    prosedur_sorting_desc(plat_nomor, model, brand, harga_sewa, supir,
                                                                          nomor_supir, brand, banyak_data)
                                                case 4:
                                                    prosedur_sorting_desc_int(plat_nomor, model, brand, harga_sewa, supir,
                                                                          nomor_supir, harga_sewa, banyak_data)
                                                case 5:
                                                    prosedur_sorting_desc(plat_nomor, model, brand, harga_sewa, supir,
                                                                          nomor_supir, supir, banyak_data)
                                                case 6:
                                                    prosedur_sorting_desc(plat_nomor, model, brand, harga_sewa, supir,
                                                                          nomor_supir, nomor_supir, banyak_data)
                                            input('[ENTER] untuk melanjutkan...')
                                            os.system(hapus)
                                            menu_admin_sorting_desc = fungsi_menu_admin_sorting_desc(
                                                menu_admin_sorting_desc)
                                os.system(hapus)
                                menu_admin_sorting = fungsi_menu_admin_sorting(menu_admin_sorting)
                        case 3:
                            menu_admin_searching = fungsi_menu_admin_searching(menu_admin_searching)
                            while (menu_admin_searching != 0):
                                os.system(hapus)
                                match menu_admin_searching:
                                    case 1:
                                        menu_admin_searching_sequential = fungsi_menu_admin_searching_sequential(
                                            menu_admin_searching_sequential)
                                        while (menu_admin_searching_sequential != 0):
                                            match menu_admin_searching_sequential:
                                                case 1:
                                                    prosedur_searching_seq(plat_nomor, model, brand, harga_sewa, supir,
                                                                           nomor_supir, model, banyak_data)
                                                case 2:
                                                    prosedur_searching_seq(plat_nomor, model, brand, harga_sewa, supir,
                                                                           nomor_supir, brand, banyak_data)
                                                case 3:
                                                    prosedur_searching_seq_int(plat_nomor, model, brand, harga_sewa,
                                                                               supir, nomor_supir, harga_sewa,
                                                                               banyak_data)
                                                case 4:
                                                    prosedur_searching_seq(plat_nomor, model, brand, harga_sewa, supir,
                                                                           nomor_supir, supir, banyak_data)
                                            input('[ENTER] untuk melanjutkan...')
                                            os.system(hapus)
                                            menu_admin_searching_sequential = fungsi_menu_admin_searching_sequential(
                                                menu_admin_searching_sequential)
                                    case 2:
                                        menu_admin_searching_binary = fungsi_menu_admin_searching_binary(
                                            menu_admin_searching_binary)
                                        while (menu_admin_searching_binary != 0):
                                            os.system(hapus)
                                            match menu_admin_searching_binary:
                                                case 1:
                                                    prosedur_searching_binary(plat_nomor, model, brand, harga_sewa,
                                                                              supir, nomor_supir, plat_nomor,
                                                                              banyak_data)
                                                case 2:
                                                    prosedur_searching_binary(plat_nomor, model, brand, harga_sewa,
                                                                              supir, nomor_supir, nomor_supir,
                                                                              banyak_data)
                                            input('[ENTER] untuk melanjutkan...')
                                            os.system(hapus)
                                            menu_admin_searching_binary = fungsi_menu_admin_searching_binary(
                                                menu_admin_searching_binary)
                                os.system(hapus)
                                menu_admin_searching = fungsi_menu_admin_searching(menu_admin_searching)
                    os.system(hapus)
                    menu_admin = fungsi_menu_admin(menu_admin)
        case 2:
            menu_user = fungsi_menu_user(menu_user)
            while menu_user != 0:
                match menu_user:
                    case 1:
                        if (banyak_data > MAKSBARIS):
                            prosedur_tampil_data_rental(plat_nomor, model, brand, harga_sewa, supir,
                                                        nomor_supir, MAKSBARIS)
                        else:
                            prosedur_tampil_data_rental(plat_nomor, model, brand, harga_sewa, supir,
                                                        nomor_supir, banyak_data)
                
                input('[ENTER] untuk melanjutkan...')
                os.system(hapus)
                menu_user = fungsi_menu_user(menu_user)
    os.system(hapus)
    menu_utama = fungsi_menu_utama(menu_utama)

# Keluar aplikasi
os.system(hapus)
print('╔══════════════════════════════════════════════════════════════════════════╗')
print('║                                                                          ║')
print('║   +  T E R I M A   K A S I H   T E L A H   M E N G G U N A K A N   +     ║')
print('║                     +   K O K O   R E N T A L   +                        ║')
print('║                                                                          ║')
print('║   Semoga perjalanan Anda menyenangkan dan penuh pengalaman seru!         ║')
print('║   Jangan ragu untuk kembali menggunakan layanan kami kapan saja.         ║')
print('║                                                                          ║')
print('║   Follow kami di @KokoRental untuk promo menarik dan info terbaru!       ║')
print('║                                                                          ║')
print('╚══════════════════════════════════════════════════════════════════════════╝')
