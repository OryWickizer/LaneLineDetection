# LaneLineDetection
## Abstract
Using OpenCV's cv2 package, Python, and ROS to determine lane line angles from a front-facing camera.

## Explaination of Provided Files

- LIMO_test.jpeg
  - example JPEG used in Process section

- laneLineAngles.py
  - python code to run on test image (LIMO_test.jpeg)
 
- codeOnLIMO.py
  - the python file to run on the LIMO

## Process

BGR (Original Image) --> HSV

![LIMO_test](https://github.com/OryWickizer/LaneLineDetection/assets/22403868/3d6ce05c-6701-4a81-9999-6db38b8fe7b7)
![hsv](https://github.com/OryWickizer/LaneLineDetection/assets/22403868/0b3dace3-c8d7-4045-8071-9406a128091b)

Create mask based on lane line hsv color values

![mask](https://github.com/OryWickizer/LaneLineDetection/assets/22403868/a5c842df-c941-4192-bc0e-908fcd218fdc)

Apply mask to HSV image

![mask applied](https://github.com/OryWickizer/LaneLineDetection/assets/22403868/69997a48-c100-4f11-829c-9305e4554313)

Convert to Grayscale

![grayed](https://github.com/OryWickizer/LaneLineDetection/assets/22403868/84512c86-2d98-4c36-bc72-829d92ae4f54)

Blur to remove noise

Find Edges, then find contours

![edges](https://github.com/OryWickizer/LaneLineDetection/assets/22403868/2288e272-acfc-4493-b17c-ec8f2e264947)

![contours](https://github.com/OryWickizer/LaneLineDetection/assets/22403868/1d1c52cd-7a1a-4e5d-b6ca-f444e35931e2)

Find boxes surrounding contours

Then find the angle of those boxes

![angles](https://github.com/OryWickizer/LaneLineDetection/assets/22403868/78a43697-ce84-40fa-8057-9e8c1eff53ab)

## Specs
Robot Platform

- AgileX LIMO

Software
- ROS 1 Melodic
- OpenCV's cv2 python package
- Python 2.7
