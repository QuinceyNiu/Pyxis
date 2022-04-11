import cv2 as cv

'''class MyCamera():
    def __init__(self, cameraNum):
        self.cap = cv.VideoCapture(cameraNum)
        self.height = 360
        self.weight = 640

    def read(self):
        iret, frame = self.cap.read()
        src = frame[60:420, :]
        if(iret != True):
            raise Exception("camera fail!")
        return src

    def release(self):
        self.cap.release()
        cv.destroyAllWindows()'''

img = cv.imread("../image/wire.jpg")
image = img[1334:2917,1550:1636]
hsv_roi = cv.cvtColor(image, cv.COLOR_BGR2HSV)
#cv.imshow("hsv", hsv_roi)
pre = cv.GaussianBlur(image, (5,5), 0)
#cv.imshow("pre", pre)
gray = cv.cvtColor(pre, cv.COLOR_BGR2GRAY)
#cv.imshow("gray", gray)
ret, binary_img = cv.threshold(gray, 50, 255, cv.THRESH_BINARY | cv.THRESH_TRIANGLE)
#cv.imshow("binary", binary_img)
meb = cv.medianBlur(binary_img, 3)
#cv.imshow("median", meb)

# 轮廓检测
contours, hierarchy = cv.findContours(meb, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
if len(contours) > 0:
    boxes = [cv.boundingRect(c) for c in contours]
    count = 0
    for box in boxes.copy():
        x,y,w,h = box
        if w*h < 100:
            boxes.remove(box)
            continue
        # print(w*h)
        image = cv.rectangle(image, (x,y), (x+w,y+h), (0,255,0), 2)
        count = count + 1
cv.imshow("result img", image)
#cv.imshow("roi", roi)
cv.waitKey(0)
cv.destroyAllWindows()

'''while(1):
    cap = cv.VideoCapture(1)
    iret, frame = cap.read()
    raw_img = frame[60:420, :]
    roi = raw_img[160:200,190:560]
    cv.imshow("roi", roi)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()'''
