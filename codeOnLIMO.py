#!/usr/bin/env python2.7

import numpy as np

# Import ROS libraries and messages
import rospy
from sensor_msgs.msg import Image

# Import OpenCV libraries and tools
import cv2
from cv_bridge import CvBridge, CvBridgeError

# Print "Hello!" to terminal
print"Hello!"

# Initialize the ROS Node named 'opencv_example', allow multiple nodes to be run with this name
rospy.init_node('opencv_example', anonymous=True)

# Print "Hello ROS!" to the Terminal and ROSLOG
rospy.loginfo("Hello ROS!")

# Initialize the CvBridge class
bridge = CvBridge()

# Define a function to show the image in an OpenCV Window
def show_image(original, hsv, segmented):
    #cv2.imshow("original", original)
    # how long to display the image
    #cv2.waitKey(30)

    cv2.imshow("hsv", hsv)
    # how long to display the image
    cv2.waitKey(30)

    cv2.imshow("segmented", segmented)
    # how long to display the image
    cv2.waitKey(30)

# Define a callback for the Image message
def image_callback(img_msg):
    # log some info about the image topic
    rospy.loginfo(img_msg.header)

    # Try to convert the ROS Image message to a CV2 Image
    try:
        original = bridge.imgmsg_to_cv2(img_msg, "bgr8")
    except CvBridgeError, e:
        rospy.logerr("CvBridge Error: {0}".format(e))

    #--------------------------
    # Save your OpenCV2 image as a jpeg 
    #time = img_msg.header.stamp
    #cv2.imwrite(''+str(time)+'.jpeg', original)
    #print "image saved"
    #rospy.sleep(2)
    #-------------------------

    # Convert the image to HSV color space
    hsv = cv2.cvtColor(original, cv2.COLOR_BGR2HSV)
    
    #Hue value varies from 0-179, Saturation value varies from 0-255 and Value value varies from 0-255.
    # hue is color (ROYGBIV)
    # saturation is how rich the color is
    # value is how bright the pixel is
    lower_bound = np.array([14, 30, 0], dtype=np.uint8)
    upper_bound = np.array([30, 150, 255], dtype=np.uint8)

    # Create the color mask
    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    # Apply the color mask to the image
    segmented = cv2.bitwise_and(hsv, hsv, mask=mask)

    # Show the converted image
    show_image(original, hsv, segmented)


# Initalize a subscriber to the "/camera/rgb/image_raw" topic with the function "image_callback" as a callback
sub_image = rospy.Subscriber("/camera/rgb/image_raw", Image, image_callback)

# Initialize an OpenCV Window named "Image Window"
#cv2.namedWindow("HSV", 1)

# Loop to keep the program from shutting down unless ROS is shut down, or CTRL+C is pressed
while not rospy.is_shutdown():
    rospy.spin()
