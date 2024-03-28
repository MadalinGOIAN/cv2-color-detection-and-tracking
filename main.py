import cv2
import numpy as np

blue_lower = np.array([95, 50, 10], np.uint8) 
blue_upper = np.array([120, 255, 255], np.uint8) 

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    blurred_frame = cv2.bilateralFilter(frame, 19, 175, 175)
    hsv_frame = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)
    
    blue_mask = cv2.inRange(hsv_frame, blue_lower, blue_upper) 
    
    kernel = np.ones((5, 5), "uint8")
    blue_mask = cv2.dilate(blue_mask, kernel) 
    res_blue = cv2.bitwise_and(frame, frame, mask = blue_mask)
    
    contours, hierarchy = cv2.findContours(blue_mask, 
										cv2.RETR_TREE, 
										cv2.CHAIN_APPROX_SIMPLE) 

    for pic, contour in enumerate(contours): 
        area = cv2.contourArea(contour) 
        if(area > 300): 
            x, y, w, h = cv2.boundingRect(contour) 
            frame = cv2.rectangle(frame, (x, y), 
									(x + w, y + h), 
									(255, 0, 0), 2)
    
    cv2.imshow('Color Detection', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
