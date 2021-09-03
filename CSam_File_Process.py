import inline as inline

import numpy as np

import cv2


directory = "C:\\Users\senguel\OneDrive - Facebook\Architecture A\Process Tracker\C-SAM Images\Siena"

fileName = '\\2021April-OAS-x292362-01c0'
imageFile = directory + fileName +".bmp"
img = cv2.imread(imageFile,0)
img_rgb = cv2.imread(imageFile)
img_copy = img.copy()
kernel = np.ones((3,3),np.uint8)
dilation = cv2.dilate(img,kernel,iterations = 1)

ret,thresh1 = cv2.threshold(img,30,255,cv2.THRESH_BINARY)
cv2.imshow('Original',img)
cv2.imshow('binary',thresh1)
print(np.min(thresh1))
print(np.max(thresh1))

# Find contours
contours, hierarchy =cv2.findContours(dilation,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)
max_area = -1
index = 0
void_area =0
for i in range(len(contours)):
    area = cv2.contourArea(contours[i])
    void_area +=area
    if area > max_area:
        cnt = contours[i]
        max_area = area
        index =i

void_area -=max_area
#print(void_area)
drawing = np.zeros((img.shape[0], img.shape[1], 1), dtype=np.uint8)

# Find the convex hull object for each contour
hull_list = []
for i in range(len(contours)):
    hull = cv2.convexHull(contours[i])
    hull_list.append(hull)

for i in range(len(contours)):
    color_contours = (255, 0, 0)  # green - color for contours
    color = (0, 0, 255)  # blue - color for convex hull
    if index == i:
        cv2.drawContours(drawing, hull_list, i, color)
        hull = hull_list[i]
        cv2.fillPoly(drawing, [hull], (255, 255, 255))
        circleArea = cv2.contourArea(contours[i])


# counting the number of pixels
number_of_white_pix = np.sum(drawing == 255)
number_of_black_pix = np.sum(drawing == 0)

wafer_pixes = number_of_white_pix
if wafer_pixes>165000:
    wafer_pixes = 165000

number_of_white_pix_original = np.sum(thresh1 >0)
number_of_black_pix_original = np.sum(thresh1 == 0)

void_pixels = number_of_white_pix_original

print('Number of white pixels in wafer area :', wafer_pixes)
#print('Number of black pixels outside wafer area:', number_of_black_pix)

print('Number of white pixels in voids:', void_pixels)
#print('Number of black pixels outside voids:', number_of_black_pix_original)

# Show in a window
percentage_void = 100 - (void_pixels/wafer_pixes)*100
print(percentage_void)
cv2.imshow('Wafer', drawing)
cv2.waitKey()
