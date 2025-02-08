import mouse
import keyboard
import time

password="admin123"
#LIST PAUJI
#flow unit>menu1>input+>enter>data>show
click_list_default = [
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
    "7","","2",""
    ]

click_list = ["4", "5", "6"]



def automate(click_list,delay=0.1,islocked=True,isselectadmin=True):
    print("TEST IN PROGRESS. DO NOT TOUCH!")
    time.sleep(1)
    mouse.move(-4000, -4000, absolute=True, duration=0.1)
    mouse.move(100, 630, absolute=False, duration=0.1)
    mouse.click()
    time.sleep(delay)
    keyboard.press_and_release('ctrl+f5')
    time.sleep(delay+0.1)
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
        keyboard.write(text_to_insert, delay=0.01)
        keyboard.press_and_release('enter')
        time.sleep(delay)


def main():
    while True:
        try:
            print("""
            1.automate default
            2.automate list
            3.automate custom
            """)
            menu = int(input(">"))
            if menu == 1:
                automate(click_list_default,0.01,True,False)
            elif menu == 2:
                automate(click_list, 0.01)
        except Exception as e:
            print("error:", e)


if __name__ == "__main__":
    main()
