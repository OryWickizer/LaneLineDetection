import cv2 
import numpy as np 
  
# read image
original = cv2.imread('LIMO_test.jpeg')

# Convert the image to HSV color space
hsv = cv2.cvtColor(original, cv2.COLOR_BGR2HSV)
cv2.imshow('hsv', hsv)

#Hue value varies from 0-179, Saturation value varies from 0-255 and Value value varies from 0-255.
# hue is color (ROYGBIV)
# saturation is how rich the color is
# value is how bright the pixel is
lower_bound = np.array([14, 30, 0], dtype=np.uint8)
upper_bound = np.array([30, 150, 255], dtype=np.uint8)

# Create the color mask
mask = cv2.inRange(hsv, lower_bound, upper_bound)
cv2.imshow('mask', mask)

# Apply the color mask to the hsv image
segmented = cv2.bitwise_and(hsv, hsv, mask=mask)
cv2.imshow('mask applied', segmented)

# convert to grayscale 
gray = cv2.cvtColor(segmented, cv2.COLOR_BGR2GRAY) 
cv2.imshow('grayed', gray)

# display the image
#cv2.imshow("original", original)
#cv2.imshow("hsv", hsv)


# Remove noise using 3x3 Kernel (Gaussian Filter)
#blurred = cv2.GaussianBlur(gray, (9,9), 1)
#blurred = cv2.blur(gray, (99,99))
blurred = cv2.medianBlur(gray,21)
cv2.imshow('blurred', gray)
  
# Find Canny edges 
edged = cv2.Canny(blurred, 30, 200) 
cv2.imshow('edges', edged)

  
# Finding Contours 
# Use a copy of the image e.g. edged.copy() 
# since findContours alters the image 
contours, hierarchy = cv2.findContours(edged,  
    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 

# ---------------------------------------------------------------------------
# Originally developed by OutOfTheBots
# (https://www.youtube.com/channel/UCCX7z2JENOSZ1mraOpyVyzg/about)
if len(contours) > 0:
    blackbox = cv2.minAreaRect(contours[3])
    (x_min, y_min), (w_min, h_min), ang = blackbox
    if ang < -45: ang += 90
    if w_min < h_min and ang > 0: ang = (90-ang)*-1
    if w_min > h_min and ang < 0: ang = 90 + ang
    setpoint = blurred.shape[1]/2
    cte = -int(x_min - setpoint)
    angle = -int(ang)

    
    box = cv2.boxPoints(blackbox)
    box = np.int0(box)
    _ = cv2.drawContours(segmented, [box], 0, (255,0,0),1)
    ang_msg = "Angle Error = " + str(angle)
    err_msg = "Error = " + str(cte)
    cv2.putText(segmented, ang_msg, (530,25), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255,0,0), 1)
    cv2.putText(segmented, err_msg, (530,50), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,0,255), 1)
    cv2.line(segmented, (int(x_min), 0), (int(x_min), blurred.shape[0]), (0,0,255), 1)


    blackbox = cv2.minAreaRect(contours[1])
    (x_min, y_min), (w_min, h_min), ang = blackbox
    if ang < -45: ang += 90
    if w_min < h_min and ang > 0: ang = (90-ang)*-1
    if w_min > h_min and ang < 0: ang = 90 + ang
    setpoint = blurred.shape[1]/2
    cte = -int(x_min - setpoint)
    angle = -int(ang)

    
    box = cv2.boxPoints(blackbox)
    box = np.int0(box)
    _ = cv2.drawContours(segmented, [box], 0, (255,0,0),1)
    ang_msg = "Angle Error = " + str(angle)
    err_msg = "Error = " + str(cte)
    cv2.putText(segmented, ang_msg, (130,25), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255,0,0), 1)
    cv2.putText(segmented, err_msg, (130,50), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,0,255), 1)
    cv2.line(segmented, (int(x_min), 0), (int(x_min), blurred.shape[0]), (0,0,255), 1)


else:
    print('no contours found')

# ---------------------------------------------------------------------------
  
cv2.imshow('Canny Edges After Contouring', edged) 
cv2.imshow('angles', segmented)
  
print("Number of Contours found = " + str(len(contours))) 
  
# Draw all contours 
# -1 signifies drawing all contours 
cv2.drawContours(original, contours, -1, (0, 255, 0), 3)
  
cv2.imshow('Contours', original) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 