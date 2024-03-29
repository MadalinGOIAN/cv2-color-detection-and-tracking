import cv2
import numpy as np

from constants import *
from user_interface import UI

def track_color():
    cap = cv2.VideoCapture(0)

    while True:
        _, frame = cap.read()
        
        blurred_frame = cv2.bilateralFilter(frame, 19, 175, 175)
        hsv_frame = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv_frame, UI.lower_limit, UI.upper_limit)
        
        kernel = np.ones((5, 5), np.uint8)
        mask = cv2.dilate(mask, kernel)
        
        contours, _ = cv2.findContours(mask,
                                            cv2.RETR_TREE,
                                            cv2.CHAIN_APPROX_SIMPLE)

        for _, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            
            if(area > 300):
                x, y, w, h = cv2.boundingRect(contour)
                frame = cv2.rectangle(frame, (x, y), (x + w, y + h), GREEN, 2)
        
        cv2.imshow('Color Detection', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
    cap.release()
