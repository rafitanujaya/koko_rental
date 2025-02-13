import keyboard
import platform
if not platform.system() == "Darwin":
    print("WIN MODE")
    import mouse
    import time






#pip install mouse,keyboard
password="admin123"
#LIST PAUJI
#flow unit>menu1>input+>enter>data>show>delete-1>show>
#TAMBAH 10 UNIT, HAPUS 3 UNIT DI INDEX 1,2,2,3
click_list_pauji = [
    "10", "1", "10","",
    "testcar1","botcar1","BK1111BT","1234567890","bob","628571234",
    "testcar2","botcar2","BK2222BT","2345678901","agus","628574444",
    "testcar3","botcar3","BK3333BT","3456789012","budi","628571212",
    "testcar4","botcar4","BK4444BT","4567890123","bangbang","628574321",
    "testcar5","botcar5","BK1111BT","1234567890","emely","628571234",
    "testcar6","botcar6","BK5555BT","2345678901","pauji","628574444",
    "testcar7","botcar7","BK6666BT","3456789012","edd","628571212",
    "testcar8","botcar8","BK7777BT","4567890123","papi","628574321",
    "testcar9","botcar9","BK8888BT","1234567890","yangmulia","628571234",
    "testcar10","botcar10","BK9999BT","2345678901","pakpol","628574444",
    "7","","2","","1","2","","2","2","","3","7",""
    ]

#list rafi
#BUAT/TAMBAH/HAPUS/MUNCUL/RESET
click_list_rafi = [
    "1","admin", "1", "1","10",
    "testcar1","botcar1","BK1111BT","1234567890","bob","628571234",
    "testcar2","botcar2","BK2222BT","2345678901","agus","628574444",
    "testcar3","botcar3","BK3333BT","3456789012","budi","628571212",
    "testcar4","botcar4","BK4444BT","4567890123","bangbang","628574321",
    "testcar5","botcar5","BK1111BT","1234567890","emely","628571234",
    "testcar6","botcar6","BK5555BT","2345678901","pauji","628574444",
    "testcar7","botcar7","BK6666BT","3456789012","edd","628571212",
    "testcar8","botcar8","BK7777BT","4567890123","papi","628574321",
    "testcar9","botcar9","BK8888BT","1234567890","yangmulia","628571234",
    "testcar10","botcar10","BK9999BT","2345678901","pakpol","628574444",
    "2","5","3","5","1","3",
    "BK9876BT","testcartambahan1","botcartambahan1","4567890123","habibi","62812123456",
    "4","1",
    "BK1234NY","testcartNYISIP1","botcarNYISIP1","4567890123","abu bakar","62812000056",
    "7","8","6","2","1","5",
    "testcar1", "botcar1", "BK1111BT", "1234567890", "bob", "628571234",
    "testcar2", "botcar2", "BK2222BT", "2345678901", "agus", "628574444",
    "testcar3", "botcar3", "BK3333BT", "3456789012", "budi", "628571212",
    "testcar4", "botcar4", "BK4444BT", "4567890123", "bangbang", "628574321",
    "testcar5", "botcar5", "BK1111BT", "1234567890", "emely", "628571234","2"
    ]
click_list_main1 = [
                    "1","admin","1","1","2",
                    "BK1234AB","AWANJA","OYOTA","92162100","Sdr MACANATO","628126213369",
                    "BK1234AB","AWANJA","OYOTA","92162100","Sdr MACANATO","628126213369",
                    "3"
                   ]
click_list_main = [
                    "1","admin","1","1","10",
                    "BK1234AB","AWANJA","OYOTA","92162100","MACANATO","628126213369",
                    "BK5678CD","MODEL-U","TELZA","6952966900","TANTIN SUR","628394756218",
                    "BK1234EF","RY-8","MANZA","75262100","CJ","628112233369",
                    "BK9876GH","ZENTRA","QWERTY","12345678","John Doe","628123456789",
                    "BK5432IJ","NEXUS-X","ASDFGH","87654321","Jane Smith","628987654321",
                    "BK1357KL","OPTIMA","ZXCVBN","23456789","Alice Won","628456789012",
                    "BK2468MN","VORTEX","POIUYT","34567890","Bob bay","628321654987",
                    "BK3690OP","PHOENIX","LKJHGF","45678901","CharlieBro","628654321098",
                    "BK4821QR","AURORA","MNBVCX","56789012","Daisy Duck","628789012345",
                    "BK5793ST", "ECLIPSE", "QWERTY", "67890123", "Eve Adams", "628890123456",
                    "","2","","3","","4","","5","","7","y","1","2",
                    "BK5678CD","MODEL-U","TELZA","6952966900","TANTIN SUR","628394756218",
                    "BK1234EF","RY-8","MANZA","75262100","CJ","628112233369",
                    "","5",
                    "BK2468MN","VORTEX","POIUYT","34567890","Bob bay","628321654987",
                    "","2","",
    ]
start = ["1","admin"]
part1 = [
                    "1","1","10",
                    "BK1234AB","AWANJA","OYOTA","92162100","MACANATO","628126213369",
                    "BK5678CD","MODEL-U","TELZA","6952966900","TANTIN SUR","628394756218",
                    "BK1234EF","RY-8","MANZA","75262100","CJ","628112233369",
                    "BK9876GH","ZENTRA","QWERTY","12345678","John Doe","628123456789",
                    "BK5432IJ","NEXUS-X","ASDFGH","87654321","Jane Smith","628987654321",
                    "BK1357KL","OPTIMA","ZXCVBN","23456789","Alice Won","628456789012",
                    "BK2468MN","VORTEX","POIUYT","34567890","Bob bay","628321654987",
                    "BK3690OP","PHOENIX","LKJHGF","45678901","CharlieBro","628654321098",
                    "BK4821QR","AURORA","MNBVCX","56789012","Daisy Duck","628789012345",
                    "BK5793ST", "ECLIPSE", "QWERTY", "67890123", "Eve Adams", "628890123456",
                    "","2","","3","","4","","5","","7","4","1","2",
                    "BK3333CD","MODEL-Y","TELZA","6952966950","TANTIN SUR","626494756218",
                    "BK3003EF","RY-7X","MANZA","75262101","DERIEL","628112238469",
                    "","0"]
part2 = [           "1","5",
                    "BK6696MN","LAUNCER","MITCUBICI","65437654","RAPI","62812321457",
                    "","2","","4","3","8","y","","1","6",
                    "BK1234AB","AWANJA","OYOTA","92162100","MACANATO","628126213369",
                    "BK5678CD","MODEL-U","TELZA","6952966900","TANTIN SUR","628394756218",
                    "BK1234EF","RY-8","MANZA","75262100","CJ","628112233369",
                    "BK9876GH","ZENTRA","QWERTY","12345678","John Doe","628123456789",
                    "BK5432IJ","NEXUS-X","ASDFGH","87654321","Jane Smith","628987654321",
                    "BK1357KL","OPTIMA","ZXCVBN","23456789","Alice Won","628456789012",
                    "","2","","0","2","1","1","","","1","","","2","","","4","","","5","","","3","","","6","","","0","0",
    ]

click_list_main_dev = start+part2
#PLAT/MODEL/BRAND/HARGA/SUPIR/NOSUPIR
def automate(click_list,delay=0.1,islocked=True,isselectadmin=True):
    print("TEST IN PROGRESS. DO NOT TOUCH!")
    time.sleep(2.5)
    mouse.move(-40000, -40000, absolute=True, duration=0.1)
    mouse.move(100, 630, absolute=False, duration=0.1)
    mouse.click()
    time.sleep(delay)
    keyboard.press_and_release('ctrl+F5')
    time.sleep(delay+1.8)
    mouse.move(600, 200, absolute=False, duration=0.1)
    if isselectadmin:
        keyboard.write("1", delay=0.01)
        keyboard.press_and_release('enter')
        time.sleep(delay)
    if islocked:
        keyboard.write(password, delay=0.01)
        keyboard.press_and_release('enter')
        time.sleep(delay)
    time.sleep(0.01)
    for text_to_insert in click_list:
        if keyboard.is_pressed('backspace'):
            exit("Emergency triggered!")
        keyboard.write(text_to_insert, delay=0.01)
        keyboard.press_and_release('enter')
        time.sleep(delay)
    print("TEST PASSED")

def automate_mac(click_list,delay=0.1,islocked=True,isselectadmin=True):
    print("PRESS ESC TO START")
    while True:
        if keyboard.is_pressed('escape'):
            break
    print("TEST IN PROGRESS. DO NOT TOUCH!")
    if isselectadmin:
        keyboard.write("1", delay=0.01)
        keyboard.press_and_release('enter')
        time.sleep(delay)
    if islocked:
        keyboard.write(password, delay=0.01)
        keyboard.press_and_release('enter')
        time.sleep(delay)
    time.sleep(0.01)
    for text_to_insert in click_list:
        if keyboard.is_pressed('escape'):
            exit("Emergency triggered!")
        keyboard.write(text_to_insert, delay=0.01)
        keyboard.press_and_release('enter')
        time.sleep(delay)
    print("TEST PASSED")

def main():
    while True:
        try:
            print("""
            1.automate pauji
            2.automate rafi
            3.automate main
            4.automate main dev
            """)
            menu = int(input(">"))
            if menu == 1:
                if platform.system() == "Darwin":
                    automate_mac(click_list_pauji,0.01,True,False)
                else:
                    automate(click_list_pauji,0.01,True,False)
            elif menu == 2:
                if platform.system() == "Darwin":
                    automate_mac(click_list_rafi, 0.01,False,False)
                else:
                    automate(click_list_rafi, 0.01,False,False)
            if menu == 3:
                if platform.system() == "Darwin":
                    automate_mac(click_list_main,0.05,False,False)
                else:
                    automate(click_list_main,0.05,False,False)
            if menu == 4:
                if platform.system() == "Darwin":
                    automate_mac(click_list_main,0.1,False,False)
                else:
                    automate(click_list_main_dev,0.1,False,False)
        except Exception as e:
            print("error:", e)


if __name__ == "__main__":

    main()