import cv2

video1 = cv2.VideoCapture(0)  # 0 is parameter for default camera in device
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # specifying fourcc code
out = cv2.VideoWriter('output.avi', fourcc, 30, (640, 480))

# in above syntax, 3rd argument is FPS and 4th is (width, height)

# XVID is video codec
# XVID is used for better compression and storage
# often used to encode video content to AVI format

while video1.isOpened():  # checking for camera
    ret, frame = video1.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # print(video1.get(cv2.CAP_PROP_FRAME_WIDTH))  # printing width
    # print(video1.get(cv2.CAP_PROP_FRAME_HEIGHT))  # printing height

    out.write(frame)  # Write the frame to the video file

    cv2.imshow("Video", gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# good practise to release resources to free up memory
# and ensuring that the associated files (video files)
# are closed properly, this is only used for external
# devices like camera and video files

video1.release()
out.release()

cv2.destroyAllWindows()
