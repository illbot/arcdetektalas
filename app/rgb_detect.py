import cv2
import numpy as np
# Short function that searches for areas that are in the Palette Human skin tone color whit a small deviation
# Input - Image to be searched
# Output - Image with the bounding boxes around the found areas and the number of boxes


def rgb_detect(img):
    # Copying given img to local
    img_local = img.copy()
    # Converting img to hsv (hopefully input images are BGR)
    image_hsv = cv2.cvtColor(img_local, cv2.COLOR_BGR2HSV)
    # Creating a result copy
    img_result = img_local.copy()
    # variable for number of faces
    faces = 0

    # Defining color ranges RGB
    # Using small range around Palette Human skin tone color
    # skin1 (197,140,133)
    # skin2 (236,188,180)
    # skin3 (209,188,164)
    # skin4 (161,102,94)
    # skin5 (80,51,53)
    # skin6 (89,47,42)
    skin1_low = np.array([195, 137, 130])
    skin1_high = np.array([200, 143, 135])
    skin2_low = np.array([233, 185, 177])
    skin2_high = np.array([238, 190, 167])
    skin3_low = np.array([205, 185, 160])
    skin3_high = np.array([213, 190, 167])
    skin4_low = np.array([158, 98, 90])
    skin4_high = np.array([165, 105, 100])
    skin5_low = np.array([75, 46, 50])
    skin5_high = np.array([85, 55, 57])
    skin6_low = np.array([85, 34, 37])
    skin6_high = np.array([93, 52, 47])

    # Creating masks
    mask_skin1 = cv2.inRange(image_hsv, skin1_low, skin1_high)
    mask_skin2 = cv2.inRange(image_hsv, skin2_low, skin2_high)
    mask_skin3 = cv2.inRange(image_hsv, skin3_low, skin3_high)
    mask_skin4 = cv2.inRange(image_hsv, skin4_low, skin4_high)
    mask_skin5 = cv2.inRange(image_hsv, skin5_low, skin5_high)
    mask_skin6 = cv2.inRange(image_hsv, skin6_low, skin6_high)

    # Searching for human skin colors
    # Should return image with face, rest is black
    img_skin1 = cv2.bitwise_and(image_hsv, image_hsv, mask=mask_skin1)
    img_skin2 = cv2.bitwise_and(image_hsv, image_hsv, mask=mask_skin2)
    img_skin3 = cv2.bitwise_and(image_hsv, image_hsv, mask=mask_skin3)
    img_skin4 = cv2.bitwise_and(image_hsv, image_hsv, mask=mask_skin4)
    img_skin5 = cv2.bitwise_and(image_hsv, image_hsv, mask=mask_skin5)
    img_skin6 = cv2.bitwise_and(image_hsv, image_hsv, mask=mask_skin6)

    # Creating grey images for contours
    gray_skin1 = cv2.cvtColor(cv2.cvtColor(img_skin1, cv2.COLOR_HSV2BGR), cv2.COLOR_BGR2GRAY)
    gray_skin2 = cv2.cvtColor(cv2.cvtColor(img_skin2, cv2.COLOR_HSV2BGR), cv2.COLOR_BGR2GRAY)
    gray_skin3 = cv2.cvtColor(cv2.cvtColor(img_skin3, cv2.COLOR_HSV2BGR), cv2.COLOR_BGR2GRAY)
    gray_skin4 = cv2.cvtColor(cv2.cvtColor(img_skin4, cv2.COLOR_HSV2BGR), cv2.COLOR_BGR2GRAY)
    gray_skin5 = cv2.cvtColor(cv2.cvtColor(img_skin5, cv2.COLOR_HSV2BGR), cv2.COLOR_BGR2GRAY)
    gray_skin6 = cv2.cvtColor(cv2.cvtColor(img_skin6, cv2.COLOR_HSV2BGR), cv2.COLOR_BGR2GRAY)

    # Searching for contours
    contours_skin1, hierarchy = cv2.findContours(gray_skin1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours_skin2, hierarchy = cv2.findContours(gray_skin2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours_skin3, hierarchy = cv2.findContours(gray_skin3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours_skin4, hierarchy = cv2.findContours(gray_skin4, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours_skin5, hierarchy = cv2.findContours(gray_skin5, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours_skin6, hierarchy = cv2.findContours(gray_skin6, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Drawing bounding boxes, counting faces
    for contour1 in contours_skin1:
        x, y, w, h = cv2.boundingRect(contour1)
        cv2.rectangle(img_result, (x, y), (x + w, y + h), (0, 0, 255), 2)
        faces = faces+1
    for contour2 in contours_skin2:
        x, y, w, h = cv2.boundingRect(contour2)
        cv2.rectangle(img_result, (x, y), (x + w, y + h), (0, 0, 255), 2)
        faces = faces + 1
    for contour3 in contours_skin3:
        x, y, w, h = cv2.boundingRect(contour3)
        cv2.rectangle(img_result, (x, y), (x + w, y + h), (0, 0, 255), 2)
        faces = faces + 1
    for contour4 in contours_skin4:
        x, y, w, h = cv2.boundingRect(contour4)
        cv2.rectangle(img_result, (x, y), (x + w, y + h), (0, 0, 255), 2)
        faces = faces + 1
    for contour5 in contours_skin5:
        x, y, w, h = cv2.boundingRect(contour5)
        cv2.rectangle(img_result, (x, y), (x + w, y + h), (0, 0, 255), 2)
        faces = faces + 1
    for contour6 in contours_skin6:
        x, y, w, h = cv2.boundingRect(contour6)
        cv2.rectangle(img_result, (x, y), (x + w, y + h), (0, 0, 255), 2)
        faces = faces + 1

    return img_result, faces

'''
img = cv2.imread('teszt_kepek/picture_02.jpg')
res, count = rgb_detect(img)
cv2.imshow('res',res)
cv2.waitKey()
'''