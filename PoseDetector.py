import cv2
import mediapipe as mp
import pyautogui
import time

noCircles = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
thickness = 1
color = (255, 0, 0)
wait = 0.85

class PoseDetector:
    cTime = 0
    pTime = 0

    def __init__(self, mode=False, upBody=False, smooth=True, detectionCon=0.5, trackCon=0.5) -> None:

        self.mode = mode
        self.upBody = upBody
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode, 1, self.smooth)

    def findPose(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(
                    img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)

        return img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS

    def getPosition(self, img, draw=True):
        lmList = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)                
                lmList.append([id, cx, cy])
                if draw:
                    if id not in noCircles:
                        cv2.circle(img, (cx, cy), 1, (255, 0, 0), cv2.FILLED)

        return lmList

    def drawBoundaries(self, img):
        h, w, c = img.shape
        h = int(h)
        w = int(w)

        cv2.line(img, (0, int(h/4)), (w, int(h/4)),
                 color, thickness)  # line 1/4 h
        cv2.line(img, (int(w/4), 0), (int(w/4), h),
                 color, thickness)  # line at 3/4 w
        cv2.line(img, (int(3*w/4), 0), (int(3*w/4), h),
                 color, thickness)  # line at 3/4 w
        cv2.line(img, (0, int(3*h/4)), (w, int(3*h/4)),
                 color, thickness)  # line at 3/4 h

        cv2.putText(img, "UP", (int(w/2) - 50, 75),
                    cv2.FONT_HERSHEY_COMPLEX, 3, color, 3)  # up text
        cv2.putText(img, "DOWN", (int(w/2) - 125, h - 25),
                    cv2.FONT_HERSHEY_COMPLEX, 3, color, 2)  # up text
        cv2.putText(img, "LEFT", (5, int(h/2)),
                    cv2.FONT_HERSHEY_COMPLEX, 1, color, 2)  # up text
        cv2.putText(img, "RIGHT", (w - 120, int(h/2)),
                    cv2.FONT_HERSHEY_COMPLEX, 1, color, 2)  # up text

    def getNoseMovementsToKeys(self, img, draw=True):
        self.cTime = time.time()
        h, w, c = img.shape
        lmList = self.getPosition(img, draw)
        xPos = 0
        yPos = 0

        for id, cx, cy in lmList:
            if id == 0:
                if cx < w/4 + 40:
                    xPos = -1

                elif cx > 3*w/4 - 40:
                    xPos = 1

                else:
                    xPos = 0

                if cy < h/4:
                    yPos = -1

                elif cy > 3*h/4:
                    yPos = 1

                else:
                    yPos = 0

        if xPos == -1:
            if self.cTime - self.pTime > wait:
                pyautogui.press('left')               
                self.pTime = self.cTime

        elif xPos == 1:
            if self.cTime - self.pTime > wait:
                pyautogui.press('right')            
                self.pTime = self.cTime

        if yPos == -1:
            if self.cTime - self.pTime > wait:
                pyautogui.press('up')
                self.pTime = self.cTime

        elif yPos == 1:
            if self.cTime - self.pTime > wait:
                pyautogui.press('down')      
                self.pTime = self.cTime
              