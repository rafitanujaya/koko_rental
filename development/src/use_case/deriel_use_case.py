import os


def function_menu_login():
    print('-------------------------------------')
    print('|<<<  P I L I H A N   L O G I N  >>>|')
    print('-------------------------------------')
    print('| 1. Login sebagai Admin            |')
    print('| 2. Login sebagai User             |')
    print('| 0. Keluar                         |')
    print('-------------------------------------')
    status = int(input('Pilihan anda: '))
    while (status < 0) or (status > 2):
        os.system('cls')
        print('pilihan tidak ada')
        os.system('pause')
        print('-------------------------------------')
        print('|<<<  P I L I H A N   L O G I N  >>>|')
        print('-------------------------------------')
        print('| 1. Login sebagai Admin            |')
        print('| 2. Login sebagai User             |')
        print('| 0. Keluar                         |')
        print('-------------------------------------')
        status = int(input('Pilihan anda: '))
    return status


def function_masuk_admin():
    percobaan = 3
    print('--------------------------------------------')
    print('|  L O G I N   S E B A G A I   A D M I N   |')
    print('--------------------------------------------')
    password = str(input('Password : '))
    while (password != PASSWORD) and (percobaan > 0):
        os.system('cls')
        print(f'pasword salah, silahkan isi lagi. sisi percobaan {percobaan}')
        os.system('pause')
        os.system('cls')
        percobaan -= 1
        print('--------------------------------------------')
        print('|  L O G I N   S E B A G A I   A D M I N   |')
        print('--------------------------------------------')
        password = str(input('Password : '))
    return password


def function_isi_banyak_data(banyak_data):
    print('--------------------------------------------')
    print('| BERAPA BANYAK DATA YANG INGIN DIMASUKAN? |')
    print('--------------------------------------------')
    print('')
    banyak_data = int(input('Banyak data : '))
    while (banyak_data < 0):
        os.system('cls')
        print('Banyak data tidak boleh kurang dari 0. ualngi!!')
        os.system('pause')
        os.system('cls')
        print('--------------------------------------------')
        print('| BERAPA BANYAK DATA YANG INGIN DIMASUKAN? |')
        print('--------------------------------------------')
        print('')
        banyak_data = int(input('Banyak data : '))
    os.system('cls')
    print(' + +  TERIMAKASI ATAS INFORMASINYA  + + ')
    print('           SELAMAT BEKERJA :)           ')
    os.system('pause')
    return banyak_data


def function_menu_admin():
    print('---------------------------')
    print('|  M E N U   A D M I N D  |')
    print('---------------------------')
    print('| 1. CRUD                 |')
    print('| 2. Sorting              |')
    print('| 3. Searching            |')
    print('| 0. keluar               |')
    print('---------------------------')
    pilihan = int(input('Pilihan anda : '))
    while (pilihan < 0) or (pilihan > 4):
        os.system('cls')
        print('Pilihan yang anda pilih tidak ada, silahkan isi kembali!')
        os.system('pause')
        os.system('cls')
        print('---------------------------')
        print('|  M E N U   A D M I N D  |')
        print('---------------------------')
        print('| 1. CRUD                 |')
        print('| 2. Sorting              |')
        print('| 3. Searching            |')
        print('| 0. keluar               |')
        print('---------------------------')
        pilihan = int(input('Pilihan anda : '))
    return pilihan


def function_Menu_CRUD():
    print('---------------------------------')
    print('|      M E N U    C R U D       |')
    print('---------------------------------')
    print('| 1. Membuat data rental        |')
    print('| 2. Menghitung data            |')
    print('| 3. Menampilkan data           |')
    print('| 4. Mencari harga              |')
    print('| 5. Menghitung rata rata harga |')
    print('| 6. Menambahkan data baru      |')
    print('| 7. Penyisipan daya            |')
    print('| 8. Penghapusan data           |')
    print('| 0. Keluar                     |')
    print('---------------------------------')
    pilihan = int(input('Pilihan anda : '))
    while (pilihan < 0) or (pilihan > 8):
        os.system('cls')
        print('pilihan tidak ada')
        os.system('pause')
        print('---------------------------------')
        print('|      M E N U    C R U D       |')
        print('---------------------------------')
        print('| 1. Membuat data rental        |')
        print('| 2. Menghitung data            |')
        print('| 3. Menampilkan data           |')
        print('| 4. Mencari harga              |')
        print('| 5. Menghitung rata rata harga |')
        print('| 6. Menambahkan data baru      |')
        print('| 7. Penyisipan daya            |')
        print('| 8. Penghapusan data           |')
        print('| 0. Keluar                     |')
        print('---------------------------------')
        pilihan = int(input('Pilihan anda : '))
    return pilihan


def function_isi_data(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL, HARGA, SUPIR, NOMOR_SUPIR, banyak_data):
    print('-----------------------------------------------')
    print('|  M E M A S U K A N   J U M L A H   D A T A  |')
    print('-----------------------------------------------')
    i = 0
    while (i < banyak_data):
        print(f'data mobil ke-{i + 1}')
        PLAT_MOBIL[i] = str(input('Plat Mobil  : ')).upper()
        BRAND_MOBIL[i] = str(input('Brand Mobil : ')).upper()
        MODEL_MOBIL[i] = str(input('Model Mobil : ')).upper()
        HARGA[i] = int(input('Harga       : Rp.'))
        SUPIR[i] = str(input('Nama Supir  : ')).upper()
        NOMOR_SUPIR[i] = str(input('Nomor Supir : '))
        print('-----------------------------------------------')
        i += 1
    banyak_data = i
    return banyak_data


def function_tapil_banyak_data(banyak_data):
    print(f'Banyak kendaraan yang tersedia yaitu {banyak_data}')


def function_tampil_data(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL, HARGA, SUPIR, NOMOR_SUPIR, banyak_data):
    print('--------------------------------------------------------------------------------------------')
    print('| No. |  Plat Mobil  |   Brand   |   Model   |     Harga     |    Supir    |  Nomor Supir  |')
    print('--------------------------------------------------------------------------------------------')
    for i in range(banyak_data):
        print(
            f'|  {i + 1:<2} |  {PLAT_MOBIL[i]:10}  |  {BRAND_MOBIL[i]:7}  |  {MODEL_MOBIL[i]:>7}  | Rp.{HARGA[i]:<10} | {SUPIR[i]:11} | {NOMOR_SUPIR[i]:<13} |')
        print('--------------------------------------------------------------------------------------------')


def function_tampil_harga(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL, HARGA, SUPIR, NOMOR_SUPIR, banyak_data):
    print('----------------------------------------------------------------------------------------------------')
    print('| keterangan |     Harga     |  Plat Mobil  |   Brand   |   Model   |    Supir    |  Nomor Supir  |')
    print('----------------------------------------------------------------------------------------------------')
    print(
        f'|  Termahal  | Rp.{HARGA[banyak_data - 1]:<10} |  {PLAT_MOBIL[banyak_data - 1]:10}  |  {BRAND_MOBIL[banyak_data - 1]:7}  |  {MODEL_MOBIL[banyak_data - 1]:>7}  | {SUPIR[banyak_data - 1]:11} | {NOMOR_SUPIR[banyak_data - 1]:<13} |')
    print(
        f'|  Termurah  | Rp.{HARGA[0]:<10} |  {PLAT_MOBIL[0]:10}  |  {BRAND_MOBIL[0]:7}  |  {MODEL_MOBIL[0]:>7}  | {SUPIR[0]:11} | {NOMOR_SUPIR[0]:<13} |')
    print('----------------------------------------------------------------------------------------------------')


def function_rata_rata_harga(HARGA, banyak_data):
    total_harga = 0
    for i in range(banyak_data):
        total_harga += HARGA[i]
    rata_rata = total_harga // banyak_data
    return rata_rata


def function_tambah_data(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL, HARGA, SUPIR, NOMOR_SUPIR, banyak_data):
    PLAT_MOBIL[banyak_data] = str(input('Plat Mobil  : ')).upper()
    BRAND_MOBIL[banyak_data] = str(input('Brand Mobil : ')).upper()
    MODEL_MOBIL[banyak_data] = str(input('Model Mobil : ')).upper()
    HARGA[banyak_data] = int(input('Harga       : Rp.'))
    SUPIR[banyak_data] = str(input('Nama Supir  : ')).upper()
    NOMOR_SUPIR[banyak_data] = str(input('Nomor Supir : '))
    os.system('cls')
    print('Data diterima :D')
    os.system('pause')
    os.system('cls')


def function_penyisipan_data(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL, HARGA, SUPIR, NOMOR_SUPIR, banyak_data, posisi):
    if (posisi - 1 >= 0) and (posisi - 1 <= banyak_data - 1):
        i = banyak_data
        while (i >= posis - 1):
            PLAT_MOBIL[i + 1] = PLAT_MOBIL[i]
            BRAND_MOBIL[i + 1] = BRAND_MOBIL[i]
            MODEL_MOBIL[i + 1] = MODEL_MOBIL[i]
            HARGA[i + 1] = HARGA[i]
            SUPIR[i + 1] = SUPIR[i]
            NOMOR_SUPIR[i + 1] = NOMOR_SUPIR[i]
            i -= 1

        PLAT_MOBIL[posis - 1] = str(input('Plat Mobil  : ')).upper()
        BRAND_MOBIL[posis - 1] = str(input('Brand Mobil : ')).upper()
        MODEL_MOBIL[posis - 1] = str(input('Model Mobil : ')).upper()
        HARGA[posis - 1] = int(input('Harga       : Rp.'))
        SUPIR[posis - 1] = str(input('Nama Supir  : ')).upper()
        NOMOR_SUPIR[posis - 1] = str(input('Nomor Supir : '))
    else:
        os.system('cls')
        print('data tidak valid!!')


def function_penghapusan_data(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL, HARGA, SUPIR, NOMOR_SUPIR, banyak_data, posisi):
    if (posisi - 1 >= 0) and (posisi - 1 <= banyak_data - 1):
        i = banyak_data
        for i in range(posis, banyak_data):
            PLAT_MOBIL[i - 1] = PLAT_MOBIL[i]
            BRAND_MOBIL[i - 1] = BRAND_MOBIL[i]
            MODEL_MOBIL[i - 1] = MODEL_MOBIL[i]
            HARGA[i - 1] = HARGA[i]
            SUPIR[i - 1] = SUPIR[i]
            NOMOR_SUPIR[i - 1] = NOMOR_SUPIR[i]

        PLAT_MOBIL[posis - 1] = '/'
        BRAND_MOBIL[posis - 1] = '/'
        MODEL_MOBIL[posis - 1] = '/'
        HARGA[posis - 1] = 0
        SUPIR[posis - 1] = '/'
        NOMOR_SUPIR[posis - 1] = 0
    else:
        os.system('cls')
        print('data tidak valid!!')


def function_Menu_sorting():
    print('-------------------------------')
    print('|  M E N U   S H O T R I N G  |')
    print('-------------------------------')
    print('| 1. Terurut secara naik      |')
    print('| 2. Terurut secara Menurun   |')
    print('| 0. Keluar                   |')
    print('-------------------------------')
    pilihan = int(input('Pilihan anda : '))
    while (pilihan < 0) or (pilihan > 2):
        os.system('cls')
        print('pilihan tidak ada')
        os.system('pause')
        print('-------------------------------')
        print('|  M E N U   S H O T R I N G  |')
        print('-------------------------------')
        print('| 1. Terurut secara naik      |')
        print('| 2. Terurut secara Menurun   |')
        print('| 0. Keluar                   |')
        print('-------------------------------')
        pilihan = int(input('Pilihan anda : '))
    return pilihan


def function_menu_shorting_naik():
    print('-----------------------------------------')
    print('|  M E N U   S H O R T I N G   N A I K  |')
    print('-----------------------------------------')
    print('| 1. Berdasarkan plat                   |')
    print('| 2. berdasarkan brand                  |')
    print('| 3. Berdasarkan model                  |')
    print('| 4. Berdasarkan harga                  |')
    print('| 5. berdasarkan nama supir             |')
    print('| 6. Berdasarkan nomor supir            |')
    print('| 0. kembali                            |')
    print('-----------------------------------------')
    pilihan = int(input('Pilihan anda : '))
    while (pilihan < 0) or (pilihan > 6):
        os.system('cls')
        print('pilihan tidak ada')
        os.system('pause')
        print('-----------------------------------------')
        print('|  M E N U   S H O R T I N G   N A I K  |')
        print('-----------------------------------------')
        print('| 1. Berdasarkan plat                   |')
        print('| 2. berdasarkan brand                  |')
        print('| 3. Berdasarkan model                  |')
        print('| 4. Berdasarkan harga                  |')
        print('| 5. berdasarkan nama supir             |')
        print('| 6. Berdasarkan nomor supir            |')
        print('| 0. kembali                            |')
        print('-----------------------------------------')
        pilihan = int(input('Pilihan anda : '))
    return pilihan


def function_shorting_naik_plat(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL, HARGA, SUPIR, NOMOR_SUPIR, banyak_data):
    for i in range(banyak_data - 1):
        j = banyak_data - 2
        while (j >= i + 1):
            if (PLAT_MOBIL[j] < PLAT_MOBIL[j - 1]):
                Temp = PLAT_MOBIL[j]
                PLAT_MOBIL[j] = PLAT_MOBIL[j - 1]
                PLAT_MOBIL[j - 1] = Temp

                Temp = BRAND_MOBIL[j]
                BRAND_MOBIL[j] = BRAND_MOBIL[j - 1]
                BRAND_MOBIL[j - 1] = Temp

                Temp = MODEL_MOBIL[j]
                MODEL_MOBIL[j] = MODEL_MOBIL[j - 1]
                MODEL_MOBIL[j - 1] = Temp

                Temp = HARGA[j]
                HARGA[j] = HARGA[j - 1]
                HARGA[j - 1] = Temp

                Temp = SUPIR[j]
                SUPIR[j] = SUPIR[j - 1]
                SUPIR[j - 1] = Temp

                Temp = NOMOR_SUPIR[j]
                NOMOR_SUPIR[j] = NOMOR_SUPIR[j - 1]
                NOMOR_SUPIR[j - 1] = Temp
            j -= 1


def function_shorting_naik_brand(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL, HARGA, SUPIR, NOMOR_SUPIR, banyak_data):
    for i in range(banyak_data - 1):
        j = banyak_data - 2
        while (j >= i + 1):
            if (BRAND_MOBIL[j] < BRAND_MOBIL[j - 1]):
                Temp = PLAT_MOBIL[j]
                PLAT_MOBIL[j] = PLAT_MOBIL[j - 1]
                PLAT_MOBIL[j - 1] = Temp

                Temp = BRAND_MOBIL[j]
                BRAND_MOBIL[j] = BRAND_MOBIL[j - 1]
                BRAND_MOBIL[j - 1] = Temp

                Temp = MODEL_MOBIL[j]
                MODEL_MOBIL[j] = MODEL_MOBIL[j - 1]
                MODEL_MOBIL[j - 1] = Temp

                Temp = HARGA[j]
                HARGA[j] = HARGA[j - 1]
                HARGA[j - 1] = Temp

                Temp = SUPIR[j]
                SUPIR[j] = SUPIR[j - 1]
                SUPIR[j - 1] = Temp

                Temp = NOMOR_SUPIR[j]
                NOMOR_SUPIR[j] = NOMOR_SUPIR[j - 1]
                NOMOR_SUPIR[j - 1] = Temp
            j -= 1


def function_shorting_naik_model(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL, HARGA, SUPIR, NOMOR_SUPIR, banyak_data):
    for i in range(banyak_data - 1):
        j = banyak_data - 2
        while (j >= i + 1):
            if (MODEL_MOBIL[j] < MODEL_MOBIL[j - 1]):
                Temp = PLAT_MOBIL[j]
                PLAT_MOBIL[j] = PLAT_MOBIL[j - 1]
                PLAT_MOBIL[j - 1] = Temp

                Temp = BRAND_MOBIL[j]
                BRAND_MOBIL[j] = BRAND_MOBIL[j - 1]
                BRAND_MOBIL[j - 1] = Temp

                Temp = MODEL_MOBIL[j]
                MODEL_MOBIL[j] = MODEL_MOBIL[j - 1]
                MODEL_MOBIL[j - 1] = Temp

                Temp = HARGA[j]
                HARGA[j] = HARGA[j - 1]
                HARGA[j - 1] = Temp

                Temp = SUPIR[j]
                SUPIR[j] = SUPIR[j - 1]
                SUPIR[j - 1] = Temp

                Temp = NOMOR_SUPIR[j]
                NOMOR_SUPIR[j] = NOMOR_SUPIR[j - 1]
                NOMOR_SUPIR[j - 1] = Temp
            j -= 1


def function_shorting_naik_harga(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL, HARGA, SUPIR, NOMOR_SUPIR, banyak_data):
    for i in range(banyak_data - 1):
        j = banyak_data - 2
        while (j >= i + 1):
            if (HARGA[j] < HARGA[j - 1]):
                Temp = PLAT_MOBIL[j]
                PLAT_MOBIL[j] = PLAT_MOBIL[j - 1]
                PLAT_MOBIL[j - 1] = Temp

                Temp = BRAND_MOBIL[j]
                BRAND_MOBIL[j] = BRAND_MOBIL[j - 1]
                BRAND_MOBIL[j - 1] = Temp

                Temp = MODEL_MOBIL[j]
                MODEL_MOBIL[j] = MODEL_MOBIL[j - 1]
                MODEL_MOBIL[j - 1] = Temp

                Temp = HARGA[j]
                HARGA[j] = HARGA[j - 1]
                HARGA[j - 1] = Temp

                Temp = SUPIR[j]
                SUPIR[j] = SUPIR[j - 1]
                SUPIR[j - 1] = Temp

                Temp = NOMOR_SUPIR[j]
                NOMOR_SUPIR[j] = NOMOR_SUPIR[j - 1]
                NOMOR_SUPIR[j - 1] = Temp
            j -= 1


def function_shorting_naik_supir(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL, HARGA, SUPIR, NOMOR_SUPIR, banyak_data):
    for i in range(banyak_data - 1):
        j = banyak_data - 2
        while (j >= i + 1):
            if (SUPIR[j] < SUPIR[j - 1]):
                Temp = PLAT_MOBIL[j]
                PLAT_MOBIL[j] = PLAT_MOBIL[j - 1]
                PLAT_MOBIL[j - 1] = Temp

                Temp = BRAND_MOBIL[j]
                BRAND_MOBIL[j] = BRAND_MOBIL[j - 1]
                BRAND_MOBIL[j - 1] = Temp

                Temp = MODEL_MOBIL[j]
                MODEL_MOBIL[j] = MODEL_MOBIL[j - 1]
                MODEL_MOBIL[j - 1] = Temp

                Temp = HARGA[j]
                HARGA[j] = HARGA[j - 1]
                HARGA[j - 1] = Temp

                Temp = SUPIR[j]
                SUPIR[j] = SUPIR[j - 1]
                SUPIR[j - 1] = Temp

                Temp = NOMOR_SUPIR[j]
                NOMOR_SUPIR[j] = NOMOR_SUPIR[j - 1]
                NOMOR_SUPIR[j - 1] = Temp
            j -= 1


def function_shorting_naik_nomor_supir(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL, HARGA, SUPIR, NOMOR_SUPIR, banyak_data):
    for i in range(banyak_data - 1):
        j = banyak_data - 2
        while (j >= i + 1):
            if (NOMOR_SUPIR[j] < NOMOR_SUPIR[j - 1]):
                Temp = PLAT_MOBIL[j]
                PLAT_MOBIL[j] = PLAT_MOBIL[j - 1]
                PLAT_MOBIL[j - 1] = Temp

                Temp = BRAND_MOBIL[j]
                BRAND_MOBIL[j] = BRAND_MOBIL[j - 1]
                BRAND_MOBIL[j - 1] = Temp

                Temp = MODEL_MOBIL[j]
                MODEL_MOBIL[j] = MODEL_MOBIL[j - 1]
                MODEL_MOBIL[j - 1] = Temp

                Temp = HARGA[j]
                HARGA[j] = HARGA[j - 1]
                HARGA[j - 1] = Temp

                Temp = SUPIR[j]
                SUPIR[j] = SUPIR[j - 1]
                SUPIR[j - 1] = Temp

                Temp = NOMOR_SUPIR[j]
                NOMOR_SUPIR[j] = NOMOR_SUPIR[j - 1]
                NOMOR_SUPIR[j - 1] = Temp
            j -= 1


def function_menu_shorting_turun():
    print('-------------------------------------------')
    print('|  M E N U   S H O R T I N G   T U R U N  |')
    print('-------------------------------------------')
    print('| 1. Berdasarkan plat                     |')
    print('| 2. berdasarkan brand                    |')
    print('| 3. Berdasarkan model                    |')
    print('| 4. Berdasarkan harga                    |')
    print('| 5. berdasarkan nama supir               |')
    print('| 6. Berdasarkan nomor supir              |')
    print('| 0. kembali                              |')
    print('-------------------------------------------')
    pilihan = int(input('Pilihan anda : '))
    while (pilihan < 0) or (pilihan > 6):
        os.system('cls')
        print('pilihan tidak ada')
        os.system('pause')
        print('-------------------------------------------')
        print('|  M E N U   S H O R T I N G   T U R U N  |')
        print('-------------------------------------------')
        print('| 1. Berdasarkan plat                     |')
        print('| 2. berdasarkan brand                    |')
        print('| 3. Berdasarkan model                    |')
        print('| 4. Berdasarkan harga                    |')
        print('| 5. berdasarkan nama supir               |')
        print('| 6. Berdasarkan nomor supir              |')
        print('| 0. kembali                              |')
        print('-------------------------------------------')
        pilihan = int(input('Pilihan anda : '))
    return pilihan


def function_shorting_turun_plat(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL, HARGA, SUPIR, NOMOR_SUPIR, banyak_data):
    for i in range(banyak_data - 1):
        for j in range(banyak_data - (i + 1)):
            if (PLAT_MOBIL[j] < PLAT_MOBIL[j + 1]):
                Temp = PLAT_MOBIL[j]
                PLAT_MOBIL[j] = PLAT_MOBIL[j + 1]
                PLAT_MOBIL[j + 1] = Temp

                Temp = BRAND_MOBIL[j]
                BRAND_MOBIL[j] = BRAND_MOBIL[j + 1]
                BRAND_MOBIL[j + 1] = Temp

                Temp = MODEL_MOBIL[j]
                MODEL_MOBIL[j] = MODEL_MOBIL[j + 1]
                MODEL_MOBIL[j + 1] = Temp

                Temp = HARGA[j]
                HARGA[j] = HARGA[j + 1]
                HARGA[j + 1] = Temp

                Temp = SUPIR[j]
                SUPIR[j] = SUPIR[j + 1]
                SUPIR[j + 1] = Temp

                Temp = NOMOR_SUPIR[j]
                NOMOR_SUPIR[j] = NOMOR_SUPIR[j + 1]
                NOMOR_SUPIR[j + 1] = Temp


def function_shorting_turun_brand(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL, HARGA, SUPIR, NOMOR_SUPIR, banyak_data):
    for i in range(banyak_data - 1):
        for j in range(banyak_data - (i + 1)):
            if (BRAND_MOBIL[j] < BRAND_MOBIL[j + 1]):
                Temp = PLAT_MOBIL[j]
                PLAT_MOBIL[j] = PLAT_MOBIL[j + 1]
                PLAT_MOBIL[j + 1] = Temp

                Temp = BRAND_MOBIL[j]
                BRAND_MOBIL[j] = BRAND_MOBIL[j + 1]
                BRAND_MOBIL[j + 1] = Temp

                Temp = MODEL_MOBIL[j]
                MODEL_MOBIL[j] = MODEL_MOBIL[j + 1]
                MODEL_MOBIL[j + 1] = Temp

                Temp = HARGA[j]
                HARGA[j] = HARGA[j + 1]
                HARGA[j + 1] = Temp

                Temp = SUPIR[j]
                SUPIR[j] = SUPIR[j + 1]
                SUPIR[j + 1] = Temp

                Temp = NOMOR_SUPIR[j]
                NOMOR_SUPIR[j] = NOMOR_SUPIR[j + 1]
                NOMOR_SUPIR[j + 1] = Temp


def function_shorting_turun_model(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL, HARGA, SUPIR, NOMOR_SUPIR, banyak_data):
    for i in range(banyak_data - 1):
        for j in range(banyak_data - (i + 1)):
            if (MODEL_MOBIL[j] < MODEL_MOBIL[j + 1]):
                Temp = PLAT_MOBIL[j]
                PLAT_MOBIL[j] = PLAT_MOBIL[j + 1]
                PLAT_MOBIL[j + 1] = Temp

                Temp = BRAND_MOBIL[j]
                BRAND_MOBIL[j] = BRAND_MOBIL[j + 1]
                BRAND_MOBIL[j + 1] = Temp

                Temp = MODEL_MOBIL[j]
                MODEL_MOBIL[j] = MODEL_MOBIL[j + 1]
                MODEL_MOBIL[j + 1] = Temp

                Temp = HARGA[j]
                HARGA[j] = HARGA[j + 1]
                HARGA[j + 1] = Temp

                Temp = SUPIR[j]
                SUPIR[j] = SUPIR[j + 1]
                SUPIR[j + 1] = Temp

                Temp = NOMOR_SUPIR[j]
                NOMOR_SUPIR[j] = NOMOR_SUPIR[j + 1]
                NOMOR_SUPIR[j + 1] = Temp


def function_shorting_turun_harga(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL, HARGA, SUPIR, NOMOR_SUPIR, banyak_data):
    for i in range(banyak_data - 1):
        for j in range(banyak_data - (i + 1)):
            if (HARGA[j] < HARGA[j + 1]):
                Temp = PLAT_MOBIL[j]
                PLAT_MOBIL[j] = PLAT_MOBIL[j + 1]
                PLAT_MOBIL[j + 1] = Temp

                Temp = BRAND_MOBIL[j]
                BRAND_MOBIL[j] = BRAND_MOBIL[j + 1]
                BRAND_MOBIL[j + 1] = Temp

                Temp = MODEL_MOBIL[j]
                MODEL_MOBIL[j] = MODEL_MOBIL[j + 1]
                MODEL_MOBIL[j + 1] = Temp

                Temp = HARGA[j]
                HARGA[j] = HARGA[j + 1]
                HARGA[j + 1] = Temp

                Temp = SUPIR[j]
                SUPIR[j] = SUPIR[j + 1]
                SUPIR[j + 1] = Temp

                Temp = NOMOR_SUPIR[j]
                NOMOR_SUPIR[j] = NOMOR_SUPIR[j + 1]
                NOMOR_SUPIR[j + 1] = Temp


def function_shorting_turun_supir(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL, HARGA, SUPIR, NOMOR_SUPIR, banyak_data):
    for i in range(banyak_data - 1):
        for j in range(banyak_data - (i + 1)):
            if (SUPIR[j] < SUPIR[j + 1]):
                Temp = PLAT_MOBIL[j]
                PLAT_MOBIL[j] = PLAT_MOBIL[j + 1]
                PLAT_MOBIL[j + 1] = Temp

                Temp = BRAND_MOBIL[j]
                BRAND_MOBIL[j] = BRAND_MOBIL[j + 1]
                BRAND_MOBIL[j + 1] = Temp

                Temp = MODEL_MOBIL[j]
                MODEL_MOBIL[j] = MODEL_MOBIL[j + 1]
                MODEL_MOBIL[j + 1] = Temp

                Temp = HARGA[j]
                HARGA[j] = HARGA[j + 1]
                HARGA[j + 1] = Temp

                Temp = SUPIR[j]
                SUPIR[j] = SUPIR[j + 1]
                SUPIR[j + 1] = Temp

                Temp = NOMOR_SUPIR[j]
                NOMOR_SUPIR[j] = NOMOR_SUPIR[j + 1]
                NOMOR_SUPIR[j + 1] = Temp


def function_shorting_turun_nomor_supir(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL, HARGA, SUPIR, NOMOR_SUPIR, banyak_data):
    for i in range(banyak_data - 1):
        for j in range(banyak_data - (i + 1)):
            if (NOMOR_SUPIR[j] < NOMOR_SUPIR[j + 1]):
                Temp = PLAT_MOBIL[j]
                PLAT_MOBIL[j] = PLAT_MOBIL[j + 1]
                PLAT_MOBIL[j + 1] = Temp

                Temp = BRAND_MOBIL[j]
                BRAND_MOBIL[j] = BRAND_MOBIL[j + 1]
                BRAND_MOBIL[j + 1] = Temp

                Temp = MODEL_MOBIL[j]
                MODEL_MOBIL[j] = MODEL_MOBIL[j + 1]
                MODEL_MOBIL[j + 1] = Temp

                Temp = HARGA[j]
                HARGA[j] = HARGA[j + 1]
                HARGA[j + 1] = Temp

                Temp = SUPIR[j]
                SUPIR[j] = SUPIR[j + 1]
                SUPIR[j + 1] = Temp

                Temp = NOMOR_SUPIR[j]
                NOMOR_SUPIR[j] = NOMOR_SUPIR[j + 1]
                NOMOR_SUPIR[j + 1] = Temp


def function_menu_searching():
    print('-----------------------------------------')
    print('| M E N U   P E N C A R I A N   D A T A |')
    print('-----------------------------------------')
    print('| 1. Mencari plat nomor                 |')
    print('| 2. Mencari brand mobil                |')
    print('| 3. Mencari model mobil                |')
    print('| 4. Mencari harga                      |')
    print('| 5. mencari nama supir                 |')
    print('| 6. Mencari nomor supir                |')
    print('| 0. keluar                             |')
    print('-----------------------------------------')
    pilihan = int(input('Pilihan anda : '))
    while (pilihan < 0) or (pilihan > 6):
        os.system('cls')
        print('pilihan tidak ada')
        os.system('pause')
        print('-----------------------------------------')
        print('| M E N U   P E N C A R I A N   D A T A |')
        print('-----------------------------------------')
        print('| 1. Mencari plat nomor                 |')
        print('| 2. Mencari brand mobil                |')
        print('| 3. Mencari model mobil                |')
        print('| 4. Mencari harga                      |')
        print('| 5. mencari nama supir                 |')
        print('| 6. Mencari nomor supir                |')
        print('| 0. keluar                             |')
        print('-----------------------------------------')
        pilihan = int(input('Pilihan anda : '))
    return pilihan


def function_cari_plat(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL, HARGA, SUPIR, NOMOR_SUPIR, banyak_data):
    cari = str(input('Plat yang ingin dicari : ')).upper()
    Ia = 0
    Ib = banyak_data - 1
    dapat = False
    while (not dapat) and (Ia <= Ib):
        k = (Ia + Ib) // 2
        if (PLAT_MOBIL[k] == cari):
            dapat = True
        else:
            if (PLAT_MOBIL[k] < cari):
                Ia = k + 1
            else:
                Ib = k - 1
    os.system('cls')
    if (dapat):
        print(f'Plat mobil {cari} ditemukan')
        print('Keterangan : ')
        print('--------------------------------------------------------------------------------------')
        print('|  Plat Mobil  |   Brand   |   Model   |     Harga     |    Supir    |  Nomor Supir  |')
        print('--------------------------------------------------------------------------------------')
        print(
            f'|  {PLAT_MOBIL[k]:10}  |  {BRAND_MOBIL[k]:7}  |  {MODEL_MOBIL[k]:>7}  | Rp.{HARGA[k]:<10} | {SUPIR[k]:11} | {NOMOR_SUPIR[k]:<13} |')
        print('--------------------------------------------------------------------------------------------')
    else:
        print(f'Plat mobil {cari} tidak ditemukan')


def function_cari_brand(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL, HARGA, SUPIR, NOMOR_SUPIR, banyak_data):
    cari = str(input('Brand yang ingin dicari  : ')).upper()
    i = 0
    while (BRAND_MOBIL[i] != cari) and (i < banyak_data):
        i += 1
    os.system('cls')
    if (BRAND_MOBIL[i] == cari):
        print(f'Brand mobil {cari} ditemukan')
        print('Keterangan : ')
        print('-------------------------------------------------------------------------------------------')
        print('| No |  Plat Mobil  |   Brand   |   Model   |     Harga     |    Supir    |  Nomor Supir  |')
        print('-------------------------------------------------------------------------------------------')
        No = 0
        for j in range(i, banyak_data):
            if (BRAND_MOBIL[j] == cari):
                No += 1
                print(
                    f'| {No:>2} |  {PLAT_MOBIL[j]:10}  |  {BRAND_MOBIL[j]:7}  |  {MODEL_MOBIL[j]:>7}  | Rp.{HARGA[j]:<10} | {SUPIR[j]:11} | {NOMOR_SUPIR[j]:<13} |')
                print('--------------------------------------------------------------------------------------------')
    else:
        print(f'Brand mobil {cari} tidak ditemukan')


def function_cari_model(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL, HARGA, SUPIR, NOMOR_SUPIR, banyak_data):
    cari = str(input('Brand yang ingin dicari  : ')).upper()
    i = 0
    while (MODEL_MOBIL[i] != cari) and (i < banyak_data):
        i += 1
    os.system('cls')
    if (MODEL_MOBIL[i] == cari):
        print(f'Model mobil {cari} ditemukan')
        print('Keterangan : ')
        print('-------------------------------------------------------------------------------------------')
        print('| No |  Plat Mobil  |   Brand   |   Model   |     Harga     |    Supir    |  Nomor Supir  |')
        print('-------------------------------------------------------------------------------------------')
        No = 0
        for j in range(i, banyak_data):
            if (MODEL_MOBIL[j] == cari):
                No += 1
                print(
                    f'| {No:>2} |  {PLAT_MOBIL[j]:10}  |  {BRAND_MOBIL[j]:7}  |  {MODEL_MOBIL[j]:>7}  | Rp.{HARGA[j]:<10} | {SUPIR[j]:11} | {NOMOR_SUPIR[j]:<13} |')
                print('--------------------------------------------------------------------------------------------')
    else:
        print(f'Model mobil {cari} tidak ditemukan')


def function_cari_harga(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL, HARGA, SUPIR, NOMOR_SUPIR, banyak_data):
    cari = int(input('Brand yang ingin dicari  : '))
    i = 0
    while (HARGA[i] != cari) and (i < banyak_data):
        i += 1
    os.system('cls')
    if (HARGA[i] == cari):
        print(f'Brand mobil {cari} ditemukan')
        print('Keterangan : ')
        print('-------------------------------------------------------------------------------------------')
        print('| No |  Plat Mobil  |   Brand   |   Model   |     Harga     |    Supir    |  Nomor Supir  |')
        print('-------------------------------------------------------------------------------------------')
        No = 0
        for j in range(i, banyak_data):
            if (HARGA[j] == cari):
                No += 1
                print(
                    f'| {No:>2} |  {PLAT_MOBIL[j]:10}  |  {BRAND_MOBIL[j]:7}  |  {MODEL_MOBIL[j]:>7}  | Rp.{HARGA[j]:<10} | {SUPIR[j]:11} | {NOMOR_SUPIR[j]:<13} |')
                print('--------------------------------------------------------------------------------------------')
    else:
        print(f'Brand mobil {cari} tidak ditemukan')


def function_cari_supir(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL, HARGA, SUPIR, NOMOR_SUPIR, banyak_data):
    cari = str(input('Brand yang ingin dicari  : ')).upper()
    i = 0
    while (SUPIR[i] != cari) and (i < banyak_data):
        i += 1
    os.system('cls')
    if (SUPIR[i] == cari):
        print(f'Brand mobil {cari} ditemukan')
        print('Keterangan : ')
        print('-------------------------------------------------------------------------------------------')
        print('| No |  Plat Mobil  |   Brand   |   Model   |     Harga     |    Supir    |  Nomor Supir  |')
        print('-------------------------------------------------------------------------------------------')
        No = 0
        for j in range(i, banyak_data):
            if (SUPIR[j] == cari):
                No += 1
                print(
                    f'| {No:>2} |  {PLAT_MOBIL[j]:10}  |  {BRAND_MOBIL[j]:7}  |  {MODEL_MOBIL[j]:>7}  | Rp.{HARGA[j]:<10} | {SUPIR[j]:11} | {NOMOR_SUPIR[j]:<13} |')
                print('--------------------------------------------------------------------------------------------')
    else:
        print(f'Brand mobil {cari} tidak ditemukan')


def function_cari_nomor_supir(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL, HARGA, SUPIR, NOMOR_SUPIR, banyak_data):
    cari = str(input('Plat yang ingin dicari : '))
    Ia = 0
    Ib = banyak_data - 1
    dapat = False
    while (not dapat) and (Ia <= Ib):
        k = (Ia + Ib) // 2
        if (NOMOR_SUPIR[k] == cari):
            dapat = True
        else:
            if (NOMOR_SUPIR[k] < cari):
                Ia = k + 1
            else:
                Ib = k - 1
    os.system('cls')
    if (dapat):
        print(f'Plat mobil {cari} ditemukan')
        print('Keterangan : ')
        print('--------------------------------------------------------------------------------------')
        print('|  Plat Mobil  |   Brand   |   Model   |     Harga     |    Supir    |  Nomor Supir  |')
        print('--------------------------------------------------------------------------------------')
        print(
            f'|  {PLAT_MOBIL[k]:10}  |  {BRAND_MOBIL[k]:7}  |  {MODEL_MOBIL[k]:>7}  | Rp.{HARGA[k]:<10} | {SUPIR[k]:11} | {NOMOR_SUPIR[k]:<13} |')
        print('--------------------------------------------------------------------------------------------')
    else:
        print(f'Plat mobil {cari} tidak ditemukan')


def function_menu_user():
    print('-----------------------')
    print('|  M E N U   U S E R  |')
    print('-----------------------')
    print('| 1. Informasi data   |')
    print('| 2. Sewa kendaraan   |')
    print('| 3. Transaksi        |')
    print('| 0. kembali          |')
    print('-----------------------')
    pilihan = int(input('Pilihan anda :'))
    while (pilihan < 0) or (pilihan > 3):
        os.system('cls')
        print('pilihan tidak ada')
        os.system('pause')
        print('-----------------------')
        print('|  M E N U   U S E R  |')
        print('-----------------------')
        print('| 1. Informasi data   |')
        print('| 2. Sewa kendaraan   |')
        print('| 3. Transaksi        |')
        print('| 0. kembali          |')
        print('-----------------------')
        pilihan = int(input('Pilihan anda : '))
    return pilihan


# badan_utama_program
PASSWORD = 'admin123'
posisi = function_menu_login()
while (posisi != 0):
    match posisi:
        case 1:
            os.system('cls')
            login_admin = function_masuk_admin()
            if (login_admin == PASSWORD):
                os.system('cls')
                banyak_data = 0
                banyak_data = function_isi_banyak_data(banyak_data)
                PLAT_MOBIL = ['/'] * banyak_data
                BRAND_MOBIL = ['/'] * banyak_data
                MODEL_MOBIL = ['/'] * banyak_data
                HARGA = [0] * banyak_data
                SUPIR = ['/'] * banyak_data
                NOMOR_SUPIR = ['/'] * banyak_data
                os.system('cls')
                pilihan_admin = function_menu_admin()
                while (pilihan_admin != 0):
                    match pilihan_admin:
                        case 1:
                            os.system('cls')
                            pilihan_CRUD = function_Menu_CRUD()
                            while (pilihan_CRUD != 0):
                                match pilihan_CRUD:
                                    case 1:
                                        os.system('cls')
                                        function_isi_data(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL, HARGA, SUPIR,NOMOR_SUPIR, banyak_data)
                                    case 2:
                                        os.system('cls')
                                        function_tapil_banyak_data(banyak_data)
                                    case 3:
                                        os.system('cls')
                                        function_tampil_data(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL, HARGA, SUPIR,NOMOR_SUPIR, banyak_data)
                                    case 4:
                                        os.system('cls')
                                        function_shorting_naik_harga(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL, HARGA, SUPIR,NOMOR_SUPIR, banyak_data)
                                        function_tampil_harga(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL, HARGA, SUPIR,NOMOR_SUPIR, banyak_data)
                                    case 5:
                                        os.system('cls')
                                        rata_rata = function_rata_rata_harga(HARGA, banyak_data)
                                        function_tampil_data(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL, HARGA, SUPIR,NOMOR_SUPIR, banyak_data)
                                        print(f'harga rata-rata sewa mobil adalah Rp.{rata_rata:,}')
                                    case 6:
                                        os.system('cls')
                                        function_tambah_data(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL, HARGA, SUPIR,NOMOR_SUPIR, banyak_data)
                                        banyak_data += 1
                                        lihatkan = str(
                                            input('Apakah anda ingin menampilkan hasilnya? [IYA / TIDAK] : ')).upper()
                                        if (lihatkan == 'IYA'):
                                            function_tampil_data()
                                        else:
                                            print('Baiklah, terimakasih. tekan enter untuk melanjutkan.')
                                    case 7:
                                        os.system('cls')
                                        posis = int(input('posisi data yang disisip : '))
                                        if (posisi > 0) or (posis < banyak_data):
                                            function_penyisipan_data(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL, HARGA, SUPIR,NOMOR_SUPIR, banyak_data, posisi)
                                            banyak_data += 1
                                            lihatkan = str(input(
                                                'Apakah anda ingin menampilkan hasilnya? [IYA / TIDAK] : ')).upper()
                                            if (lihatkan == 'IYA'):
                                                function_tampil_data()
                                            else:
                                                print('Baiklah, terimakasih. tekan enter untuk melanjutkan.')
                                        else:
                                            print('posisi tidak valid. tolong ulangi!')
                                    case 8:
                                        os.system('cls')
                                        posis = int(input('posisi data yang dihapus : '))
                                        if (posisi > 0) or (posis < banyak_data):
                                            function_penghapusan_data(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL, HARGA,SUPIR, NOMOR_SUPIR, banyak_data, posisi)
                                            banyak_data -= 1
                                            lihatkan = str(input(
                                                'Apakah anda ingin menampilkan hasilnya? [IYA / TIDAK] : ')).upper()
                                            if (lihatkan == 'IYA'):
                                                function_tampil_data()
                                            else:
                                                print('Baiklah, terimakasih. tekan enter untuk melanjutkan.')
                                        else:
                                            print('posisi tidak valid. tolong ulangi!')

                                os.system('pause')
                                os.system('cls')
                                pilihan_CRUD = function_Menu_CRUD()
                        case 2:
                            os.system('cls')
                            pilihan_sorting = function_Menu_sorting()
                            while (pilihan_sorting != 0):
                                match pilihan_sorting:
                                    case 1:
                                        os.system('cls')
                                        Pilihan_shorting_naik = function_menu_shorting_naik()
                                        while (Pilihan_shorting_naik != 0):
                                            match Pilihan_shorting_naik:
                                                case 1:
                                                    os.system('cls')
                                                    function_shorting_naik_plat(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL,HARGA, SUPIR, NOMOR_SUPIR, banyak_data)
                                                    function_tampil_data(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL, HARGA,SUPIR, NOMOR_SUPIR, banyak_data)
                                                case 2:
                                                    os.system('cls')
                                                    function_shorting_naik_brand(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL,HARGA, SUPIR, NOMOR_SUPIR, banyak_data)
                                                    function_tampil_data(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL, HARGA,SUPIR, NOMOR_SUPIR, banyak_data)
                                                case 3:
                                                    os.system('cls')
                                                    function_shorting_naik_model(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL,HARGA, SUPIR, NOMOR_SUPIR, banyak_data)
                                                    function_tampil_data(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL, HARGA,SUPIR, NOMOR_SUPIR, banyak_data)
                                                case 4:
                                                    os.system('cls')
                                                    function_shorting_naik_harga(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL,HARGA, SUPIR, NOMOR_SUPIR, banyak_data)
                                                    function_tampil_data(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL, HARGA,SUPIR, NOMOR_SUPIR, banyak_data)
                                                case 5:
                                                    os.system('cls')
                                                    function_shorting_naik_supir(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL,HARGA, SUPIR, NOMOR_SUPIR, banyak_data)
                                                    function_tampil_data(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL, HARGA,SUPIR, NOMOR_SUPIR, banyak_data)
                                                case 6:
                                                    os.system('cls')
                                                    function_shorting_naik_nomor_supir(PLAT_MOBIL, BRAND_MOBIL,MODEL_MOBIL, HARGA, SUPIR,NOMOR_SUPIR, banyak_data)
                                                    function_tampil_data(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL, HARGA,SUPIR, NOMOR_SUPIR, banyak_data)
                                            os.system('pause')
                                            os.system('cls')
                                            Pilihan_shorting_naik = function_menu_shorting_naik()
                                    case 2:
                                        os.system('cls')
                                        Pilihan_shorting_turun = function_menu_shorting_turun()
                                        while (Pilihan_shorting_turun != 0):
                                            match Pilihan_shorting_turun:
                                                case 1:
                                                    os.system('cls')
                                                    function_shorting_turun_plat(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL,HARGA, SUPIR, NOMOR_SUPIR, banyak_data)
                                                    function_tampil_data(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL, HARGA,SUPIR, NOMOR_SUPIR, banyak_data)
                                                case 2:
                                                    os.system('cls')
                                                    function_shorting_turun_brand(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL,HARGA, SUPIR, NOMOR_SUPIR,banyak_data)
                                                    function_tampil_data(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL, HARGA,SUPIR, NOMOR_SUPIR, banyak_data)
                                                case 3:
                                                    os.system('cls')
                                                    function_shorting_turun_model(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL,HARGA, SUPIR, NOMOR_SUPIR,banyak_data)
                                                    function_tampil_data(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL, HARGA,SUPIR, NOMOR_SUPIR, banyak_data)
                                                case 4:
                                                    os.system('cls')
                                                    function_shorting_turun_harga(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL,HARGA, SUPIR, NOMOR_SUPIR,banyak_data)
                                                    function_tampil_data(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL, HARGA,SUPIR, NOMOR_SUPIR, banyak_data)
                                                case 5:
                                                    os.system('cls')
                                                    function_shorting_turun_supir(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL,HARGA, SUPIR, NOMOR_SUPIR,banyak_data)
                                                    function_tampil_data(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL, HARGA,SUPIR, NOMOR_SUPIR, banyak_data)
                                                case 6:
                                                    os.system('cls')
                                                    function_shorting_turun_nomor_supir(PLAT_MOBIL, BRAND_MOBIL,MODEL_MOBIL, HARGA, SUPIR,NOMOR_SUPIR, banyak_data)
                                                    function_tampil_data(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL, HARGA,SUPIR, NOMOR_SUPIR, banyak_data)
                                            os.system('pause')
                                            os.system('cls')
                                            Pilihan_shorting_turun = function_menu_shorting_turun()
                                os.system('pause')
                                os.system('cls')
                                pilihan_sorting = function_Menu_sorting()
                        case 3:
                            os.system('cls')
                            Pilihan_searching = function_menu_searching()
                            while (Pilihan_searching != 0):
                                match Pilihan_searching:
                                    case 1:
                                        os.system('cls')
                                        function_shorting_naik_plat(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL, HARGA, SUPIR,NOMOR_SUPIR, banyak_data)
                                        function_cari_plat(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL, HARGA, SUPIR,NOMOR_SUPIR, banyak_data)
                                    case 2:
                                        os.system('cls')
                                        function_cari_brand(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL, HARGA, SUPIR,NOMOR_SUPIR, banyak_data)
                                    case 3:
                                        os.system('cls')
                                        function_cari_model(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL, HARGA, SUPIR,NOMOR_SUPIR, banyak_data)
                                    case 4:
                                        os.system('cls')
                                        function_cari_harga(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL, HARGA, SUPIR,NOMOR_SUPIR, banyak_data)
                                    case 5:
                                        os.system('cls')
                                        function_cari_supir(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL, HARGA, SUPIR,NOMOR_SUPIR, banyak_data)
                                    case 6:
                                        os.system('cls')
                                        function_shorting_naik_nomor_supir(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL, HARGA,SUPIR, NOMOR_SUPIR, banyak_data)
                                        function_cari_nomor_supir(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL, HARGA, SUPIR,NOMOR_SUPIR, banyak_data)
                                os.system('pause')
                                os.system('cls')
                                Pilihan_searching = function_menu_searching()
                    os.system('pause')
                    os.system('cls')
                    pilihan_admin = function_menu_admin()
            else:
                print('Anda sudah 3 kali salah, anda sudah tidak bisa masuk')
        case 2:
            os.system('cls')
            pilihan_user = function_menu_user()
            while (pilihan_user != 0):
                match pilihan_user:
                    case 1:
                        os.system('cls')
                    # case 2 :
                    # case 3 :
    os.system('pause')
    os.system('cls')
    posisi = function_menu_login()
print('terimakasih sudah menggunakan layanan kali :D')
