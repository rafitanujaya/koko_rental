def function_akun_user(akun_user) :
    if akun_user == 'y' :
        return True
    else :
        return False
def procedure_buat_akun(data_user,data_pass) :
    print('Silahkan buat akun')
    i = 0
    while data_user[i] != '/' :
        i += 1
    data_user[i] = str(input('Masukkan username baru : '))
    data_pass[i] = str(input('Masukkan password baru : '))
def function_login_user(data_user, data_pass, user_login, user_pass) :
    counter = 0

#main program user
data_user = ['/'] * 10
data_pass = ['/'] * 10
akun_user = str(input('Sudah Punya Akun? [y/n]: '))
status_akun = function_akun_user(akun_user)
if not status_akun :
    procedure_buat_akun(data_user,data_pass)
print('Silahkan Login Dahulu')
user_login = str(input('Masukkan username : '))
user_pass = str(input('Masukkan password : '))

