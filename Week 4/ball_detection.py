import numpy as np    # import libraries
import cv2 as cv
import time
import imutils
from collections import deque

capture = cv.VideoCapture(0)    # capture object to capture frames from webcam

fourcc = cv.VideoWriter_fourcc(*'XVID')
record = cv.VideoWriter('Detection.avi', fourcc, 20.0, (640,480))    # record object to record video    

path = deque(maxlen=60)    # deque that stored path history of the object

time.sleep(5)    # letting webcam warmup

while capture.isOpened():
    isTrue, frame = capture.read()    # read one frame from webcam

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)    # convert to hsv colourspace

    lower = np.array([10,100,100], np.uint8)    # lower and upper hsv limits  
    upper = np.array([40,255,255], np.uint8)

    mask = cv.inRange(hsv, lower, upper)    # creating a mask to detect object 
    mask = cv.erode(mask, None, iterations = 5)
    mask = cv.dilate(mask, None, iterations = 5)

    contours = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)  # outer contours of detected object
    contours = imutils.grab_contours(contours)    # elimintes false positive contours
    center = None

    if len(contours) > 0:
        c = max(contours, key = cv.contourArea)    # find the contour that encloses max area
        ((x,y), rad) = cv.minEnclosingCircle(c)    # coordinates of centre and radius
        M = cv.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"])) 

        if rad > 20:    # threshold radius calue to eliminate mistaken blue objects
            cv.circle(frame, (int(x), int(y)), int(rad),(0, 255, 255), 4)  # draw circle around to indicate detection
            cv.circle(frame, center, 5, (0, 0, 255), -1)    # indicate the centre

    path.appendleft(center)

    for i in range(1, len(path)):
        if path[i-1] is None or path[i] is None:      # if centre of current index of previous is None move to next iteration
            continue
        thickness = int(np.sqrt(20/float(i+1)) * 2.5)
        cv.line(frame, path[i-1], path[i], (0,0,255), thickness)  # drawing path using two consecutive paths in deque
    
    record.write(frame)    # writing the final frame after detector indications in the recording

    cv.imshow("Live feed", frame)    # display the frame 
    if cv.waitKey(1) == 27:    # keep iterating till esc is pressed
        break

capture.release()
record.release()
cv.destroyAllWindows()