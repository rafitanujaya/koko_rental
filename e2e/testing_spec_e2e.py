import mouse
import keyboard
import time

print("TEST IN PROGRESS. DO NOT TOUCH!")
time.sleep(1)

mouse.move(-4000, -4000, absolute=True, duration=0.1)
mouse.move(500,800, absolute=True, duration=0.1)
# Click at the current mouse position
mouse.click()

text_to_insert = "test"
keyboard.write(text_to_insert, delay=0.01)
