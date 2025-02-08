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


def function_menu_admin():
    print('---------------------------')
    print('|  M E N U   A D M I N D  |')
    print('---------------------------')
    print('| 1. CRUD                 |')
    print('| 2. Sorting              |')
    print('| 3. Searching            |')
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


def function_isi_data(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL, HARGA, SUPIR, NOMOR_SUPIR):
    print('-----------------------------------------------')
    print('|  M E M A S U K A N   J U M L A H   D A T A  |')
    print('-----------------------------------------------')
    i = 0
    print(f'data mobil ke-{i + 1}')
    PLAT_MOBIL[i] = str(input('Plat Mobil : ')).upper()
    while (PLAT_MOBIL[i] != 'STOP'):
        BRAND_MOBIL[i] = str(input('Brand Mobil : '))
        MODEL_MOBIL[i] = str(input('Model Mobil : '))
        HARGA[i] = int(input('Harga       : Rp.'))
        SUPIR[i] = str(input('Nama Supir  : '))
        NOMOR_SUPIR[i] = int(input('Nomor Supir : '))
        i += 1
        if (i == 9):
            PLAT_MOBIL = 'STOP'
        else:
            print(f'data mobil ke-{i + 1}')
            PLAT_MOBIL[i] = str(input('Plat Mobil : ')).upper()
    banyak_data = i
    return banyak_data


def function_tampil_data(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL, HARGA, SUPIR, NOMOR_SUPIR, banyak_data):
    print('--------------------------------------------------------------------------------------------')
    print('| No. |  Plat Mobil  |   Brand   |   Model   |     Harga     |    Supir    |  Nomor Supir  |')
    print('--------------------------------------------------------------------------------------------')
    for i in range(banyak_data):
        print(
            f'|  {i + 1:<2} |  {PLAT_MOBIL[i]:10}  |  {BRAND_MOBIL[i]:7}  |  {MODEL_MOBIL[i]:7}  | Rp.{HARGA[i]:<10} | {SUPIR[i]:11} | {NOMOR_SUPIR[i]:<13} |')
        print('--------------------------------------------------------------------------------------------')


def function_rata_rata_harga(HARGA, banyak_data):
    total_harga = 0
    for i in range(banyak_data):
        total_harga += HARGA[i]
    rata_rata = total_harga // banyak_data
    return rata_rata


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
        print('-----------------------------------------')
        pilihan = int(input('Pilihan anda : '))
    return pilihan


def function_shorting_naik_plat(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL, HARGA, SUPIR, NOMOR_SUPIR, banyak_data):
    for i in range(banyak_data - 1):
        j = banyak_data
        while (j >= i + 1):
            if (PLAT_MOBIL[j] < PLAT_MOBIL[j + 1]):
                Temp = PLAT_MOBIL
                PLAT_MOBIL[j] = PLAT_MOBIL[j - 1]
                PLAT_MOBIL[j - 1] = Temp

                Temp = BRAND_MOBIL
                BRAND_MOBIL[j] = BRAND_MOBIL[j - 1]
                BRAND_MOBIL[j - 1] = Temp

                Temp = MODEL_MOBIL
                MODEL_MOBIL[j] = MODEL_MOBIL[j - 1]
                MODEL_MOBIL[j - 1] = Temp

                Temp = HARGA
                HARGA[j] = HARGA[j - 1]
                HARGA[j - 1] = Temp

                Temp = SUPIR
                SUPIR[j] = SUPIR[j - 1]
                SUPIR[j - 1] = Temp

                Temp = NOMOR_SUPIR
                NOMOR_SUPIR[j] = NOMOR_SUPIR[j - 1]
                NOMOR_SUPIR[j - 1] = Temp
            j -= 1


def function_shorting_naik_brand(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL, HARGA, SUPIR, NOMOR_SUPIR, banyak_data):
    for i in range(banyak_data - 1):
        j = banyak_data
        while (j >= i + 1):
            if (BRAND_MOBIL[j] < BRAND_MOBIL[j + 1]):
                Temp = PLAT_MOBIL
                PLAT_MOBIL[j] = PLAT_MOBIL[j - 1]
                PLAT_MOBIL[j - 1] = Temp

                Temp = BRAND_MOBIL
                BRAND_MOBIL[j] = BRAND_MOBIL[j - 1]
                BRAND_MOBIL[j - 1] = Temp

                Temp = MODEL_MOBIL
                MODEL_MOBIL[j] = MODEL_MOBIL[j - 1]
                MODEL_MOBIL[j - 1] = Temp

                Temp = HARGA
                HARGA[j] = HARGA[j - 1]
                HARGA[j - 1] = Temp

                Temp = SUPIR
                SUPIR[j] = SUPIR[j - 1]
                SUPIR[j - 1] = Temp

                Temp = NOMOR_SUPIR
                NOMOR_SUPIR[j] = NOMOR_SUPIR[j - 1]
                NOMOR_SUPIR[j - 1] = Temp
            j -= 1


def function_shorting_naik_model(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL, HARGA, SUPIR, NOMOR_SUPIR, banyak_data):
    for i in range(banyak_data - 1):
        j = banyak_data
        while (j >= i + 1):
            if (MODEL_MOBIL[j] < MODEL_MOBIL[j + 1]):
                Temp = PLAT_MOBIL
                PLAT_MOBIL[j] = PLAT_MOBIL[j - 1]
                PLAT_MOBIL[j - 1] = Temp

                Temp = BRAND_MOBIL
                BRAND_MOBIL[j] = BRAND_MOBIL[j - 1]
                BRAND_MOBIL[j - 1] = Temp

                Temp = MODEL_MOBIL
                MODEL_MOBIL[j] = MODEL_MOBIL[j - 1]
                MODEL_MOBIL[j - 1] = Temp

                Temp = HARGA
                HARGA[j] = HARGA[j - 1]
                HARGA[j - 1] = Temp

                Temp = SUPIR
                SUPIR[j] = SUPIR[j - 1]
                SUPIR[j - 1] = Temp

                Temp = NOMOR_SUPIR
                NOMOR_SUPIR[j] = NOMOR_SUPIR[j - 1]
                NOMOR_SUPIR[j - 1] = Temp
            j -= 1


def function_shorting_naik_harga(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL, HARGA, SUPIR, NOMOR_SUPIR, banyak_data):
    for i in range(banyak_data - 1):
        j = banyak_data
        while (j >= i + 1):
            if (HARGA[j] < HARGA[j + 1]):
                Temp = PLAT_MOBIL
                PLAT_MOBIL[j] = PLAT_MOBIL[j - 1]
                PLAT_MOBIL[j - 1] = Temp

                Temp = BRAND_MOBIL
                BRAND_MOBIL[j] = BRAND_MOBIL[j - 1]
                BRAND_MOBIL[j - 1] = Temp

                Temp = MODEL_MOBIL
                MODEL_MOBIL[j] = MODEL_MOBIL[j - 1]
                MODEL_MOBIL[j - 1] = Temp

                Temp = HARGA
                HARGA[j] = HARGA[j - 1]
                HARGA[j - 1] = Temp

                Temp = SUPIR
                SUPIR[j] = SUPIR[j - 1]
                SUPIR[j - 1] = Temp

                Temp = NOMOR_SUPIR
                NOMOR_SUPIR[j] = NOMOR_SUPIR[j - 1]
                NOMOR_SUPIR[j - 1] = Temp
            j -= 1


def function_shorting_naik_supir(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL, HARGA, SUPIR, NOMOR_SUPIR, banyak_data):
    for i in range(banyak_data - 1):
        j = banyak_data
        while (j >= i + 1):
            if (SUPIR[j] < NOMOR_SUPIR[j + 1]):
                Temp = PLAT_MOBIL
                PLAT_MOBIL[j] = PLAT_MOBIL[j - 1]
                PLAT_MOBIL[j - 1] = Temp

                Temp = BRAND_MOBIL
                BRAND_MOBIL[j] = BRAND_MOBIL[j - 1]
                BRAND_MOBIL[j - 1] = Temp

                Temp = MODEL_MOBIL
                MODEL_MOBIL[j] = MODEL_MOBIL[j - 1]
                MODEL_MOBIL[j - 1] = Temp

                Temp = HARGA
                HARGA[j] = HARGA[j - 1]
                HARGA[j - 1] = Temp

                Temp = SUPIR
                SUPIR[j] = SUPIR[j - 1]
                SUPIR[j - 1] = Temp

                Temp = NOMOR_SUPIR
                NOMOR_SUPIR[j] = NOMOR_SUPIR[j - 1]
                NOMOR_SUPIR[j - 1] = Temp
            j -= 1


def function_shorting_naik_nomor_supir(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL, HARGA, SUPIR, NOMOR_SUPIR, banyak_data):
    for i in range(banyak_data - 1):
        j = banyak_data
        while (j >= i + 1):
            if (NOMOR_SUPIR[j] < NOMOR_SUPIR[j + 1]):
                Temp = PLAT_MOBIL
                PLAT_MOBIL[j] = PLAT_MOBIL[j - 1]
                PLAT_MOBIL[j - 1] = Temp

                Temp = BRAND_MOBIL
                BRAND_MOBIL[j] = BRAND_MOBIL[j - 1]
                BRAND_MOBIL[j - 1] = Temp

                Temp = MODEL_MOBIL
                MODEL_MOBIL[j] = MODEL_MOBIL[j - 1]
                MODEL_MOBIL[j - 1] = Temp

                Temp = HARGA
                HARGA[j] = HARGA[j - 1]
                HARGA[j - 1] = Temp

                Temp = SUPIR
                SUPIR[j] = SUPIR[j - 1]
                SUPIR[j - 1] = Temp

                Temp = NOMOR_SUPIR
                NOMOR_SUPIR[j] = NOMOR_SUPIR[j - 1]
                NOMOR_SUPIR[j - 1] = Temp
            j -= 1


# badan_utama_program
MAKSDATA = 10
PASSWORD = 'admin123'
PLAT_MOBIL = ['/'] * MAKSDATA
BRAND_MOBIL = ['/'] * MAKSDATA
MODEL_MOBIL = ['/'] * MAKSDATA
HARGA = [0] * MAKSDATA
SUPIR = ['/'] * MAKSDATA
NOMOR_SUPIR = ['/'] * MAKSDATA
posisi = function_menu_login()
while (posisi != 0):
    match posisi:
        case 1:
            os.system('cls')
            login_admin = function_masuk_admin()
            if (login_admin == PASSWORD):
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
                                        banyak_data = function_isi_data(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL, HARGA,
                                                                        SUPIR, NOMOR_SUPIR)
                                    # case 2 :
                                    case 3:
                                        os.system('cls')
                                        if (banyak_data <= MAKSDATA):
                                            function_tampil_data(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL, HARGA, SUPIR,
                                                                 NOMOR_SUPIR, banyak_data)
                                        else:
                                            function_tampil_data(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL, HARGA, SUPIR,
                                                                 NOMOR_SUPIR, MAKSDATA)
                                    # case 4 :
                                    case 5:
                                        os.system('cls')
                                        rata_rata = function_rata_rata_harga(HARGA, banyak_data)
                                        function_tampil_data(PLAT_MOBIL, BRAND_MOBIL, MODEL_MOBIL, HARGA, SUPIR,
                                                             NOMOR_SUPIR, banyak_data)
                                        print(f'harga rata-rata sewa mobil adalah Rp.{rata_rata:,.2}')
                                    # case 6 :
                                    # case 7 :
                                    # case 8 :
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
                                os.system('pause')
                                os.system('cls')
                                pilihan_sorting = function_Menu_sorting()
                        case 3:
                            Pilihan_searching = function_menu_searching()
                    os.system('pause')
                    os.system('cls')
                    pilihan_admin = function_menu_admin()
            else:
                print('Anda sudah 3 kali salah, anda sudah tidak bisa masuk')
    os.system('pause')
    os.system('cls')
    posisi = function_menu_login()
