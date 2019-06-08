import numpy as np
import cv2

# Options are cv2.IMREAD_UNCHANGED, cv2.IMREAD_COLOR, cv2.IMREAD_GRAYSCALE
img = cv2.imread('messi5.jpeg', 0)
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('messigray.png',img)
    cv2.destroyAllWindows()