import cv2 as cv
import numpy as np
import time

#Connecting program to primary webcam using VideoCapture object
capture = cv.VideoCapture(0)  

# 10 seconds delay using time to allow the webcam to start up
time.sleep(10) 

#specifications for saving the final recording
fourcc = cv.VideoWriter_fourcc(*'XVID')
recording = cv.VideoWriter('videorecording.avi', fourcc, 20.0, (640,480)) 

 # capturing initial background image 
for i in range(10):
    isTrue, background = capture.read()  


while capture.isOpened():
    #capturing current frame
    isTrue, frame = capture.read()

    #converting the BGR values to their corresponding HSV values
    hsv= cv.cvtColor(frame, cv.COLOR_BGR2HSV)  

    #Hue values of red are typically from 0-30 and 150-180. 
    #In Opencv we have to fit them into 8bit value (0,180) 
    #let us consider two masks with ranges (0,10) and (170,180)

    red1lower = np.array([0, 120, 70])
    red1upper = np.array([10, 255, 255])
    mask1 = cv.inRange(hsv, red1lower, red1upper)  

    red2lower = np.array([170, 120, 70])
    red2upper = np.array([180, 255, 255])
    mask2 = cv.inRange(hsv, red2lower, red2upper)   

    #combining both the masks into a single matrix
    mask = mask1 + mask2  

    # Morphology transformations to reduce noise
    mask = cv.morphologyEx(mask, cv.MORPH_OPEN, np.ones((3,3), np.uint8))
    mask = cv.morphologyEx(mask, cv.MORPH_DILATE, np.ones((3,3), np.uint8))

    #Inversion of mask using bitwise not
    mask_n = cv.bitwise_not(mask) 

    # Part of the frame taken from background
    res1 = cv.bitwise_and(background, background, mask = mask)
    # Part of the frame which is not red
    res2 = cv.bitwise_and(frame, frame, mask = mask_n)

    # Combining the frames to provide the "invisibility effect"
    final_frame = cv.addWeighted(res1, 1, res2, 1, 0) 

    # Write the output frame to recoring
    recording.write(final_frame)
    
    # Display of the Live webcam feed 
    cv.imshow('Output Camera', final_frame)
    # Terminating the output camera on key press of escape key
    if cv.waitKey(1) == 27:  
        break

capture.release()
recording.release()
cv.destroyAllWindows()