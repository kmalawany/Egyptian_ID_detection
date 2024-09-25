from correct_alignment import apply_alignment
import cv2
from ultralytics import YOLO
import argparse
from pytesseract import TesseractError


def main():
    try:
        image = cv2.imread(args["image"])
    except FileNotFoundError as e:
        raise FileNotFoundError('Image not found')

    detection_model = YOLO('yolo_id_detection.pt')
    segment_model = YOLO('yolo_segmentation.pt')

    results = detection_model.predict(image, imgsz=640, conf=0.50)
    bbox = 0
    box_coordinates = 0
    boxes = results[0].boxes.xyxy
    classes = results[0].boxes.cls

    for box, cls in zip(boxes, classes):

        if cls == 1.0:
            x1, y1, x2, y2 = box.int()
            new_image = image[y1:y2, x1:x2]
            try:
                rotated_image = apply_alignment(new_image)
            except TesseractError as e:
                ValueError('No text detected please take another image')

            final_results = segment_model.predict(rotated_image)
            final_results[0].show()


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True,
                    help="path to input image")
    args = vars(ap.parse_args())
    main()
