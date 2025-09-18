import cv2

def crop(image_path: str, bbox):
    x, y, w, h = bbox
    img = cv2.imread(image_path)
    return img[y:y+h, x:x+w]
