import cv2
import numpy as np


img = cv2.imread("image.png")
cv2.imshow("test", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_bound = np.array([0, 100, 100])
upper_bound = np.array([13, 255, 255])
mask = cv2.inRange(hsv, lower_bound, upper_bound)
cv2.imshow("test", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

kernel = np.ones((7,7),np.uint8)
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
cv2.imshow("test", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

segmented_img = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow("test", segmented_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
output = cv2.drawContours(segmented_img, contours, -1, (0, 0, 255), 3)

cv2.imshow("Output", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
