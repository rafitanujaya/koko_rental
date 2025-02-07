#  deriel
import os
def menu_login():
    print('<<<   login  >>>')
    print('----------------')
    print('1. Admin')
    print('2. User')
    print('0. Keluar')
    print('----------------')
    status = int(input('Pilihan anda: '))
    while(status < 0) or (status > 2):
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

def masuk_admin():
    print('--------------------------------------------')
    print('|  L O G I N   S E B A G A I   A D M I N   |')
    print('--------------------------------------------')
    password = chr(input('Password : '))

    percobaan = 3
    while (password != 'admin123') and (percobaan > 0):
        percobaan -= 1
        os.system('cls')
        print(f'pasword salah, silahkan isi lagi. sisi percobaan {percobaan}')
        os.system('pause')
        os.system('cls')
        print('--------------------------------------------')
        print('|  L O G I N   S E B A G A I   A D M I N   |')
        print('--------------------------------------------')
        password = chr(input('Password : '))
    return password

def menu_admin():
    print('---------------------------')
    print('|  M E N U   A D M I N D  |')
    print('---------------------------')
    print('| 1. CRUD                 |')
    print('| 2. Sorting              |')
    print('| 3. Searching            |')
    print('---------------------------')
    pilihan = int(input('Pilihan anda : '))
    while(pilihan < 0) or (pilihan > 4):
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


posisi = menu_login()
while (posisi != 0):
    match posisi:
        case '1':
                os.system('cls')
                login_admin = masuk_admin()
                if (login_admin == 'admind123'):
                    os.system('cls')
                    pilihan_admin = menu_admin()

