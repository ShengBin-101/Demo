# Simple loading and displaying and resizing of image

import cv2
import numpy as np

# To read image from disk, we use
# cv2.imread function, in below method,
path= r"C:\Users\sheng\Desktop\MyTestApp\images\faces.jpg"

img = cv2.imread(path, cv2.IMREAD_COLOR)
half = cv2.resize(img, (0, 0), fx = 0.5, fy = 0.5)

# Creating GUI window to display an image on screen
# first Parameter is windows title (should be in string format)
# Second Parameter is image array
cv2.imshow("image", img)
cv2.imshow("resized image", half)

# To hold the window on screen, we use cv2.waitKey method
# Once it detected the close input, it will release the control
# To the next line
# First Parameter is for holding screen for specified milliseconds
# It should be positive integer. If 0 pass an parameter, then it will
# hold the screen until user close it.
cv2.waitKey(0)
 
# It is for removing/deleting created GUI window from screen
# and memory
cv2.destroyAllWindows()