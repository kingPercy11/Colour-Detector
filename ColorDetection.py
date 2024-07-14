import cv2
import numpy as np


def color_detection(image_path):
    image = cv2.imread(image_path)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    #mask of hsv values
    lower_hue = int(input("Enter lower hue value (0-179): "))
    upper_hue = int(input("Enter upper hue value (0-179): "))
    lower_saturation = int(input("Enter lower saturation value (0-255): "))
    upper_saturation = int(input("Enter upper saturation value (0-255): "))
    lower_value = int(input("Enter lower value (brightness) value (0-255): "))
    upper_value = int(input("Enter upper value (brightness) value (0-255): "))
    lower_bound = np.array([lower_hue, lower_saturation, lower_value], dtype=np.uint8)
    upper_bound = np.array([upper_hue, upper_saturation, upper_value], dtype=np.uint8)
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    result = cv2.bitwise_and(image, image, mask=mask)
    cv2.imshow('Original Image', image)
    cv2.imshow('Color Detection Result', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


path = input("Enter the image path: ")
color_detection(path)
