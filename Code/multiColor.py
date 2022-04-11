import cv2 as cv
import numpy as np

# 视频操作
cap = cv.VideoCapture(1)

while (1):
    # 读取帧
    _, pre = cap.read()
    # 高斯滤波去除噪声
    frame = cv.GaussianBlur(pre, [5, 5], 0)

    # 转换颜色空间 BGR 到 HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # 定义HSV中蓝色的范围
    lower_blue = np.array([106, 43, 46])
    upper_blue = np.array([130, 255, 255])
    # 设置HSV的阈值使得只取蓝色
    mask_B = cv.inRange(hsv, lower_blue, upper_blue)

    lower_yellow = np.array([26, 43, 46])
    upper_yellow = np.array([34, 255, 255])
    mask_Y = cv.inRange(hsv, lower_yellow, upper_yellow)

    lower_red1 = np.array([0, 43, 46])
    upper_red1 = np.array([20, 255, 255])
    mask_R1 = cv.inRange(hsv, lower_red1, upper_red1)

    lower_red2 = np.array([150, 43, 46])
    upper_red2 = np.array([180, 255, 255])
    mask_R2 = cv.inRange(hsv, lower_red2, upper_red2)

    mask=mask_B+mask_Y+mask_R1+mask_R2

    # 将掩膜和图像逐像素相加
    res = cv.bitwise_and(frame, frame, mask=mask)

    cv.imshow('frame', frame)
    cv.imshow('mask', mask)
    cv.imshow('res', res)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()

'''
# 图像操作
img = cv.imread("../image/template.jpg")
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# 定义HSV中蓝色的范围
lower_blue = np.array([100, 43, 46])
upper_blue = np.array([124, 255, 255])
# 设置HSV的阈值使得只取蓝色
mask_B = cv.inRange(hsv, lower_blue, upper_blue)

lower_yellow = np.array([26, 43, 46])
upper_yellow = np.array([34, 255, 255])
mask_Y = cv.inRange(hsv, lower_yellow, upper_yellow)

lower_red1 = np.array([0, 43, 46])
upper_red1 = np.array([10, 255, 255])
mask_R1 = cv.inRange(hsv, lower_red1, upper_red1)

lower_red2 = np.array([156, 43, 46])
upper_red2 = np.array([180, 255, 255])
mask_R2 = cv.inRange(hsv, lower_red2, upper_red2)

mask=mask_B+mask_Y+mask_R1+mask_R2

# 将掩膜和图像逐像素相加
res = cv.bitwise_and(img, img, mask=mask)

cv.imshow('img', img)
cv.imshow('mask', mask)
cv.imshow('res', res)

cv.waitKey(0)
cv.destroyAllWindows()
'''