# LaneLineDetection
## Abstract
Using OpenCV's cv2 package, Python, and ROS to determine lane line angles from a front-facing camera.

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



Platform

- AgileX LIMO

Software
- ROS 1 Melodic
