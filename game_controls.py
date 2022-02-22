from cv2 import threshold
from matplotlib.pyplot import contour
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
                    else:
                        last_dir = 'left'
                else:
                    if ydif > 0:
                        last_dir = 'down'
                    else:
                        last_dir = 'up'
                pyautogui.press(last_dir)
                last_position = (x,y)

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
    colorLower = (29, 86, 6)
    colorUpper = (100, 255, 255)

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
        frame = vs.read()
        flippedFrame = cv2.flip(frame, 1)

        resizedFrame = imutils.resize(flippedFrame, width = 600)
        blurFrame = cv2.GaussianBlur(resizedFrame, (5,5), 0)
        HSVframe = cv2.cvtColor(blurFrame, cv2.COLOR_BGR2HSV)
        #mask
        mask = cv2.inRange(HSVframe, colorLower, colorUpper)
        erosion = cv2.erode(mask, None, iterations=2)
        dilation = cv2.dilate(erosion, None, iterations=2)
        contours,_ = cv2.findContours(dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        # unsure about the list
        center = None
        if len(contours) > 0:
            print('contours', contours)
            maxContour = max(contours, key = cv2.contourArea)
            radius = cv2.minEnclosingCircle(maxContour)
            M = cv2.moments(maxContour)
            center = (int(M['m10'] / M['m00']), int(M['m01'] / M['m00']))
            if radius[1] > 10:
                cv2.circle(frame, (int(radius[0][0]), int(radius[0][1])), int(radius[1]), (0,255,255), 2)
                cv2.circle(frame, center, 5, (0,255,255), -1)
                pts.appendleft(center)
                print('pts', pts)
        
        if num_frames >= 10 and len(pts) >= 10:
            first = pts[0]
            tenth = pts[9]
            dX = tenth[0] - first[0]
            dY = tenth[1] - first[1]
            threshold = 200
            if abs(dX) > threshold or abs(dY) > threshold:
                if abs(dX) > abs(dY):
                    if dX > 0:
                        direction = 'right'
                        print('right')
                    else:
                        direction = 'left'
                        print('left')
                else:
                    if dY > 0:
                        direction = 'down'
                        print('down')
                    else:
                        direction = 'up'
                        print('up')
                cv2.putText(frame, direction, (20,40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3)
                if last_dir != direction:
                    pyautogui.press(direction)
                    print(last_dir)
                    last_dir = direction
        cv2.imshow('Game Control Window', frame)
        cv2.waitKey(1)
        num_frames += 1

        



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
    handDetect = mp.solutions.hands
    hands = handDetect.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)
    drawing = mp.solutions.drawing_utils
    
    while True:
        frame = vs.read()
        flippedFrame = cv2.flip(frame, 1)
        resizedFrame = imutils.resize(flippedFrame, width = 600)
        blurFrame = cv2.GaussianBlur(resizedFrame, (5,5), 0)
        HSVframe = cv2.cvtColor(blurFrame, cv2.COLOR_BGR2RGB)

        processedFrame = hands.process(frame)   #what is hands we changed to handDetect
        numFingers = 0
        majorFeatures = []

        if processedFrame != None:                  # loop through number of hands
            for item in processedFrame:
                for id, lm in enumerate(item.landmark):
                    height = frame.shape[0]
                    width = frame.shape[1]
                    x = lm.x*width
                    y = lm.y*height
                    cv2.circle(frame, (x,y), 3, (255, 0, 255), cv2.FILLED)
                    majorFeatures.append((id,x,y))
        
        if len(majorFeatures) != 0:
            #thumb 
            if majorFeatures[4][1] < majorFeatures[3][1]:
                numFingers += 1
            # index finger
            if majorFeatures[8][2] < majorFeatures[6][2]:
                numFingers += 1
            #middle finger
            if majorFeatures[12][2] < majorFeatures[10][2]:
                numFingers += 1
            #ring finger
            if majorFeatures[16][2] < majorFeatures[14][2]:
                numFingers += 1
            #little finger
            if majorFeatures[20][2] < majorFeatures[18][2]:
                numFingers += 1
        
        if numFingers == 1:
            direction = 'right'
        elif numFingers == 2:
            direction = 'left'
        elif numFingers == 3:
            direction = 'up'
        elif numFingers == 4:
            direction = 'down'
        elif numFingers == 5:
            exit()
        
        pyautogui.press(direction)
        cv2.putText(frame,str(int(numFingers)),(10,70),cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)
        cv2.imshow("Image", frame)
        cv2.waitKey(1)

        if last_dir != direction:
            last_dir = direction


    



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
