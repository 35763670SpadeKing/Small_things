
import keyboard 
import time

pressed = False  

def on_left_button_down():
    global pressed
    pressed = True
    keyboard.press('left')

def on_left_button_up():
    global pressed
    if pressed:
        keyboard.release('left')
    pressed = False

def timer_tick():
    global pressed
    if pressed:
        keyboard.send('left')       

def other_key_down(event):
    pass

keyboard.on_release('left', on_left_button_up)  
keyboard.on_press('left', on_left_button_down)  

keyboard.on_press(other_key_down)

while True:
    try:
        timer_tick()
        time.sleep(0.2)
    except:
        pass