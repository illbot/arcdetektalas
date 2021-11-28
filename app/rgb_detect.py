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
    personnel_number = 0

    # Defining color ranges RGB
    # Using small range around Palette Human skin tone color
    # skin1 RGB(197,140,133) -> HSV(7,32.5,77.3) ~ (7, 32, 77)
    skin1_low = np.array([2, 27, 72])
    skin1_high = np.array([12, 37, 82])
    # skin2 RGB(236,188,180) -> HSV(9,23.7,92.5) ~ (9,24,93)
    skin2_low = np.array([4, 19, 88])
    skin2_high = np.array([14, 29, 98])
    # skin3 RGB(209,188,164) -> HSV(32,21.5,82) ~ (32,22,82)
    skin3_low = np.array([27, 17, 77])
    skin3_high = np.array([37, 27, 87])
    # skin4 RGB(161,102,94) -> HSV(7,41.6,63.1) ~ (7,42,63)
    skin4_low = np.array([2, 37, 58])
    skin4_high = np.array([12, 47, 68])
    # skin5 RGB(80,51,53) -> HSV(356,36.2,31.4) ~ (356,36,31)
    skin5_low = np.array([351, 31, 26])
    skin5_high = np.array([361, 41, 36])
    # skin6 RGB(89,47,42) -> HSV(6,52.8,34.9) ~ (6,53,35)
    skin6_low = np.array([1, 48, 30])
    skin6_high = np.array([11, 58, 40])

    # Creating masks
    mask_skin1 = cv2.inRange(image_hsv, skin1_low, skin1_high)
    mask_skin2 = cv2.inRange(image_hsv, skin2_low, skin2_high)
    mask_skin3 = cv2.inRange(image_hsv, skin3_low, skin3_high)
    mask_skin4 = cv2.inRange(image_hsv, skin4_low, skin4_high)
    mask_skin5 = cv2.inRange(image_hsv, skin5_low, skin5_high)
    mask_skin6 = cv2.inRange(image_hsv, skin6_low, skin6_high)

    # Adding masks
    mask = mask_skin1 + mask_skin2 + mask_skin3 + mask_skin4 + mask_skin5 + mask_skin6

    # Searching for human skin colors
    # Should return image with face, rest is black
    img_skin = cv2.bitwise_and(image_hsv, image_hsv, mask=mask)

    # Creating grey images for contours
    gray_skin = cv2.cvtColor(cv2.cvtColor(img_skin, cv2.COLOR_HSV2RGB), cv2.COLOR_RGB2GRAY)

    # Canny edge detect on gray image
    canny_img = cv2.Canny(gray_skin, 1, 1)

    # Dilate / Erode to sum smaller areas
    kernel_dil = np.ones((10, 10), np.uint8)
    kernel_erode = np.ones((9, 9), np.uint8)
    dilated_img = cv2.dilate(canny_img, kernel_dil, 1)
    eroded_img = cv2.erode(dilated_img, kernel_erode, 1)

    # Searching for contours
    contours_skin, hierarchy = cv2.findContours(eroded_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Drawing bounding boxes, counting faces
    for contour in contours_skin:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(img_result, (x, y), (x + w, y + h), (0, 0, 255), 3)
        personnel_number = personnel_number + 1

    return img_result, personnel_number
