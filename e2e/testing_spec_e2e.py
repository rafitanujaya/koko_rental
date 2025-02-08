import mouse
import keyboard
import time

password="admin123"
click_list_default = ["1", "1", "1","","testcar","botcar","BK3333BT","1234567890","botnamehere","628571234","7"]
click_list = ["4", "5", "6"]



def automate(click_list,delay=0.1,islocked=True,isselectadmin=True):
    print("TEST IN PROGRESS. DO NOT TOUCH!")
    time.sleep(1)
    mouse.move(-4000, -4000, absolute=True, duration=0.1)
    mouse.move(100, 630, absolute=False, duration=0.1)
    mouse.click()
    time.sleep(delay)
    mouse.move(600, 200, absolute=False, duration=0.1)
    if isselectadmin:
        keyboard.write("1", delay=0.01)
        keyboard.press_and_release('enter')
        time.sleep(delay)
    if islocked:
        keyboard.write(password, delay=0.01)
        keyboard.press_and_release('enter')
        time.sleep(delay)

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
