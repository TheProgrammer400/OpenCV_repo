import cv2

img = cv2.imread('lena.jpg', 1)


# overwriting the image

img = cv2.line(img, (0, 98), (100, 100), (100, 100, 0), 10)
# 1st argument --> image
# 2nd argument --> co-ordinates
# 3rd argument --> co-ordinates
# 4th argument --> color in BGR format
# 5th argument --> thickness

img = cv2.arrowedLine(img, (0, 0), (100, 100), (100, 100, 0), 10)
# same arguments as line

img = cv2.circle(img, (300, 300), 89, (0, 20, 0), 10)
# 2nd argument --> center
# 3rd argument --> radius
# 4th argument --> color
# 5th argument --> thickness

# defining font for text

font = cv2.FONT_HERSHEY_SIMPLEX

img = cv2.putText(img, "This damn project", (10, 500), font, 1, (20, 0, 20), 10)  # writing text
# 2nd argument --> text
# 3rd argument --> origin
# 4th argument --> font
# 5th argument --> font size
# 6th --> color
# 7th argument --> thickness

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
