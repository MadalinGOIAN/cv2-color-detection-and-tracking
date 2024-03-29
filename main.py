import cv2
import numpy as np

blue_lower = np.array([100, 100, 100], np.uint8) 
blue_upper = np.array([130, 255, 255], np.uint8)

red_lower = np.array([0, 110, 110], np.uint8) 
red_upper = np.array([5, 255, 255], np.uint8)

yellow_lower = np.array([20, 150, 150], np.uint8)
yellow_upper = np.array([35, 255, 255], np.uint8)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    blurred_frame = cv2.bilateralFilter(frame, 19, 175, 175)
    hsv_frame = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)
    
    mask = cv2.inRange(hsv_frame, yellow_lower, yellow_upper) 
    
    kernel = np.ones((5, 5), "uint8")
    mask = cv2.dilate(mask, kernel) 
    res_blue = cv2.bitwise_and(frame, frame, mask = mask)
    
    contours, hierarchy = cv2.findContours(mask, 
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

### Code to find color bounds in HSV
# image = np.zeros((600, 600, 3), np.uint8)
# hsv_pixel = np.array([[[30, 255, 255]]], np.uint8) 

# bgr_pixel = cv2.cvtColor(hsv_pixel, cv2.COLOR_HSV2BGR)

# image[:,:,0] = bgr_pixel[0][0][0]
# image[:,:,1] = bgr_pixel[0][0][1]
# image[:,:,2] = bgr_pixel[0][0][2]

# cv2.imshow('Hue', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
