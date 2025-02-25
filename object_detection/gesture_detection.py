import numpy as np
import math
import cv2 as cv

def hand_gesture_recognition():
    cap = cv.VideoCapture('/dev/video0')

    while True:
        _, img = cap.read()
        cv.rectangle(img, (300, 300), (100, 100), (0, 255, 0), 0)
        crop_img = img[100:300, 100:300]
        grey = cv.cvtColor(crop_img, cv.COLOR_BGR2GRAY)
        value = (35, 35)
        blurred_ = cv.GaussianBlur(grey, value, 0)
        _, thresholded = cv.threshold(blurred_, 127, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)

        image, contours, hierarchy = cv.findContours(thresholded.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
        count1 = max(contours, key=lambda x: cv.contourArea(x))
        x, y, w, h = cv.boundingRect(count1)
        cv.rectangle(crop_img, (x, y), (x + w, y + h), (0, 0, 255), 0)
        hull = cv.convexHull(count1)
        drawing = np.zeros(crop_img.shape, np.uint8)
        cv.drawContours(drawing, [count1], 0, (0, 255, 0), 0)
        cv.drawContours(drawing, [hull], 0, (0, 0, 255), 0)
        hull = cv.convexHull(count1, returnPoints=False)
        defects = cv.convexityDefects(count1, hull)

        count_defects = 0
        cv.drawContours(thresholded, contours, -1, (0, 255, 0), 3)

        for i in range(defects.shape[0]):
            s, e, f, d = defects[i, 0]
            start = tuple(count1[s][0])
            end = tuple(count1[e][0])
            far = tuple(count1[f][0])
            a = math.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
            b = math.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
            c = math.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)
            angle = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)) * 57

            if angle <= 90:
                count_defects += 1
                cv.circle(crop_img, far, 1, [0, 0, 255], -1)

            cv.line(crop_img, start, end, [0, 255, 0], 2)

        if count_defects == 1:
            cv.putText(img, "2 fingers", (50, 50), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255))
        elif count_defects == 2:
            str = "3 fingers"
            cv.putText(img, str, (5, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255))
        elif count_defects == 3:
            cv.putText(img, "4 fingers", (50, 50), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255))
        elif count_defects == 4:
            cv.putText(img, "5 fingers", (50, 50), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255))
        elif count_defects == 0:
            cv.putText(img, "one", (50, 50), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255))

        cv.imshow('main window', img)
        all_img = np.hstack((drawing, crop_img))
        cv.imshow('Contours', all_img)
        k = cv.waitKey(10)
        if k == 27:
            break

    cap.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    hand_gesture_recognition()
