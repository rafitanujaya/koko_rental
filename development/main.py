# IMPORT 
import os

# DEKLARASI VARIABEL
PASSWORD = 'admin'
password = ''

# Menu
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


# start variabel

# end variabel

# start prosedur

# end prosdure

# start fungsi

# end fungsi


def fungsi_menu_utama(menu_utama):
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

def fungsi_validasi_admin(password):
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
    if(password != PASSWORD):
        os.system(hapus)
        print('╔══════════════════════════════════════════════════════════════════════════╗')
        print('║  Anda telah kehabisan kesempatan! Silakan hubungi developer.             ║')
        print('╚══════════════════════════════════════════════════════════════════════════╝')
        input('Tekan [ENTER] untuk melanjutkan.')
        os.system(hapus)
        return False
    else: 
        return True

def fungsi_menu_admin(menu_admin):
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
    
    while(menu_admin < 0) or (menu_admin > 3):
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

def fungsi_menu_admin_crud(menu_admin_crud):
    print('╔══════════════════════════════════════════════════════════════════════════╗')
    print('║                 -  +  -  M E N U   C. R. U. D.  -  +  -                  ║')
    print('╠═══════════════════════════════════╦══════════════════════════════════════╣')
    print('║  1. MEMBUAT / MEMASUKAN DATA      ║  6. MENAMBAHKAN DATA BARU            ║')
    print('║  2. JUMLAH BAANYAK DATA           ║  7. MENYISIPKAN SEBUAH DATA          ║')
    print('║  3. MENAMPILKAN DATA              ║  8. MENGHAPUS SEBUAH DATA            ║')
    print('║  4. HARGA TERMAHAL DAN TERMURAH   ║  9. DATA INSTAN                      ║')
    print('║  5. RATA-RATA HARGA RENTAL        ║                                      ║')
    print('╠═══════════════════════════════════╩══════════════════════════════════════╣')
    print('║                               0. KEMBALI                                 ║')
    print('╚══════════════════════════════════════════════════════════════════════════╝')
    print('>>> Masukkan pilihan Anda dan tekan [ENTER] untuk melanjutkan.')
    menu_admin_crud = int(input(' Masukan pilihan anda : '))
    
    while(menu_admin_crud < 0) or (menu_admin_crud > 9):
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
        print('║  1. MEMBUAT / MEMASUKAN DATA      ║  6. MENAMBAHKAN DATA BARU            ║')
        print('║  2. JUMLAH BAANYAK DATA           ║  7. MENYISIPKAN SEBUAH DATA          ║')
        print('║  3. MENAMPILKAN DATA              ║  8. MENGHAPUS SEBUAH DATA            ║')
        print('║  4. HARGA TERMAHAL DAN TERMURAH   ║  9. DATA INSTAN                      ║')
        print('║  5. RATA-RATA HARGA RENTAL        ║                                      ║')
        print('╚═══════════════════════════════════╩══════════════════════════════════════╝')
        input('Tekan [ENTER] untuk melanjutkan.')
        os.system(hapus) 
        
        print('╔══════════════════════════════════════════════════════════════════════════╗')
        print('║                 -  +  -  M E N U   C. R. U. D.  -  +  -                  ║')
        print('╠═══════════════════════════════════╦══════════════════════════════════════╣')
        print('║  1. MEMBUAT / MEMASUKAN DATA      ║  6. MENAMBAHKAN DATA BARU            ║')
        print('║  2. JUMLAH BAANYAK DATA           ║  7. MENYISIPKAN SEBUAH DATA          ║')
        print('║  3. MENAMPILKAN DATA              ║  8. MENGHAPUS SEBUAH DATA            ║')
        print('║  4. HARGA TERMAHAL DAN TERMURAH   ║  9. DATA INSTAN                      ║')
        print('║  5. RATA-RATA HARGA RENTAL        ║                                      ║')
        print('╠═══════════════════════════════════╩══════════════════════════════════════╣')
        print('║                               0. KEMBALI                                 ║')
        print('╚══════════════════════════════════════════════════════════════════════════╝')
        print('>>> Masukkan pilihan Anda dan tekan [ENTER] untuk melanjutkan.')
        menu_admin_crud = int(input(' Masukan pilihan anda : '))   
    
    return menu_admin_crud

def fungsi_menu_admin_sorting(menu_admin_sorting):
    print('╔══════════════════════════════════════════════════════════════════════════╗')
    print('║              -  +  -  M E N U   P E N G U R U T A N  -  +  -             ║')
    print('╠═══════════════════════════════════╦══════════════════════════════════════╣')
    print('║  1. SECARA MENAIK ( ASCENDING )   ║  2. SECARA MENURUN ( DESCENDING )    ║')
    print('╠═══════════════════════════════════╩══════════════════════════════════════╣')
    print('║                               0. KEMBALI                                 ║')
    print('╚══════════════════════════════════════════════════════════════════════════╝')
    print('>>> Masukkan pilihan Anda dan tekan [ENTER] untuk melanjutkan.')
    menu_admin_sorting = int(input(' Masukan pilihan anda : '))
    
    while(menu_admin_sorting < 0) or (menu_admin_sorting > 2):
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
        
def fungsi_menu_admin_sorting_asc(menu_admin_sorting_asc):
    print('╔══════════════════════════════════════════════════════════════════════════╗')
    print('║      -  +  -  M E N U   P E N G U R U T A N   M E N A I K  -  +  -       ║')
    print('╠═══════════════════════════════════╦══════════════════════════════════════╣')
    print('║  1. BERDASARKAN PLAT NOMOR        ║  5. BERDASARKAN NAMA SUPIR           ║')
    print('║  2. BERDASARKAN MODEL             ║  6. BERDASARKAN NOMOR TELEPON SUPIR  ║')
    print('║  3. BERDASARKAN BRAND             ║  7. DATA INSTAN                      ║')
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
        print('║  0. KEMBALI                       ║  7. DATA INSTAN                      ║')
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
        
def fungsi_menu_admin_sorting_desc(menu_admin_sorting_desc):
    print('╔══════════════════════════════════════════════════════════════════════════╗')
    print('║      -  +  -  M E N U   P E N G U R U T A N   M E N U R U N  -  +  -       ║')
    print('╠═══════════════════════════════════╦══════════════════════════════════════╣')
    print('║  1. BERDASARKAN PLAT NOMOR        ║  5. BERDASARKAN NAMA SUPIR           ║')
    print('║  2. BERDASARKAN MODEL             ║  6. BERDASARKAN NOMOR TELEPON SUPIR  ║')
    print('║  3. BERDASARKAN BRAND             ║  7. DATA INSTAN                      ║')
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
        print('║  0. KEMBALI                       ║  7. DATA INSTAN                      ║')
        print('╚═══════════════════════════════════╩══════════════════════════════════════╝')
        input('Tekan [ENTER] untuk melanjutkan.')
        os.system(hapus) 
        
        print('╔══════════════════════════════════════════════════════════════════════════╗')
        print('║      -  +  -  M E N U   P E N G U R U T A N   M E N U R U N  -  +  -       ║')
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
    
def fungsi_menu_admin_searching(menu_admin_searching):
    print('╔══════════════════════════════════════════════════════════════════════════╗')
    print('║               -  +  -  M E N U   P E N C A R I A N  -  +  -              ║')
    print('╠═══════════════════════════════════╦══════════════════════════════════════╣')
    print('║  1. SECARA BERUNTUN ( SQUENTIAL ) ║  2. SECARA BINARY                    ║')
    print('╠═══════════════════════════════════╩══════════════════════════════════════╣')
    print('║                               0. KEMBALI                                 ║')
    print('╚══════════════════════════════════════════════════════════════════════════╝')
    print('>>> Masukkan pilihan Anda dan tekan [ENTER] untuk melanjutkan.')
    menu_admin_searching = int(input(' Masukan pilihan anda : '))
    
    while(menu_admin_searching < 0 ) and (menu_admin_searching > 2):
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
        
def fungsi_menu_admin_searching_sequential(menu_admin_searching_sequential):
    print('╔══════════════════════════════════════════════════════════════════════════╗')
    print('║     -  +  -  M E N U   P E N C A R I A N   B E R U N T U N  -  +  -      ║')
    print('╠═══════════════════════════════════╦══════════════════════════════════════╣')
    print('║  1. BERDASARKAN MODEL             ║  3. BERDASARKAN HARGA                ║')
    print('║  2. BERDASARKAN BRAND             ║  4. BERDASARKAN NAMA SUPIR           ║')
    print('║  3. BERDASARKAN HARGA             ║  5. DATA INSTAN                      ║')
    print('╠═══════════════════════════════════╩══════════════════════════════════════╣')
    print('║                               0. KEMBALI                                 ║')
    print('╚══════════════════════════════════════════════════════════════════════════╝')
    print('>>> Masukkan pilihan Anda dan tekan [ENTER] untuk melanjutkan.')
    menu_admin_searching_sequential = int(input(' Masukan pilihan anda : '))
    
    while(menu_admin_searching_sequential < 0) and (menu_admin_searching_sequential > 4):
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
        print('║  0. KELUAR                        ║  5. DATA INSTAN                      ║')
        print('╚═══════════════════════════════════╩══════════════════════════════════════╝')
        input('Tekan [ENTER] untuk melanjutkan.')
        os.system(hapus) 
        print('╔══════════════════════════════════════════════════════════════════════════╗')
        print('║     -  +  -  M E N U   P E N C A R I A N   B E R U N T U N  -  +  -      ║')
        print('╠═══════════════════════════════════╦══════════════════════════════════════╣')
        print('║  1. BERDASARKAN MODEL             ║  3. BERDASARKAN HARGA                ║')
        print('║  2. BERDASARKAN BRAND             ║  4. BERDASARKAN NAMA SUPIR           ║')
        print('║  3. BERDASARKAN HARGA             ║  5. DATA INSTAN                      ║')
        print('╠═══════════════════════════════════╩══════════════════════════════════════╣')
        print('║                               0. KEMBALI                                 ║')
        print('╚══════════════════════════════════════════════════════════════════════════╝')
        print('>>> Masukkan pilihan Anda dan tekan [ENTER] untuk melanjutkan.')
        menu_admin_searching_sequential = int(input(' Masukan pilihan anda : '))
        
    return menu_admin_searching_sequential

def fungsi_menu_admin_searching_binary(menu_admin_searching_binary):
    print('╔══════════════════════════════════════════════════════════════════════════╗')
    print('║       -  +  -  M E N U   P E N C A R I A N   B I N A R Y  -  +  -        ║')
    print('╠═══════════════════════════════════╦══════════════════════════════════════╣')
    print('║  1. BERDASARKAN PLAT NOMOR        ║  2. BERDASARKAN NOMOR TELEPON SUPIR  ║')
    print('║  0. KEMBALI                       ║  3. DATA INSTAN                      ║')
    print('╚═══════════════════════════════════╩══════════════════════════════════════╝')
    print('>>> Masukkan pilihan Anda dan tekan [ENTER] untuk melanjutkan.')
    menu_admin_searching_binary = int(input(' Masukan pilihan anda : '))
    
    while(menu_admin_searching_binary < 0 ) and (menu_admin_searching_binary > 3):
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
        print('║  0. KEMBALI                       ║  3. DATA INSTAN                      ║')
        print('╚═══════════════════════════════════╩══════════════════════════════════════╝')
        input('Tekan [ENTER] untuk melanjutkan.')
        os.system(hapus) 

        print('╔══════════════════════════════════════════════════════════════════════════╗')
        print('║       -  +  -  M E N U   P E N C A R I A N   B I N A R Y  -  +  -        ║')
        print('╠═══════════════════════════════════╦══════════════════════════════════════╣')
        print('║  1. BERDASARKAN PLAT NOMOR        ║  2. BERDASARKAN NOMOR TELEPON SUPIR  ║')
        print('║  0. KEMBALI                       ║  3. DATA INSTAN                      ║')
        print('╚═══════════════════════════════════╩══════════════════════════════════════╝')
        print('>>> Masukkan pilihan Anda dan tekan [ENTER] untuk melanjutkan.')
        menu_admin_searching_binary = int(input(' Masukan pilihan anda : '))
    return menu_admin_searching_binary



menu_utama = fungsi_menu_utama(menu_utama)
while menu_utama != 0:
    os.system(hapus)
    match menu_utama: 
        case 1:
            login = fungsi_validasi_admin(password)
            if (login):
                menu_admin = fungsi_menu_admin(menu_admin)
                while(menu_admin != 0):
                    os.system(hapus)
                    match menu_admin:
                        case 1:
                            menu_admin_crud =  fungsi_menu_admin_crud(menu_admin_crud)
                            while(menu_admin_crud != 0):
                                os.system(hapus)
                                match menu_admin_crud:
                                    case 1:
                                        print('1')
                                    case 2:
                                        print('2')
                                    case 3:
                                        print('3')
                                    case 4:
                                        print('4')
                                    case 5:
                                        print('5')
                                    case 6:
                                        print('6')
                                    case 7:
                                        print('7')
                                    case 8:
                                        print('8')
                                    case 9:
                                        print('9')
                                os.system(hapus)
                                menu_admin_crud =  fungsi_menu_admin_crud(menu_admin_crud)
                        case 2:
                            menu_admin_sorting = fungsi_menu_admin_sorting(menu_admin_sorting)
                            while(menu_admin_sorting != 0):
                                os.system(hapus)
                                match menu_admin_sorting:
                                    case 1:
                                        menu_admin_sorting_asc = fungsi_menu_admin_sorting_asc(menu_admin_sorting_asc)
                                        while(menu_admin_sorting_asc != 0):
                                            os.system(hapus)
                                            match menu_admin_sorting_asc:
                                                case 1:
                                                    print('1')
                                                case 2:
                                                    print('1')
                                                case 3:
                                                    print('1')
                                                case 4:
                                                    print('1')
                                                case 5:
                                                    print('1')
                                                case 6:
                                                    print('1')
                                                case 7:
                                                    print('1')
                                            os.system(hapus)
                                            menu_admin_sorting_asc = fungsi_menu_admin_sorting_asc(menu_admin_sorting_asc)
                                    case 2:
                                        menu_admin_sorting_desc = fungsi_menu_admin_sorting_desc(menu_admin_sorting_desc)
                                        while(menu_admin_sorting_desc != 0):
                                            os.system(hapus)
                                            match menu_admin_sorting_desc:
                                                case 1:
                                                    print('1')
                                                case 2:
                                                    print('1')
                                                case 3:
                                                    print('1')
                                                case 4:
                                                    print('1')
                                                case 5:
                                                    print('1')
                                                case 6:
                                                    print('1')
                                                case 7:
                                                    print('1')
                                            os.system(hapus)
                                            menu_admin_sorting_desc = fungsi_menu_admin_sorting_desc(menu_admin_sorting_desc)
                                os.system(hapus)
                                menu_admin_sorting = fungsi_menu_admin_sorting(menu_admin_sorting)
                        case 3:
                            menu_admin_searching = fungsi_menu_admin_searching(menu_admin_searching)
                            while(menu_admin_searching != 0):
                                os.system(hapus)
                                match menu_admin_searching:
                                    case 1:
                                        menu_admin_searching_sequential = fungsi_menu_admin_searching_sequential(menu_admin_searching_sequential)
                                        while(menu_admin_searching_sequential != 0):
                                            match menu_admin_searching_sequential:
                                                case 1:
                                                    print('1')
                                                case 2:
                                                    print('2')
                                                case 3:
                                                    print('2')
                                                case 4:
                                                    print('2')
                                                case 5:
                                                    print('2')
                                            os.system(hapus)
                                            menu_admin_searching_sequential = fungsi_menu_admin_searching_sequential(menu_admin_searching_sequential)
                                    case 2:
                                        menu_admin_searching_binary = fungsi_menu_admin_searching_binary(menu_admin_searching_binary)
                                        while(menu_admin_searching_binary != 0):
                                            os.system(hapus)
                                            match menu_admin_searching_binary:
                                                case 1:
                                                    print('1')
                                                case 2:
                                                    print('1')
                                                case 3:
                                                    print('1')
                                            os.system(hapus)
                                            menu_admin_searching_binary = fungsi_menu_admin_searching_binary(menu_admin_searching_binary)
                                os.system(hapus)
                                menu_admin_searching = fungsi_menu_admin_searching(menu_admin_searching)
                    os.system(hapus)
                    menu_admin = fungsi_menu_admin(menu_admin)
        case 2:
            print('b')
    menu_utama = fungsi_menu_utama(menu_utama)

# Keluar aplikasi
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
