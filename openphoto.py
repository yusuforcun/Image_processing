import cv2

# Load an image
img = cv2.imread('veri1.jpg')

# Display the image
cv2.imshow('image', img)

cam = cv2.imread('cam',cam)

cv2.imshow("cam",cam)

# Wait for a key press and then close the window
cv2.waitKey(0)
cv2.destroyAllWindows()