# required packages
# numpy==1.22.3
# opencv-python==4.5.5.64
# PySimpleGUI==4.59.0
import cv2
import numpy as np 
import math

cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    output = frame.copy()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 

    # Blur using 3 * 3 kernel. 
    gray_blurred = cv2.blur(gray, (3, 3)) 
    # font 
    font = cv2.FONT_HERSHEY_SIMPLEX 
    
    # org 
    org = (00, 185) 
    
    # fontScale 
    fontScale = 1
    
    # Red color in BGR 
    color = (0, 0, 255) 
    
    # Line thickness of 2 px 
    thickness = 2
    width  = cap.get(cv2.CAP_PROP_FRAME_WIDTH,)
    # Apply Hough transform on the blurred image. 
    detected_circles = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT, 1, 20, param1 = 50, 
                param2 = 30, minRadius = 0, maxRadius = 0) 

    if detected_circles is not None: 
        # Convert the circle parameters a, b and r to integers. 
        detected_circles = np.uint16(np.around(detected_circles)) 
        for pt in detected_circles[0, :]: 
            a, b, r = pt[0], pt[1], pt[2] 
            # Draw the circumference of the circle. 
            cv2.circle(frame, (a, b), r, (0, 255, 0), 2) 
            # Draw a small circle (of radius 1) to show the center.
            distance = 0
            try:
                distance = math.sqrt( ((b-0)**2)+((a-width)**2))
            except:
                distance = 0
            cv2.putText(frame, str(distance) , org, font, fontScale, 
                  color, thickness, cv2.LINE_AA, False) 
            cv2.circle(frame, (a, b), 1, (0, 0, 255), 3) 
            cv2.imshow("Detected Circle", frame)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cap.destroyAllWindows()
