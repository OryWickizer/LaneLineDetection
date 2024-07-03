# LaneLineDetection
## Abstract
Using OpenCV's cv2 package, Python, and ROS to determine lane line angles from a front-facing camera.

## Explaination of Provided Files

- LIMO_test.jpeg
  - The example JPEG used in the "Example of a JPEG to Lane Line Angles" section of this GitHub.

- laneLineAngles.py
  - The python code that is run on a test image (here, LIMO_test.jpeg) to find lane lines and lane line angles.
 
- codeOnLIMO.py
  - The Python file that is used in the "Using the AgileX LIMO's Onboard Camera to Find Lane Lines in Real-time" section of this GitHub on the LIMO to:
     - take images from the AgileX LIMO's Dabai camera stream and to
     - process those images in real-time to find lane lines and display them on the LIMO's screen.

## Example of a JPEG to Lane Line Angles

This section used the laneLineAngles.py file and the LIMO_test.jpeg file on a Windows PC.

BGR (Original Image) --> HSV

![LIMO_test](https://github.com/OryWickizer/LaneLineDetection/assets/22403868/3d6ce05c-6701-4a81-9999-6db38b8fe7b7)
![hsv](https://github.com/OryWickizer/LaneLineDetection/assets/22403868/0b3dace3-c8d7-4045-8071-9406a128091b)

Create a mask based on the lane line HSV color values:

![mask](https://github.com/OryWickizer/LaneLineDetection/assets/22403868/a5c842df-c941-4192-bc0e-908fcd218fdc)

Apply that mask to the HSV image to get just the lane lines (and some noise from the trees):

![mask applied](https://github.com/OryWickizer/LaneLineDetection/assets/22403868/69997a48-c100-4f11-829c-9305e4554313)

Convert the image to Grayscale:

![grayed](https://github.com/OryWickizer/LaneLineDetection/assets/22403868/84512c86-2d98-4c36-bc72-829d92ae4f54)

Blur the image to remove noise (not shown).

Find the edges of the lane lines, and then find the corresponding contours:

![edges](https://github.com/OryWickizer/LaneLineDetection/assets/22403868/2288e272-acfc-4493-b17c-ec8f2e264947)

![contours](https://github.com/OryWickizer/LaneLineDetection/assets/22403868/1d1c52cd-7a1a-4e5d-b6ca-f444e35931e2)

Create boxes to surround the contours. Then, find the angles of those boxes relative to a vertical line (angles shown in blue):

![angles](https://github.com/OryWickizer/LaneLineDetection/assets/22403868/78a43697-ce84-40fa-8057-9e8c1eff53ab)

## Using the AgileX LIMO's Onboard Camera to Find Lane Lines in Real-time

I wish I would have thought to get a video of the LIMO running this program, but here at least is an image of the process:

![Limo running code to find lane lines](https://github.com/OryWickizer/LaneLineDetection/assets/22403868/837249b5-9ec9-475e-884f-61c18ddd3287)

Here, the LIMO is running the Python file codeOnLIMO.py to find and display lane lines in real-time.

The code is taking images from the onboard camera's (the camera is called Dabai) stream and processing them to find lane lines several times a second.

## Next Steps

The next steps in this project could involve:
- Getting the code running on the LIMO to find lane lane angles, as is done in the laneLineAngles.py code.
- Using the found lane line angles as part of a control algorithm to keep the LIMO moving in-between lane lines.

## Specs
Robot Platform

- AgileX LIMO

Software
- ROS 1 Melodic
- OpenCV's cv2 python package
- Python 2.7
