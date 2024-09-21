from pytesseract import Output
import pytesseract
import argparse
import imutils
import cv2


def apply_alignment(image):
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = pytesseract.image_to_osd(image, output_type=Output.DICT, config='-c min_characters_to_try=20')
    # display the orientation information
    print("[INFO] detected orientation: {}".format(
        results["orientation"]))
    print("[INFO] rotate by {} degrees to correct".format(
        results["rotate"]))
    print("[INFO] detected script: {}".format(results["script"]))

    rotated_image = imutils.rotate_bound(image, angle=results["rotate"])

    return rotated_image
