from cv2 import threshold
import pyautogui


last_position = (None,None)

last_dir = ''

def keypress():
    ''' 
    Choose any four keys that a user can press to control the game.
    Update this doc string with your choices. 
    '''

    import keyboard
# put your code here
    while(keyboard.is_pressed("esc") == False):
        if(keyboard.is_pressed('T')):
            pyautogui.press("up")
            #print("up")
        elif(keyboard.is_pressed('H')):
            #print("right")
            pyautogui.press("right") 
        elif(keyboard.is_pressed('G')):
            #print("down")
            pyautogui.press("down")
        elif(keyboard.is_pressed('F')):
            #print("left") 
            pyautogui.press("left")

 
    
    


def trackpad_mouse():
    ''' 
    Control the game by moving the mouse/finger on trackpad left, right, up, or down. 
    '''

    from pynput import mouse

    def on_move(x, y):
        # put your code here
        global last_position
        global last_dir
        if last_position[0] == None or last_position[1] == None:
            last_position = (x,y)
        else:
            xdif =  x - last_position[0]
            ydif = y - last_position[1] 
            threshold = 200
            if abs(xdif) > threshold or abs(ydif) > threshold:
                if abs(xdif) > abs(ydif):
                    if xdif > 0:
                        last_dir = 'right'
                        print('right')
                    else:
                        last_dir = 'left'
                        print('left')
                else:
                    if ydif > 0:
                        last_dir = 'down'
                        print('up')
                    else:
                        last_dir = 'up'
                        print('down')
                pyautogui.press(last_dir)
                print(last_dir)
                last_position = (x,y)
                print(last_position)

    with mouse.Listener(on_move=on_move) as listener:
        listener.join() 

def color_tracker():
    import cv2
    import imutils
    import numpy as np
    from collections import deque
    import time
    import multithreaded_webcam as mw

    # You need to define HSV colour range MAKE CHANGE HERE
    colorLower = None
    colorUpper = None

    # set the limit for the number of frames to store and the number that have seen direction change
    buffer = 20
    pts = deque(maxlen = buffer)

    # store the direction and number of frames with direction change
    num_frames = 0
    (dX, dY) = (0, 0)
    direction = ''
    global last_dir

    #Sleep for 2 seconds to let camera initialize properly
    time.sleep(2)
    #Start video capture
    vs = mw.WebcamVideoStream().start()


    while True:
        # your code here
        continue
        



def finger_tracking():
    import cv2
    import imutils
    import numpy as np
    import time
    import multithreaded_webcam as mw
    import mediapipe as mp

    ##Sleep for 2 seconds to let camera initialize properly
    time.sleep(2)
    #Start video capture
    vs = mw.WebcamVideoStream().start()

    # put your code here


def unique_control():
    # put your code here
    pass

def main():
    control_mode = input("How would you like to control the game? ")
    if control_mode == '1':
        keypress()
    elif control_mode == '2':
        trackpad_mouse()
    elif control_mode == '3':
        color_tracker()
    elif control_mode == '4':
        finger_tracking()
    elif control_mode == '5':
        unique_control()

if __name__ == '__main__':
	main()
