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
        center = None
        if len(contours) > 0:
            maxContour = max(contours, key = cv2.contourArea)
            radius = cv2.minEnclosingCircle(maxContour)
            M = cv2.moments(maxContour)
            center = (int(M['m10'] / M['m00']), int(M['m01'] / M['m00']))
            if radius[1] > 10:
                cv2.circle(frame, (int(radius[0][0]), int(radius[0][1])), int(radius[1]), (0,255,255), 2)
                cv2.circle(frame, center, 5, (0,255,255), -1)
                pts.appendleft(center)

        
        if num_frames >= 10 and len(pts) >= 10:
            first = pts[0]
            tenth = pts[9]
            dX = tenth[0] - first[0]
            dY = tenth[1] - first[1]
            threshold = 150
            if abs(dX) > threshold or abs(dY) > threshold:
                if abs(dX) > abs(dY):
                    if dX > 0:
                        direction = 'left'
                    else:
                        direction = 'right'
                else:
                    if dY > 0:
                        direction = 'up'
                    else:
                        direction = 'down'
                cv2.putText(frame, direction, (20,40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3)
                if last_dir != direction:
                    pyautogui.press(direction)
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

    global last_dir
    
    while True:
        frame = vs.read()
        flippedFrame = cv2.flip(frame, 1)
        resizedFrame = imutils.resize(flippedFrame, width = 600)
        #blurFrame = cv2.GaussianBlur(resizedFrame, (5,5), 0)
        HSVframe = cv2.cvtColor(resizedFrame, cv2.COLOR_BGR2RGB)

        processedFrame = hands.process(HSVframe)   
        numFingers = 0
        majorFeatures = []

        if processedFrame.multi_hand_landmarks:                  # loop through number of hands
            for landmarks in processedFrame.multi_hand_landmarks:

                for id, lm in enumerate(landmarks.landmark):
                    height = resizedFrame.shape[0]
                    width = resizedFrame.shape[1]
                    x = int (lm.x*width)
                    y = int (lm.y*height)
                    cv2.circle(resizedFrame, (x,y), 3, (255, 0, 255), cv2.FILLED)
                    majorFeatures.append([id,x,y])
                drawing.draw_landmarks(resizedFrame, landmarks, handDetect.HAND_CONNECTIONS)
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
        
        if numFingers == 1 and last_dir != 'right':
            direction = 'right'
            pyautogui.press(direction)
            last_dir = direction
        elif numFingers == 2 and last_dir != 'left':
            direction = 'left'
            pyautogui.press(direction)
            last_dir = direction
        elif numFingers == 3 and last_dir != 'up':
            direction = 'up'
            pyautogui.press(direction)
            last_dir = direction
        elif numFingers == 4 and last_dir != 'down':
            direction = 'down'
            pyautogui.press(direction)
            last_dir = direction
        elif numFingers == 5:
            cv2.putText(resizedFrame,'HCI Rules!',(60,70),cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 3, (255,0,255), 3)
            
        
        
        cv2.putText(resizedFrame,str(int(numFingers)),(10,70),cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)
        cv2.imshow("Image", resizedFrame)
        cv2.waitKey(1)

        #if last_dir != direction:
        #    last_dir = direction


    



def unique_control():
    import speech_recognition as sr
    import pyttsx3

    #sr.init('nsss', False)
    r = sr.Recognizer()
    global last_dir
    direction = ''

    while(1):    
      
    # Exception handling to handle
    # exceptions at the runtime
        try:
            
            # use the microphone as source for input.
            with sr.Microphone() as inputSource:
                
                # wait for a second to let the recognizer
                # adjust the energy threshold based on
                # the surrounding noise level 
                r.adjust_for_ambient_noise(inputSource, duration=0.2)
                
                #listens for the user's input 
                inputAudio = r.listen(inputSource)
                
                # Using ggogle to recognize audio
                MyText = r.recognize_google(inputAudio)
                direction = MyText.lower()
                if direction != last_dir :#and (direction == 'left' or direction == 'right' or direction == 'up' or direction == 'down'):
                    pyautogui.press(direction)
                    last_dir = direction
                    print(direction)

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            
        except sr.UnknownValueError:
            print("unknown error occured")

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
