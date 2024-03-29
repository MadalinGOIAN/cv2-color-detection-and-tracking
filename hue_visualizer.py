import cv2
import numpy as np

image = np.zeros((600, 600, 3), np.uint8)
hsv_pixel = np.array([[[0, 255, 255]]], np.uint8) 
i = 0

while True:
    bgr_pixel = cv2.cvtColor(hsv_pixel, cv2.COLOR_HSV2BGR)

    image[:,:,0] = bgr_pixel[0][0][0]
    image[:,:,1] = bgr_pixel[0][0][1]
    image[:,:,2] = bgr_pixel[0][0][2]

    cv2.imshow('Hue', image)
    cv2.waitKey(500)
    
    print(f"i = {i}")
    i = i + 1
    hsv_pixel[0][0][0] = i
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
