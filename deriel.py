#  deriel
import os
from abi import *
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
        print('<<<   login  >>>')
        print('----------------')
        print('1. Admin')
        print('2. User')
        print('0. Keluar')
        print('----------------')
        status = int(input('Pilihan anda: '))
    return status

if __name__ == "__main__":
    posisi = menu_login()
    while(posisi != 0):
        match posisi:
            case '1':
                seq_menu_utama()
