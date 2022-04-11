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
        cv.destroyAllWindows()
'''
while(1):
    cap = cv.VideoCapture(1)
    iret, frame = cap.read()
    raw_img = frame[60:420, :]
    roi = raw_img[160:200,190:560]
    cv.imshow("roi", roi)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()
