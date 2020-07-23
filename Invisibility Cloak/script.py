# import dependencies

import numpy as np
import cv2
import time

# create a capture instance
cap = cv2.VideoCapture(0)

# wait 5 seconds for the camera module to initalise
time.sleep(5)

#capture the background to replace with the cloak
background = 0
for i in range(15):
    ret, background = cap.read()

# while the camera is on
while(cap.isOpened()):
    
    #capture the live feed
    ret, image = cap.read()
    if not ret:
        break
    
    #convert the live feed to hsv
    hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

    #create mask for lower limit of hsv values
    lower_limit = np.array([0,120,70])
    upper_limit = np.array([10,255,255])
    mask1 = cv2.inRange(hsv,lower_limit, upper_limit)

    #create mask for the upper limit of hsv values
    lower_limit = np.array([170,120,70])
    upper_limit = np.array([180,255,255])
    mask2 = cv2.inRange(hsv,lower_limit,upper_limit)

    #The values for the upper and lower sections of various colours 
    #are to be referenced from the image provided in the repo

    #Mask 1 and Mask 2 are logically or'ed
    mask1 = mask1 + mask2
    
    #smoothen the mask selection
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN,np.ones((3,3),np.uint8), iterations = 2)
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE,np.ones((3,3),np.uint8), iterations = 1)

    #select everythinng but the cloak
    mask2 = cv2.bitwise_not(mask1)

    #replace the cloak with the background image captured earlier
    res1 = cv2.bitwise_and(background, background, mask = mask1)

    #use the live feed rest of the are
    res2 = cv2.bitwise_and(image, image, mask= mask2)

    #final result
    final_res = cv2.addWeighted(res1, 1, res2, 1, 0)

    #display the output
    cv2.imshow("Invisiblity Cloak", final_res)

    #exit on ESC
    k = cv2.waitKey(10)
    if k ==27:
        break

cap.release()
cv2.destroyAllWindows()