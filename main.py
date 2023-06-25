import cv2, time
from PoseDetector import PoseDetector
import mediapipe as mp

pTime = 0
black_flag = False
cap = cv2.VideoCapture(0)

detector = PoseDetector()

while True:
    reg, img = cap.read()
    img = cv2.flip(img, 1)

    detector.drawBoundaries(img)

    if not reg:
        break

    img, p_landmarks, p_connections = detector.findPose(img, False)
    detector.getNoseMovementsToKeys(img, False)

    if black_flag:
        img = img * 0

    mp.solutions.drawing_utils.draw_landmarks(img, p_landmarks, p_connections)
    lmList = detector.getPosition(img)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.imshow("image", img)
    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()