# Got pics from video
import os
import cv2

path = os.getcwd()
path = os.path.join(path, "WhirlyBirdStills")

if not os.path.exists(path):
    os.mkdir(path)

cap = cv2.VideoCapture(r'WhirlyBird.mp4')
count = 0
while (cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    imgPath = os.path.join(path, f'{count}.jpg')
    cv2.imwrite(imgPath, frame)
    count += 1
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
print("Total frames: ", count, sep='\t')
cap.release()
cv2.destroyAllWindows()