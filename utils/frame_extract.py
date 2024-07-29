import cv2

vid = r"C:\Users\EricS\Downloads\Auto Drive.mp4"
save_path = r"C:\Users\EricS\Downloads\ftc_frames"

cap = cv2.VideoCapture(vid)

for i in range(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))):
    _, image = cap.read()
    cv2.imwrite(f"{save_path}\\frame{i}.jpg", image)
    print(f"Read frame {i}: {_}")
