import cv2

img = cv2.imread('lena.jpg', 1)
cv2.imshow('image', img)

while True:

    key = cv2.waitKey(0)  # taking key as input

    if key == 27:  # ascii value of esc key
        cv2.destroyAllWindows()
        break
    elif key == ord('s'):
        cv2.imwrite('lena_copy.jpg', img)  # saving copy of image
        cv2.destroyAllWindows()
        break
    else:
        pass
