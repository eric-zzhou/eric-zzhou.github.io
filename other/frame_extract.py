import cv2

vid = r"C:\Users\EricS\Downloads\Auto Drive.mp4"
save_path = r"C:\Users\EricS\Downloads\ftc_frames"

vidcap = cv2.VideoCapture(vid)
success, image = vidcap.read()
count = 0
while success:
    cv2.imwrite(f"{save_path}\\frame{count}.jpg", image)  # save frame as JPEG file
    success, image = vidcap.read()
    print("Read a new frame: ", success)
    count += 1
